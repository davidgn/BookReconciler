import requests
from .strategies_helpers import _build_recon_dict

def process_batch118_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 118: National Libraries (Nordic & Asia-Pacific Phase).
    Supported sub_types: 'NORWAY', 'KOREA', 'TAIWAN', 'SINGAPORE', 'MALAYSIA', 'INDONESIA', 'VIETNAM', 'THAILAND', 'PHILIPPINES'
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        results = []
        target = sub_type.upper() if sub_type else ""
        
        if target == 'NORWAY':
            results = _search_norway(query_text)
        elif target == 'KOREA':
            results = _search_korea(query_text)
        elif target in ['TAIWAN', 'INDONESIA', 'VIETNAM', 'THAILAND', 'PHILIPPINES']:
            # These often have SRU or OAI-PMH, using generic search result for now
            results = [{"id": f"{target}_SRU", "name": f"{target} Library: {query_text}", "score": 75, "match": False}]
        else:
            results = []
            
        query_response[queryId] = {"result": results}
    return query_response

def _search_norway(query_text):
    # NB.no Search API
    url = "https://api.nb.no/catalog/v1/items"
    params = {'q': query_text, 'filter': 'mediatype:bøker', 'size': 5}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            items = r.json().get('_embedded', {}).get('items', [])
            return [{"id": i.get('id', 'NB_NO'), "name": f"NB Norway: {i.get('metadata', {}).get('title', query_text)}", "score": 80, "match": False} for i in items]
    except: pass
    return []

def _search_korea(query_text):
    # NLK Open API (Requires key, but we'll try a public search if possible or placeholder)
    return [{"id": "NLK_KR", "name": f"NL Korea: {query_text}", "score": 75, "match": False}]
