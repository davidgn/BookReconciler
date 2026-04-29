import requests
import xml.etree.ElementTree as ET
from .strategies_helpers import _build_recon_dict

def process_nla_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = "https://trove.nla.gov.au/sru/index"
        params = {
            'operation': 'searchRetrieve',
            'version': '1.1',
            'query': f'text="{query_text}"',
            'maximumRecords': 5,
            'recordSchema': 'info:srw/schema/1/marcxml-v1.1'
        }
        try:
            r = requests.get(url, params=params, timeout=10)
            if r.status_code == 200:
                # Trove SRU results
                query_response[queryId] = {"result": [{"id": "NLA_SRU", "name": f"NLA/Trove: {query_text}", "score": 70, "match": False}]}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
