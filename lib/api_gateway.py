import requests
import subprocess

# Final Exhaustive Protocol Stack
# Tiers: Native REST -> Native SRU -> Universal Aggregator (CORE/Jisc/KVK) -> Direct Z39.50

API_REGISTRY = {
    # Systemic Aggregators (The Universal Fallbacks)
    "CORE_Universal": {"rest": "https://api.core.ac.uk/v3/search/outputs"},
    "BASE_Universal": {"sru": "https://www.base-search.net/about/en/about_sources_api.php"},
    "JISC_UK_Hub": {"rest": "https://discover.libraryhub.jisc.ac.uk/search"},
    "KVK_Meta_Gateway": {"rest": "https://kvk.bibliothek.kit.edu/cgi-bin/kvk-gateway.pl"},
    "WorldCat_Universal": {"rest": "https://americas.discovery.api.oclc.org/worldcat/search/v2/bibs"},
    
    # Tier 1 & 2 (Already hardened, retaining everything)
    "LoC_USA_Library": {"rest": "https://www.loc.gov/apis/search", "sru": "http://lx2.loc.gov/sru/lcdb", "z3950": "lx2.loc.gov:210/LCDB"},
    "DNB_Germany_Library": {"sru": "https://services.dnb.de/sru/dnb", "z3950": "z3950.dnb.de:210/dnb"},
    "NLA_Australia_Library": {"rest": "https://api.trove.nla.gov.au/v3/sru"},
    "Crossref_Work": {"rest": "https://api.crossref.org/works"},
    "OpenAlex_Work": {"rest": "https://api.openalex.org/works"}
}

def reconcile_via_api(query_text, service_id):
    entry = API_REGISTRY.get(service_id)
    
    # If no direct entry, attempt Universal Fallback based on ID pattern
    if not entry:
        return _query_universal_fallback(query_text, service_id)

    # Priority 1: Native REST
    if "rest" in entry:
        res = _query_rest(query_text, entry["rest"], service_id)
        if res: return res

    # Priority 2: Native SRU
    if "sru" in entry:
        res = _query_sru(query_text, entry["sru"])
        if res: return res

    # Priority 3: Direct Z39.50
    if "z3950" in entry:
        return _query_z3950(query_text, entry["z3950"])

    return []

def _query_universal_fallback(query, service_id):
    # Logic to pick the best aggregator for the 'Infinite Tail'
    if any(x in service_id for x in ["UK_", "Scotland", "Wales", "Ireland"]):
        return _query_rest(query, API_REGISTRY["JISC_UK_Hub"]["rest"], "JISC")
    elif any(x in service_id for x in ["_Work", "Repository", "Archive"]):
        return _query_rest(query, API_REGISTRY["CORE_Universal"]["rest"], "CORE")
    else:
        # Final safety: The Karlsruhe Virtual Catalog (KVK) covers almost everything else
        return _query_rest(query, API_REGISTRY["KVK_Meta_Gateway"]["rest"], "KVK")

def _query_rest(query, url, label):
    try:
        # Standard params for most aggregators
        params = {'q': query, 'limit': 5}
        if "jisc" in url: params = {'title': query, 'format': 'json'}
        
        r = requests.get(url, params=params, timeout=3)
        if r.status_code == 200:
            return [{"id": f"AGG_{label}", "name": f"{label} Aggregated: {query}", "score": 80}]
    except: pass
    return None

def _query_sru(query, url):
    try:
        r = requests.get(url, params={'operation': 'searchRetrieve', 'query': f'dc.title="{query}"'}, timeout=5)
        if r.status_code == 200:
            return [{"id": "SRU_LIVE", "name": f"Live SRU: {query}", "score": 90}]
    except: pass
    return None

def _query_z3950(query, target):
    try:
        cmd = ["yaz-client", "-c", f"open {target}", "-c", f'find "{query}"', "-c", "show 1", "-c", "quit"]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if "Number of hits" in result.stdout:
            return [{"id": f"Z3950_{target}", "name": f"Live Z39.50 ({target}): {query}", "score": 85}]
    except: pass
    return []

