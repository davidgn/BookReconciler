import requests
from .strategies_helpers import _build_recon_dict

def process_rs_memoirs_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # Crossref search filtered for Royal Society Memoirs (10.1098/rsbm)
        url = f"https://api.crossref.org/works?query.bibliographic={query_text}&filter=issn:0080-4606&rows=5"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                items = r.json().get('message', {}).get('items', [])
                matches = []
                for item in items:
                    title = item.get('title', [query_text])[0]
                    matches.append({
                        "id": item.get('DOI', ''),
                        "name": title,
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
