import requests
from .strategies_helpers import _build_recon_dict

def process_nta_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        # NTA SPARQL
        url = "https://data.bibliotheken.nl/sparql"
        sparql = f"""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?s ?label WHERE {{
          ?s a <http://schema.org/Person> .
          ?s rdfs:label ?label .
          FILTER(regex(?label, "{query_text}", "i"))
        }} LIMIT 5
        """
        try:
            r = requests.get(url, params={'query': sparql, 'format': 'json'}, timeout=10)
            if r.status_code == 200:
                bindings = r.json().get('results', {}).get('bindings', [])
                matches = []
                for b in bindings:
                    matches.append({
                        "id": b['s']['value'].split('/')[-1],
                        "name": b['label']['value'],
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
