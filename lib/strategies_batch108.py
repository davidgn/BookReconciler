from .strategies_helpers import _build_recon_dict

def process_batch108_query(query, passed_config, name_prefix):
    """
    Batch 108: Finalizing National Library Stragglers.
    China (NLC), Indonesia (NL), Finland (NL Work), Chile (CNL), 
    Costa Rica (NL), Cuba (NL), Aruba (NL), Medicine (NLM), 
    Turkey (NL), Iran (NL), South Korea (NL), Singapore (NL), Malaysia (NL).
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        query_response[queryId] = {
            "result": [
                {
                    "id": f"{name_prefix}_SEARCH",
                    "name": f"{name_prefix}: {query[queryId]['query']}",
                    "score": 85,
                    "match": False
                }
            ]
        }
    return query_response
