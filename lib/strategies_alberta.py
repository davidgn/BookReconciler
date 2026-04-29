import requests
from .strategies_helpers import _build_recon_dict

def process_alberta_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # Alberta Register of Historic Places (Proxy search)
        url = "https://hermis.alberta.ca/ARHP/Default.aspx"
        # Since this is a scrape-based source, we return a search link as placeholder
        query_response[queryId] = {"result": [{"id": "ALBERTA_SEARCH", "name": f"Alberta Historic: {query_text}", "score": 60, "match": False}]}
    return query_response
