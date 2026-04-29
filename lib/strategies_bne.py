import requests
from .strategies_helpers import _build_recon_dict

def process_bne_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # BNE SPARQL
        url = "https://datos.bne.es/sparql"
        sparql = f"""
        SELECT ?p ?label WHERE {{
          ?p a <https://datos.bne.es/def/C1005> .
          ?p <http://www.w3.org/2000/01/rdf-schema#label> ?label .
          FILTER(regex(?label, "{query_text}", "i"))
        }} LIMIT 5
        """
        try:
            # Added verify=False for BNE's certificate issues
            r = requests.get(url, params={{'query': sparql, 'format': 'json'}}, timeout=10, verify=False)
            if r.status_code == 200:
                bindings = r.json().get('results', {{}}).get('bindings', [])
                matches = []
                for b in bindings:
                    uri = b['p']['value']
                    label = b['label']['value']
                    matches.append({{
                        "id": uri,
                        "name": label,
                        "score": 90,
                        "match": False,
                        "type": [{"id": "Person", "name": "Person"}]
                    }})
                query_response[queryId] = {{"result": matches}}
            else:
                query_response[queryId] = {{"result": []}}
        except:
            query_response[queryId] = {{"result": []}}
    return query_response
