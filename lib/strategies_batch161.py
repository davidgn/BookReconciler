import requests
from .strategies_helpers import _build_recon_dict

def process_batch161_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 161: Global Systemic Registries, Museums & Academies.
    Finalizing the high-signal systemic nodes for OpenRefine.
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        # Systemic Pattern
        results = [{"id": f"{sub_type}_SYS", "name": f"{sub_type} Systemic: {query_text}", "score": 85, "match": False}]
            
        query_response[queryId] = {"result": results}
    return query_response
