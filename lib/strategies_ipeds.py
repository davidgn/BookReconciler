import requests
from .strategies_helpers import _build_recon_dict

def process_ipeds_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # IPEDS / US Dept of Ed API
        url = f"https://api.data.gov/ed/collegescorecard/v1/schools?school.name={query_text}&fields=id,school.name"
        query_response[queryId] = {"result": [{"id": "IPEDS_SEARCH", "name": f"IPEDS: {query_text}", "score": 80, "match": False}]}
    return query_response
