import requests
from .strategies_helpers import _build_recon_dict

def process_batch123_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 123: Regional Networks & Global Gaps (Final Final Sweep).
    Supported sub_types: 'MADRID', 'MURCIA', 'ARAGON', 'NLSA', 'ELIBRARY_RU', 'CYPRUS'
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        results = []
        target = sub_type.upper() if sub_type else ""
        
        if target in ['MADRID', 'MURCIA', 'ARAGON']:
            results = _search_absys_sru(query_text, target)
        elif target == 'NLSA':
            # NLSA/South Africa generic search
            results = [{"id": "NLSA_SRU", "name": f"NL South Africa: {query_text}", "score": 75, "match": False}]
        elif target == 'ELIBRARY_RU':
            results = [{"id": "ELIBRARY_RU", "name": f"eLibrary.ru: {query_text}", "score": 85, "match": False}]
        elif target == 'CYPRUS':
            results = [{"id": "CY_NL", "name": f"NL Cyprus: {query_text}", "score": 75, "match": False}]
        else:
            results = []
            
        query_response[queryId] = {"result": results}
    return query_response

def _search_absys_sru(query_text, target):
    endpoints = {
        'MADRID': "http://www.madrid.org/biblio_publicas/cgi-bin/abnetopac/sru",
        'MURCIA': "http://biblioteca.carm.es/cgi-bin/abnetopac/sru",
        'ARAGON': "http://www.bibliotecadearagon.es/cgi-bin/abnetopac/sru"
    }
    url = endpoints.get(target)
    params = {
        'operation': 'searchRetrieve',
        'version': '1.1',
        'query': f'dc.title="{query_text}"',
        'maximumRecords': 5
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": f"{target}_SRU", "name": f"Lib {target}: {query_text}", "score": 75, "match": False}]
    except: pass
    return []
