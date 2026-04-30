import requests
from .strategies_helpers import _build_recon_dict

def process_doab_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = f"https://directory.doabooks.org/rest/search?query={query_text}&scope=/"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                query_response[queryId] = {"result": [{"id": "DOAB_SEARCH", "name": f"DOAB: {query_text}", "score": 80, "match": False}]}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
