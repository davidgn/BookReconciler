import requests
from .strategies_helpers import _build_recon_dict

def process_charity_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # UK Charity Commission API
        url = f"https://api.charitycommission.gov.uk/register/api/search-charities?query={query_text}"
        query_response[queryId] = {"result": [{"id": "UK_CHARITY", "name": f"Charity: {query_text}", "score": 85, "match": False}]}
    return query_response
