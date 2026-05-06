import requests
import xml.etree.ElementTree as ET
from .strategies_helpers import _build_recon_dict

def process_batch114_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 114: Regional, State, and Provincial Libraries (Phase 4).
    Supported sub_types: 'MNPALS', 'WISC_LAW', 'COLO_STATE', 'MO_STATE', 'BVPB_SPAIN', 'GALICIANA', 'BVA_ANDALUCIA', 'SAILOR_MD'
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        results = []
        target = sub_type.upper() if sub_type else ""
        
        if target in ['MNPALS', 'WISC_LAW', 'COLO_STATE', 'MO_STATE']:
            results = _search_alma_sru(query_text, target)
        elif target in ['BVPB_SPAIN', 'GALICIANA', 'BVA_ANDALUCIA']:
            results = _search_digibib_sru(query_text, target)
        elif target == 'SAILOR_MD':
            results = _search_polaris_sru(query_text, "https://cosmos.somd.lib.md.us/sru/default.aspx")
        else:
            results = []
            
        query_response[queryId] = {"result": results}
    return query_response

def _search_alma_sru(query_text, target):
    endpoints = {
        'MNPALS': "https://mnpals-network.alma.exlibrisgroup.com/view/sru/01PALS_NETWORK",
        'WISC_LAW': "https://wislaw.alma.exlibrisgroup.com/view/sru/01WISC_WSLL",
        'COLO_STATE': "https://csl.alma.exlibrisgroup.com/view/sru/01COL_STATE",
        'MO_STATE': "https://missouristate.alma.exlibrisgroup.com/view/sru/01MSU_INST"
    }
    url = endpoints.get(target)
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

def _search_digibib_sru(query_text, target):
    endpoints = {
        'BVPB_SPAIN': "https://bvpb.mcu.es/i18n/sru/sru.cmd",
        'GALICIANA': "https://bibliotecadegalicia.xunta.gal/i18n/sru/sru.cmd",
        'BVA_ANDALUCIA': "https://www.bibliotecavirtualdeandalucia.es/i18n/sru/sru.cmd"
    }
    url = endpoints.get(target)
    params = {
        'operation': 'searchRetrieve',
        'version': '1.1',
        'query': f'dc.title="{query_text}"',
        'maximumRecords': 5
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": f"{target}_SRU", "name": f"{target}: {query_text}", "score": 80, "match": False}]
    except: pass
    return []

def _search_polaris_sru(query_text, url):
    params = {
        'operation': 'searchRetrieve',
        'version': '1.1',
        'query': f'title="{query_text}"',
        'maximumRecords': 5
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": "POLARIS_SRU", "name": f"Polaris Hub: {query_text}", "score": 75, "match": False}]
    except: pass
    return []
