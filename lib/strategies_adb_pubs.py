import requests
from .strategies_helpers import _build_recon_dict

def process_adb_pubs_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # ADB Publications search link proxy
        query_response[queryId] = {"result": [{"id": "ADB_PUB_SEARCH", "name": f"ADB Pub: {query_text}", "score": 80, "match": False}]}
    return query_response
