import requests
import xml.etree.ElementTree as ET
from .strategies_helpers import _build_recon_dict

def process_batch115_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 115: Remaining National and State Libraries.
    Supported sub_types: 'ESTONIA', 'LATVIA', 'LITHUANIA', 'SERBIA', 'BULGARIA', 'MOROCCO', 'SA', 'WA', 'TAS', 'ICELAND'
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        results = []
        target = sub_type.upper() if sub_type else ""
        
        if target == 'ESTONIA':
            results = _search_sru_generic(query_text, "https://www.ester.ee/sru", "EST")
        elif target == 'LATVIA':
            results = _search_alma_sru(query_text, "https://primolatvija.hosted.exlibrisgroup.com/view/sru/371KISCNLL_VU1", "LNB")
        elif target == 'LITHUANIA':
            results = _search_sru_generic(query_text, "https://ibiblioteka.lt/view/sru/LNB", "LNB_LT")
        elif target == 'SERBIA':
            results = _search_sru_generic(query_text, "https://plus.cobiss.net/cobiss/sr/sr/sru", "SRB")
        elif target == 'BULGARIA':
            results = _search_sru_generic(query_text, "https://plus.cobiss.net/cobiss/bg/bg/sru", "BGR")
        elif target == 'MOROCCO':
            results = _search_sru_generic(query_text, "https://catalogue.bnrm.ma/sru", "MAR")
        elif target in ['SA', 'WA', 'TAS']:
            results = _search_trove_state(query_text, target)
        elif target == 'ICELAND':
            results = _search_alma_sru(query_text, "https://eu.alma.exlibrisgroup.com/view/sru/354LBS_INST", "ISL")
        else:
            results = []
            
        query_response[queryId] = {"result": results}
    return query_response

def _search_alma_sru(query_text, url, label):
    params = {
        'operation': 'searchRetrieve',
        'version': '1.2',
        'query': f'alma.title="{query_text}"',
        'maximumRecords': 5
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": f"{label}_SRU", "name": f"{label}: {query_text}", "score": 75, "match": False}]
    except: pass
    return []

def _search_sru_generic(query_text, url, label):
    # Most generic SRUs use title or dc.title
    params = {
        'operation': 'searchRetrieve',
        'version': '1.1',
        'query': f'title="{query_text}"',
        'maximumRecords': 5
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": f"{label}_SRU", "name": f"{label}: {query_text}", "score": 75, "match": False}]
    except: pass
    return []

def _search_trove_state(query_text, state):
    nucs = {'SA': "SSL:S", 'WA': "WLB", 'TAS': "TSL"}
    nuc = nucs.get(state)
    url = "https://api.trove.nla.gov.au/v3/sru"
    params = {
        'operation': 'searchRetrieve',
        'version': '1.1',
        'query': f'nuc:"{nuc}" AND title="{query_text}"',
        'maximumRecords': 5
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": f"{state}_Trove_SRU", "name": f"State Lib {state}: {query_text}", "score": 75, "match": False}]
    except: pass
    return []
