import requests
from .strategies_helpers import _build_recon_dict

def process_eutransparency_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = f"https://ec.europa.eu/transparencyregister/public/consultation/search.do?searchField={query_text}"
        query_response[queryId] = {"result": [{"id": "EU_TRANS_SEARCH", "name": f"EU Transparency: {query_text}", "score": 80, "match": False}]}
    return query_response
