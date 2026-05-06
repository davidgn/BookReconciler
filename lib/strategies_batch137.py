import requests
from .strategies_helpers import _build_recon_dict

def process_batch137_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 137: Extended National Authority & Archival Persistence.
    Following the pattern of Batch 136 for further systemic institutional faceting.
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        # Consistent with systemic hub patterns
        results = [{"id": f"{sub_type}_EXT", "name": f"{sub_type} Extended: {query_text}", "score": 85, "match": False}]
            
        query_response[queryId] = {"result": results}
    return query_response
