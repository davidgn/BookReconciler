import requests
from .strategies_helpers import _build_recon_dict

def process_threesixtygiving_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # 360Giving character data search
        url = "https://findthatcharity.org.uk/search"
        params = {'q': query_text}
        try:
            r = requests.get(url, params=params, timeout=10)
            # FindThatCharity is the best web-proxy for 360Giving
            query_response[queryId] = {"result": [{"id": "360G_SEARCH", "name": f"360Giving/Charity: {query_text}", "score": 80, "match": False}]}
        except:
            query_response[queryId] = {"result": []}
    return query_response
