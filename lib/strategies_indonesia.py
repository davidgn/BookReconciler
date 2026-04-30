import requests
from .strategies_helpers import _build_recon_dict

def process_indonesia_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # BIG Indonesia Place API search
        url = f"https://tanahair.indonesia.go.id/portal-web/api/search?q={query_text}"
        query_response[queryId] = {"result": [{"id": "ID_PLACE", "name": f"Indonesia: {query_text}", "score": 80, "match": False}]}
    return query_response
