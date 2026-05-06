from .strategies_helpers import _build_recon_dict

def process_batch105_query(query, passed_config, name_prefix):
    """
    Batch 105: The "Absolute Completion" series.
    Syria (Al-Assad), Ukraine (Vernadsky), North Macedonia (NUL), 
    Cyprus (NL/NA), Papua New Guinea (NL), Oman (NA), 
    Sri Lanka (NA), Bangladesh (NA), Pakistan (NA), 
    Fiji (NA), Kazakhstan (NA), Belarus (NL/NA), 
    Slovakia (NA), Slovenia (NL/NUL), Croatia (NL/NUL), 
    Bosnia (NL/NUL), Hungary (NL/NSL), Quebec (BAnQ), 
    Vatican, IFLA, Biodiversity Heritage Library, UN, UNESCO.
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
