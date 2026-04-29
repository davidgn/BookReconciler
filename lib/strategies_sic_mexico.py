import requests
from .strategies_helpers import _build_recon_dict

def process_sic_mexico_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # SIC Mexico search (heuristic/proxy to their web search)
        url = f"https://sic.cultura.gob.mx/buscar.php?q={query_text}"
        # SIC Mexico usually requires browser headers
        headers = {'User-Agent': 'Mozilla/5.0'}
        try:
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                # Basic placeholder as SIC doesn't have a clean JSON API
                query_response[queryId] = {"result": [{"id": "SIC_SEARCH", "name": f"SIC Mexico: {query_text}", "score": 60, "match": False}]}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
