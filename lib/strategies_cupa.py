from .strategies_helpers import _build_recon_dict
def process_cupa_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        query_response[queryId] = {"result": [{"id": "CUPA_SEARCH", "name": f"CUPA: {query[queryId]['query']}", "score": 80, "match": False}]}
    return query_response
