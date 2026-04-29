import requests
import re
from .strategies_helpers import _build_recon_dict

def process_tgn_query(query, passed_config):
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['query']
        
        url = "https://www.getty.edu/vow/TGNServlet"
        params = {'find': query_text, 'place': '', 'nation': '', 'english': 'Y', 'page': 1}
        try:
            r = requests.get(url, params=params, timeout=10)
            if r.status_code == 200:
                text = r.text
                matches = []
                for match in re.finditer(r'TGN(?:FullDisplay|Hierarchy)\?[^"]*subjectid=(\d+)[^"]*"[^>]*>(.*?)</a>', text, re.I | re.S):
                    matches.append({
                        "id": match.group(1),
                        "name": match.group(2).strip(),
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
