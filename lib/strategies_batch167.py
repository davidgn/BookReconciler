import requests
from .strategies_helpers import _build_recon_dict

def process_batch167_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 167: Regional Scholarly Networks & Scientific Registries.
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        # Systemic Pattern for Regional Hubs
        results = [{"id": f"{sub_type}_HUB", "name": f"{sub_type}: {query_text}", "score": 85, "match": False}]
            
        query_response[queryId] = {"result": results}
    return query_response
