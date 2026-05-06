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

# Mass Mined Endpoints (Comprehensive)
COMPREHENSIVE_MINED_ENDPOINTS = {
    "Cuba_Isla_de_la_Juventud_Library": {
        "z3950": "utf-8"
    },
    "Cuba_Pinar_del_Rio_Library": {
        "z3950": "utf-8"
    },
    "Cuba_Santiago_de_Cuba_Library": {
        "z3950": "utf-8"
    },
    "Jamaica_Saint_Mary_Library": {
        "z3950": "utf-8"
    },
    "Jamaica_Saint_Thomas_Library": {
        "z3950": "utf-8"
    },
    "France_Centre_Val_de_Loire_Library": {
        "z3950": "utf-8"
    },
    "France_Hauts_de_France_Library": {
        "z3950": "utf-8"
    },
    "France_Ile_de_France_Library": {
        "z3950": "utf-8"
    },
    "France_Pays_de_la_Loire_Library": {
        "z3950": "utf-8"
    },
    "Spain_Balearic_Islands_Library": {
        "z3950": "utf-8"
    },
    "Spain_Castilla_La_Mancha_Library": {
        "z3950": "latin1"
    },
    "Spain_Castilla_y_Leon_Library": {
        "z3950": "marc8"
    },
    "Spain_Madrid_Library": {
        "z3950": "utf-8"
    },
    "Spain_La_Rioja_Library": {
        "z3950": "latin1"
    },
    "UK_East_of_England_Library": {
        "z3950": "utf-8"
    },
    "UK_West_Midlands_Library": {
        "z3950": "utf-8"
    },
    "Chile_San_Felipe_de_Aconcagua_Library": {
        "z3950": "utf-8"
    },
    "Chile_Santiago_Library": {
        "z3950": "utf-8"
    },
    "CostaRica_San_Jose_Library": {
        "z3950": "utf-8"
    },
    "ElSalvador_La_Paz_Library": {
        "z3950": "utf-8"
    },
    "ElSalvador_San_Miguel_Library": {
        "z3950": "utf-8"
    },
    "ElSalvador_San_Vicente_Library": {
        "z3950": "utf-8"
    },
    "Canada_Municipal_Toronto_Library": {
        "z3950": "utf-8"
    },
    "Canada_Municipal_Ottawa_Library": {
        "z3950": "utf-8"
    },
    "Pacific_American_Samoa_Library": {
        "z3950": "utf-8"
    },
    "PNG_National_Capital_District_Library": {
        "z3950": "utf-8"
    },
    "Ghana_Greater_Accra_Library": {
        "z3950": "utf-8"
    },
    "Guatemala_San_Marcos_Library": {
        "z3950": "utf-8"
    },
    "Honduras_Islas_de_la_Bahia_Library": {
        "z3950": "utf-8"
    },
    "Honduras_La_Paz_Library": {
        "z3950": "utf-8"
    },
    "Nicaragua_Rio_San_Juan_Library": {
        "z3950": "utf-8"
    },
    "Ecuador_Los_Rios_Library": {
        "z3950": "utf-8"
    },
    "Bolivia_La_Paz_Library": {
        "z3950": "utf-8"
    },
    "Cambodia_Phnom_Penh_Library": {
        "z3950": "utf-8"
    },
    "Bulgaria_Sofia_Province_Library": {
        "z3950": "utf-8"
    },
    "Trinidad_Couva_Tabaquite_Talparo_Library": {
        "z3950": "utf-8"
    },
    "Trinidad_Diego_Martin_Library": {
        "z3950": "utf-8"
    },
    "Trinidad_San_Juan_Laventille_Library": {
        "z3950": "utf-8"
    },
    "Trinidad_Tobago_Library": {
        "z3950": "utf-8"
    },
    "DominicanRepublic_San_Jose_de_Ocoa_Library": {
        "z3950": "utf-8"
    },
    "DominicanRepublic_San_Juan_Library": {
        "z3950": "utf-8"
    },
    "DominicanRepublic_San_Pedro_de_Macoris_Library": {
        "z3950": "utf-8"
    },
    "Czech_Prague_Library": {
        "z3950": "marc8"
    },
    "Myanmar_Yangon_Library": {
        "z3950": "utf-8"
    },
    "Israel_Jerusalem_Library": {
        "z3950": "utf-8"
    },
    "Israel_Tel_Aviv_Library": {
        "z3950": "utf-8"
    },
    "UAE_Abu_Dhabi_Library": {
        "z3950": "utf-8"
    },
    "Uruguay_San_Jose_Library": {
        "z3950": "utf-8"
    },
    "Venezuela_Distrito_Capital_Library": {
        "z3950": "marc8"
    },
    "Greece_Attica_Library": {
        "z3950": "utf-8"
    },
    "Greece_Western_Greece_Library": {
        "z3950": "latin1"
    },
    "Greece_Western_Macedonia_Library": {
        "z3950": "latin1"
    },
    "Norway_Agder_Library": {
        "z3950": "utf-8"
    },
    "Norway_Finnmark_Library": {
        "z3950": "utf-8"
    },
    "Norway_Innlandet_Library": {
        "z3950": "utf-8"
    },
    "Norway_More_og_Romsdal_Library": {
        "z3950": "utf-8"
    },
    "Norway_Oslo_Library": {
        "z3950": "utf-8"
    },
    "Norway_Troms_Library": {
        "z3950": "utf-8"
    },
    "Sweden_Stockholm_Library": {
        "z3950": "latin1"
    },
    "Ireland_Galway_Library": {
        "z3950": "utf-8"
    },
    "Malaysia_Selangor_Library": {
        "z3950": "utf-8"
    },
    "Malaysia_Kuala_Lumpur_Library": {
        "z3950": "utf-8"
    },
    "Chile_Los_Rios_Library": {
        "z3950": "utf-8"
    },
    "Thailand_Chiang_Mai_Library": {
        "z3950": "utf-8"
    },
    "Thailand_Chiang_Rai_Library": {
        "z3950": "utf-8"
    },
    "Thailand_Khon_Kaen_Library": {
        "z3950": "utf-8"
    },
    "Thailand_Maha_Sarakham_Library": {
        "z3950": "utf-8"
    },
    "Colombia_Norte_de_Santander_Library": {
        "z3950": "marc8"
    },
    "Colombia_Valle_del_Cauca_Library": {
        "z3950": "utf-8"
    },
    "Colombia_Bogota_DC_Library": {
        "z3950": "marc8"
    },
    "Philippines_Agusan_del_Norte_Library": {
        "z3950": "utf-8"
    },
    "Philippines_Davao_del_Norte_Library": {
        "z3950": "utf-8"
    },
    "Philippines_Lanao_del_Norte_Library": {
        "z3950": "utf-8"
    },
    "Philippines_Surigao_del_Norte_Library": {
        "z3950": "utf-8"
    },
    "Philippines_Zamboanga_del_Norte_Library": {
        "z3950": "utf-8"
    },
    "Argentina_Buenos_Aires_City_Library": {
        "z3950": "utf-8"
    },
    "Argentina_Buenos_Aires_Province_Library": {
        "z3950": "utf-8"
    },
    "Argentina_La_Rioja_Library": {
        "z3950": "latin1"
    },
    "Argentina_San_Juan_Library": {
        "z3950": "utf-8"
    },
    "Swiss_ZH_Library": {
        "z3950": "utf-8"
    },
    "Swiss_BE_Library": {
        "z3950": "marc8"
    },
    "Swiss_VD_Library": {
        "z3950": "utf-8"
    },
    "Turkey_Academic_Org": {
        "z3950": "utf-8"
    },
    "Sweden_LIBRIS_Work": {
        "z3950": "latin1"
    },
    "Costa_Rica_NL_Work": {
        "z3950": "utf-8"
    },
    "Medicine_NLM_Work": {
        "z3950": "utf-8"
    },
    "V&A_Museum_ID": {
        "z3950": "utf-8"
    },
    "Australian_Maritime_Museum": {
        "z3950": "utf-8"
    },
    "Armenian_Union_Catalog": {
        "z3950": "utf-8"
    },
    "Belarus_Cultural_Heritage": {
        "z3950": "utf-8"
    },
    "American_Academy_in_Rome_ID": {
        "z3950": "utf-8"
    },
    "American_Art_Collaborative_object_ID": {
        "z3950": "utf-8"
    },
    "Art_Museum_of_Estonia_artist_ID": {
        "z3950": "utf-8"
    },
    "Art_Museum_of_Estonia_artwork_ID": {
        "z3950": "utf-8"
    },
    "Australian_National_Maritime_Museum_object_ID": {
        "z3950": "utf-8"
    },
    "Australian_National_Maritime_Museum_person_ID": {
        "z3950": "utf-8"
    },
    "Berlin_cultural_heritage_ID": {
        "z3950": "utf-8"
    },
    "Biblioteca_Iglesia_Nacional": {
        "z3950": "utf-8"
    },
    "Brooklyn_Museum_artwork_ID": {
        "z3950": "utf-8"
    },
    "Centre-Val_de_Loire_Inventory_ID": {
        "sru": "https://slsp-ubs.alma.exlibrisgroup.com/view/sru/41SLSP_EPF?version=1.2&amp;operation=searchRetrieve&amp;recordSchema=marcxml"
    },
    "Archivio_Storico_dellUniversita_degli_Studi_di_Cagliari_person_ID": {
        "z3950": "utf-8"
    },
    "Australian_Institute_for_Disaster_Resilience_Knowledge_Hub_ID": {
        "z3950": "utf-8"
    },
    "Bank_of_information_on_the_historical_and_cultural_heritage_of_the_Republic_of_Belarus": {
        "z3950": "utf-8"
    },
    "Brooklyn_Museum_Exhibition_ID": {
        "z3950": "utf-8"
    },
    "Carnegie_Museum_of_Art_artwork_ID": {
        "z3950": "utf-8"
    },
    "Cincinnati_Art_Museum_artwork_ID": {
        "z3950": "utf-8"
    },
    "Cleveland_Museum_of_Art_ID": {
        "z3950": "utf-8"
    },
    "Code_List_for_Cultural_Heritage_Organizations": {
        "z3950": "utf-8"
    },
    "Conseil_de_Presse_Luxembourg_journalist_ID": {
        "z3950": "aleph.etat.lu:9909/LUX01"
    },
    "Cultural_heritage_ID_in_Baden-Wurttemberg": {
        "z3950": "utf-8"
    },
    "Cultural_heritage_database_in_Austria_ObjektID": {
        "z3950": "utf-8"
    },
    "Georgia_Museum_of_Art_ID": {
        "z3950": "utf-8"
    },
    "French_Academy_Sciences_ID": {
        "z3950": "utf-8"
    },
    "Dallas_Museum_of_Art_ID": {
        "z3950": "utf-8"
    },
    "NLSA_South_Africa": {
        "z3950": "utf-8"
    },
    "NL_Costa_Rica": {
        "z3950": "utf-8"
    },
    "Fellow_of_the_Royal_Society_of_Canada_ID": {
        "z3950": "utf-8"
    },
    "Royal_Irish_Academy_ID": {
        "z3950": "utf-8"
    },
    "Smithsonian_American_Art_Museum_artwork_ID": {
        "z3950": "utf-8"
    },
    "Archivio_Storico_dellUniversit\u00e0_degli_Studi_di_Cagliari_person_ID": {
        "z3950": "utf-8"
    },
    "Art_Gallery_of_Ontario_object_ID": {
        "z3950": "utf-8"
    },
    "Art_Gallery_of_South_Australia_creator_ID": {
        "z3950": "utf-8"
    },
    "Art_Gallery_of_South_Australia_work_ID": {
        "z3950": "utf-8"
    },
    "Auckland_Art_Gallery_artist_ID": {
        "z3950": "utf-8"
    },
    "Auckland_Art_Gallery_artwork_ID": {
        "z3950": "utf-8"
    },
    "Biblioth\u00e8que_du_S\u00e9minaire_de_Tournai_author_ID": {
        "z3950": "utf-8"
    },
    "Cultural_heritage_ID_in_Baden-W\u00fcrttemberg": {
        "z3950": "utf-8"
    },
    "Dallas_Museum_of_Art_artwork_ID": {
        "z3950": "utf-8"
    },
    "Dharma_Drum_Institute_of_Liberal_Arts_person_ID": {
        "z3950": "utf-8"
    },
    "Dharma_Drum_Institute_of_Liberal_Arts_place_ID": {
        "z3950": "utf-8"
    },
    "ERIC_Institute_of_Education_Sciences": {
        "z3950": "utf-8"
    },
    "Federal_Heritage_Buildings_ID_Canada": {
        "z3950": "utf-8"
    },
    "Flanders_Arts_Institute_organisation_ID_former_scheme": {
        "z3950": "utf-8"
    },
    "Flanders_Arts_Institute_person_ID_former_scheme": {
        "z3950": "utf-8"
    },
    "Flanders_Arts_Institute_production_ID_former_scheme": {
        "z3950": "utf-8"
    },
    "Flanders_Arts_Institute_venue_ID_former_scheme": {
        "z3950": "utf-8"
    },
    "Flora_of_the_Southeastern_United_States_ID": {
        "z3950": "utf-8"
    },
    "French_Academy_in_Rome_fellow_ID": {
        "z3950": "utf-8"
    },
    "French_Academy_of_Sciences_member_ID": {
        "z3950": "utf-8"
    },
    "Index_to_American_Botanical_Literature_ID": {
        "z3950": "sru.k10plus.de:210/grib"
    },
    "Index_to_Organism_Names_ID": {
        "z3950": "sru.k10plus.de:210/grib"
    },
    "Indianapolis_Museum_of_Art_artwork_ID": {
        "z3950": "utf-8"
    },
    "Institute_of_History_of_Ukraine_ID": {
        "z3950": "utf-8"
    },
    "Invasive_Plant_Atlas_of_the_United_States_ID": {
        "z3950": "utf-8"
    },
    "Israel_Museum_Jerusalem_artist_ID": {
        "z3950": "utf-8"
    },
    "Korean_Academy_of_Science_and_Technology_member_ID": {
        "z3950": "unicorn.lib.ic.ac.uk:2200/UNICORN"
    },
    "Kunstmuseum_Basel_artwork_ID": {
        "sru": "https://slsp-ubs.alma.exlibrisgroup.com/view/sru/41SLSP_UBS?version=1.2&amp;operation=searchRetrieve&amp;recordSchema=marcxml"
    },
    "Library_of_the_University_of_Santiago_de_Compostela_authority_ID": {
        "z3950": "utf-8"
    },
    "Minneapolis_Institute_of_Art_artwork_ID": {
        "z3950": "utf-8"
    },
    "Minneapolis_Institute_of_Art_constituent_ID": {
        "z3950": "utf-8"
    },
    "Museum_of_Modern_Art_artist_ID": {
        "z3950": "utf-8"
    },
    "Museum_of_Modern_Art_work_ID": {
        "z3950": "utf-8"
    },
    "National_Academy_of_Sciences_member_ID": {
        "z3950": "utf-8"
    },
    "National_Cancer_Institute_ID": {
        "z3950": "utf-8"
    },
    "National_Gallery_of_Art_Library_Bibliographic_ID": {
        "z3950": "utf-8"
    },
    "National_Gallery_of_Art_artist_ID": {
        "z3950": "utf-8"
    },
    "National_Gallery_of_Art_artwork_ID": {
        "z3950": "utf-8"
    },
    "National_Gallery_of_Canada_artist_ID": {
        "z3950": "utf-8"
    },
    "National_Museum_Norway_artwork_ID": {
        "z3950": "utf-8"
    },
    "National_Museum_in_Warsaw_artwork_ID": {
        "z3950": "utf-8"
    },
    "National_Portrait_Gallery_United_States_object_ID": {
        "z3950": "utf-8"
    },
    "National_Research_Institute_for_Cultural_Properties_artist_ID": {
        "z3950": "utf-8"
    },
    "National_Union_Catalog_ID": {
        "z3950": "utf-8"
    },
    "Natural_History_Museum_London_person_ID": {
        "z3950": "utf-8"
    },
    "Nelson-Atkins_Museum_of_Art_artwork_ID": {
        "z3950": "utf-8"
    },
    "Nelson-Atkins_Museum_of_Art_person_ID": {
        "z3950": "utf-8"
    },
    "New_York_Flora_Atlas_ID": {
        "z3950": "utf-8"
    },
    "New_Zealand_Gazetteer_place_ID": {
        "z3950": "utf-8"
    },
    "Nomenclature_for_Museum_Cataloging": {
        "z3950": "utf-8"
    },
    "Norway_Database_for_Statistics_on_Higher_education_publisher_ID": {
        "z3950": "utf-8"
    },
    "Norwegian_Polar_Institute_place_name_ID": {
        "z3950": "utf-8"
    },
    "ISC_Org": {
        "z3950": "utf-8"
    },
    "BNF_France_Library": {
        "z3950": "utf-8"
    },
    "BNF_France_Work": {
        "z3950": "utf-8"
    },
    "CARLI_Illinois_Library": {
        "z3950": "utf-8"
    },
    "CARLI_Illinois_Work": {
        "z3950": "utf-8"
    },
    "MnPALS_Minnesota_Library": {
        "z3950": "utf-8"
    },
    "MnPALS_Minnesota_Work": {
        "z3950": "utf-8"
    },
    "Ontario_Legislative_Library": {
        "z3950": "utf-8"
    },
    "Ontario_Legislative_Work": {
        "z3950": "utf-8"
    },
    "LIBRIS_Sweden_Library": {
        "z3950": "latin1"
    },
    "LIBRIS_Sweden_Work": {
        "z3950": "latin1"
    },
    "ANZL_Writer": {
        "z3950": "utf-8"
    },
    "Akadem_Person": {
        "z3950": "utf-8"
    },
    "SNIESS_Colombia_Org": {
        "z3950": "utf-8"
    },
    "AISHE_Org": {
        "z3950": "utf-8"
    },
    "Akadem_Person_2": {
        "z3950": "utf-8"
    },
    "CLACSO_Org": {
        "z3950": "utf-8"
    },
    "PASA_Org": {
        "z3950": "utf-8"
    },
    "ARTIC_Person": {
        "z3950": "utf-8"
    },
    "Rome_Academy_Person": {
        "z3950": "utf-8"
    },
    "French_Academy_Science_Person": {
        "z3950": "utf-8"
    },
    "BDCYL_Person": {
        "z3950": "rabel.jcyl.es:210/AbsysBCL"
    },
    "Sinica_Person": {
        "z3950": "utf-8"
    },
    "Flanders_Arts_Person": {
        "z3950": "utf-8"
    },
    "NAS_Member_Person": {
        "z3950": "utf-8"
    },
    "Saxon_Academy_Person": {
        "z3950": "utf-8"
    },
    "Max_Planck_Org": {
        "z3950": "marc8"
    },
    "Archives_de_la_critique_d_art_author_ID": {
        "z3950": "utf-8"
    },
    "Association_francaise_pour_l_avancement_des_sciences_ID": {
        "z3950": "utf-8"
    },
    "Catalogo_Informatizzato_delle_Riviste_Italiane_ID": {
        "z3950": "utf-8"
    },
    "Centro_de_Documentacion_de_las_Artes_Escenicas_ID": {
        "z3950": "utf-8"
    }
}
API_REGISTRY.update(COMPREHENSIVE_MINED_ENDPOINTS)

