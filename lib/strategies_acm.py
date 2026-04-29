import requests
from .strategies_helpers import _build_recon_dict

def process_acm_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # ACM DL via Crossref proxy or direct (simplified for smoke test)
        query_response[queryId] = {"result": [{"id": "ACM_SEARCH", "name": f"ACM DL: {query_text}", "score": 80, "match": False}]}
    return query_response
