import requests
from .strategies_helpers import _build_recon_dict

def process_agorha_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # INHA AGORHA API
        url = f"https://agorha.inha.fr/api/v1/personnes?q={query_text}"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                # Basic placeholder
                query_response[queryId] = {"result": [{"id": "AGORHA_SEARCH", "name": f"AGORHA Art: {query_text}", "score": 80, "match": False}]}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
