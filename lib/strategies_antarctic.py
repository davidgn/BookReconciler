import requests
from .strategies_helpers import _build_recon_dict

def process_antarctic_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # Australian Antarctic Gazetteer CKAN API
        url = f"https://data.aad.gov.au/api/3/action/package_search?q={query_text}"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                # Basic placeholder for Antarctic locations
                query_response[queryId] = {"result": [{"id": "AAD_SEARCH", "name": f"Antarctic: {query_text}", "score": 80, "match": False}]}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
