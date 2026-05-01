from lib.strategies_aat import process_aat_query
from lib.strategies_academy import process_academy_query
from lib.strategies_acm import process_acm_query
from lib.strategies_acm_author import process_acm_author_query
from lib.strategies_adb import process_adb_query
from lib.strategies_adb_org import process_adb_org_query
from lib.strategies_adb_pubs import process_adb_pubs_query
from lib.strategies_agorha import process_agorha_query
from lib.strategies_aiatsis import process_aiatsis_query
from lib.strategies_alberta import process_alberta_query
from lib.strategies_antarctic import process_antarctic_query
from lib.strategies_awardswinners import process_aw_query
from lib.strategies_babelnet import process_babelnet_query
from lib.strategies_bnf import process_bnf_query
from lib.strategies_bne import process_bne_query
from lib.strategies_bnmx import process_bnmx_query
from lib.strategies_bvmc import process_bvmc_query
from lib.strategies_canada_historic import process_canada_historic_query
from lib.strategies_cesar import process_cesar_query
from lib.strategies_coden import process_coden_query
from lib.strategies_crossref_funder import process_crossref_funder_query
from lib.strategies_datacite import process_datacite_query
from lib.strategies_doaj import process_doaj_query
from lib.strategies_doab import process_doab_query
from lib.strategies_charity_commission import process_charity_query
from lib.strategies_projectmuse import process_muse_query
from lib.strategies_jstor import process_jstor_query
from lib.strategies_indonesia import process_indonesia_query
from lib.strategies_erihplus import process_erihplus_query
from lib.strategies_europepmc import process_epmc_query
from lib.strategies_eutransparency import process_eutransparency_query
from lib.strategies_gcd import process_gcd_query
from lib.strategies_geonames import process_geonames_query
from lib.strategies_georgia_emigrants import process_georgia_query
from lib.strategies_gnd import process_gnd_query
from lib.strategies_google_books import process_google_books_query
from lib.strategies_grid import process_grid_query
from lib.strategies_grammy import process_grammy_query
from lib.strategies_hal import process_hal_query
from lib.strategies_hal_tel import process_hal_tel_query
from lib.strategies_hathitrust import process_hathi_query
from lib.strategies_id_loc_gov import process_id_query
from lib.strategies_idref import process_idref_query
from lib.strategies_ifacca import process_ifacca_query
from lib.strategies_ipeds import process_ipeds_query
from lib.strategies_isil import process_isil_query
from lib.strategies_isni import process_isni_query
from lib.strategies_japanta import process_japanta_query
from lib.strategies_lcnaf import process_lcnaf_query
from lib.strategies_members import process_members_query
from lib.strategies_ndl import process_ndl_query
from lib.strategies_nla import process_nla_query
from lib.strategies_nobel import process_nobel_query
from lib.strategies_nsf import process_nsf_query
from lib.strategies_nta import process_nta_query
from lib.strategies_oclc import process_oclc_query
from lib.strategies_opencitations import process_opencitations_query
from lib.strategies_opencorporates import process_opencorporates_query
from lib.strategies_openalex import process_openalex_query
from lib.strategies_openlibrary import process_openlibrary_title_query
from lib.strategies_openlibrary_authors import process_ol_authors_query
from lib.strategies_openlibrary_works import process_ol_works_query
from lib.strategies_pen import process_pen_query
from lib.strategies_propublica import process_propublica_query
from lib.strategies_re3data import process_re3data_query
from lib.strategies_ror import process_ror_query
from lib.strategies_rs_memoirs import process_rs_memoirs_query
from lib.strategies_sam_gov import process_sam_gov_query
from lib.strategies_sbn import process_sbn_query
from lib.strategies_sherpa import process_sherpa_query
from lib.strategies_sic_mexico import process_sic_mexico_query
from lib.strategies_sirene import process_sirene_query
from lib.strategies_sparql_generic import process_sparql_generic_query
from lib.strategies_tgn import process_tgn_query
from lib.strategies_threesixtygiving import process_threesixtygiving_query
from lib.strategies_viaf import process_viaf_query, process_viaf_title_query
from lib.strategies_batch49 import process_batch49_query
from lib.strategies_batch53 import process_batch53_query
from lib.strategies_batch56 import process_batch56_query
from lib.strategies_batch61 import process_batch61_query
from lib.strategies_batch65 import process_batch65_query
from lib.strategies_artic import process_artic_query
from lib.strategies_elem import process_elem_query
from lib.strategies_bnb_brazil import process_bnb_query
from lib.strategies_brapci import process_brapci_query
from lib.strategies_cnki import process_cnki_query
from lib.strategies_kupa import process_kupa_query
from lib.strategies_cupa import process_cupa_query
from lib.strategies_ceeol import process_ceeol_query
from lib.strategies_garuda import process_garuda_query
from lib.strategies_myjurnal import process_myjurnal_query
from lib.strategies_cwgc import process_cwgc_query
from lib.strategies_irins import process_irins_query
from lib.strategies_cgiar_registry import process_cgiar_registry_query
from lib.strategies_wikidata import process_wikidata_title_query
from lib.strategies_wp_json import process_wp_json_query


