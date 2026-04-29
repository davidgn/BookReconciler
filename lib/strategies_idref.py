import requests
from .strategies_helpers import _build_recon_dict

def process_idref_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = f"https://www.idref.fr/SUDOC/automated/search?q=persname_t:({query_text})"
        # Simplified parser for IdRef
        try:
            r = requests.get(url, params={'wt': 'json', 'rows': 5}, timeout=10)
            if r.status_code == 200:
                docs = r.json().get('response', {}).get('docs', [])
                matches = []
                for doc in docs:
                    matches.append({
                        "id": doc.get('ppn_z', ''),
                        "name": doc.get('affcourt_z', ''),
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
