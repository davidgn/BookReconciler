import requests
from .strategies_helpers import _build_recon_dict

def process_artic_query(query, passed_config, endpoint_type="artists"):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = f"https://api.artic.edu/api/v1/{endpoint_type}/search?q={query_text}"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                results = r.json().get('data', [])
                matches = []
                for res in results[:5]:
                    matches.append({
                        "id": str(res.get('id', '')),
                        "name": res.get('title', ''),
                        "score": 90,
                        "match": False,
                        "type": [{"id": "Artist" if endpoint_type == "artists" else "Work", "name": "Artist" if endpoint_type == "artists" else "Work"}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