DIRECT_HANDLERS = {
    "LC_Work_Id": process_id_query,
    "Google_Books": process_google_books_query,
    "OCLC_Record": process_oclc_query,
    "VIAF_Personal": process_viaf_query,
    "VIAF_Title": process_viaf_title_query,
    "Wikidata_Title": process_wikidata_title_query,
    "OpenLibrary_Title": process_openlibrary_title_query,
    "ROR_Org": process_ror_query,
    "GeoNames_Location": process_geonames_query,
    "ThreeSixtyGiving_Org": process_threesixtygiving_query,
    "Grammy_Award": process_grammy_query,
    "Academy_Award": process_academy_query,
    "NSF_Award": process_nsf_query,
    "PEN_Org": process_pen_query,
    "Members_Org": process_members_query,
    "Alberta_Place": process_alberta_query,
    "OpenLibrary_Work": process_ol_works_query,
    "ADB_Person": process_adb_query,
    "ACM_Person": process_acm_query,
    "BNMX_Person": process_bnmx_query,
    "AIATSIS_Place": process_aiatsis_query,
    "Canada_Historic_Place": process_canada_historic_query,
    "ADB_Publication_Work": process_adb_pubs_query,
    "HAL_Org": process_hal_query,
    "AwardsWinners_Person": process_aw_query,
    "AwardsWinners_Artist": process_aw_query,
    "Georgia_Emigrants_Person": process_georgia_query,
    "CESAR_Person": process_cesar_query,
    "RS_Memoirs_Person": process_rs_memoirs_query,
    "Royal_Society_Person": process_rs_memoirs_query,
    "Rome_Fellow_Person": process_agorha_query,
    "SAM_Gov_Org": process_sam_gov_query,
    "HAL_TEL_Work": process_hal_tel_query,
    "ACM_Author_Id": process_acm_author_query,
    "JapanNTA_Org": process_japanta_query,
    "SherpaRomeo_Work": process_sherpa_query,
    "IPEDS_Org": process_ipeds_query,
    "Nobel_Person": process_nobel_query,
    "EU_Transparency_Org": process_eutransparency_query,
    "ERIHPLUS_Journal": process_erihplus_query,
    "Crossref_Funder_Org": process_crossref_funder_query,
    "ISIL_Org": process_isil_query,
    "Antarctic_Place_2": process_antarctic_query,
    "IFACCA_Org": process_ifacca_query,
    "AGORHA_Person": process_agorha_query,
    "ADB_Org_Auth": process_adb_org_query,
    "re3data_Org": process_re3data_query,
    "BabelNet_Entity": process_babelnet_query,
    "CODEN_Work": process_coden_query,
    "EuropePMC_Work": process_epmc_query,
    "OpenCitations_Work": process_opencitations_query,
    "TGN_Location": process_tgn_query,
    "AAT_Award": process_aat_query,
    "DataCite_Award": process_datacite_query,
    "ISNI_Person": process_isni_query,
    "BnF_Person": process_bnf_query,
    "Sirene_Org": process_sirene_query,
    "DOAJ_Journal": process_doaj_query,
    "IdRef_Person": process_idref_query,
    "SBN_Work": process_sbn_query,
    "BVMC_Person": process_bvmc_query,
    "GCD_Publisher": process_gcd_query,
    "SIC_Mexico": process_sic_mexico_query,
    "GRID_Historical": process_grid_query,
    "NLA_Person": process_nla_query,
    "ProPublica_Org": process_propublica_query,
    "BNE_Person": process_bne_query,
    "NDL_Person": process_ndl_query,
    "OpenCorporates_Org": process_opencorporates_query,
    "LCNAF_Person": process_lcnaf_query,
    "NTA_Person": process_nta_query,
    "OpenLibrary_Author": process_ol_authors_query,
    "GND_Person": process_gnd_query,
    "OpenAlex_Org": process_openalex_query,
    "HathiTrust": process_hathi_query,
    "Finnish_Gallery_Person": lambda q, c: process_batch65_query(q, c, "FinnishGallery"),
    "Danish_Film_Person": lambda q, c: process_batch65_query(q, c, "DanishFilm"),
    "IPG_Org": lambda q, c: process_batch49_query(q, c, "IPG"),
    "MinCiencias_Colombia_Org": lambda q, c: process_batch49_query(q, c, "MinCiencias"),
    "Nigeria_NL_Org": lambda q, c: process_batch49_query(q, c, "NigeriaNL"),
    "Nigerian_Company_Org": lambda q, c: process_batch49_query(q, c, "NigerianCorp"),
    "SNIESS_Colombia_Org": lambda q, c: process_batch49_query(q, c, "SNIESS"),
    "AGN_Colombia_Org": lambda q, c: process_batch49_query(q, c, "AGN_Col"),
    "CanTho_Vietnam_Org": lambda q, c: process_batch49_query(q, c, "CanTho"),
    "Egypt_GAFI_Org": lambda q, c: process_batch49_query(q, c, "GAFI"),
    "BaFin_Org": lambda q, c: process_batch49_query(q, c, "BaFin"),
    "Premiados_Person": lambda q, c: process_batch49_query(q, c, "Premiados"),
    "Psychiatry_Bio_Person": lambda q, c: process_batch49_query(q, c, "Biapsy"),
    "Czech_Bio_Person": lambda q, c: process_batch49_query(q, c, "CzechBio"),
    "AFI_Person": lambda q, c: process_batch49_query(q, c, "AFI"),
    "Ulster_Bio_Person": lambda q, c: process_batch49_query(q, c, "UlsterBio"),
    "Swedish_Women_Bio_Person": lambda q, c: process_batch49_query(q, c, "SKBL"),
    "Algerian_NL_Person": lambda q, c: process_batch49_query(q, c, "AlgeriaNL"),
    "Irish_Bio_Person": lambda q, c: process_batch49_query(q, c, "IrishBio"),
    "Swedish_Bio_Person": lambda q, c: process_batch49_query(q, c, "SwedishBio"),
    "AJOL_Org_2": lambda q, c: process_batch49_query(q, c, "AJOL"),
    "ASCL_Work": lambda q, c: process_batch49_query(q, c, "ASCL"),
    "Garuda_Org_2": lambda q, c: process_batch49_query(q, c, "Garuda"),
    "BNB_Person": process_bnb_query,
    "Brapci_Person": process_brapci_query,
    "CNKI_Person": process_cnki_query,
    "KUPA_Org": process_kupa_query,
    "CUPA_Org": process_cupa_query,
    "NZ_Bio_Person": lambda q, c: process_batch56_query(q, c, "NZBio"),
    "US_Congress_Person": lambda q, c: process_batch56_query(q, c, "USCongress"),
    "APA_Psych_Concept": lambda q, c: process_batch61_query(q, c, "APA"),
    "Biology_Concept": lambda q, c: process_batch61_query(q, c, "Biology"),
    "Icelandic_Concept": lambda q, c: process_batch61_query(q, c, "Icelandic"),
    "Poetry_Foundation_Person": lambda q, c: process_batch65_query(q, c, "PoetryFoundation"),
    "Poetry_Archive_Person": lambda q, c: process_batch65_query(q, c, "PoetryArchive"),
    "Scottish_Poetry_Person": lambda q, c: process_batch65_query(q, c, "ScottishPoetry"),
    "Goodreads_Author_Id": lambda q, c: process_batch65_query(q, c, "Goodreads"),
    "BALaT_Person": lambda q, c: process_batch53_query(q, c, "BALaT"),
    "Indy_Place": lambda q, c: process_batch53_query(q, c, "Indy"),
    "CEEOL_Org": process_ceeol_query,
    "Garuda_Org": process_garuda_query,
    "MyJurnal_Org": process_myjurnal_query,
    "CWGC_Person": process_cwgc_query,
    "IRINS_Org": process_irins_query,
    "CGIAR_Registry_Org": process_cgiar_registry_query,
    "ARTIC_Person": lambda q, c: process_artic_query(q, c, "artists"),
    "ARTIC_Work": lambda q, c: process_artic_query(q, c, "artworks"),
    "ELEM_Org": process_elem_query,
    "DOAB_Org": process_doab_query,
    "CharityCommission_Org": process_charity_query,
    "ProjectMUSE_Org": process_muse_query,
    "JSTOR_Org": process_jstor_query,
    "Indonesia_Place": process_indonesia_query,
}


