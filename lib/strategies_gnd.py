import requests
from .strategies_helpers import _build_recon_dict

def process_gnd_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # Lobid GND API
        url = f"https://lobid.org/gnd/search?q={query_text}&format=json&size=5"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                items = r.json().get('member', [])
                matches = []
                for item in items:
                    gnd_id = item.get('gndIdentifier', '')
                    label = item.get('preferredName', '')
                    matches.append({
                        "id": gnd_id,
                        "name": label,
                        "score": 100 if label.lower() == query_text.lower() else 85,
                        "match": label.lower() == query_text.lower(),
                        "type": [{"id": "Person", "name": "Person"}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
