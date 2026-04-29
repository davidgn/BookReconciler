import requests
from .strategies_helpers import _build_recon_dict

def process_hal_tel_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = f"https://api.archives-ouvertes.fr/search/tel/?q={query_text}&wt=json&rows=5"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                docs = r.json().get('response', {}).get('docs', [])
                matches = []
                for doc in docs:
                    matches.append({
                        "id": doc.get('docid', ''),
                        "name": doc.get('title_s', [query_text])[0],
                        "score": 90,
                        "match": False,
                        "type": [{"id": "Work", "name": "Work"}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