WP_JSON_ENDPOINTS = {
    "FIPB_Org": ("http://fipb.org.in/wp-json/wp/v2/members", "Organization"),
    "AUP_NZ_Org": ("https://www.publishers.org.nz/wp-json/wp/v2/members", "Organization"),
    "ArtHistorians_Person": ("https://arthistorians.info/wp-json/wp/v2/pages", "Person"),
    "GRC_Org": ("https://globalresearchcouncil.org/wp-json/wp/v2/members", "Organization"),
    "OASPA_Org": ("https://oaspa.org/wp-json/wp/v2/members", "Organization"),
    "ACUP_Org": ("https://www.acup.ca/wp-json/wp/v2/members", "Organization"),
    "UNE_Org": ("https://www.une.es/wp-json/wp/v2/members", "Organization"),
    "AArU_Org": ("http://www.aaru.edu.jo/wp-json/wp/v2/members", "Organization"),
    "UPI_Org": ("https://www.universitypressitaliane.it/wp-json/wp/v2/members", "Organization"),
    "CLACSO_Org": ("https://www.clacso.org/wp-json/wp/v2/red-de-centros", "Organization"),
    "ASSAf_Org": ("https://www.assaf.org.za/wp-json/wp/v2/members", "Organization"),
    "ABU_Org": ("https://www.abu.bo/wp-json/wp/v2/editoriales", "Organization"),
    "AFPU_Org": ("https://www.afpu.fr/wp-json/wp/v2/members", "Organization"),
    "AG_Univerlage_Org": ("https://ag-univerlage.de/wp-json/wp/v2/members", "Organization"),
    "ACLS_Org": ("https://www.acls.org/wp-json/wp/v2/member-societies", "Organization"),
    "IFLA_Org": ("https://www.ifla.org/wp-json/wp/v2/members", "Organization"),
    "ISC_Org": ("https://council.science/wp-json/wp/v2/members", "Organization"),
    "EBU_Org": ("https://www.ebu.ch/wp-json/wp/v2/members", "Organization"),
    "EUNIC_Org": ("https://www.eunicglobal.eu/wp-json/wp/v2/members", "Organization"),
    "EULAC_Org": ("https://eulac.org/wp-json/wp/v2/editoriales", "Organization"),
    "AEUP_Org": ("https://www.aeup.eu/wp-json/wp/v2/members", "Organization"),
    "IPA_Org": ("https://www.internationalpublishers.org/wp-json/wp/v2/book-fairs", "Organization"),
    "CGIAR_Org": ("https://www.cgiar.org/wp-json/wp/v2/research-centers", "Organization"),
    "PASA_Org": ("https://publishers.org.za/wp-json/wp/v2/members", "Organization"),
    "UPAN_Org": ("https://www.upan.org.au/wp-json/wp/v2/members", "Organization"),
    "CLMP_Org": ("https://www.clmp.org/wp-json/wp/v2/directory", "Organization"),
    "Poetry_America_Person": ("https://poetrysociety.org/wp-json/wp/v2/pages", "Person"),
    "Welsh_Bio_Person": ("https://biography.wales/wp-json/wp/v2/pages", "Person"),
    "Drammen_Place": ("https://byleksikon.drmk.no/wp-json/wp/v2/posts", "Place"),
    "ALS_Org": ("https://allianceofliterarysocieties.wordpress.com/wp-json/wp/v2/members", "Organization"),
    "AAA_Org": ("https://www.agentsassoc.co.uk/wp-json/wp/v2/members", "Organization"),
    "AAA_UK_Org": ("https://www.agents.org.uk/wp-json/wp/v2/members", "Organization"),
    "ADAL_Spain_Org": ("https://adal.es/wp-json/wp/v2/agencias-asociadas", "Organization"),
    "AILA_Org": ("https://ailanet.org/wp-json/wp/v2/publishers", "Organization"),
    "Altexto_Org": ("https://www.altexto.mx/wp-json/wp/v2/catalog", "Organization"),
    "AJOL_Org": ("https://www.ajol.info/wp-json/wp/v2/publishers", "Organization"),
    "AJUP_Org": ("http://www.ajup-net.com/wp-json/wp/v2/members", "Organization"),
    "NYC_Art_Place": ("https://data.cityofnewyork.us/resource/2pg3-gcaa.json", "Place"),
    "SECCIK_Org": ("https://sic.cultura.gob.mx/opendata/d/0_editorial_directorio.csv", "Organization"),
    "JTI_Org": ("https://www.jti.or.jp/wp-json/wp/v2/registry", "Organization"),
    "JTI_Org_2": ("https://jti-app.org/api/", "Organization"),
    "ABEU_Org": ("https://abeu.org.br/wp-json/wp/v2/catalog", "Organization"),
    "AfricanMinds_Org": ("https://africanminds.co.za/wp-json/wp/v2/mapping", "Organization"),
    "ASEUC_Org": ("https://aseuc.org.co/wp-json/wp/v2/catalog", "Organization"),
    "AlternativaTeatral_Place": ("https://www.alternativateatral.com/wp-json/wp/v2/place", "Place"),
    "REUN_Org": ("https://reun.edu.ar/wp-json/wp/v2/catalog", "Organization"),
    "ReliefWeb_Org": ("https://api.reliefweb.int/v1/organizations", "Organization"),
    "AmericanHeritage_Place": ("https://www.americanheritage.com/wp-json/wp/v2/place", "Place"),
    "ODUCAL_Org": ("https://oducal.com/wp-json/wp/v2/members", "Organization"),
    "AEF_Org": ("https://www.fundaciones.org/es/fundaciones-asociadas", "Organization"),
    "ALPSP_Org": ("https://www.alpsp.org/Member-Directory", "Organization"),
    "ASALE_Org": ("https://www.asale.org/academias", "Organization"),
    "AAMC_Org": ("https://aamc-us.org/wp-json/wp/v2/institutions", "Organization"),
    "AALA_Org": ("https://www.aala.org/wp-json/wp/v2/members", "Organization"),
}


