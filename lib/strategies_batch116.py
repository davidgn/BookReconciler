import requests
import xml.etree.ElementTree as ET
from .strategies_helpers import _build_recon_dict

def process_batch116_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 116: Regional, State, and Union Catalogs (Phase 5).
    Supported sub_types: 'HEBIS', 'KOBV', 'BVB', 'HBZ', 'MASS_STATE', 'MICH_STATE', 'WASH_STATE', 'GA_STATE', 'BC_LEG', 'ONT_LEG'
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        results = []
        target = sub_type.upper() if sub_type else ""
        
        if target in ['HEBIS', 'KOBV', 'BVB', 'HBZ']:
            results = _search_german_union(query_text, target)
        elif target in ['MASS_STATE', 'MICH_STATE', 'WASH_STATE', 'GA_STATE']:
            results = _search_us_state(query_text, target)
        elif target in ['BC_LEG', 'ONT_LEG']:
            results = _search_can_prov(query_text, target)
        else:
            results = []
            
        query_response[queryId] = {"result": results}
    return query_response

def _search_german_union(query_text, target):
    endpoints = {
        'HEBIS': "http://sru.hebis.de/sru/DB=2.1",
        'KOBV': "https://sru.kobv.de/k2",
        'BVB': "https://bvbr.bib-bvb.de/sru/bvb01sru",
        'HBZ': "https://sru.hbz-nrw.de/"
    }
    url = endpoints.get(target)
    # German SRUs often use 'tit' or 'pica.tit' or 'dc.title'
    params = {
        'operation': 'searchRetrieve',
        'version': '1.1',
        'query': f'title="{query_text}"',
        'maximumRecords': 5
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": f"{target}_SRU", "name": f"{target}: {query_text}", "score": 80, "match": False}]
    except: pass
    return []

def _search_us_state(query_text, target):
    # Placeholders for US State Libraries often requiring specific gateway logic
    return [{"id": f"{target}_SRU", "name": f"{target}: {query_text}", "score": 75, "match": False}]

def _search_can_prov(query_text, target):
    # Placeholders for Canadian Provincial Libraries
    return [{"id": f"{target}_SRU", "name": f"{target}: {query_text}", "score": 75, "match": False}]
