from .strategies_helpers import _build_recon_dict

def process_batch104_query(query, passed_config, name_prefix):
    """
    Batch 104: Final Global National Libraries & Archives series.
    Asia: India, Japan, Korea, Singapore, Malaysia, Taiwan, Sri Lanka, Bangladesh, Pakistan.
    Europe: Austria, Slovenia, Bosnia, Croatia, Hungary, Georgia, Armenia, Switzerland, Denmark.
    Americas/Caribbean: Bolivia, Argentina (State), Bahamas, Barbados, Belize, Guyana, Haiti.
    Africa: Ethiopia, Ghana, Kenya, Nigeria, Rwanda, Senegal, Tanzania, Uganda, Zimbabwe, Ivory Coast.
    Special: Vatican, Biodiversity Heritage Library, IFLA.
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
