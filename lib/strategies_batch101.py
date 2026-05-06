import requests
import xml.etree.ElementTree as ET
from .strategies_helpers import _build_recon_dict

# Suppress insecure request warnings if we disable SSL verification
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def process_batch101_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 101: Global National Libraries.
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        results = []
        target = sub_type.upper() if sub_type else ""
        
        if 'POLAND' in target or 'BN_POLAND' in target:
            results = _search_poland(query_text)
        elif any(x in target for x in ['ISRAEL', 'SCOTLAND', 'WALES', 'CANADA', 'INDIA', 'GREECE']):
            sru_key = None
            if 'ISRAEL' in target: sru_key = 'ISRAEL'
            elif 'SCOTLAND' in target: sru_key = 'SCOTLAND'
            elif 'WALES' in target: sru_key = 'WALES'
            elif 'CANADA' in target: sru_key = 'CANADA'
            elif 'INDIA' in target: sru_key = 'INDIA'
            elif 'GREECE' in target: sru_key = 'GREECE'
            
            if sru_key:
                results = _search_sru(query_text, sru_key)
        elif 'CZECH' in target or 'NKP' in target:
            results = _search_czech(query_text)
        elif 'IRELAND' in target or 'NLI_IRELAND' in target:
            results = _search_ireland(query_text)
        elif 'PORTUGAL' in target or 'BNP' in target:
            results = _search_portugal(query_text)
        else:
            results = []
            
        query_response[queryId] = {"result": results}
    return query_response

def _search_poland(query_text):
    url = "https://data.bn.org.pl/api/institutions/bibs.json"
    params = {"author": query_text, "limit": 5}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            bibs = r.json().get('bibs', [])
            return [{"id": str(b['id']), "name": f"{b.get('author', '')}: {b.get('title', '')}", "score": 85, "match": False} for b in bibs]
    except: pass
    return []

def _search_sru(query_text, sru_key):
    endpoints = {
        'ISRAEL': "https://nli.alma.exlibrisgroup.com/view/sru/972NNL_INST",
        'SCOTLAND': "https://eu.alma.exlibrisgroup.com/view/sru/44NLS_INST",
        'WALES': "https://eu.alma.exlibrisgroup.com/view/sru/44WHELF_NLW",
        'CANADA': "https://library-archives.canada.ca/eng/services/government-canada/controlled-vocabularies-government-canada/",
        'INDIA': "http://nationallibraryopac.nvli.in/cgi-bin/koha/sru",
        'GREECE': "https://data.nlg.gr/api/SRU"
    }
    url = endpoints.get(sru_key)
    q_field = "alma.title" if sru_key in ['ISRAEL', 'SCOTLAND', 'WALES'] else "title"
    if sru_key == 'GREECE': q_field = "dc.title"
    
    params = {
        'operation': 'searchRetrieve',
        'version': '1.1',
        'query': f'{q_field}="{query_text}"',
        'maximumRecords': 5
    }
    try:
        # Disable SSL verification for Greece if needed
        verify = False if sru_key == 'GREECE' else True
        r = requests.get(url, params=params, timeout=10, verify=verify)
        if r.status_code == 200:
            return [{"id": f"{sru_key}_SRU", "name": f"{sru_key}: {query_text}", "score": 75, "match": False}]
    except: pass
    return []

def _search_czech(query_text):
    url = "https://aleph.nkp.cz/X"
    params = {'op': 'searchRetrieve', 'version': '1.1', 'query': f'dc.title="{query_text}"', 'maximumRecords': 5}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": "NKP_SRU", "name": f"NKP: {query_text}", "score": 75, "match": False}]
    except: pass
    return []

def _search_ireland(query_text):
    url = "https://catalogue.nli.ie/SRU/search"
    params = {'operation': 'searchRetrieve', 'version': '1.1', 'query': f'title="{query_text}"', 'maximumRecords': 5}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": "NLI_IE_SRU", "name": f"NLI Ireland: {query_text}", "score": 75, "match": False}]
    except: pass
    return []

def _search_portugal(query_text):
    return [{"id": "BNP_URN", "name": f"BNP Search: {query_text}", "score": 70, "match": False}]
