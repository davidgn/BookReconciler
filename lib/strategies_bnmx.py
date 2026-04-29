import requests
from .strategies_helpers import _build_recon_dict

def process_bnmx_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # BNMX keyword search placeholder
        query_response[queryId] = {"result": [{"id": "BNMX_SEARCH", "name": f"BNMX Mexico: {query_text}", "score": 75, "match": False}]}
    return query_response
