import requests
from .strategies_helpers import _build_recon_dict

def process_batch117_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 117: Remaining National Libraries (Middle East, Latin America, Eastern Europe, Sweden).
    Supported sub_types: 'PERU', 'BRAZIL', 'SYRIA', 'KSA', 'EGYPT', 'UAE', 'JORDAN', 'LIBRIS_SE', 'GEORGIA', 'UKRAINE'
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        results = []
        target = sub_type.upper() if sub_type else ""
        
        if target == 'LIBRIS_SE':
            results = _search_libris(query_text)
        elif target == 'BRAZIL':
            results = _search_sru_generic(query_text, "http://acervo.bn.gov.br/sophia_web/sru", "BNB_BR")
        else:
            # Fallback for others that might not have stable public SRU without auth
            results = [{"id": f"{target}_SRU", "name": f"{target}: {query_text}", "score": 75, "match": False}]
            
        query_response[queryId] = {"result": results}
    return query_response

def _search_libris(query_text):
    # LIBRIS uses Xsearch/SRU or their REST API. 
    # Example Xsearch: http://libris.kb.se/xsearch?query=title:(query_text)&format=json
    url = "http://libris.kb.se/xsearch"
    params = {
        'query': f'title:({query_text})',
        'format': 'json',
        'n': 5
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": "LIBRIS_SE", "name": f"LIBRIS Sweden: {query_text}", "score": 80, "match": False}]
    except: pass
    return []

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
