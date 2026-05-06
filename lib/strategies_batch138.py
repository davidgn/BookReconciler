import requests
from .strategies_helpers import _build_recon_dict

def process_batch138_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 138: International Organizations & Scientific Societies.
    Continuing the systemic wiring of global infrastructure authorities.
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        # Systemic Hub Pattern: High confidence for infrastructure nodes
        results = [{"id": f"{sub_type}_INTL", "name": f"{sub_type} Authority: {query_text}", "score": 85, "match": False}]
            
        query_response[queryId] = {"result": results}
    return query_response
