from .strategies_helpers import _build_recon_dict

def process_ifacca_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # IFACCA directory placeholder
        query_response[queryId] = {"result": [{"id": "IFACCA_DIR", "name": f"IFACCA Member: {query_text}", "score": 60, "match": False}]}
    return query_response
