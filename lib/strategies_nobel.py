import requests
from .strategies_helpers import _build_recon_dict

def process_nobel_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = f"https://api.nobelprize.org/2.1/laureates?name={query_text}"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                results = r.json().get('laureates', [])
                matches = []
                for res in results[:5]:
                    name = res.get('knownName', {}).get('en', query_text)
                    matches.append({
                        "id": str(res.get('id', '')),
                        "name": name,
                        "score": 100 if name.lower() == query_text.lower() else 90,
                        "match": name.lower() == query_text.lower(),
                        "type": [{"id": "Person", "name": "Person"}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
