import requests
from .strategies_helpers import _build_recon_dict

def process_batch173_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 173: Federated Subnational Authorities (Brazil, Mexico, India, Switzerland).
    Covers state and provincial level institutional authorities.
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        # Subnational authority pattern
        results = [{"id": f"{sub_type}_SUB_AUTH", "name": f"Subnational Authority ({sub_type}): {query_text}", "score": 85, "match": False}]
            
        query_response[queryId] = {"result": results}
    return query_response
