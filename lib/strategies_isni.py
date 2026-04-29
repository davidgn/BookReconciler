import requests
import re
from .strategies_helpers import _build_recon_dict

def process_isni_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = "https://isni.oclc.org/sru/"
        params = {
            'operation': 'searchRetrieve',
            'query': f'pica.nw = "{query_text}"',
            'recordSchema': 'isni-b', 'maximumRecords': 5,
            'version': '1.1',
        }
        try:
            r = requests.get(url, params=params, timeout=10)
            if r.status_code == 200:
                isnies = re.findall(r'<isniUnformatted>(\d{16})</isniUnformatted>', r.text)
                # Note: simplified label extraction for reconciler
                matches = []
                for raw in isnies:
                    isni = f'{raw[:4]} {raw[4:8]} {raw[8:12]} {raw[12:]}'
                    matches.append({
                        "id": isni,
                        "name": isni, # Use ID as name if label is complex to parse here
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
