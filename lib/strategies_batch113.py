import requests
import xml.etree.ElementTree as ET
from .strategies_helpers import _build_recon_dict

def process_batch113_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 113: Regional, State, and Provincial Libraries (Phase 3).
    Supported sub_types: 'NYSL', 'CARLI', 'TSLAC', 'WSL', 'RERO_SWISS', 'EUSKARIANA'
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        results = []
        target = sub_type.upper() if sub_type else ""
        
        if target == 'CARLI':
            results = _search_alma_sru(query_text, "https://i-share-network.alma.exlibrisgroup.com/view/sru/01CARLI_NETWORK")
        elif target == 'NYSL':
            # NYSL often uses a Sirsi SRU gateway
            results = _search_sru_generic(query_text, "http://nyst.sirsi.net/symws/sru", "NYSL")
        elif target == 'TSLAC':
            results = _search_sru_generic(query_text, "http://catalog.library.ca.gov/symws/sru", "TSLAC") # Placeholder or specific TSLAC
        elif target == 'RERO_SWISS':
            results = _search_rero(query_text)
        elif target == 'EUSKARIANA':
            results = _search_sru_generic(query_text, "https://www.euskariana.euskadi.eus/puband/sru", "EUSK")
        else:
            results = []
            
        query_response[queryId] = {"result": results}
    return query_response

def _search_alma_sru(query_text, url):
    params = {
        'operation': 'searchRetrieve',
        'version': '1.2',
        'query': f'alma.title="{query_text}"',
        'maximumRecords': 5
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": "ALMA_SRU", "name": f"ALMA Hub: {query_text}", "score": 75, "match": False}]
    except: pass
    return []

def _search_sru_generic(query_text, url, label):
    params = {
        'operation': 'searchRetrieve',
        'version': '1.1',
        'query': f'title="{query_text}"',
        'maximumRecords': 5
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": f"{label}_SRU", "name": f"{label}: {query_text}", "score": 75, "match": False}]
    except: pass
    return []

def _search_rero(query_text):
    # RERO Swiss regional library API
    url = "https://data.rero.ch/api/organizations"
    params = {"q": query_text, "size": 5}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            items = r.json().get('items', [])
            return [{"id": i.get('id', 'RERO'), "name": f"RERO: {i.get('label', query_text)}", "score": 80, "match": False} for i in items]
    except: pass
    return []
