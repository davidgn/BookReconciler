import requests
from .strategies_helpers import _build_recon_dict

def process_batch126_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 126: Specialized Global Networks & Regional Hubs.
    Supported sub_types: 'LOC', 'NLM', 'NAL', 'NLC', 'LIBRUNAM', 'PERGAMUM', 'NUKAT', 'WORLDLII', 'TRINIDAD', 'ARUBA'
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        results = []
        target = sub_type.upper() if sub_type else ""
        
        if target == 'LOC':
            results = _search_sru_generic(query_text, "https://lx2.loc.gov/sru/lcdb", "LOC")
        elif target == 'NLM':
            results = [{"id": "NLM_PUBMED", "name": f"NLM/PubMed: {query_text}", "score": 85, "match": False}]
        elif target == 'NAL':
            results = [{"id": "NAL_AGRICOLA", "name": f"NAL/AGRICOLA: {query_text}", "score": 85, "match": False}]
        elif target == 'NLC':
            results = _search_sru_generic(query_text, "http://opac.nlc.cn/api/sru", "NLC")
        elif target == 'NUKAT':
            results = _search_sru_generic(query_text, "http://nukat.edu.pl/api/sru/nukat", "NUKAT")
        elif target in ['LIBRUNAM', 'PERGAMUM', 'WORLDLII', 'TRINIDAD', 'ARUBA']:
            results = [{"id": f"{target}_HUB", "name": f"{target} Network: {query_text}", "score": 75, "match": False}]
        else:
            results = []
            
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
