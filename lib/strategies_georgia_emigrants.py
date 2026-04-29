import requests
from .strategies_helpers import _build_recon_dict

def process_georgia_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # Biographical Dictionary of Emigrants of Georgia
        url = f"http://www.nplg.gov.ge/emigrants/en/search?q={query_text}"
        try:
            # Simple placeholder as they don't have a clean JSON search
            query_response[queryId] = {"result": [{"id": "GEORGIA_SEARCH", "name": f"Georgia Emigrant: {query_text}", "score": 80, "match": False}]}
        except:
            query_response[queryId] = {"result": []}
    return query_response
