import requests
from .strategies_helpers import _build_recon_dict

def process_sherpa_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # Sherpa/Romeo V2 API
        url = f"https://v2.sherpa.ac.uk/cgi/retrieve?item-type=publication&format=json&filter=[[\"issn\",\"equals\",\"{query_text}\"]]"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                # Basic placeholder for journal-level reconciliation
                query_response[queryId] = {"result": [{"id": "SHERPA_SEARCH", "name": f"Sherpa/Romeo: {query_text}", "score": 90, "match": False}]}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
