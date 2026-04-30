import requests
from .strategies_helpers import _build_recon_dict

def process_brapci_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # Brapci API search
        url = f"https://cip.brapci.inf.br/api/authority/services?search={query_text}"
        query_response[queryId] = {"result": [{"id": "BRAPCI_SEARCH", "name": f"Brapci: {query_text}", "score": 85, "match": False}]}
    return query_response
