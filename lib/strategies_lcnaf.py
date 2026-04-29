import requests
from .strategies_helpers import _build_recon_dict

def process_lcnaf_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = f"https://id.loc.gov/authorities/names/suggest/?q={query_text}"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                # LC Suggest returns [query, labels, descriptions, uris]
                data = r.json()
                labels = data[1]
                uris = data[3]
                matches = []
                for i in range(min(len(labels), 5)):
                    matches.append({
                        "id": uris[i].split('/')[-1],
                        "name": labels[i],
                        "score": 95 if labels[i].lower() == query_text.lower() else 85,
                        "match": labels[i].lower() == query_text.lower(),
                        "type": [{"id": "Person", "name": "Person"}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
