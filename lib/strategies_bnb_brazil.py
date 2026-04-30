import requests
import xml.etree.ElementTree as ET
from .strategies_helpers import _build_recon_dict

def process_bnb_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # BNB SRU search
        url = "http://acervo.bn.gov.br/sophia_web/sru"
        params = {
            'operation': 'searchRetrieve',
            'version': '1.1',
            'query': f'dc.title="{query_text}"',
            'maximumRecords': 5
        }
        try:
            r = requests.get(url, params=params, timeout=10)
            # Simplified placeholder for BNB results
            query_response[queryId] = {"result": [{"id": "BNB_SEARCH", "name": f"BNB Brazil: {query_text}", "score": 85, "match": False}]}
        except:
            query_response[queryId] = {"result": []}
    return query_response
