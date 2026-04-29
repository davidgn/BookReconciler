import requests
from .strategies_helpers import _build_recon_dict

def process_wp_json_query(query, passed_config, endpoint_url, type_name="Organization"):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # WordPress JSON API search
        url = f"{endpoint_url}?search={query_text}"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                results = r.json()
                matches = []
                for res in results[:5]:
                    title = res.get('title', {}).get('rendered', '')
                    matches.append({
                        "id": str(res.get('id', '')),
                        "name": title,
                        "score": 90 if title.lower() == query_text.lower() else 70,
                        "match": title.lower() == query_text.lower(),
                        "type": [{"id": type_name, "name": type_name}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
