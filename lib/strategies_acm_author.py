import requests
from .strategies_helpers import _build_recon_dict

def process_acm_author_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # ACM DL Author search placeholder (requires specific scraper or API key)
        query_response[queryId] = {"result": [{"id": "ACM_AUTHOR_SEARCH", "name": f"ACM Author: {query_text}", "score": 80, "match": False}]}
    return query_response
