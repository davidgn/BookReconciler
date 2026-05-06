import requests
from .strategies_helpers import _build_recon_dict

def process_batch172_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 172: Non-Sovereign & Territorial Library/Archive Hubs.
    Covers dependent territories and autonomous regions.
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        # Territorial authority pattern
        results = [{"id": f"{sub_type}_TERR_AUTH", "name": f"Territorial Authority ({sub_type}): {query_text}", "score": 85, "match": False}]
            
        query_response[queryId] = {"result": results}
    return query_response