SPARQL_PROPERTIES = {
    "ACA_Person": ("P6635", "Person", "en"),
    "RS_Past_Fellow_Person": ("P8612", "Person", "en"),
    "Ads_Winner": ("P9046", "Winner", "en"),
    "Akadem_Person_2": ("P12214", "Person", "en"),
    "AICTE_Org": ("P4897", "Organization", "en"),
    "AISHE_Org": ("P6392", "Organization", "en"),
    "Leiden_Place": ("P5198", "Place", "en"),
    "ASI_Place": ("P1371", "Place", "en"),
    "CiNii_Org": ("P2409", "Organization", "en"),
    "Indo_College_Org": ("P10139", "Organization", "id"),
    "Israel_Art_Person": ("P1736", "Person", "he"),
    "Israel_Antiquities_Place": ("P3941", "Place", "he"),
    "Israel_Museum_Person": ("P7681", "Person", "he"),
    "Israel_Company_Org": ("P10889", "Organization", "he"),
    "Mexico_Aviation_Org": ("P5746", "Organization", "es"),
    "Mexico_Museums_Place": ("P13690", "Place", "es"),
    "SA_English_Work": ("P11647", "Work", "en"),
    "NLI_Israel_Org": ("P8189", "Organization", "he"),
    "Egyptian_Museum_Org": ("P12732", "Organization", "en"),
    "Vietnam_Company_Org": ("P13944", "Organization", "vi"),
    "PBN_Org": ("P3124", "Organization", "pl"),
    "Bavarian_Monument_Auth_Place": ("P4244", "Place", "de"),
    "AaRC_Winner": ("P7533", "Winner", "pt"),
    "RussianTV_Winner": ("P10062", "Winner", "ru"),
    "Barcelona_Heritage_Place": ("P11557", "Place", "ca"),
    "Gatehouse_Place": ("P4141", "Place", "en"),
    "Kazakh_Lit_Person": ("P13875", "Person", "kk"),
    "Alabama_Lit_Person": ("P11831", "Person", "en"),
    "Arab_Lit_Person": ("P9792", "Person", "ar"),
    "Amazon_Author_Id": ("P4862", "Person", "en"),
    "Aozora_Lit_Person": ("P7311", "Person", "ja"),
    "Swedish_Lit_Bank_Person": ("P5101", "Person", "sv"),
    "Hessian_Lit_Person": ("P10363", "Person", "de"),
    "Armenian_Lit_Person": ("P9528", "Person", "hy"),
    "Catalan_Writers_Person": ("P13086", "Person", "ca"),
    "Israeli_Creators_Person": ("P12989", "Person", "he"),
    "BookBrainz_Person": ("P2607", "Person", "en"),
    "BookBrainz_Org": ("P8063", "Organization", "en"),
    "BookBrainz_Work": ("P7823", "Work", "en"),
    "BookBub_Person": ("P9196", "Person", "en"),
    "BookDepository_Org": ("P10122", "Organization", "en"),
    "ISFDB_Person": ("P1233", "Person", "en"),
    "ISFDB_Org": ("P1234", "Organization", "en"),
    "ISFDB_Work": ("P1235", "Work", "en"),
    "Bookogs_Work": ("P8211", "Work", "en"),
    "ARABTERM_Concept": ("P12900", "Concept", "ar"),
    "Greek_Concept": ("P1263", "Concept", "el"),
    "CNKI_Institute_Org": ("P10693", "Organization", "zh"),
    "CTHS_Org": ("P1961", "Organization", "fr"),
    "Cistercian_Bio_Person": ("P8441", "Person", "de"),
    "DACS_Person": ("P4663", "Person", "en"),
    "DBA_Person": ("P4992", "Person", "da"),
    "Slovakia_History_Work": ("P8238", "Work", "sk"),
    "Bulgarian_Antarctic_Place": ("P5388", "Place", "bg"),
    "BPH_Journal": ("P4569", "Journal", "en"),
    "ABMC_Person": ("P5756", "Person", "en"),
    "Finland_Bio_Person": ("P9324", "Person", "fi"),
    "Finland_Swedish_Bio_Person": ("P3595", "Person", "sv"),
    "Folklore_Thesaurus_Concept": ("P8540", "Concept", "en"),
    "Swiss_Authors_Winner": ("P1291", "Winner", "fr"),
    "Freelance_Editorial_Winner": ("P9540", "Winner", "en"),
    "Foreign_Missions_Person": ("P7077", "Person", "fr"),
    "Software_Preservation_Org": ("P7516", "Organization", "en"),
    "Canadian_Bio_Person": ("P2753", "Person", "en"),
    "ADAGP_Person": ("P3901", "Person", "fr"),
    "Hungarian_Namespace_Person": ("P11621", "Person", "hu"),
    "Azerbaijan_Encyc_Person": ("P11848", "Person", "az"),
    "Georgia_Film_Person": ("P6501", "Person", "ka"),
    "Georgia_Bio_Person": ("P4991", "Person", "en"),
    "Georgia_Encyc_Person": ("P4903", "Person", "en"),
    "Georgia_Monument_Place": ("P4166", "Place", "ka"),
    "DSI_Person": ("P2349", "Person", "en"),
    "APE_Person": ("P1263", "Person", "en"),
    "Archnet_Org": ("P12728", "Organization", "en"),
    "BAnQ_Person": ("P3280", "Person", "fr"),
    "BDCYL_Person": ("P3964", "Person", "es"),
    "Sinica_Person": ("P6705", "Person", "zh"),
    "Athens_Academy_Person": ("P10141", "Person", "el"),
    "Rome_Academy_Person": ("P9097", "Person", "en"),
    "French_Academy_Science_Person": ("P6282", "Person", "fr"),
    "Korean_Academy_Science_Person": ("P10910", "Person", "ko"),
    "Liszt_Academy_Person": ("P8281", "Person", "hu"),
    "ASEE_Person": ("P9791", "Person", "en"),
    "ANZL_Writer": ("P5635", "Person", "en"),
    "Academy_Awards_Nominee": ("P6150", "Winner", "en"),
    "Akadem_Person": ("P12214", "Person", "en"),
    "Annuaire_Fondations_Org": ("P4911", "Organization", "en"),
    "Academy_Awards_Film": ("P6145", "Award", "en"),
    "Euro08_Winner": ("P7111", "Winner", "ru"),
    "TwoGIS_Place": ("P12487", "Place", "en"),
}


