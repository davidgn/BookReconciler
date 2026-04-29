import requests
from .strategies_helpers import _build_recon_dict

def process_sirene_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = "https://recherche-entreprises.api.gouv.fr/search"
        params = {'q': query_text, 'per_page': 5}
        try:
            r = requests.get(url, params=params, timeout=10)
            if r.status_code == 200:
                results = r.json().get('results', [])
                matches = []
                for res in results:
                    matches.append({
                        "id": res.get('siren', ''),
                        "name": res.get('nom_complet', ''),
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
