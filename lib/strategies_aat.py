import requests
import json
from .strategies_helpers import _build_recon_dict

def process_aat_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # Getty AAT JSON service
        url = f"http://vocab.getty.edu/sparql.json"
        sparql = f"""
        select ?s ?label {{
          ?s a skos:Concept; luc:term "{query_text}"; gvp:prefLabelGVP [skosxl:literalForm ?label].
          filter (exists {{?s gvp:broaderExtended aat:300027150}}) # Broader: Awards/Prizes
        }} limit 5
        """
        try:
            r = requests.get(url, params={{'query': sparql}}, timeout=10)
            if r.status_code == 200:
                bindings = r.json().get('results', {{}}).get('bindings', [])
                matches = []
                for b in bindings:
                    uri = b['s']['value']
                    label = b['label']['value']
                    matches.append({{
                        "id": uri,
                        "name": label,
                        "score": 90,
                        "match": False,
                        "type": [{"id": "Award", "name": "Award"}]
                    }})
                query_response[queryId] = {{"result": matches}}
            else:
                query_response[queryId] = {{"result": []}}
        except:
            query_response[queryId] = {{"result": []}}
    return query_response
