import requests
from .strategies_helpers import _build_recon_dict

def process_canada_historic_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # Open Canada API for Historic Places
        url = f"https://open.canada.ca/data/en/api/3/action/package_search?q={query_text}"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                results = r.json().get('result', {}).get('results', [])
                matches = []
                for res in results[:5]:
                    matches.append({
                        "id": res.get('id', ''),
                        "name": res.get('title', ''),
                        "score": 90,
                        "match": False,
                        "type": [{"id": "Place", "name": "Place"}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
