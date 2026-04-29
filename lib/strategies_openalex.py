import requests
import json
from .strategies_helpers import _build_recon_dict

def process_openalex_query(query, passed_config):
    query_response = {}
    
    for queryId in query:
        if queryId == 'req_ip': continue
        
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # Search OpenAlex Publishers
        url = f"https://api.openalex.org/publishers?search={query_text}"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                results = r.json().get('results', [])
                matches = []
                for res in results[:5]:
                    matches.append({
                        "id": res.get('id', ''),
                        "name": res.get('display_name', ''),
                        "score": 100 if res.get('display_name').lower() == query_text.lower() else 75,
                        "match": res.get('display_name').lower() == query_text.lower(),
                        "type": [{"id": "Publisher", "name": "Publisher"}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
            
    return query_response
