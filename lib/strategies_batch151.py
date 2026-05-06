import requests
from .strategies_helpers import _build_recon_dict

def process_batch151_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 151: Core National Authorities & Regional Administration.
    Finalizing high-signal systemic nodes from the master registry.
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        # Systemic Pattern
        results = [{"id": f"{sub_type}_SYS", "name": f"{sub_type} Authority: {query_text}", "score": 85, "match": False}]
            
        query_response[queryId] = {"result": results}
    return query_response
