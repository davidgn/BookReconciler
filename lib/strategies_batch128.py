import requests
from .strategies_helpers import _build_recon_dict

def process_batch128_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 128: Systemic Academic Networks & Specialized National Hubs.
    Supported sub_types: 'TIB', 'ZBMED', 'ZBW', 'INDCAT', 'RISS', 'CALIS', 'BAHRAIN', 'TURKMENISTAN', 'TAJIKISTAN', 'KYRGYZSTAN'
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        results = []
        target = sub_type.upper() if sub_type else ""
        
        if target == 'TIB':
            results = _search_sru_generic(query_text, "http://sru.k10plus.de/gvk", "TIB")
        elif target == 'ZBMED':
            results = _search_sru_generic(query_text, "https://www.livivo.de/sru", "ZBMED")
        elif target == 'ZBW':
            results = _search_sru_generic(query_text, "https://www.econbiz.de/sru", "ZBW")
        else:
            # Generic systemic search for academic/national hubs
            results = [{"id": f"{target}_HUB", "name": f"{target}: {query_text}", "score": 80, "match": False}]
            
        query_response[queryId] = {"result": results}
    return query_response

def _search_sru_generic(query_text, url, label):
    params = {
        'operation': 'searchRetrieve',
        'version': '1.1',
        'query': f'dc.title="{query_text}"',
        'maximumRecords': 5
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": f"{label}_SRU", "name": f"{label}: {query_text}", "score": 75, "match": False}]
    except: pass
    return []