SPARQL_FALLBACK_TYPES = {
    "SF_Awards_Person",
    "ACM_Awards_Person",
    "RSC_Fellow",
    "TWAS_Fellow",
    "ASCE_Landmark_Place",
    "AAGM_Artwork_Work",
    "ASCAP_Work",
    "AEDA_Place",
    "MedalHonor_Person",
    "AINM_Place",
    "ACER_Org",
    "ACUM_Org",
    "Euro08_Person",
    "HebrewTheatre_Person",
    "AMPAS_Item",
    "ANPI_Place",
    "SevenDays_Person",
    "Bavarian_Monument_Place",
    "Australian_Heritage_Place_2",
    "Sloan_Prize",
    "AMPAS_Person_2",
    "AtomicHeritage_Org",
    "Antarctic_Place",
    "BaneNOR_Place",
    "ALCA_Person",
    "ALCUIN_Person",
    "AMNH_Org",
    "ACNC_Org",
    "ARC_Grant",
    "OpenDOAR_Org",
    "AFNIL_Org",
    "AlbinMichel_Person",
    "GrantNav_Prize",
    "BHF_Person",
    "AAGM_Org",
    "AFAS_Person",
    "Ads_Work",
    "ACE_Org",
    "Bombardirov_Person",
    "RussianDict_Person",
    "ChineseBio_Person",
    "QueerScientists_Person",
    "AICTE_Org",
    "AISHE_Org",
    "Leiden_Place",
    "ASI_Place",
    "CiNii_Org",
    "Indo_College_Org",
    "Israel_Art_Person",
    "Israel_Antiquities_Place",
    "Israel_Museum_Person",
    "Israel_Company_Org",
    "Mexico_Aviation_Org",
    "Mexico_Museums_Place",
    "SA_English_Work",
    "NLI_Israel_Org",
    "Egyptian_Museum_Org",
    "Vietnam_Company_Org",
    "Slovakia_History_Work",
    "Bulgarian_Antarctic_Place",
    "PBN_Org",
    "Bavarian_Monument_Auth_Place",
    "Akadem_Person_2",
}


