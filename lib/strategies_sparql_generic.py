import requests
from .strategies_helpers import _build_recon_dict

def process_sparql_generic_query(query, passed_config, sparql_template, endpoint_url="https://query.wikidata.org/sparql", type_name="Person"):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item.get('query') or reconcile_item.get('title') or data.get('query', '')

        sparql = sparql_template.replace("QUERY_TEXT", query_text)
        try:
            r = requests.get(endpoint_url, params={'query': sparql, 'format': 'json'}, timeout=10)
            if r.status_code == 200:
                bindings = r.json().get('results', {}).get('bindings', [])
                matches = []
                for b in bindings:
                    uri = b['item']['value']
                    label = b['itemLabel']['value']
                    matches.append({
                        "id": uri.split('/')[-1],
                        "name": label,
                        "score": 90,
                        "match": False,
                        "type": [{"id": type_name, "name": type_name}]
                    })
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