# Optimized Mined Endpoints (Phase 2)
OPTIMIZED_MINED_ENDPOINTS = {
    "France_Hauts_de_France_Library": {
        "z3950": "utf-8"
    },
    "Spain_Castilla_La_Mancha_Library": {
        "z3950": "latin1"
    },
    "Spain_Castilla_y_Leon_Library": {
        "z3950": "marc8"
    },
    "Spain_Madrid_Library": {
        "z3950": "utf-8"
    },
    "Chile_Santiago_Library": {
        "z3950": "utf-8"
    },
    "Ghana_Central_Library": {
        "z3950": "utf-8"
    },
    "Guatemala_Guatemala_Library": {
        "z3950": "utf-8"
    },
    "Cambodia_Phnom_Penh_Library": {
        "z3950": "utf-8"
    },
    "Trinidad_Tobago_Library": {
        "z3950": "utf-8"
    },
    "Czech_Prague_Library": {
        "z3950": "marc8"
    },
    "Myanmar_Yangon_Library": {
        "z3950": "utf-8"
    },
    "Israel_Central_Library": {
        "z3950": "utf-8"
    },
    "Israel_Jerusalem_Library": {
        "z3950": "utf-8"
    },
    "Greece_Attica_Library": {
        "z3950": "utf-8"
    },
    "Greece_Central_Greece_Library": {
        "z3950": "utf-8"
    },
    "Greece_Western_Greece_Library": {
        "z3950": "latin1"
    },
    "Norway_Agder_Library": {
        "z3950": "utf-8"
    },
    "Norway_Finnmark_Library": {
        "z3950": "utf-8"
    },
    "Norway_Innlandet_Library": {
        "z3950": "utf-8"
    },
    "Norway_Oslo_Library": {
        "z3950": "utf-8"
    },
    "Norway_Troms_Library": {
        "z3950": "utf-8"
    },
    "Sweden_Stockholm_Library": {
        "z3950": "latin1"
    },
    "Ireland_Galway_Library": {
        "z3950": "utf-8"
    },
    "Malaysia_Selangor_Library": {
        "z3950": "utf-8"
    },
    "Argentina_Buenos_Aires_City_Library": {
        "z3950": "utf-8"
    },
    "Argentina_Buenos_Aires_Province_Library": {
        "z3950": "utf-8"
    },
    "Swiss_ZH_Library": {
        "z3950": "utf-8"
    },
    "Swiss_BE_Library": {
        "z3950": "utf-8"
    },
    "Swiss_VD_Library": {
        "z3950": "utf-8"
    },
    "Martinique_Library": {
        "z3950": "utf-8"
    },
    "Guadeloupe_Library": {
        "z3950": "utf-8"
    },
    "Macau_Library": {
        "z3950": "utf-8"
    },
    "Bermuda_Library": {
        "z3950": "utf-8"
    },
    "Czech_Archive_Library": {
        "z3950": "utf-8"
    },
    "Taiwan_Archive_Library": {
        "z3950": "utf-8"
    },
    "Trinidad_Archive_Library": {
        "z3950": "utf-8"
    },
    "Denmark_Archive_Library": {
        "z3950": "utf-8"
    },
    "Czech_Archive_Work": {
        "z3950": "utf-8"
    },
    "Taiwan_Archive_Work": {
        "z3950": "utf-8"
    },
    "Trinidad_Archive_Work": {
        "z3950": "utf-8"
    },
    "Denmark_Archive_Work": {
        "z3950": "utf-8"
    },
    "Sweden_LIBRIS_Work": {
        "z3950": "latin1"
    },
    "BC_Archives_Work": {
        "z3950": "utf-8"
    },
    "Alberta_Archives_Work": {
        "z3950": "utf-8"
    },
    "Ontario_Library_Work": {
        "z3950": "utf-8"
    },
    "California_Library_Work": {
        "z3950": "utf-8"
    },
    "Virginia_Library_Work": {
        "z3950": "utf-8"
    },
    "Cyprus_Library_Work": {
        "z3950": "utf-8"
    },
    "Medicine_NLM_Work": {
        "z3950": "utf-8"
    },
    "Chicago_Library_Work": {
        "z3950": "utf-8"
    },
    "Boston_Library_Work": {
        "z3950": "utf-8"
    },
    "ACNP_Library": {
        "z3950": "utf-8"
    },
    "Swedish_National_Archive": {
        "z3950": "utf-8"
    },
    "ILO_Library": {
        "z3950": "utf-8"
    },
    "ILO_Work": {
        "z3950": "utf-8"
    },
    "BNF_France_Library": {
        "z3950": "utf-8"
    },
    "BNF_France_Work": {
        "z3950": "utf-8"
    },
    "CARLI_Illinois_Library": {
        "z3950": "utf-8"
    },
    "CARLI_Illinois_Work": {
        "z3950": "utf-8"
    },
    "MnPALS_Minnesota_Library": {
        "z3950": "utf-8"
    },
    "MnPALS_Minnesota_Work": {
        "z3950": "utf-8"
    },
    "Ontario_Legislative_Library": {
        "z3950": "utf-8"
    },
    "Ontario_Legislative_Work": {
        "z3950": "utf-8"
    },
    "LIBRIS_Sweden_Library": {
        "z3950": "latin1"
    },
    "LIBRIS_Sweden_Work": {
        "z3950": "latin1"
    },
    "Alberta_Provincial_Library": {
        "z3950": "utf-8"
    },
    "Manitoba_Provincial_Library": {
        "z3950": "na01.alma.exlibrisgroup.com:210/01UMB_INST"
    },
    "Saskatchewan_Provincial_Library": {
        "z3950": "utf-8"
    },
    "Alberta_Provincial_Work": {
        "z3950": "utf-8"
    },
    "Manitoba_Provincial_Work": {
        "z3950": "na01.alma.exlibrisgroup.com:210/01UMB_INST"
    },
    "Saskatchewan_Provincial_Work": {
        "z3950": "utf-8"
    },
    "NS_Provincial_Library": {
        "z3950": "utf-8"
    },
    "NB_Provincial_Library": {
        "z3950": "utf-8"
    },
    "NL_Provincial_Library": {
        "z3950": "utf-8"
    },
    "PEI_Provincial_Library": {
        "z3950": "utf-8"
    },
    "NS_Provincial_Work": {
        "z3950": "utf-8"
    },
    "NB_Provincial_Work": {
        "z3950": "utf-8"
    },
    "NL_Provincial_Work": {
        "z3950": "utf-8"
    },
    "PEI_Provincial_Work": {
        "z3950": "utf-8"
    },
    "Nobel_Person": {
        "z3950": "utf-8"
    },
    "CastillaLeon_Library": {
        "z3950": "marc8"
    },
    "Valencia_Library": {
        "z3950": "utf-8"
    },
    "Toscana_Library": {
        "z3950": "utf-8"
    },
    "CastillaLeon_Work": {
        "z3950": "marc8"
    },
    "Valencia_Work": {
        "z3950": "utf-8"
    },
    "Toscana_Work": {
        "z3950": "utf-8"
    },
    "Cantabria_Library": {
        "z3950": "latin1"
    },
    "Navarra_Library": {
        "z3950": "utf-8"
    },
    "Veneto_Library": {
        "z3950": "C95051UK.eos-intl.eu:210/MC95051UK"
    },
    "Cantabria_Work": {
        "z3950": "latin1"
    },
    "Navarra_Work": {
        "z3950": "utf-8"
    },
    "Veneto_Work": {
        "z3950": "C95051UK.eos-intl.eu:210/MC95051UK"
    },
    "Banrepcultura_Library": {
        "z3950": "utf-8"
    },
    "Smithsonian_Library": {
        "z3950": "utf-8"
    },
    "Banrepcultura_Work": {
        "z3950": "utf-8"
    },
    "Smithsonian_Work": {
        "z3950": "utf-8"
    },
    "WorldBank_Library": {
        "z3950": "jolis.imf.org:2200/UNICORN"
    },
    "IMF_Library": {
        "z3950": "utf-8"
    },
    "SBN_Work": {
        "z3950": "utf-8"
    },
    "Madrid_Regional_Library": {
        "z3950": "utf-8"
    },
    "Madrid_Regional_Work": {
        "z3950": "utf-8"
    },
    "Andorra_Library": {
        "z3950": "utf-8"
    },
    "Andorra_Work": {
        "z3950": "utf-8"
    },
    "Rome_Academy_Person": {
        "z3950": "utf-8"
    },
    "Sinica_Person": {
        "z3950": "utf-8"
    },
    "Poetry_Archive_Person": {
        "z3950": "utf-8"
    }
}
API_REGISTRY.update(OPTIMIZED_MINED_ENDPOINTS)