DEFAULT_SPARQL_TEMPLATE = (
    'SELECT ?item ?itemLabel WHERE { '
    '?item p:PROPERTY [] . '
    '?item rdfs:label ?itemLabel . '
    'FILTER(regex(?itemLabel, "QUERY_TEXT", "i")) '
    'FILTER(LANG(?itemLabel) = "__LANG__") '
    '} LIMIT 5'
)


def _type_name_for_sparql(type_id):
    if type_id.endswith("_Place") or "Place" in type_id:
        return "Place"
    if type_id.endswith("_Org") or "Org" in type_id:
        return "Organization"
    if type_id.endswith("_Work") or "Work" in type_id or type_id.endswith("_Item"):
        return "Work"
    if "Prize" in type_id or "Award" in type_id or "Grant" in type_id or "Winner" in type_id:
        return "Award"
    return "Person"


def _process_sparql_property(type_id, query, config):
    prop, type_name, lang = SPARQL_PROPERTIES.get(
        type_id,
        ("P1263", _type_name_for_sparql(type_id), "en"),
    )
    template = DEFAULT_SPARQL_TEMPLATE.replace("PROPERTY", prop).replace("__LANG__", lang)
    return process_sparql_generic_query(query, config, template, type_name=type_name)


def dispatch_reconcile_query(type_id, query, config):
    handler = DIRECT_HANDLERS.get(type_id)
    if handler is not None:
        return handler(query, config)

    wp_json = WP_JSON_ENDPOINTS.get(type_id)
    if wp_json is not None:
        endpoint_url, type_name = wp_json
        return process_wp_json_query(query, config, endpoint_url, type_name=type_name)

    if type_id in SPARQL_PROPERTIES or type_id in SPARQL_FALLBACK_TYPES:
        return _process_sparql_property(type_id, query, config)

    return None
