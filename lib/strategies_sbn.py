import requests
import xml.etree.ElementTree as ET
from .strategies_helpers import _build_recon_dict

def process_sbn_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = "https://opac.sbn.it/opacSRU"
        params = {
            'operation': 'searchRetrieve',
            'version': '1.1',
            'query': f'sub=" {query_text} "',
            'maximumRecords': 5,
            'recordSchema': 'isbd'
        }
        try:
            r = requests.get(url, params=params, timeout=10)
            if r.status_code == 200:
                root = ET.fromstring(r.text)
                matches = []
                # Very basic XML extraction for SBN
                for record in root.findall('.//{http://www.loc.gov/zing/srw/}recordData'):
                    matches.append({
                        "id": "SBN_ID", # Complex to extract from ISBD schema without full parser
                        "name": record.text or "SBN Record",
                        "score": 70,
                        "match": False,
                        "type": [{"id": "Work", "name": "Work"}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
