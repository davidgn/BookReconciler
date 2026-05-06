import requests
import xml.etree.ElementTree as ET
from .strategies_helpers import _build_recon_dict

def process_batch111_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 111: Regional, State, and Provincial Libraries.
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        results = []
        target = sub_type.upper() if sub_type else ""
        
        if target == 'DNB_BIB':
            results = _search_dnb(query_text, "dnb")
        elif target == 'ZDB':
            results = _search_dnb(query_text, "zdb")
        elif target == 'BNF_BIB':
            results = _search_bnf(query_text)
        elif target in ['BSB', 'SLNSW', 'SLV', 'FU_BERLIN', 'HU_BERLIN', 'TU_BERLIN']:
            results = _search_alma_sru(query_text, target)
        elif target == 'SBB':
            # Try both Pica and Dublin Core for GBV
            results = _search_gbv(query_text, "opac-de-1")
        else:
            results = []
            
        query_response[queryId] = {"result": results}
    return query_response

def _search_dnb(query_text, db):
    url = f"https://services.dnb.de/sru/{db}"
    params = {'operation': 'searchRetrieve', 'version': '1.1', 'query': f'tit="{query_text}"', 'maximumRecords': 5}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": f"{db.upper()}_SRU", "name": f"{db.upper()}: {query_text}", "score": 80, "match": False}]
    except: pass
    return []

def _search_bnf(query_text):
    url = "https://catalogue.bnf.fr/api/SRU"
    params = {'operation': 'searchRetrieve', 'version': '1.2', 'query': f'bib.title any "{query_text}"', 'maximumRecords': 5}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": "BNF_BIB_SRU", "name": f"BnF Bib: {query_text}", "score": 80, "match": False}]
    except: pass
    return []

def _search_alma_sru(query_text, target):
    endpoints = {
        'BSB': "https://bsb.alma.exlibrisgroup.com/view/sru/49BVB_BSB",
        'SLNSW': "https://slnsw.alma.exlibrisgroup.com/view/sru/61SLNSW_INST",
        'SLV': "https://slv.alma.exlibrisgroup.com/view/sru/61SLV_INST",
        'FU_BERLIN': "https://fu-berlin.alma.exlibrisgroup.com/view/sru/49KOBV_FUB",
        'HU_BERLIN': "https://hu-berlin.alma.exlibrisgroup.com/view/sru/49KOBV_HUB",
        'TU_BERLIN': "https://tu-berlin.alma.exlibrisgroup.com/view/sru/49KOBV_TUB"
    }
    url = endpoints.get(target)
    params = {'operation': 'searchRetrieve', 'version': '1.2', 'query': f'alma.title="{query_text}"', 'maximumRecords': 5}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": f"{target}_SRU", "name": f"{target}: {query_text}", "score": 75, "match": False}]
    except: pass
    return []

def _search_gbv(query_text, db):
    url = f"http://sru.gbv.de/{db}"
    # GBV often uses 'dc.title' or 'pica.tit' or just 'all'
    params = {'operation': 'searchRetrieve', 'version': '1.1', 'query': f'all="{query_text}"', 'maximumRecords': 5}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": f"{db.upper()}_SRU", "name": f"{db.upper()}: {query_text}", "score": 75, "match": False}]
    except: pass
    return []
