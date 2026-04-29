import requests
from .strategies_helpers import _build_recon_dict

def process_doaj_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = f"https://doaj.org/api/v2/search/journals/{query_text}"
        params = {'pageSize': 5}
        try:
            r = requests.get(url, params=params, timeout=10)
            if r.status_code == 200:
                results = r.json().get('results', [])
                matches = []
                for res in results:
                    bib = res.get('bibjson', {})
                    matches.append({
                        "id": bib.get('eissn', bib.get('pissn', '')),
                        "name": bib.get('title', ''),
                        "score": 80,
                        "match": False,
                        "type": [{"id": "Journal", "name": "Journal"}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
