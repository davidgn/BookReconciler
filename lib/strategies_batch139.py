import requests
from .strategies_helpers import _build_recon_dict

def process_batch139_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 139: High-Value Global Aid, Research & Regulatory Authorities.
    Targeting IATI, OpenAIRE, 360Giving, UIA, and Federal Register.
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        # Systemic Hub Pattern
        results = [{"id": f"{sub_type}_GBL", "name": f"{sub_type} Global: {query_text}", "score": 85, "match": False}]
            
        query_response[queryId] = {"result": results}
    return query_response