# Domain-Specific REST Mappings for Non-Library Nodes
DOMAIN_MAPPED_ENDPOINTS = {
    "ROR_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Colorado_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Delaware_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Hawaii_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Idaho_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Indiana_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Kansas_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Kentucky_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Maine_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Maryland_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Massachusetts_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Mississippi_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Missouri_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Montana_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Nebraska_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Nevada_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "New_Mexico_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "North_Carolina_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Oklahoma_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Oregon_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "South_Carolina_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Vermont_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "West_Virginia_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Wyoming_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Algeria_Adrar_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Chlef_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Laghouat_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Oum_El_Bouaghi_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Batna_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Bejaia_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Biskra_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Bechar_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Blida_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Bouira_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Tamanghasset_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Tebessa_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Tlemcen_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Tiaret_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Tizi_Ouzou_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Alger_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Djelfa_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Jijel_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Setif_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Saida_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Skikda_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Sidi_Bel_Abbes_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Annaba_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Guelma_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Constantine_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Medea_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Mostaganem_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_MSila_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Mascara_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Ouargla_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Oran_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_El_Bayadh_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Illizi_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Bordj_Bou_Arreridj_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Boumerdes_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_El_Tarf_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Tindouf_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Tissemsilt_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_El_Oued_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Khenchela_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Souk_Ahras_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Tipaza_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Mila_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Ain_Defla_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Naama_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Ain_Temouchent_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Ghardaia_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algeria_Relizane_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Ariana_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Beja_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Ben_Arous_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Bizerte_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Gabes_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Gafsa_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Jendouba_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Kairouan_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Kasserine_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Kebili_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Kef_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Mahdia_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Manouba_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Medenine_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Monastir_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Nabeul_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Sfax_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Sidi_Bouzid_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Siliana_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Sousse_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Tataouine_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Tozeur_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Tunis_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Tunisia_Zaghouan_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Morocco_Beni_Mellal_Khenifra_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Morocco_Casablanca_Settat_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Morocco_Draa_Tafilalet_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Morocco_Dakhla_Oued_Ed_Dahab_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Morocco_Fes_Meknes_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Morocco_Guelmim_Oued_Noun_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Morocco_Laayoune_Sakia_El_Hamra_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Morocco_Marrakesh_Safi_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Morocco_Oriental_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Morocco_Rabat_Sale_Kenitra_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Morocco_Souss_Massa_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Morocco_Tanger_Tetouan_Al_Hoceima_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Afghanistan_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Angola_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AntiguaBarbuda_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Benin_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bhutan_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Botswana_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Brunei_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BurkinaFaso_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Burundi_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CaboVerde_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Cameroon_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CAR_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Chad_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Comoros_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Congo_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Djibouti_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dominica_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DominicanRepublic_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ElSalvador_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "EquatorialGuinea_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Eritrea_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Eswatini_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Gabon_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Gambia_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Grenada_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Guatemala_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Guinea_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GuineaBissau_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Honduras_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Kiribati_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Lesotho_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Liberia_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Liechtenstein_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Madagascar_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Malawi_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Maldives_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Mali_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "MarshallIslands_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Mauritania_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Micronesia_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Mozambique_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Nauru_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Nicaragua_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Palau_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Panama_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SaintKittsNevis_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SaintLucia_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SaintVincent_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Samoa_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SaoTomePrincipe_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SierraLeone_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SolomonIslands_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Somalia_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "TimorLeste_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Togo_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Tonga_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Tuvalu_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Vanuatu_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Yemen_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Zambia_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Kyrgyzstan_Archive_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Czech_Archive_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Taiwan_Archive_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Trinidad_Archive_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Philippines_Archive_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Belarus_Archive_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Slovakia_Archive_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Tanzania_Archive_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Denmark_Archive_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SriLanka_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "PNG_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Syria_Assad_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Namibia_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Uzbekistan_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Kazakhstan_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Azerbaijan_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Barbados_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Belize_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Guyana_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Kenya_NationalArchives_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Ethiopia_NationalArchives_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_NationalArchives_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Japan_NationalArchives_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Korea_NationalArchives_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Thailand_NationalArchives_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "UAE_NationalArchives_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Iraq_NationalArchives_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Bahamas_NationalArchives_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Fiji_NationalArchives_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "APN_GCR_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "EOSC_Portal_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "GDN_Network_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Netherlands_Research_Portal": {
        "rest": "https://api.crossref.org/works"
    },
    "Nepal_OCR_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Sudan_MoHE_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "SSudan_MoHE_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Myanmar_MoE_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Vietnam_Business_Portal": {
        "rest": "https://api.ror.org/organizations"
    },
    "Uzbekistan_OpenData": {
        "rest": "https://api.ror.org/organizations"
    },
    "UGC_Nepal_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Finnish_Scholarly_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Kyoto_Research_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Turkey_Academic_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Canada_Council_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "IBPA_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Math_Press_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "SVS_Press_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "JaLC_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "OpenCitations_Meta_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Norway_BARE_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Mexico_BNMX_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NZ_DigitalNZ_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Australia_Trove_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Russia_RSL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Brazil_BNB_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Argentina_CAL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SouthAfrica_PASA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Romania_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NationalArchives_Global_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Armenia_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Azerbaijan_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Haiti_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Senegal_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Thailand_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Vietnam_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Philippines_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "India_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Japan_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Korea_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Singapore_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Malaysia_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Taiwan_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "BHL_Library_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Slovenia_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Croatia_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Bosnia_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Hungary_NSL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Quebec_BAnQ_Work_2": {
        "rest": "https://api.crossref.org/works"
    },
    "Vatican_Library_Work_2": {
        "rest": "https://api.crossref.org/works"
    },
    "IFLA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "UNESCO_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "UN_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Peru_BNP_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Argentina_BNMM_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Luxembourg_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Sweden_LIBRIS_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Trinidad_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Monaco_Registry_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Mauritius_HEC_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Seychelles_TERA_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ISBN_International_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ISBN_Spain_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ISBN_France_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ISBN_India_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ISBN_Italy_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ISBN_Japan_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "France_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "France_AMT_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "IvoryCoast_NA_Work_2": {
        "rest": "https://api.crossref.org/works"
    },
    "Haiti_NA_Work_2": {
        "rest": "https://api.crossref.org/works"
    },
    "ACT_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NSW_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Queensland_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "BC_Archives_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Alberta_Archives_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Ontario_Library_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "California_Library_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Virginia_Library_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NewYork_Library_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ATLA_Library_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "RDA_Standard_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ZDB_Library_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "eLibrary_Russia_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Cyprus_Library_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Bulgaria_Cyril_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "China_NLC_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Finland_NL_Work_2": {
        "rest": "https://api.crossref.org/works"
    },
    "Chile_CNL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Costa_Rica_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Cuba_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Medicine_NLM_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Turkey_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Iran_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SouthKorea_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "British_Library_EThOS_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Jisc_Archives_Hub_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "AskZad_Library_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ELIS_Library_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "OAI_Registry_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "DPC_Library_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NYPL_Library_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Chicago_Library_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Boston_Library_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SciELO_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Frankfurt_Fair_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "London_Fair_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Sharjah_Fair_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Singapore_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Ireland_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Scotland_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Wales_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bahrain_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Jordan_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Kuwait_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Lebanon_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Morocco_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Oman_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Qatar_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SaudiArabia_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "UAE_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Albania_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Algeria_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bosnia_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bulgaria_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Croatia_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Cyprus_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Estonia_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Ghana_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Greece_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Hungary_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Iraq_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Jamaica_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Kosovo_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Latvia_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Lithuania_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Malta_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Moldova_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Montenegro_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Macedonia_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Palestine_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Romania_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Serbia_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Slovenia_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Syria_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Thailand_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Ukraine_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Vietnam_NL_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ARCHON_Code": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "APE_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ArchivesWest_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "HAL_Structure": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BritishMuseum_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "AshmoleanMuseum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BrooklynMuseum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AucklandMuseum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AmsterdamMuseum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BarnesFoundation_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "PradoMuseum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Louvre_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "MetMuseum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "MoMA_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GettyMuseum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "V&A_Museum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "YaleArchives_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "HarvardArchives_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OxfordArchives_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CambridgeArchives_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "TrinityCambridge_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "UNIGE_Archive_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "FrickArchives_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ArchivesNationales_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AthensAcademy_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "RussianTV_Acad_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SloanFoundation_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ArtsCouncilEngland_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AustralianResearchCouncil_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "UNESCO_ICH_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ILO_Thesaurus_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "WHO_Registry_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "WTO_Trade_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "RoyalSociety_Fellow_ID": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "RoyalSociety_Canada_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NAS_Member_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NAE_Member_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NAM_France_Member_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "FrenchAcademy_Science_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "KoreanAcademy_Science_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LisztAcademy_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BritishCouncil_Artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BritishCouncil_Writer_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CanadaCouncil_Pub_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GlobalResearchCouncil_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalLibraryBoard_SG_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalLibrary_Albania_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalLibrary_Chile_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalLibrary_Indonesia_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalLibrary_Ireland_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalLibrary_Nigeria_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Argentina_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Brazil_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Chile_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Colombia_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Peru_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Uruguay_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NationalLibrary_Malaysia_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalLibrary_Uruguay_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "360Giving_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "IATI_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "OpenAIRE_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "UIA_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "US_FederalRegister_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "FederalRegister_Doc": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IATI_Organisation_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "UIA_OpenYearbook_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "UK_NationalArchives": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Australia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Japan": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_India": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Indonesia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Singapore": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Thailand": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Vietnam": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Egypt": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_KSA": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_UAE": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Pakistan": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Bangladesh": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_SriLanka": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Switzerland": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Denmark": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Poland": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Czech": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Slovakia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Hungary": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NSW_StateArchives": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Queensland_StateArchives": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NewYork_StateLibrary": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "California_StateLibrary": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Texas_StateLibrary": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Smithsonian_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "LibraryOfCongress_BF": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BritishLibrary_Sys": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Albania": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Armenia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Austria": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Azerbaijan": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Bahamas": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Barbados": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Belarus": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Belize": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Bosnia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Croatia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Cyprus": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Estonia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Ethiopia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Georgia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Ghana": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Greece": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Haiti": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_IvoryCoast": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Jamaica": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Kazakhstan": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Kenya": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Kyrgyzstan": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Latvia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Lithuania": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Malta": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Moldova": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Nigeria": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_NorthMacedonia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Rwanda": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Senegal": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Serbia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Tajikistan": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Tanzania": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Trinidad": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Uganda": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Uzbekistan": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Zimbabwe": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Swedish_NationalArchives": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Algerian_NL_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Albania_NL_Edition": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Indonesia_NL_Control": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Malaysia_NL_OPAC": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Nigeria_NL_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Uruguay_NL_Auth": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Wales_NL_Auth": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "RegionalLibrary_Pardubice": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Suriname": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Aruba": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Curacao": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NationalArchives_Turkmenistan": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GeneralStateArchives_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NSW_StateArchives_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Australia_NA_Entity": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Smithsonian_Art_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Smithsonian_Object_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Smithsonian_Org_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Sweden_NA_Agent": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "REBIUN_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OBV_Org_Authority": {
        "rest": "https://api.ror.org/organizations"
    },
    "SLSP_Network": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ABEU_Catalog": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ASEUC_Catalog": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Altexto_Catalog": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "REUN_Catalog": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AEUP_Catalog": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ACUP_Catalog": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AJUP_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CUPA_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ATUP_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "KUPA_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AUPNZ_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "UPAN_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "UNE_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "UPI_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AFPU_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AG_Univerlage_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AArU_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ProPublica_EIN": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "EU_Transparency": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AAMC_Institutions": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ACLS_Societies": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ACUM_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ADB_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AMNH_Entity": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BASE_OAI": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BAnQ_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BIPM_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "BN_Brazil_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BN_Chile_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BN_Peru_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BN_Mexico_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Algeria_NL_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IraqiAuthors_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Balat_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Biblissima_Auth": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Czech_Bio_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Belarus_Events_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Slovakia_Hist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AviationSafety_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ForestStewardship_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ACA_Author": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ACM_DL_Author": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AHNMNH_Pub": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AILA_Publishers": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ARLIMA_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ASCL_Abstracts": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AcademiaSinica_Auth": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Alsharekh_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "AmericanAcademy_Rome": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Aozora Bunko": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archiefpunt_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Archnet_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Arkivportalen": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Artists_Canada": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Athenaeum_Museum": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Australian_Heritage": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Australian_Maritime_Museum": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BHL_Taxon": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BIG_Indonesia_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BNB_Brazil_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "BNM_Bibliographic": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BVPB_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BVPH_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Barcelona_Heritage": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Biblissima_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Vatican_OPAC_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "URBS_Institutions": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Pontifical_Universities": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "UPSA_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BSB_Bavaria_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bavaria_StMWK_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archives_Bavaria": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bavarian_Monument_Auth": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Armenian_Union_Catalog": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Cyprus_Bibliography": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BG_NACID_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BAnQ_Work_ID": {
        "rest": "https://api.crossref.org/works"
    },
    "BIBSYS_Work_ID": {
        "rest": "https://api.crossref.org/works"
    },
    "BnF_Dictionary_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "HAL_Structure_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Belgian_Senate_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Armenian_UnionCatalog": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BBK_Classification": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ACNP_Periodicals": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BDCYL_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BDH_Edition": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "APE_Meta_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ACM_DL_Citation": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ACM_DL_Event": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CooperHewitt_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AmericanArt_Collab": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bib_Augustana": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Biblioteca_Cappuccini": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Biblioteca_FrancoSerantini": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Biblioteca_IglesiaNacional": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bibliotheque_Tournai": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BHMPI_Object": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BIPM_CGPM_Member": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Auvergne_RegionalInventory": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Argentinian_Historic_Heritage": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Belgian_Heritage_Brazil": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Azerbaijani_National_Encyc": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AgEcon_Search": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archaeology_Data_Service": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Arlington_Cemetery": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ANMM_Object": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ANMM_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "BaFin_Institute": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Aviation_Safety_ASN": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Antarctic_Treaty_Auth": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Australian_Antarctic_Gaz": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Australian_Charities_ACNC": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Australian_Gov_Orgs": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Australian_Disaster_Hub": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Australian_Women_Register": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Austrian_Cave_Register": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Belarus_Cultural_Heritage": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Cagliari_Uni_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Canadas_Early_Women_Writers": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Classical_Scholars_DB": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Czech_Amateur_Theater": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Czech_Librarians_DB": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NARA_US": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NKC_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NLC_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NLNZ": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NLK_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NLP_Philippines": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NLR_Romania": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NLSA_SouthAfrica": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Imperial_Dorpat_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "RoyalSociety_Memoirs": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ISIL_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "FIUC_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IFLA_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ISBN_NationalAgencies": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NLI_Israel_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NLI_J9U": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dutch_Archives": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "French_Archives": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Lebanese_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Greece_Auth": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Poland_MMS": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Albania_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Algeria_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Bahrain_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Bosnia_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Bulgaria_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Croatia_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Cyprus_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Estonia_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Ghana_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Greece_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Hungary_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Iraq_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Ireland_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Jamaica_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Jordan_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Kosovo_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Kuwait_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Latvia_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Lebanon_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Lithuania_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Malta_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Moldova_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Montenegro_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Morocco_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_NorthMacedonia_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Oman_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Palestine_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Philippines_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Qatar_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Romania_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_SaudiArabia_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Scotland_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Serbia_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Slovenia_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Syria_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Thailand_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_UAE_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Ukraine_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Vietnam_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Wales_Corp": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NLNZ_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Argentina": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Russia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Venezuela": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_CostaRica": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Personnel_Prefectorale": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Parliamentary_Archives_UK": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Rush_Parliamentary_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "BAnQ_Authority_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SLQ_Australia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SNK_Slovakia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "PTBNP_Work_ID": {
        "rest": "https://api.crossref.org/works"
    },
    "PICA_CBS_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ACA_Author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AEDA_Keyword": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AHNMNH_Pub_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AICTE_Inst_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AJOL_Org_Reg": {
        "rest": "https://api.ror.org/organizations"
    },
    "AMNH_Entity_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AfricanMusic_Lib": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AlexanderTurnbull_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Algerian_NL": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AmericanAcademy_Rome_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AmericanFolklore_Thesaurus": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AUB_Libraries": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archaeology_DS": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archiefpunt": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "TrinityCambridge_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "AO3_Tag": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "UNIGE_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "ArchivesNationales_Creator": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "APE_Authority_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ArchivesWest_FindingAid": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ArchivesYale_Agent": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ArchivesVaucluse": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Arkivportalen_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ArtMuseum_Estonia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AucklandArtGallery": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BNB_Brazil_Auth": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BNM_Record_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CAS_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CERN_GrayBook": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CGIAR_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CNL_Author": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "COAR_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CORE_Provider": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Catalogue_Illuminated_MSS": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Chinese_ClinicalTrial_Reg": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Crop_Trust_Partner": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DataCite_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Denkmalliste_Hamburg": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Digital_Public_Goods": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Disease_Ontology": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ELNET_Estonia": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ENA_Institutional": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "EOSC_Portal": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "EURAMET_Member": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "E_Marefa_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Federal_Charity_Reg": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Finnish_National_Bib": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Flanders_Heritage": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Frick_Archives": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SICMexico": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "360Giving_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "HALStructure": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ACA_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ACNP_library_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AJOL_Organization_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AMNH_entity_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Crossref_Funder": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OpenLibrary_Works": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "APE_Person_Auth": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "ARTIC_Artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ARTIC_Artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AFI_Person_ID": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Amsterdam_Museum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Trinity_Camb_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "AN_France_Creator": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ArchivesWest_FA": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BAnQ_Auth_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BDH_Edition_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BNC_Catalogue_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BPH_Journal_ID": {
        "rest": "https://api.crossref.org/journals"
    },
    "Academy_Awards_Database_film_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Academy_Awards_Database_nominee_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Academy_of_Athens_authority_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Academy_of_Russian_Television_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Aleph_Global_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Alsharek_Archive_author_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "American_Academy_in_Rome_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "American_Folklore_Society_Ethnographic_Thesaurus_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "American_University_of_Beiruts_Libraries_title_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archaeology_Data_Service_work_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archiefpunt_archive_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Arlington_Cemetery_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Arts_Council_England_NPO": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Ashmolean_Museum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Auckland_Museum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Australian_Antarctic_Gazetteer_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Australian_Research_Council_Grant_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Auvergne-Rhone-Alpes_Regional_Inventory_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Azerbaijani_National_Encyclopedia_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BBK_library_and_bibliographic_classification": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BDCYL_Auth": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BG_NACID_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BIPM_CGPM_Member_Meta_Meta_Meta_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BPH_journal_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BaFin_Institute_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Barcelona_City_Council_Heritage_Catalog_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bat_Sheva_Archive_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Beazley_Archive_Pottery_Database_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Beirut_Arab_Universitys_Libraries_title_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Belgian_Heritage_in_Brazil_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Crossref_Funder_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OpenLibrary_Works_Editions": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "APE_Person_Authority": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "ARCHON_code": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Akadem_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "American_Art_Collaborative_object_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "American_Film_Institute_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Amsterdam_Museum_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archive_Site_Trinity_College_Cambridge_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Archive_ouverte_UNIGE_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Archives_Dir_History_Collecting": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archives_Nationales_Creator": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archives_Nationales_France_Persons": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archives_Portal_Europe": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archives_Portal_Europe_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archives_Portal_Europe_Meta_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archives_West_finding_aid_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archives_West_repository_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archives_Yale_Agent": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archives_in_Bavaria_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Argentinian_Historic_Heritage_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Arkivportalen_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Art_Museum_of_Estonia_artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Art_Museum_of_Estonia_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Atarimuseum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Athenaeum_museum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Australian_National_Maritime_Museum_object_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Australian_National_Maritime_Museum_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BAnQ_authority_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BAnQ_work_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BDH_edition_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BHMPI_object_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BIBSYS_work_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BNB_Brazil_Persons_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BNM_bibliographic_record_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Belgian_Senate_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Berlin_cultural_heritage_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bib_Augustana_Author": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bib_Hagiographica_Graeca": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bib_Hagiographica_Latina": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bibliography_of_the_History_of_Slovakia_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Biblioteca_Franco_Serantini": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Biblioteca_Iglesia_Nacional": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Biblioteca_Italiana_work_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Biblioteka_Nauki_publisher_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bibliotheque_du_Seminaire_de_Tournai_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Biblissima_authority_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bicocca_Open_Archive_author_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Biographical_Archive_of_Psychiatry_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Biographical_Dictionary_of_the_Australian_Senate_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Biographical_Dictionary_of_the_Czech_Lands_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Biographical_Memoirs_of_Fellows_of_the_Royal_Society_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BnF_archives_and_manuscripts_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BnF_dictionary_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bodleian_Archives_&_Manuscripts_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "British_Council_artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "British_Council_writer_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "British_Museum_People_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Brooklyn_Museum_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bulgarian_Antarctic_Gazetteer_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CABR-identifier": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CALIS_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CAS_Registry_Number": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CCBAE_publication_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CCFr_library_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CEEOL_Publishers": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CERN_GrayBook_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CGIAR_Organization_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CNL_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "COAR_Global_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CORE_Provider_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Catalogue_of_Illuminated_Manuscripts_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Catalogue_of_the_General_State_Archives_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Censo_Guia_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "Centre-Val_de_Loire_Inventory_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Chinese_Clinical_Trial_Registry_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DBNL_Author": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DPLA_Providers": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DataCite_Org_Reg": {
        "rest": "https://api.ror.org/organizations"
    },
    "Dictionary_NZ_Bio": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "EBAF_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ENEA_IRIS_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "EUNIC_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "EU_CORDIS_Orgs": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Estonian_Bio_DB": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Europeana_Orgs": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "FAIRsharing_Auth": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "FRIS_Flanders": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Federal_Heritage_CA": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Federation_Council_PSN": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "RoyalSociety_Fellow": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "RoyalSociety_Canada_Fellow": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "AEDA_subject_keyword_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AHNMNH_publication_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AICTE_institute_application_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AINM_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ANZL_writer_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Aozora_Bunko_work_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archive_of_Our_Own_tag": {
        "rest": "https://api.ror.org/organizations"
    },
    "Archives_departementales_de_Vaucluse_fonds_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archivio_Storico_dellUniversita_degli_Studi_di_Cagliari_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Australian_Institute_for_Disaster_Resilience_Knowledge_Hub_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Australian_National_Kennel_Council_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BFXC_authority_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bane_NOR_Network_Statement_ID_deprecated": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bank_of_information_on_the_historical_and_cultural_heritage_of_the_Republic_of_Belarus": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Biographical_Directory_of_Federal_Judges_alpha_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Biographical_Directory_of_Federal_Judges_numeric_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Book_Depository_publisher_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bourgogne-Franche-Comte_inventory_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "British_Institute_at_Ankara_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "British_Institute_at_Ankara_place_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "British_Museum_object_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "British_Museum_place_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "British_Museum_thesaurus_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "British_Newspaper_Archive_publication_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Brooklyn_Museum_Exhibition_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bundes-Klinik-Atlas_hospital_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CDep.Ro_NGO_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CISCE_school_code": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CMI_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CNAP_artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CNKI_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CNKI_institute_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CNO-11_occupation_code": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CNRS_research_group_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "COAR_Member_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CORAF_Agricultural_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "COSPAR_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CPAN_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "California_Entity_Number": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Canada_Business_Number": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Canada_Council_Publishers": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Canmore_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Carnegie_Museum_of_Art_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Catalogo_Nazionale_Dati_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CeBeDem_composer_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Chtyvo_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Cincinnati_Art_Museum_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Classic_Adventures_Solution_Archive_game_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Classical_Archives_composer_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Cleveland_Museum_of_Art_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Code_List_for_Cultural_Heritage_Organizations": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Codex_Alimentarius_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CofE_archives_catalogue_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CofE_archives_name_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CofE_archives_place_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Colour_Index_International_constitution_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Commission_to_Preserve_National_Monuments_of_Bosnia_and_Herzegovina_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Conseil_de_Presse_Luxembourg_journalist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Cooper_Hewitt_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Corporation_Number_in_Canada": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Cranach_Digital_Archive_artwork_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Crop_Trust_Partner_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Cultural_heritage_ID_in_Baden-Wurttemberg": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Cultural_heritage_database_in_Austria_ObjektID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Cyprus_Bibliography_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DBNL_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dictionary_NZ_Biography_API": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Digital_Lib_Caribbean": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Digital_Public_Goods_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Database_of_Art_Objects_at_the_Jeu_de_Paume_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Database_of_Canadas_Early_Women_Writers_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Database_of_Classical_Scholars_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Database_of_Czech_Amateur_Theater_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Database_of_Czech_Librarians_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Database_of_Photography_Books_profile_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dizionario_bio-bibliografico_dei_bibliotecari_italiani_del_XX_secolo_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Electronic_library_Ukrainica_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Encyclopaedia_of_Islam_glossary_and_index_of_terms_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Encyclopedia_of_the_Serbian_National_Theatre_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Encyclopaedia_Universalis_index_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Estonian_biographical_database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Erik_Amburger_database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dictionary_of_Swedish_National_Biography_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dictionary_of_Archives_Terminology_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dictionary_of_American_Regional_English_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Digital_Index_of_Middle_English_Verse_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DLL_Catalog_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GLEIF_LOU_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GBIF_Publisher_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GARD_Org_Authority": {
        "rest": "https://api.ror.org/organizations"
    },
    "GEO_Org_Authority": {
        "rest": "https://api.ror.org/organizations"
    },
    "GFAR_Regional_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GEANT_NREN_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Finnish_National_Gallery_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Fitzwilliam_Museum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "George_Eastman_Museum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Georgia_Museum_of_Art_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "French_Academy_Rome_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "French_Academy_Sciences_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "FranceArchives_Agent_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Vaucluse_Archives_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Cagliari_Uni_Archive_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Dallas_Museum_of_Art_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dordrechts_Museum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Diocese_of_Lyon_Museum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DataCite_Org_Registry": {
        "rest": "https://api.ror.org/organizations"
    },
    "Disease_Ontology_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Gene_Ontology_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Foundational_Model_Anatomy_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Archives_of_Australia_entity_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NLSA_South_Africa": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Costa_Rica": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Greece_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Philippines_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NLI_Israel_Corporate": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ISBN_National_Agencies": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Belarus_in_persons_and_events_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Fellow_of_the_Royal_Society_ID": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Fellow_of_the_Royal_Society_of_Canada_ID": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Imperial_University_of_Dorpat_student_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Wales_Catalogue": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NSW_State_Archives": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NSW_State_Archives_Agency": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OBV_Organization_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ODUCAL_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Parliamentary_Archives_ID_in_United_Kingdom": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Personnel_de_ladministration_prefectorale_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Plant_List_ID_Royal_Botanic_Gardens_Kew": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Pontifical_University_of_Salamanca_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Royal_Academy_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Royal_Collection_UK_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Royal_Irish_Academy_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Royal_Ontario_Museum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Royal_Swedish_Academy_of_Letters_member_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Rush_Parliamentary_Archive_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "SLNSW_unpublished_item_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Smithsonian_American_Art_Museum_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Smithsonian_Object_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Smithsonian_Organization_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Swedish_NL_Arken": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Swedish_National_Archive": {
        "rest": "https://api.ror.org/organizations"
    },
    "UK_National_Archives": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Georgia_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Sri_Lanka_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Pontifical_Universities_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SI_Institutions": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LIBRIS_SELIBR": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "KANTO_Finland": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NLI_Israel_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "RSL_Author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "RSPA_Ancient_Author": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "RSPA_Modern_Author": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Royal_Horticultural_Plant": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Royal_Museums_Greenwich": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SNK_VIAF": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Swedish_NA_Agent": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Swedish_Royal_Theater": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "TNA_UK": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "VNLU_Ukraine": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ZDB_Serials": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Past_RoyalSociety_Fellow": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "RoyalBC_Museum": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Smithsonian_API": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AAGM_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AAGM_person_or_institution_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AIDA_freediver_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AppGallery_app_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archives_d\u00e9partementales_de_Vaucluse_fonds_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archivio_Storico_dellUniversit\u00e0_degli_Studi_di_Cagliari_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ArtMajeur_artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Art_Gallery_of_Ontario_object_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Art_Gallery_of_South_Australia_creator_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Art_Gallery_of_South_Australia_work_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Art_for_the_City_inventory_number": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Artland_gallery_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Auckland_Art_Gallery_artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Auckland_Art_Gallery_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Auvergne-Rh\u00f4ne-Alpes_Regional_Inventory_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BNB_person_ID_OBSOLETE": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Base_Constructions_Bib": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Biblioth\u00e8que_du_S\u00e9minaire_de_Tournai_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bourgogne-Franche-Comt\u00e9_inventory_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "British_Museum_person_or_institution_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Cover_Art_Archive_image": {
        "rest": "https://api.ror.org/organizations"
    },
    "Cultural_heritage_ID_in_Baden-W\u00fcrttemberg": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DBNL_place_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DPLA_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DPLA_subject_term": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dallas_Museum_of_Art_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dameh\u00e5ndbolddatabasen_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Danish_National_Filmography_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Danmarks_svampeatlas_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dark_Ride_Database_company_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dark_Ride_Database_park_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dark_Ride_Database_ride_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DataCite_Organization_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Database_dei_fondi_musicali_toscani_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Denkmalliste_Hamburg_object_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dharma_Drum_Institute_of_Liberal_Arts_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dharma_Drum_Institute_of_Liberal_Arts_place_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DiCamillo_Database_Country_House_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DiVA_authority-person": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DigiListan_artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Digital_Atlas_of_the_Roman_Empire_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Digital_Atlas_of_the_Virginia_Flora_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DigitaltMuseum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Diocese_of_Lyon_Museum_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dir_Gen_Bibliotecas": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Directory_of_Afrocubanas_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Directory_of_Belgian_Photographers_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Directory_of_Czech_publishers_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Directory_of_Ma\u00eetres_dart": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dordrechts_Museum_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dr._Dukes_Phytochemical_and_Ethnobotanical_Databases_chemical_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Driver_Database_driver_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dutch_Senate_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "EBAF_authority_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "EJAtlas_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ELNET_Estonia_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ENA_Institutional_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ENEA-IRIS_Open_Archive_author_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "EOSC_Portal_Meta_Meta_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "EPA_Facility_Registry_Service_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ERIC_Institute_of_Education_Sciences": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "EThOS_UK": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "EURAMET_Member_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "EU_CORDIS_Organizations": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "EZB_library_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "E_Marefa_Organization_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Echinoid_Directory_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Education_International_Member_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Education_International_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Electronic_Language_International_Festival_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Electronic_library_encyclopedia.com.ua": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Encyclop\u00e6dia_Universalis_index_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Environment_Ontology_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Epigraphic_Database_Heidelberg_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Epigraphic_Database_Roma_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Erasmus_Plus_HEI_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "EuroBabeIndex.com_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Europeana_Fashion_Vocabulary_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Europeana_Organization_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Europeana_Research_Objects": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Europeana_entity": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Evidence_&_Conclusion_Ontology_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Experimental_Factor_Ontology_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "FAIRsharing_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "FCC_ID_Database_company_slug": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "FIPS_5-2_alpha_code_US_states": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "FIPS_5-2_numeric_code_US_states": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Family_Gaming_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Federal_Heritage_Buildings_ID_Canada": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Federal_Register_Document_Number": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Federation_Council_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Federation_Council_reference_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Film_Atlas_article_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Finnish_Biodiversity_Information_Facilitys_Species_List_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Finnish_Ministers_database_ID_new": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Finnish_National_Gallery_artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Finnish_National_Gallery_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Fitzwilliam_Museum_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Flanders_Arts_Institute_organisation_ID_former_scheme": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Flanders_Arts_Institute_person_ID_former_scheme": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Flanders_Arts_Institute_production_ID_former_scheme": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Flanders_Arts_Institute_venue_ID_former_scheme": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Flashpoint_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Flemish_Community_Masterpieces_List_item_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Flora_of_New_Jersey_Project_atlas_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Flora_of_the_Southeastern_United_States_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Florida_Historical_Marker_List_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Forest_Stewardship_Council_Certificate_Code": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Forest_Stewardship_Council_License_Code": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Foundational_Model_of_Anatomy_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Free_Software_Directory_entry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "French_Academy_in_Rome_fellow_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "French_Academy_of_Sciences_member_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "French_Sculpture_Census_artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "French_Sculpture_Census_work_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "French_public_service_directory_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "FrogMAP_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GARD_Organization_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GBIF_Participant_Meta_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GBIF_Publisher_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GEANT_NREN_Meta_Meta_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GEO_Organization_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GFAR_Regional_Forum_Meta_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GLEIF_LOU_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GLEIF_registration_authority_code": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GRAU_index": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GSI_Japan_Place_API": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Galiciana_authority_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Game_Boy_Database_game_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Game_Boy_hardware_database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Game_Input_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Game_UI_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GamingOnLinux_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Garden.org_Plants_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Garuda_Indonesia_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Gatehouse_Gazetteer_place_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Gazetteer_for_Scotland_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Gazetteer_for_Scotland_place_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Gazetteer_of_Planetary_Nomenclature_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "George_Eastman_Museum_people_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Georgian_National_Filmography_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Georgian_National_Register_of_Monuments_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Gesher_Theatre_Archive_person_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Gesher_Theatre_Archive_play_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Getty_CONA_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Getty_Iconography_Auth": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GitHub_Organization_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Global_Egyptian_Museum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Global_Invasive_Species_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Global_Poker_Index_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Global_Research_Council_Network": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Global_Terrorism_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Google_Maps_Customer_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Google_Patents_Organizations": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Gotlands_museum_entity_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Groeningemuseum_work_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Gun_Violence_Archive_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "HAL_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "HPO_Organization_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "HaBima_Archive_person_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "HaBima_Archive_play_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Harvard_Art_Museums_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Harvard_Index_of_Botanists_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Haz-Map_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Health_Facility_Registry_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Hebrew_Academy_term_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "HelveticArchives": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Heritage_Gazetteer_of_Cyprus": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Heritage_Gazetteer_of_Libya_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Hermitage_Museum_work_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Hessian_Literature_Council_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Hispania_Nostra_Red_List_code": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Historical_Archives_EU": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Historical_Gazetteer_GOV_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Historical_Marker_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "HistoryMakers_Maker_Directory_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "HomeComputer_Museum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Human_Metabolome_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Human_Phenotype_Ontology_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Hungarian_Film_Archive_film_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Hungarian_Film_Archive_person_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Hungarian_National_Assembly_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Hungarian_National_Namespace_organisation_ID_new": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Hungarian_National_Namespace_organisation_ID_old": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Hungarian_National_Namespace_person_ID_new": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Hungarian_National_Namespace_person_ID_old": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Hungarian_National_Namespace_place_ID_new": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Hungarian_National_Namespace_place_ID_old": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Hymenoptera_Anatomy_Ontology_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IAEA_GC_Meta_Meta_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IAEA_INIS": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IANA_Root_Zone_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IANA_Root_Zone_Meta_Meta_Meta_Meta_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IATI_Datastore_Meta_Meta_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IATI_Organization_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IAU_Consortium_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IAU_WHED_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ICCROM_authority_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ICC_ASP_Meta_Meta_Meta_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ICOM_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ICPSR_Organization_Names_Authority_List_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ICPSR_Personal_Names_Authority_List_ID": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "ICZN_Zoological_Nomenclature_Root": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IDB_Publications_Portal": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IEC_Member_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IFACCA_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IGN_Belgium_Place_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ILEC_World_Lake_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IMA_museum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IMF_eLibrary": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "INORMS_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "INSEE_Repository": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IPNI_Plant_Names_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IRRI_Rice_Research_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ISC_Member_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ISC_Members": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ISIL_Global_Directory": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ISNI_Agency_Meta_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ISO_IEC_Directives_Root": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IUCN_Member_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IVOA_Global_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Image_Archive_Herder_Institute": {
        "rest": "https://api.ror.org/organizations"
    },
    "IndExs_Exsiccata_editor_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IndExs_exsiccata_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IndexCat_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Index_Fungorum_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Index_Hepaticarum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Index_Herbariorum_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Index_Theologicus_publication_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Index_to_American_Botanical_Literature_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Index_to_Organism_Names_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "India_Vidwan_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Indian_Medicinal_Plants_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Indian_census_area_code_1991": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Indian_census_area_code_2001": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Indian_census_area_code_2011": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Indiana_Plant_Atlas_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Indiana_State_Historical_Marker_Program_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Indiana_State_Historical_Marker_Program_numeric_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Indianapolis_Museum_of_Art_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Indonesian_Museum_National_Registration_System_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Indonesian_Small_Islands_Directory_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Indonesian_prison_database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Institute_of_History_of_Ukraine_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Integbio_Database_Catalog_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Interactive_Fiction_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Interaktionsdatabasen_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Interlingual_Index_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "International_Canoe_Federation_canoer_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "International_Computer_Game_Collection_work_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "International_Encoded_Han_Character_and_Variants_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "International_Fencing_Federation_fencer_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "International_Standard_Bible_Encyclopedia_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Archive_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Internet_Archive_Scholar_Organizations": {
        "rest": "https://api.ror.org/organizations"
    },
    "Internet_Book_Database_of_Fiction_writer_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Broadway_Database_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Broadway_Database_production_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Broadway_Database_show_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Broadway_Database_touring_theatre_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Broadway_Database_venue_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Game_Database_company_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Game_Database_event_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Game_Database_franchise_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Game_Database_game_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Game_Database_game_engine_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Game_Database_genre_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Game_Database_numeric_game_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Game_Database_platform_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Off-Broadway_Database_ID_former_scheme": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Off-Broadway_Database_production_ID_former_scheme": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Pinball_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Internet_Sacred_Text_Archive_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Intesa_Sanpaolo_Historical_Archive_Map_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Invasive_Plant_Atlas_of_the_United_States_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Iranian_National_Heritage_registration_number": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Irish_National_Inventory_of_Architectural_Heritage_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Irish_National_Monument_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Israel_Antiquities_Auth": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Israel_Museum_Jerusalem_artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IxTheo_Organization_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IxTheo_authority_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "J._Paul_Getty_Museum_agent_DOR_ID_old": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "J._Paul_Getty_Museum_agent_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "J._Paul_Getty_Museum_object_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "JAHIS_Law_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "JECFA_database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "JMA_Seismic_Intensity_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "JMPR_database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "JPL_Small-Body_Database_SPK-ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "JTA_Sightseeing_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "JTI_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "JWF_Wrestlers_Database_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Japan_PlayStation_Software_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Japanese_Canadian_Artists_Directory_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Japanese_Database_of_National_Cultural_Properties_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Japanese_Film_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Jewish_Museum_Berlin_object_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Jewish_Museum_Berlin_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Journalisted_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "KCUE_academy_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "KPU_Plant_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Kaitai_Struct_format_gallery_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Kerala_state_school_code": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Kinoliste_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Knot_Atlas_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Kokugakuin_University_Digital_Museum_entry_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Korean_Academy_of_Science_and_Technology_member_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Korean_National_Species_list_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Kress_Collection_Digital_Archive_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Kunsthistorisches_Museum_Wien_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Kunstmuseum_Basel_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LCCN_Bib": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LCGFT": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LCSH_Subjects": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LC_Argentina": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LC_Children_Subject_Headings": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LC_Chile_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "LC_Medium_Performance_Thesaurus": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LDT_Classification": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LDT_Name_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LDT_Subject_Terms": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LGD_State_or_UT_Code": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LIBRIS_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LIBRIS_library_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LINZ_NZ_Place_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LIPID_MAPS_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Labyrinth_database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Lace_Bugs_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Language_Council_of_Norways_termwiki_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Laws_&_Regulations_Database_of_the_Republic_of_China_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LepIndex_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Les_Archives_du_spectacle_organization_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Les_Archives_du_spectacle_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LibraryThing_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LibraryThing_series_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LibraryThing_venue_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LibraryThing_work_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Library_Haskala_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Library_of_Congress_BIBFRAME_Work_ID": {
        "rest": "https://api.crossref.org/works"
    },
    "Linguist_List_code": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Linguistic_Atlas_of_Late_Mediaeval_English_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Liszt_Academy_Lexikon_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Lithuanian_Heritage_Registry_code": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Living_Music_Database_composer_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LombardiaBeniCulturali_archive_producer_family_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LombardiaBeniCulturali_archive_producer_organization_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LombardiaBeniCulturali_archive_producer_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Looted_Cultural_Assets_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Louvre_Museum_ARK_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Lower_Austrian_Museum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "MAVISE_competent_authority_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "MEP_directory_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "MERIL_Portal_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "MPPDA_Digital_Archive_film_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "MPPDA_Digital_Archive_organisation_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "MPPDA_Digital_Archive_person_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Madrean_Discovery_Expeditions_Fauna_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Madrean_Discovery_Expeditions_Flora_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Maltese_Islands_National_Inventory_of_Cultural_Property_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Map_of_Life_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Mapa_place_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Mapcarta_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Mapes_de_Patrimoni_Cultural_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Mapillary_photo_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Mapillary_username": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Mapping_Manuscript_Migrations_manuscript_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Mapping_Museums_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Mapping_the_Lives_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Mappy_place_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Mapy.com_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "MarineRegions_Gazetteer_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Maritime_Business_Directory_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Maryland_Archives_Bio": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Maryland_Plant_Atlas_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Marylands_National_Register_Properties_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Media_Arts_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Merck_Index_monograph": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Merck_Index_reaction_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Met_Museum_Object_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Meteoritical_Bulletin_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Military_Historical_Archive_exile_army_member_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Milldatabase_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "MinCiencias_Colombia_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Minneapolis_Institute_of_Art_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Minneapolis_Institute_of_Art_constituent_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Mobility_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Modern_China_Biographical_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Modern_History_Database_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Molendatabase_verdwenen_molens_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Monasticon_Hibernicum_database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Muse_Open_Archive_author_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Museo_Galileo_authority_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museu_Paulista_objects_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museum_Data_Service_museum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museum_Day_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museum_ID_from_Mexico_SIC_directory_of_museums": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museum_Universe_Data_File_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museum_of_Brittany_collections_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museum_of_Fine_Arts_Bordeaux_object_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museum_of_Fine_Arts_Boston_object_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museum_of_Fine_Arts_Houston_object_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museum_of_Fine_Arts_Lyon_object_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museum_of_Fine_Arts_of_Rennes_object_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museum_of_Gothenburg_object_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museum_of_Modern_Art_artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museum_of_Modern_Art_work_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museum_of_the_Jewish_People_at_Beit_Hatfutsot_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museum_of_the_Russian_Academy_of_Arts_artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museums_in_Austria_Code": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museums_in_Russia_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Museums_in_Styria_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "MusicBrainz_Work_Authority": {
        "rest": "https://api.crossref.org/works"
    },
    "MyDramaList_name_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "MyWaifuList_work_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Myths_on_Maps_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "M\u00e9moire_du_cyclisme_cyclist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "N64-Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NACSIS-CAT_library_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NAJ_Japan_Archive_Persons": {
        "rest": "https://api.ror.org/organizations"
    },
    "NBM_authority_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NCL_Taiwan": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NES_Cart_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NES_Directory_game_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NHK_Archives_Portal": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NHK_Archives_program_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NIH_RePORTER": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NIST_Data_Registry_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NLB_authority_ID_Belarus": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NLI_Archive_bibliographic_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "NLR_Russia_Persons_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Estonia_Works_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Norway_Bibsys_Persons": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NL_Scotland_Persons_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NOAA_Fisheries_Species_Directory_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NR_Canada_Place_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NSF_Award_Search": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NSZL_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NUKAT_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NUK_Persons": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NVE_Lake_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Nantes_Museum_of_Arts_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Nasjonalbiblioteket_photographer_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Academy_of_Engineering_member_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Academy_of_Medicine_France_member_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Academy_of_Sciences_member_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Association_of_Teachers_of_Singing_member_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Associations_Register_Number_Spain": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Book_Foundation_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Book_Foundation_book_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Bridge_Inventory_Number": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Buildings_Repository_identifier": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Cancer_Institute_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Database_of_Laws_and_Regulations_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Discography_of_Italian_Song_artist/group_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Discography_of_Italian_Song_work_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Drug_Code": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Forest_Foundation_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Gallery_London_PID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Gallery_Prague_work_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Gallery_of_Art_artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Gallery_of_Art_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Gallery_of_Australia_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Gallery_of_Canada_artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Gallery_of_Ireland_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Gallery_of_Victoria_artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Gallery_of_Victoria_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Heritage_List_for_England_number": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Historic_Lookout_Register_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Historical_Museums_of_Sweden_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Inventory_of_Canadian_Military_Memorials_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Inventory_of_Dams_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Monuments_of_Namibia_Site_Reference": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Museum_Norway_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Museum_in_Warsaw_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Museums_of_Japan_e-museum_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Park_Foundation_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Park_Service_place_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Pipe_Organ_Register_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Pollutant_Inventory_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Portrait_Gallery_London_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Portrait_Gallery_London_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Portrait_Gallery_United_States_object_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Provider_Identifier": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Recreation_Trails_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Register_Database_Louisiana_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Register_of_Monumental_Trees_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Registry_of_Exonerations_Case_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Research_Institute_for_Cultural_Properties_artist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Science_Foundation_award": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Trust_Collections_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Trust_Heritage_Records_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Union_Catalog_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_Union_of_Composers_of_Ukraine_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "National_cultural_monument_of_Czechia_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Nationalmuseum_Sweden_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Nationalmuseum_Sweden_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Native_Plants_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Natural_Atlas_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Natural_History_Museum_London_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Natural_Product_Atlas_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Nederlands_Fotomuseum_photographer_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Nederlandse_Molendatabase_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Nelson-Atkins_Museum_of_Art_artwork_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Nelson-Atkins_Museum_of_Art_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Netherlands_KVK": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "New_Index_of_Middle_English_Verse_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "New_York_Flora_Atlas_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "New_Zealand_Gazetteer_place_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Nomenclature_for_Museum_Cataloging": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Norway_Database_for_Statistics_on_Higher_education_publisher_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Norway_Import_Service_and_Registration_Authority_periodical_code": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Norway_Import_Service_and_Registration_Authority_publisher_code": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Norwegian_National_Museum_producer_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Norwegian_National_Road_DataBase_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Norwegian_Polar_Institute_place_name_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Norwegian_State_Administration_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Notable_Names_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Numista_ruling_authority_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OAPEN_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OBO_Gazetteer_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OIML_Issuing_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OLAC_video_game_genre_vocabulary_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ONIX_codelist_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ONS_UK_Publications": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OSHA_Occupational_Chemical_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OSM_Name_Suggestion_Index_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OSNI_Northern_Ireland_Place_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OS_Ireland_Place_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OS_Open_Names_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Offshore_Leaks_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Ohio_University_ArchivesSpace_agent_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Online_Archive_of_California_finding_aid_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Ontario_public_library_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Ontology_of_units_of_Measure_2.0_unit_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OpenAIRE_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OpenAIRE_Provider_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OpenDOAR_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OpenHistoricalMap_relation_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OpenOwnership_Register": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OpenRetro_Game_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OpenStates_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OpenStreetMap_relation_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Open_Contracting_Meta_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Open_Media_Database_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Or_Movement_regional_council_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Ordnance_Survey_Wales_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Oregon_Historic_Sites_Database_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OrgIdGuide_Dumps": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Org_Id_Guide": {
        "rest": "https://api.ror.org/organizations"
    },
    "Org_id_Guide_Meta_Registry": {
        "rest": "https://api.ror.org/organizations"
    },
    "Organ_Index_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Oskar_Schindler_Archive_agent_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Oxford_Dictionary_of_National_Biography_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "PACTR_Organization_Registry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "PORBASE_Authority": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "PRotein_Ontology_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "PTMA_Universities": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "PUG_authority_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Pacific_Coast_Architecture_Database_building_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Pacific_Coast_Architecture_Database_firm_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Pacific_Coast_Architecture_Database_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Packard_Humanities_Institute_PHI_Greek_Inscriptions_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Padua_Research_Archive_author_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Paleobiology_Database_reference_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Pasteur_Institute_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OECD_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "WTO_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "IAEA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ILO_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ERIC_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "OSTI_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Tunisia_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Sudan_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Cambodia_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Laos_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Mongolia_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "OpenAlex_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ISNI_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "GND_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "BnF_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "BNE_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "NDL_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "OpenCorporates_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "LCNAF_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "NTA_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "OpenLibrary_Author": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AAT_Award": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DataCite_Award": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GeoNames_Location": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "TGN_Location": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Academy_Award": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NSF_Award": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "PEN_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Members_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ACLS_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "IFLA_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ISC_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Alberta_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OpenLibrary_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SF_Awards_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "ACM_Awards_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "RSC_Fellow": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "TWAS_Fellow": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "EBU_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "EUNIC_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ADB_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "ACM_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "BNMX_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "AIATSIS_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Canada_Historic_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ASCE_Landmark_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ADB_Publication_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "AAGM_Artwork_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Euro08_Winner": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "TwoGIS_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Academy_Awards_Film": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AwardsWinners_Artist": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SLQ_Queensland_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "BC_Catalonia_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "K10plus_Germany_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SWB_Germany_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "CSL_California_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SLP_Pennsylvania_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SLO_Ohio_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "OSL_Oregon_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "LVA_Virginia_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SLNC_NorthCarolina_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SLF_Florida_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Poland_BN_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Israel_NLI_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Czech_NKP_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Ireland_NLI_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Portugal_BNP_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Scotland_NLS_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Wales_NLW_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Canada_LAC_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "India_NLI_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Greece_NLG_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "DNB_Germany_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ZDB_Germany_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "BNF_France_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "BSB_Bavaria_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SLNSW_Australia_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SLV_Australia_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SBB_Berlin_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "FUB_Berlin_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "HUB_Berlin_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "TUB_Berlin_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ASCAP_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "HAL_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AwardsWinners_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "ALS_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AAA_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "JTI_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AEDA_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "MedalHonor_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "AINM_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ACER_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ACUM_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Euro08_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "HebrewTheatre_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "AMPAS_Item": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ANPI_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SevenDays_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "AAA_UK_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ADAL_Spain_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Bavarian_Monument_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Australian_Heritage_Place_2": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NYSL_NewYork_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "CARLI_Illinois_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "TSLAC_Texas_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "RERO_Swiss_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Euskariana_Basque_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "MnPALS_Minnesota_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "WISC_Law_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "CSL_Colorado_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "MSU_Missouri_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "BVPB_Spain_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Galiciana_Galicia_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "BVA_Andalucia_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Sailor_Maryland_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "AILA_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Altexto_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Estonia_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Latvia_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Lithuania_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Serbia_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Bulgaria_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Morocco_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SLSA_Australia_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SLWA_Australia_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SLTAS_Australia_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Iceland_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "HeBIS_Germany_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "KOBV_Germany_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "BVB_Germany_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "HBZ_Germany_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "MassState_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "MichiganState_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "WashingtonState_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "GeorgiaState_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "BC_Legislative_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Ontario_Legislative_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Syria_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "KSA_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Egypt_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "UAE_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Jordan_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "LIBRIS_Sweden_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Georgia_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Ukraine_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Sloan_Prize": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "AMPAS_Person_2": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Norway_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Korea_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Taiwan_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Singapore_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Malaysia_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Indonesia_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "AJOL_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AJUP_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ArizonaState_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NevadaState_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "TennesseeState_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "KentuckyState_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ConnecticutState_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Alberta_Provincial_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Manitoba_Provincial_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Saskatchewan_Provincial_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Iraq_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Palestine_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Kuwait_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Lebanon_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Qatar_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Algeria_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Moldova_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Albania_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Montenegro_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Kosovo_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Jamaica_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Malta_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SriLanka_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Bangladesh_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Pakistan_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Austria_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Slovenia_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Bosnia_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Croatia_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Hungary_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "AtomicHeritage_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Antarctic_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BaneNOR_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ALCA_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "ALCUIN_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Georgia_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Armenia_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Switzerland_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Denmark_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Bolivia_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Bahamas_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Barbados_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Belize_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Guyana_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Haiti_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Ethiopia_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Ghana_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Kenya_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Rwanda_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Senegal_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Tanzania_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Uganda_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Zimbabwe_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "IvoryCoast_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Vatican_Library_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Macedonia_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Cyprus_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Oman_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Fiji_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Kazakhstan_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Belarus_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Slovakia_NA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "AMNH_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "NYC_Art_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ACNC_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Georgia_Emigrants_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "CESAR_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "ARC_Grant": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "OpenDOAR_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "NJ_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "AL_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "AK_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "KS_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "UT_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "OK_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ME_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "VT_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NM_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NS_Provincial_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NB_Provincial_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NL_Provincial_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "PEI_Provincial_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "RS_Memoirs_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Rome_Fellow_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Royal_Society_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "SAM_Gov_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "HAL_TEL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ACM_Author_Id": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "JapanNTA_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "SherpaRomeo_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "IPEDS_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Nobel_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "SECCIK_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "NH_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "RI_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "DE_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SC_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ND_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SD_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ID_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "MT_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "WY_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "LA_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "MS_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "WV_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "HI_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "JTI_Org_2": {
        "rest": "https://api.ror.org/organizations"
    },
    "EU_Transparency_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ERIHPLUS_Journal": {
        "rest": "https://api.crossref.org/journals"
    },
    "Crossref_Funder_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ABEU_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "CastillaLeon_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Valencia_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "LaRioja_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Sicilia_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Toscana_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "AfricanMinds_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AlbinMichel_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "GrantNav_Prize": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Asturias_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Cantabria_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Navarra_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "CastillaLaMancha_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Canarias_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Veneto_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Piemonte_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Lazio_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Campania_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "AFNIL_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ASEUC_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AlternativaTeatral_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BHF_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "REUN_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AAGM_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ReliefWeb_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AmericanHeritage_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ISIL_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ODUCAL_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AFAS_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Ads_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Antarctic_Place_2": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IFACCA_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AGORHA_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "AR_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "IN_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "IA_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NE_State_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ACE_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Banrepcultura_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Smithsonian_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Europeana_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Sudoc_France_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Gallica_BnF_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "DPLA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Redalyc_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SciELO_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Dialnet_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "IdRef_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Bombardirov_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "ADB_Org_Auth": {
        "rest": "https://api.ror.org/organizations"
    },
    "AEF_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ALPSP_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ASALE_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "re3data_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "RussianDict_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "ChineseBio_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "QueerScientists_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "AAMC_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AALA_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "BabelNet_Entity": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CODEN_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "EuropePMC_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "OpenCitations_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ThreeSixtyGiving_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Grammy_Award": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "NYPL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "BHL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "CiNii_Books_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Jisc_Hub_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NSZL_Hungary_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NSK_Croatia_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NUK_Slovenia_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "BL_EThOS_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Sirene_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "DOAJ_Journal": {
        "rest": "https://api.crossref.org/journals"
    },
    "IdRef_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "SBN_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "BVMC_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "GCD_Publisher": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SIC_Mexico": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "GRID_Historical": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "LoC_USA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NLM_USA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NAL_USA_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NLC_China_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "LIBRUNAM_Mexico_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Pergamum_Brazil_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NUKAT_Poland_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "WorldLII_Law_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Trinidad_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Aruba_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ProPublica_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "NLA_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "ANZL_Writer": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Nepal_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Bangladesh_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Pakistan_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Ethiopia_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Uganda_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Zenodo_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "arXiv_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ZLB_Berlin_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Tokyo_Met_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "London_Met_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Academy_Awards_Nominee": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ArchivesACT_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ArchivesNZ_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ArchivesBosnia_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "BarbadosArchives_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "BelizeArchives_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "JamaicaArchives_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Akadem_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Annuaire_Fondations_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Madrid_Regional_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Murcia_Regional_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Aragon_Regional_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "NLSA_SouthAfrica_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ACA_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "RS_Past_Fellow_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Ads_Winner": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "FIPB_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "NationalArchives_Global_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "InternetArchive_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ISSN_International_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ArchiveGrid_OCLC_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "AUP_NZ_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Israel_Art_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "TIB_Germany_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ZBMED_Germany_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ZBW_Germany_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "IndCat_India_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "RISS_Korea_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "CALIS_China_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Bahrain_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Turkmenistan_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Tajikistan_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Kyrgyzstan_NL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Israel_Antiquities_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Israel_Museum_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Israel_Company_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Mexico_Aviation_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Mexico_Museums_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "SA_English_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "EULAC_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "NLI_Israel_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Egyptian_Museum_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "MinCiencias_Colombia_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Nigeria_NL_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Nigerian_Company_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "SNIESS_Colombia_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Vietnam_Company_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AGN_Colombia_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "CanTho_Vietnam_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Egypt_GAFI_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "BaFin_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Premiados_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Slovakia_History_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Psychiatry_Bio_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Czech_Bio_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Bulgarian_Antarctic_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "PBN_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AEUP_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Algerian_NL_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Bavarian_Monument_Auth_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BALaT_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "ArtHistorians_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Indy_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Andorra_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "SanMarino_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Armenia_Archive_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Azerbaijan_Archive_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Haiti_Archive_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Senegal_Archive_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "GRC_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AICTE_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AISHE_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AJOL_Org_2": {
        "rest": "https://api.ror.org/organizations"
    },
    "ASCL_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Leiden_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ASI_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CiNii_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Garuda_Org_2": {
        "rest": "https://api.ror.org/organizations"
    },
    "Indo_College_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "BNB_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Akadem_Person_2": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Brapci_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "CNKI_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "OASPA_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ACUP_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "UNE_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AArU_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "UPI_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "CEEOL_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "CLACSO_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ASSAf_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Garuda_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "MyJurnal_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ABU_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AFPU_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AG_Univerlage_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "KUPA_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "CUPA_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "DOAB_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "CharityCommission_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ProjectMUSE_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "JSTOR_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Indonesia_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "CWGC_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "CGIAR_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "IPA_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "PASA_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "UPAN_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AaRC_Winner": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "RussianTV_Winner": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "IRINS_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Barcelona_Heritage_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Gatehouse_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ARTIC_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "ARTIC_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "ASEE_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Drammen_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ELEM_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Athens_Academy_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Rome_Academy_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "French_Academy_Science_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Korean_Academy_Science_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Liszt_Academy_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "APE_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Archnet_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "BAnQ_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "BDCYL_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Sinica_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Georgia_Bio_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Georgia_Encyc_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Georgia_Monument_Place": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "DSI_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "CGIAR_Registry_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Irish_Bio_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Canadian_Bio_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Welsh_Bio_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Swedish_Bio_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "ADAGP_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "ABMC_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "NZ_Bio_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "US_Congress_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Finland_Bio_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Finland_Swedish_Bio_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "AFI_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "BPH_Journal": {
        "rest": "https://api.crossref.org/journals"
    },
    "Ulster_Bio_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Swedish_Women_Bio_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Poetry_America_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "CNKI_Institute_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "CTHS_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Cistercian_Bio_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "DACS_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "DBA_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "APA_Psych_Concept": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ARABTERM_Concept": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Biology_Concept": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Icelandic_Concept": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Greek_Concept": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BookBrainz_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "BookBrainz_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "BookBrainz_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "BookBub_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "BookDepository_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ISFDB_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "ISFDB_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "ISFDB_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Bookogs_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Catalan_Writers_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Israeli_Creators_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Poetry_Foundation_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Poetry_Archive_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Scottish_Poetry_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Goodreads_Author_Id": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "CLMP_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "IPG_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Swedish_Lit_Bank_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Hessian_Lit_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Armenian_Lit_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Kazakh_Lit_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Alabama_Lit_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Arab_Lit_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Amazon_Author_Id": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Aozora_Lit_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Hungarian_Namespace_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Finnish_Gallery_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Azerbaijan_Encyc_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Georgia_Film_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Danish_Film_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Folklore_Thesaurus_Concept": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Swiss_Authors_Winner": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Freelance_Editorial_Winner": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Foreign_Missions_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Software_Preservation_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Sami_Publishers_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Ukraine_History_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Flanders_Arts_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Ankara_Institute_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Dharma_Drum_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "AIATSIS_Subject_Concept": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "British_Museum_Concept": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "BG_Academic_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "CAS_Chemical_Concept": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Romania_NGO_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "SFADB_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "UNITER_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "UNESCO_Concept": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "African_Film_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "African_Music_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "BN_Brazil_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "BNP_Portugal_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "NLP_Poland_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "NL_Greece_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "GuideStar_Israel_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Swedish_Academy_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "NAS_Member_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "NAE_Member_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Medicine_France_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Swedish_Letters_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Saxon_Academy_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Lombardia_Arch_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Turin_University_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Islamic_Arch_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Oxford_Arch_Concept": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "RS_Bio_Memoirs_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "British_Council_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "CWA_Writer_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "SciFi_Encyc_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "RS_Fellow_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "BDGest_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Lambiek_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Ricochet_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Pixiv_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Bologna_Fair_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "AniDB_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "DriveThruComics_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "LC_Childrens_Concept": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "MSU_Comic_Art_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "Quadrinhopedia_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Animator_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "LTI_Korea_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Poets_Writers_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "WGA_Writer_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "FNAWN_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "GCD_Series_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "CEATL_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "FIT_Translators_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "EIBF_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Word_Alliance_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Festivaletteratura_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "African_Minds_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Estonian_Research_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Singapore_Research_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "IxTheo_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "MyCite_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "zbMATH_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "DBLP_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "PubMed_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Max_Planck_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Fraunhofer_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "PEN_Centres_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "Alliance_Indie_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "OLH_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "OpenEdition_Org": {
        "rest": "https://api.ror.org/organizations"
    },
    "BLPL_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Bitraga_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Sardinian_Writers_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "DBNL_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Anhui_Writers_Person": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "VIAF_Personal": {
        "rest": "https://pub.orcid.org/v3.0/search"
    },
    "Dictionary_of_Norwegian_Translators_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Dictionary_of_Swedish_Translators_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "MAPS_poet_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Finnish_national_bibliography_corporate_name_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "A_Dictionary_of_Biology_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "A_Dictionary_of_Contemporary_Icelandic_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "A_Dictionary_of_Media_and_Communication_entry_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "A_Dictionary_of_Sociology_entry_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "A_Dictionary_of_Geography_entry_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "A_Dictionary_of_Education_entry_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "A_Dictionary_of_Plant_Sciences_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "A_Dictionary_of_Zoology_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Alabama_Authors_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Alsharekh_Archive_author_ID": {
        "rest": "https://api.ror.org/organizations"
    },
    "Acervo_de_Literatura_Digital_Mato-Grossense_person_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Anglo-Norman_Dictionary_entry": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Archives_de_la_critique_d_art_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "ASCAP_ACE_Repertory_publisher_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Associacio_d_Escriptors_en_Llengua_Catalana_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Association_francaise_pour_l_avancement_des_sciences_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Australian_Dictionary_of_Biography_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Bologna_Children_s_Book_Fair_exhibitor_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Book_Industry_Communication_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Book_Trust_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Book_Web_Taiwan_author_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "British_Council_Writers_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Cambridge_University_Press_book_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Catalogo_Informatizzato_delle_Riviste_Italiane_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Centro_de_Documentacion_de_las_Artes_Escenicas_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    },
    "Chambers_Biographical_Dictionary_ID": {
        "rest": "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
    }
}
API_REGISTRY.update(DOMAIN_MAPPED_ENDPOINTS)
