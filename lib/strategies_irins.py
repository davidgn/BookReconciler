from .strategies_helpers import _build_recon_dict
def process_irins_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        query_response[queryId] = {"result": [{"id": "IRINS_SEARCH", "name": f"IRINS India: {query[queryId]['query']}", "score": 85, "match": False}]}
    return query_response
