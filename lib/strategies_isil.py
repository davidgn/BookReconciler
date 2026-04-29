import requests
from .strategies_helpers import _build_recon_dict

def process_isil_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # ISIL Registry W3ID JSON-LD search (approximate search)
        url = f"https://w3id.org/isil/search?q={query_text}"
        try:
            r = requests.get(url, headers={'Accept': 'application/json'}, timeout=10)
            if r.status_code == 200:
                results = r.json().get('results', [])
                matches = []
                for res in results[:5]:
                    matches.append({
                        "id": res.get('isil', ''),
                        "name": res.get('name', ''),
                        "score": 90,
                        "match": False,
                        "type": [{"id": "Organization", "name": "Organization"}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
