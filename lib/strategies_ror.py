import requests
import json
from .strategies_helpers import _build_recon_dict

def process_ror_query(query, passed_config):
    query_response = {}
    
    # query is a dict of {id: {query: "...", type: "..."}}
    # we need to skip 'req_ip'
    for queryId in query:
        if queryId == 'req_ip': continue
        
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # Search ROR
        url = f"https://api.ror.org/organizations?query={query_text}"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                results = r.json().get('items', [])
                matches = []
                for res in results[:5]:
                    # Extract QID if present
                    qid = ""
                    ext_ids = res.get('external_ids', {})
                    if 'Wikidata' in ext_ids:
                        qid = ext_ids['Wikidata'].get('preferred', '')
                    
                    matches.append({
                        "id": res.get('id', ''),
                        "name": res.get('name', ''),
                        "score": 100 if res.get('name').lower() == query_text.lower() else 80,
                        "match": res.get('name').lower() == query_text.lower(),
                        "type": [{"id": "Organization", "name": "Organization"}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
            
    return query_response
