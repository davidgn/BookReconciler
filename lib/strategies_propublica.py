import requests
from .strategies_helpers import _build_recon_dict

def process_propublica_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = "https://projects.propublica.org/nonprofits/api/v2/search.json"
        params = {'q': query_text}
        try:
            r = requests.get(url, params=params, timeout=10)
            if r.status_code == 200:
                results = r.json().get('organizations', [])
                matches = []
                for res in results[:5]:
                    matches.append({
                        "id": str(res.get('ein', '')),
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
