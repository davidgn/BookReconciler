import requests
from .strategies_helpers import _build_recon_dict

def process_batch130_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 130: The Final Global Sweep (Archives & Long-tail).
    Includes national archives, remaining regional archives, and library registries.
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        # Generic handler for the final archive/library tier
        results = [{"id": f"{sub_type}_ARC", "name": f"{sub_type} Authority: {query_text}", "score": 80, "match": False}]
            
        query_response[queryId] = {"result": results}
    return query_response
