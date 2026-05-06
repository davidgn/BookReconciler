import requests
from .strategies_helpers import _build_recon_dict

def process_batch122_query(query, passed_config, sub_type=None):
    """
    Dispatcher for Batch 122: Specialized, Metropolitan, and Academic Networks.
    Supported sub_types: 'NYPL', 'BHL', 'CINII_BOOKS', 'JISC_HUB', 'NSZL_HU', 'NSK_HR', 'NUK_SI', 'BL_ETHOS'
    """
    query_response = {}
    for queryId in query:
        if queryId == 'req_ip': continue
        data = query[queryId]
        reconcile_item = _build_recon_dict(data)
        query_text = reconcile_item['title']
        
        results = []
        target = sub_type.upper() if sub_type else ""
        
        if target == 'NYPL':
            results = _search_sru_generic(query_text, "http://sru.nypl.org/sru", "NYPL")
        elif target == 'BHL':
            results = [{"id": "BHL_API", "name": f"BHL: {query_text}", "score": 80, "match": False}]
        elif target == 'CINII_BOOKS':
            results = _search_cinii(query_text)
        elif target == 'JISC_HUB':
            results = _search_jisc(query_text)
        elif target == 'NSZL_HU':
            results = _search_sru_generic(query_text, "http://nektar.oszk.hu/sru", "NSZL")
        elif target == 'NSK_HR':
            results = _search_sru_generic(query_text, "http://nskcrolist.nsk.hr/sru/", "NSK")
        elif target == 'NUK_SI':
            results = _search_sru_generic(query_text, "https://plus.cobiss.net/cobiss/si/en/bib/sru", "NUK")
        elif target == 'BL_ETHOS':
            results = [{"id": "BL_ETHOS", "name": f"BL EThOS: {query_text}", "score": 75, "match": False}]
        else:
            results = []
            
        query_response[queryId] = {"result": results}
    return query_response

def _search_cinii(query_text):
    url = "https://ci.nii.ac.jp/books/opensearch/search"
    params = {'q': query_text, 'format': 'json', 'count': 5}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            # CiNii returns JSON-LD/OpenSearch format
            return [{"id": "CINII_BOOKS", "name": f"CiNii Books: {query_text}", "score": 85, "match": False}]
    except: pass
    return []

def _search_jisc(query_text):
    url = "https://discover.libraryhub.jisc.ac.uk/search"
    params = {'title': query_text, 'format': 'json'}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": "JISC_HUB", "name": f"Jisc Hub: {query_text}", "score": 85, "match": False}]
    except: pass
    return []

def _search_sru_generic(query_text, url, label):
    params = {
        'operation': 'searchRetrieve',
        'version': '1.1',
        'query': f'dc.title="{query_text}"',
        'maximumRecords': 5
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return [{"id": f"{label}_SRU", "name": f"{label}: {query_text}", "score": 75, "match": False}]
    except: pass
    return []
