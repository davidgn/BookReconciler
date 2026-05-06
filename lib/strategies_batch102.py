from .strategies_helpers import _build_recon_dict

def process_batch102_query(query, passed_config, name_prefix):
    """
    Batch 102: Expanding National Libraries
    Norway, Mexico (UNAM), NZ (DigitalNZ), Australia (Trove v3), Russia (RSL),
    Greece (NLG), Brazil (BNB), Argentina (CAL), South Africa (PASA), 
    Bulgaria, Romania, Serbia, Thailand, Vietnam, Philippines.
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
