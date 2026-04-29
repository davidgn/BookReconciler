import requests
from .strategies_helpers import _build_recon_dict

def process_crossref_funder_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = f"https://api.crossref.org/funders?query={query_text}"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                results = r.json().get('message', {}).get('items', [])
                matches = []
                for res in results[:5]:
                    matches.append({
                        "id": res.get('id', ''),
                        "name": res.get('name', ''),
                        "score": 90 if res.get('name').lower() == query_text.lower() else 70,
                        "match": res.get('name').lower() == query_text.lower(),
                        "type": [{"id": "Funder", "name": "Funder"}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
