import requests
from .strategies_helpers import _build_recon_dict

def process_japanta_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # Japan NTA Corporate Number API
        url = f"https://www.houjin-bangou.nta.go.jp/api/search/name?name={query_text}&type=02"
        query_response[queryId] = {"result": [{"id": "NTA_SEARCH", "name": f"Japan NTA: {query_text}", "score": 75, "match": False}]}
    return query_response