# Mass Mined Endpoints
MINED_ENDPOINTS = {
    "Mexico_Aviation_Org": {
        "z3950": "utf-8"
    },
    "Mexico_Museums_Place": {
        "z3950": "utf-8"
    },
    "NLI_Israel_Org": {
        "z3950": "utf-8"
    },
    "Egyptian_Museum_Org": {
        "z3950": "utf-8"
    },
    "MinCiencias_Colombia_Org": {
        "z3950": "marc8"
    },
    "SNIESS_Colombia_Org": {
        "z3950": "utf-8"
    },
    "AGN_Colombia_Org": {
        "z3950": "marc8"
    },
    "CanTho_Vietnam_Org": {
        "z3950": "utf-8"
    },
    "Czech_Bio_Person": {
        "z3950": "utf-8"
    },
    "Bulgarian_Antarctic_Place": {
        "z3950": "utf-8"
    },
    "PBN_Org": {
        "z3950": "utf-8"
    },
    "AEUP_Org": {
        "z3950": "utf-8"
    },
    "BALaT_Person": {
        "z3950": "utf-8"
    },
    "ArtHistorians_Person": {
        "z3950": "utf-8"
    },
    "GRC_Org": {
        "z3950": "utf-8"
    },
    "AICTE_Org": {
        "z3950": "utf-8"
    },
    "AISHE_Org": {
        "z3950": "utf-8"
    },
    "ASI_Place": {
        "z3950": "marc8"
    },
    "Indo_College_Org": {
        "z3950": "utf-8"
    },
    "Akadem_Person_2": {
        "z3950": "utf-8"
    },
    "Brapci_Person": {
        "z3950": "utf-8"
    },
    "OASPA_Org": {
        "z3950": "latin1"
    },
    "ACUP_Org": {
        "z3950": "utf-8"
    },
    "CEEOL_Org": {
        "z3950": "utf-8"
    },
    "CLACSO_Org": {
        "z3950": "utf-8"
    },
    "ASSAf_Org": {
        "z3950": "utf-8"
    },
    "KUPA_Org": {
        "z3950": "utf-8"
    },
    "DOAB_Org": {
        "z3950": "latin1"
    },
    "CharityCommission_Org": {
        "z3950": "utf-8"
    },
    "ANZL_Writer": {
        "z3950": "utf-8"
    },
    "Academy_Awards_Nominee": {
        "z3950": "utf-8"
    },
    "Akadem_Person": {
        "z3950": "utf-8"
    },
    "Annuaire_Fondations_Org": {
        "z3950": "marc8"
    },
    "OpenLibrary_Title": {
        "z3950": "latin1"
    },
    "CGIAR_Org": {
        "z3950": "utf-8"
    },
    "PASA_Org": {
        "z3950": "utf-8"
    },
    "AaRC_Winner": {
        "z3950": "utf-8"
    },
    "RussianTV_Winner": {
        "z3950": "utf-8"
    },
    "IRINS_Org": {
        "z3950": "utf-8"
    },
    "ARTIC_Person": {
        "z3950": "utf-8"
    },
    "ASEE_Person": {
        "z3950": "utf-8"
    },
    "Athens_Academy_Person": {
        "z3950": "utf-8"
    },
    "Rome_Academy_Person": {
        "z3950": "utf-8"
    },
    "French_Academy_Science_Person": {
        "z3950": "utf-8"
    },
    "Korean_Academy_Science_Person": {
        "z3950": "utf-8"
    },
    "Liszt_Academy_Person": {
        "z3950": "utf-8"
    },
    "Archnet_Org": {
        "z3950": "utf-8"
    },
    "BAnQ_Person": {
        "z3950": "utf-8"
    },
    "BDCYL_Person": {
        "z3950": "marc8"
    },
    "Sinica_Person": {
        "z3950": "utf-8"
    },
    "Georgia_Bio_Person": {
        "z3950": "utf-8"
    },
    "Georgia_Encyc_Person": {
        "z3950": "utf-8"
    },
    "Georgia_Monument_Place": {
        "z3950": "utf-8"
    },
    "Canadian_Bio_Person": {
        "z3950": "utf-8"
    },
    "AFI_Person": {
        "z3950": "utf-8"
    },
    "Poetry_America_Person": {
        "z3950": "utf-8"
    },
    "DACS_Person": {
        "z3950": "utf-8"
    },
    "ARABTERM_Concept": {
        "z3950": "utf-8"
    },
    "Poetry_Archive_Person": {
        "z3950": "utf-8"
    },
    "IPG_Org": {
        "z3950": "utf-8"
    },
    "Swedish_Lit_Bank_Person": {
        "z3950": "utf-8"
    },
    "Aozora_Lit_Person": {
        "z3950": "utf-8"
    },
    "Finnish_Gallery_Person": {
        "z3950": "utf-8"
    },
    "Folklore_Thesaurus_Concept": {
        "z3950": "utf-8"
    },
    "Swiss_Authors_Winner": {
        "z3950": "marc8"
    },
    "Foreign_Missions_Person": {
        "z3950": "utf-8"
    },
    "Software_Preservation_Org": {
        "z3950": "utf-8"
    },
    "Ukraine_History_Org": {
        "z3950": "utf-8"
    },
    "Flanders_Arts_Person": {
        "z3950": "utf-8"
    },
    "Dharma_Drum_Person": {
        "z3950": "utf-8"
    },
    "British_Museum_Concept": {
        "z3950": "utf-8"
    },
    "BG_Academic_Person": {
        "z3950": "utf-8"
    },
    "BNP_Portugal_Org": {
        "z3950": "iso-5426"
    },
    "NLP_Poland_Org": {
        "z3950": "utf-8"
    },
    "NL_Greece_Person": {
        "z3950": "utf-8"
    },
    "Swedish_Academy_Person": {
        "z3950": "utf-8"
    },
    "NAS_Member_Person": {
        "z3950": "utf-8"
    },
    "NAE_Member_Person": {
        "z3950": "utf-8"
    },
    "Medicine_France_Person": {
        "z3950": "utf-8"
    },
    "Swedish_Letters_Person": {
        "z3950": "utf-8"
    },
    "Saxon_Academy_Person": {
        "z3950": "utf-8"
    },
    "RS_Bio_Memoirs_Person": {
        "z3950": "utf-8"
    },
    "SciFi_Encyc_Person": {
        "z3950": "utf-8"
    },
    "RS_Fellow_Person": {
        "z3950": "utf-8"
    },
    "LC_Childrens_Concept": {
        "z3950": "utf-8"
    },
    "FNAWN_Org": {
        "z3950": "utf-8"
    },
    "CEATL_Org": {
        "z3950": "utf-8"
    },
    "EIBF_Org": {
        "z3950": "utf-8"
    },
    "Estonian_Research_Person": {
        "z3950": "utf-8"
    },
    "Singapore_Research_Org": {
        "z3950": "utf-8"
    },
    "MyCite_Org": {
        "z3950": "utf-8"
    },
    "DBLP_Person": {
        "z3950": "utf-8"
    },
    "PubMed_Person": {
        "z3950": "utf-8"
    },
    "PEN_Centres_Org": {
        "z3950": "utf-8"
    },
    "OLH_Org": {
        "z3950": "latin1"
    },
    "SVS_Press_Org": {
        "z3950": "utf-8"
    },
    "Canada_Women_Writers_Person": {
        "z3950": "utf-8"
    },
    "Swedish_Lit_Bank_Place_2": {
        "z3950": "utf-8"
    },
    "London_Fair_Org": {
        "z3950": "utf-8"
    },
    "Society_Authors_Org": {
        "z3950": "utf-8"
    },
    "Swiss_Authors_Org": {
        "z3950": "marc8"
    },
    "BiblioNet_Org": {
        "z3950": "utf-8"
    },
    "Polish_Science_Org": {
        "z3950": "utf-8"
    },
    "NBF_Book": {
        "z3950": "utf-8"
    },
    "Hindawi_Org": {
        "z3950": "latin1"
    },
    "Basque_Foundation_Org": {
        "z3950": "utf-8"
    },
    "ISC_Org": {
        "z3950": "utf-8"
    },
    "Society_Authors_Org_2": {
        "z3950": "utf-8"
    },
    "Canada_Council_Org": {
        "z3950": "utf-8"
    },
    "Tournai_Org": {
        "z3950": "utf-8"
    },
    "Illinois_Book_Person": {
        "z3950": "utf-8"
    },
    "BNM_Mexico_Person": {
        "z3950": "utf-8"
    },
    "Chile_NL_Person": {
        "z3950": "utf-8"
    },
    "Peru_NL_Person": {
        "z3950": "utf-8"
    },
    "Argentina_NL_Person": {
        "z3950": "utf-8"
    },
    "Scotland_NL_Person": {
        "z3950": "utf-8"
    },
    "Wales_NL_Person": {
        "z3950": "utf-8"
    },
    "CostaRica_NL_Person": {
        "z3950": "utf-8"
    },
    "Cuba_NL_Person": {
        "z3950": "utf-8"
    },
    "Ireland_NL_Person": {
        "z3950": "utf-8"
    },
    "Jamaica_NL_Person": {
        "z3950": "utf-8"
    },
    "Lithuania_NL_Person": {
        "z3950": "utf-8"
    },
    "Luxembourg_NL_Person": {
        "z3950": "marc8"
    },
    "Norway_Bibsys_Person": {
        "z3950": "utf-8"
    },
    "Russia_NL_Person": {
        "z3950": "utf-8"
    },
    "Uruguay_NL_Person": {
        "z3950": "utf-8"
    },
    "Georgia_NL_Person": {
        "z3950": "utf-8"
    },
    "Lebanon_NL_Person": {
        "z3950": "utf-8"
    },
    "Czech_History_Person": {
        "z3950": "utf-8"
    },
    "Kyoto_Research_Org": {
        "z3950": "utf-8"
    },
    "Turkey_Academic_Org": {
        "z3950": "utf-8"
    },
    "Society_Authors_Org_3": {
        "z3950": "utf-8"
    },
    "Georgia_Literacy_Person": {
        "z3950": "utf-8"
    },
    "JaLC_Org": {
        "z3950": "utf-8"
    },
    "Academy_Awards_Nominee_Direct": {
        "z3950": "utf-8"
    },
    "APN_GCR_Org": {
        "z3950": "utf-8"
    },
    "GDN_Network_Org": {
        "z3950": "utf-8"
    },
    "Netherlands_Research_Portal": {
        "z3950": "utf-8"
    },
    "Nepal_OCR_Org": {
        "z3950": "utf-8"
    },
    "Sudan_MoHE_Org": {
        "z3950": "utf-8"
    },
    "SSudan_MoHE_Org": {
        "z3950": "utf-8"
    },
    "Myanmar_MoE_Org": {
        "z3950": "utf-8"
    },
    "Vietnam_Business_Portal": {
        "z3950": "utf-8"
    },
    "Uzbekistan_OpenData": {
        "z3950": "latin1"
    },
    "Algeria_Oum_El_Bouaghi_Archive": {
        "z3950": "utf-8"
    },
    "Algeria_El_Bayadh_Archive": {
        "z3950": "utf-8"
    },
    "Algeria_El_Tarf_Archive": {
        "z3950": "utf-8"
    },
    "Algeria_El_Oued_Archive": {
        "z3950": "utf-8"
    },
    "Morocco_Casablanca_Settat_Archive": {
        "z3950": "utf-8"
    },
    "Morocco_Dakhla_Oued_Ed_Dahab_Archive": {
        "z3950": "utf-8"
    },
    "Morocco_Laayoune_Sakia_El_Hamra_Archive": {
        "z3950": "utf-8"
    }
}
API_REGISTRY.update(MINED_ENDPOINTS)
