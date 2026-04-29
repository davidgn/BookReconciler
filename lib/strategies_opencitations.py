import requests
from .strategies_helpers import _build_recon_dict

def process_opencitations_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = f"https://opencitations.net/meta/api/v1/metadata/{query_text}"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                results = r.json()
                matches = []
                for res in results[:5]:
                    matches.append({
                        "id": res.get('doi', ''),
                        "name": res.get('title', ''),
                        "score": 80,
                        "match": False,
                        "type": [{"id": "Work", "name": "Work"}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
