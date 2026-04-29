import requests
from .strategies_helpers import _build_recon_dict

def process_datacite_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = f"https://api.datacite.org/dois?query={query_text}&resource-type-id=Text&page[size]=5"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                results = r.json().get('data', [])
                matches = []
                for res in results:
                    attr = res.get('attributes', {{}})
                    doi = res.get('id', '')
                    title = attr.get('titles', [{{}}])[0].get('title', doi)
                    matches.append({{
                        "id": doi,
                        "name": title,
                        "score": 80,
                        "match": False,
                        "type": [{"id": "Work", "name": "Work"}]
                    }})
                query_response[queryId] = {{"result": matches}}
            else:
                query_response[queryId] = {{"result": []}}
        except:
            query_response[queryId] = {{"result": []}}
    return query_response
