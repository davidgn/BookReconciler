import requests
from .strategies_helpers import _build_recon_dict

def process_pen_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # PEN Centres via Wikidata
        url = "https://query.wikidata.org/sparql"
        sparql = f"""
        SELECT ?item ?itemLabel WHERE {{
          ?item p:P6209 [].
          ?item rdfs:label ?itemLabel.
          FILTER(regex(?itemLabel, "{query_text}", "i"))
          FILTER(LANG(?itemLabel) = "en")
        }} LIMIT 5
        """
        try:
            r = requests.get(url, params={{'query': sparql, 'format': 'json'}}, timeout=10)
            if r.status_code == 200:
                bindings = r.json().get('results', {{}}).get('bindings', [])
                matches = []
                for b in bindings:
                    matches.append({{
                        "id": b['item']['value'].split('/')[-1],
                        "name": b['itemLabel']['value'],
                        "score": 90,
                        "match": False,
                        "type": [{"id": "Organization", "name": "Organization"}]
                    }})
                query_response[queryId] = {{"result": matches}}
            else:
                query_response[queryId] = {{"result": []}}
        except:
            query_response[queryId] = {{"result": []}}
    return query_response
