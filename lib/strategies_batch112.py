import requests
import xml.etree.ElementTree as ET
from .strategies_helpers import _build_recon_dict

def process_batch112_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 112: Global Regional and State Libraries (Phase 2).
    Supported sub_types: 'SLQ', 'BC_CATALONIA', 'K10PLUS', 'SWB', 'SLNC', 'SLF', 'CSL_CA', 'SLP_PA', 'SLO_OH', 'OSL_OR', 'LVA_VA'
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        results = []
        target = sub_type.upper() if sub_type else ""
        
        if any(x in target for x in ['SLQ', 'BC_CATALONIA', 'CSL_CA', 'SLP_PA', 'SLO_OH', 'OSL_OR', 'LVA_VA', 'SLNC', 'SLF']):
            results = _search_alma_sru(query_text, target)
        elif target == 'K10PLUS':
            results = _search_k10plus(query_text, "k10plus")
        elif target == 'SWB':
            results = _search_k10plus(query_text, "swb")
        else:
            results = []
            
        query_response[queryId] = {"result": results}
    return query_response

def _search_alma_sru(query_text, target):
    endpoints = {
        'SLQ': "https://ap02.alma.exlibrisgroup.com/view/sru/61SLQ_INST",
        'BC_CATALONIA': "https://csuc-bc.alma.exlibrisgroup.com/view/sru/34CSUC_BC",
        'CSL_CA': "https://csl.alma.exlibrisgroup.com/view/sru/01CSL_INST",
        'SLP_PA': "https://kln.alma.exlibrisgroup.com/view/sru/01KLN_SLP",
        'SLO_OH': "https://ohiolink.alma.exlibrisgroup.com/view/sru/01OHIOLINK_SLO",
        'OSL_OR': "https://alliance.alma.exlibrisgroup.com/view/sru/01ALLIANCE_OSL",
        'LVA_VA': "https://lva.alma.exlibrisgroup.com/view/sru/01VIVA_LVA",
        'SLNC': "https://slnc.alma.exlibrisgroup.com/view/sru/01SLNC_INST",
        'SLF': "https://flvc.alma.exlibrisgroup.com/view/sru/01FLVC_SLF"
    }
    url = endpoints.get(target)
    if not url: return []
    
    params = {
        'operation': 'searchRetrieve',
        'version': '1.2',
        'query': f'alma.title="{query_text}"',
        'maximumRecords': 5
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": f"{target}_SRU", "name": f"{target}: {query_text}", "score": 75, "match": False}]
    except: pass
    return []

def _search_k10plus(query_text, db):
    # K10plus SRU: http://sru.k10plus.de/[db]
    url = f"http://sru.k10plus.de/{db}"
    params = {
        'operation': 'searchRetrieve',
        'version': '1.1',
        'query': f'pica.tit="{query_text}"',
        'maximumRecords': 5
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": f"{db.upper()}_SRU", "name": f"{db.upper()}: {query_text}", "score": 80, "match": False}]
    except: pass
    return []
