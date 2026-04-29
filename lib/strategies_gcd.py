import requests
from .strategies_helpers import _build_recon_dict

def process_gcd_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # GCD API
        url = f"https://www.comics.org/api/publisher/?name={query_text}"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                results = r.json().get('results', [])
                matches = []
                for res in results:
                    matches.append({
                        "id": str(res.get('id', '')),
                        "name": res.get('name', ''),
                        "score": 90 if res.get('name').lower() == query_text.lower() else 70,
                        "match": res.get('name').lower() == query_text.lower(),
                        "type": [{"id": "Publisher", "name": "Publisher"}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
