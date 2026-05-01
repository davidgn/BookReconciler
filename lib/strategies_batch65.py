from .strategies_helpers import _build_recon_dict
def process_batch65_query(query, passed_config, name_prefix):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        query_response[queryId] = {"result": [{"id": f"{name_prefix}_SEARCH", "name": f"{name_prefix}: {query[queryId]['query']}", "score": 90, "match": False}]}
    return query_response
