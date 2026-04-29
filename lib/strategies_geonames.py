import requests
import html
import re
from .strategies_helpers import _build_recon_dict

def process_geonames_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = "https://www.geonames.org/search.html"
        params = {'q': query_text}
        try:
            r = requests.get(url, params=params, timeout=10)
            if r.status_code == 200:
                text = r.text
                matches = []
                # Simple regex to extract geonameid and label from search table
                for match in re.finditer(r'<a href="/(\d+)/[^"]+\.html">([^<]+)</a>', text, re.I | re.S):
                    matches.append({
                        "id": match.group(1),
                        "name": html.unescape(match.group(2)).strip(),
                        "score": 90,
                        "match": False,
                        "type": [{"id": "Location", "name": "Location"}]
                    })
                    if len(matches) >= 5: break
                query_response[queryId] = {"result": matches}
            else:
                query_response[queryId] = {"result": []}
        except:
            query_response[queryId] = {"result": []}
    return query_response
