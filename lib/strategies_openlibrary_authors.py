import requests
from .strategies_helpers import _build_recon_dict

def process_ol_authors_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = f"https://openlibrary.org/search/authors.json?q={query_text}"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                docs = r.json().get('docs', [])
                matches = []
                for doc in docs[:5]:
                    matches.append({
                        "id": doc.get('key', ''),
                        "name": doc.get('name', ''),
                        "score": 90,
                        "match": False,
                        "type": [{"id": "Person", "name": "Person"}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
