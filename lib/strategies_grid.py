import requests
from .strategies_helpers import _build_recon_dict

def process_grid_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # GRID is now integrated into ROR, so we use the ROR query but filter for status
        url = f"https://api.ror.org/organizations?query={query_text}"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                items = r.json().get('items', [])
                matches = []
                for item in items:
                    matches.append({
                        "id": item.get('id', ''),
                        "name": item.get('name', ''),
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
