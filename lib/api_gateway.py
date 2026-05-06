import os
import json

API_REGISTRY = {
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
    },
    "Japan_NDL_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru",
        "z3950": "id.ndl.go.jp:210/ndla"
    },
    "Canada_LAC_Library": {
        "sru": "http://amicus.collectionscanada.gc.ca:210/NLC",
        "z3950": "amicus.collectionscanada.gc.ca:210/NLC"
    },
    "Israel_NLI_Library": {
        "sru": "https://nli.alma.exlibrisgroup.com/view/sru/972NNL_INST",
        "z3950": "nli.alma.exlibrisgroup.com:210/972NNL_INST"
    },
    "Poland_BN_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json",
        "sru": "http://data.bn.org.pl/api/sru/bibs"
    },
    "Czech_NKC_Library": {
        "sru": "https://aleph.nkp.cz/X",
        "z3950": "aleph.nkp.cz:9991/NKC-UTF"
    },
    "Sweden_Libris_Library": {
        "rest": "http://libris.kb.se/xsearch",
        "sru": "http://libris.kb.se/sru"
    },
    "Norway_NL_Library": {
        "rest": "https://api.nb.no/catalog/v1/items",
        "sru": "https://api.nb.no/sru"
    },
    "Denmark_NL_Library": {
        "sru": "https://kbdk-sru.kb.dk/sru/",
        "z3950": "z3950.kb.dk:210/catalog"
    },
    "Finland_NL_Library": {
        "sru": "https://fennica.linneanet.fi/sru",
        "z3950": "fennica.linneanet.fi:210/voyager"
    },
    "Portugal_BNP_Library": {
        "sru": "http://purl.pt/index/sru",
        "z3950": "biblioteca.bnp.pt:210/biblios"
    },
    "Estonia_NL_Library": {
        "sru": "https://data.nlib.ee/sru/ESTER",
        "z3950": "data.nlib.ee:210/ESTER"
    },
    "Latvia_NL_Library": {
        "sru": "https://primolatvija.hosted.exlibrisgroup.com/view/sru/371KISCNLL_VU1",
        "z3950": "primolatvija.hosted.exlibrisgroup.com:210/371KISCNLL_VU1"
    },
    "Lithuania_NL_Library": {
        "sru": "https://ibiblioteka.lt/view/sru/LNB",
        "z3950": "ibiblioteka.lt:210/KNYGOS"
    },
    "Iceland_NL_Library": {
        "sru": "https://leitir.is/sru",
        "z3950": "leitir.is:210/geg"
    },
    "India_NLI_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru",
        "z3950": "103.19.252.137:2100/default"
    },
    "UAE_NL_Library": {
        "sru": "https://api.nla.ae/sru",
        "z3950": "nla.ae:210/biblios"
    },
    "Turkey_NL_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Greece_NL_Library": {
        "sru": "https://data.nlg.gr/api/SRU",
        "z3950": "z3950.nlg.gr:210/biblios"
    },
    "Brazil_BN_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru",
        "z3950": "acervo.bn.gov.br:210/biblios"
    },
    "Chile_NL_Library": {
        "sru": "http://200.28.148.146:210/BNC01",
        "z3950": "200.28.148.146:210/BNC01"
    },
    "Uruguay_NL_Library": {
        "sru": "http://200.40.211.131:210/BNU01",
        "z3950": "200.40.211.131:210/BNU01"
    },
    "Singapore_NLB_Library": {
        "rest": "https://catalogue.nlb.gov.sg/cgi-bin/koha/opac-search.pl",
        "sru": "http://catalogue.nlb.gov.sg/cgi-bin/koha/sru"
    },
    "Hungary_NL_Library": {
        "z3950": "amicus.oszk.hu:1616/ANY"
    },
    "Slovakia_NL_Library": {
        "z3950": "z3950.snk.sk:1111/clas01"
    },
    "Puerto_Rico_NL_Library": {
        "z3950": "bnpr.kohacatalog.com:9999/biblios"
    },
    "Italy_SBN_Library": {
        "z3950": "opac.sbn.it:2100/nopac"
    },
    "Smithsonian_Library": {
        "rest": "https://api.si.edu/openaccess/api/v1.0/search"
    },
    "Europeana_Library": {
        "rest": "https://api.europeana.eu/record/v2/search.json"
    },
    "DPLA_Library": {
        "rest": "https://api.dp.la/v2/items"
    },
    "Zenodo_Library": {
        "rest": "https://zenodo.org/api/records"
    },
    "arXiv_Library": {
        "rest": "http://export.arxiv.org/api/query"
    },
    "Banrepcultura_Library": {
        "z3950": "na06.alma.exlibrisgroup.com:1921/57BDLRDC_INST"
    },
    "Argentina_BNMM_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Mexico_NLC_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Colombia_UNAL_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Lebanon_AUB_Library": {
        "z3950": "libcat.aub.edu.lb:210/innopac"
    },
    "Sudan_OU_Library": {
        "z3950": "ous.daphnis.opalsinfo.net:210/ous_ous"
    },
    "UAE_HCT_Library": {
        "z3950": "library.hct.ac.ae:210/INNOPAC"
    },
    "Pakistan_CPL_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Bangladesh_BRAC_Library": {
        "z3950": "library.bracu.ac.bd:9999/biblios"
    },
    "Colorado_State_Library": {
        "z3950": "csl.alma.exlibrisgroup.com:1921/01COL_STATE"
    },
    "Delaware_State_Library": {
        "z3950": "dela.sirsi.net:2200/Unicorn"
    },
    "Hawaii_State_Library": {
        "z3950": "kanawai.bywatersolutions.com:9997/biblios"
    },
    "Idaho_State_Library": {
        "z3950": "voyager.boisestate.edu:7025/voyager"
    },
    "Indiana_State_Library": {
        "z3950": "z3950.evergreen.lib.in.us:210/egin"
    },
    "Kansas_State_Library": {
        "z3950": "k-state.alma.exlibrisgroup.com:1921/01KSU_INST"
    },
    "Kentucky_State_Library": {
        "z3950": "library.acaweb.org:210/innopac"
    },
    "Maine_State_Library": {
        "z3950": "mainecat.maine.edu:210/INNOPAC"
    },
    "Maryland_State_Library": {
        "z3950": "cosmos.somd.lib.md.us:210/cosmos"
    },
    "Massachusetts_State_Library": {
        "z3950": "catalog.helmlib.org:9998/biblios"
    },
    "Mississippi_State_Library": {
        "z3950": "alcorn.sirsi.net:9019/Unicorn"
    },
    "Missouri_State_Library": {
        "z3950": "lindahall.alma.exlibrisgroup.com:210/01LINDAHALL_INST"
    },
    "Montana_State_Library": {
        "z3950": "mtsc.sirsi.net:2200/UNICORN"
    },
    "Nebraska_State_Library": {
        "z3950": "z3950.biblionix.com:210/mortonjames"
    },
    "Nevada_State_Library": {
        "z3950": "z3950.unr.edu:210/innopac"
    },
    "New_Mexico_State_Library": {
        "z3950": "nmsu.alma.exlibrisgroup.com:1921/01NEWMEX_INST"
    },
    "North_Carolina_State_Library": {
        "z3950": "slnc.alma.exlibrisgroup.com:1921/01SLNC_INST"
    },
    "Oklahoma_State_Library": {
        "z3950": "okstate-stillwater.alma.exlibrisgroup.com:1921/01OKSTATESTILL_OKSTAT"
    },
    "Oregon_State_Library": {
        "z3950": "alliance.alma.exlibrisgroup.com:1921/01ALLIANCE_OSL"
    },
    "South_Carolina_State_Library": {
        "z3950": "pascal-musc.alma.exlibrisgroup.com:1921/01PASCAL_MUSC"
    },
    "Vermont_State_Library": {
        "z3950": "vermont-vt.alma.exlibrisgroup.com:1921/01UVM_INST"
    },
    "West_Virginia_State_Library": {
        "z3950": "library.acaweb.org:210/innopac"
    },
    "Wyoming_State_Library": {
        "z3950": "wyld.sirsi.net:2200/UNICORN"
    },
    "Alabama_State_Library": {
        "z3950": "alcorn.sirsi.net:9019/Unicorn"
    },
    "Alaska_State_Library": {
        "z3950": "a50019.eos-intl.net:210/main"
    },
    "Arizona_State_Library": {
        "z3950": "arizona-asu.alma.exlibrisgroup.com:1921/01ASU_INST"
    },
    "Georgia_State_Library": {
        "z3950": "galileo-gsu.alma.exlibrisgroup.com:1921/01GALI_GSU"
    },
    "Michigan_State_Library": {
        "z3950": "elibrary.mel.org:210/INNOPAC"
    },
    "Minnesota_State_Library": {
        "z3950": "mnpals-network.alma.exlibrisgroup.com:1921/01PALS_NETWORK"
    },
    "North_Dakota_State_Library": {
        "z3950": "na01.alma.exlibrisgroup.com:1921/01ODIN_NETWORK"
    },
    "South_Dakota_State_Library": {
        "z3950": "sdsl.bywatersolutions.com:9991/biblios"
    },
    "Utah_State_Library": {
        "z3950": "pion.sirsi.net:8319/unicorn"
    },
    "Virginia_State_Library": {
        "z3950": "lva.alma.exlibrisgroup.com:1921/01VIVA_LVA"
    },
    "Washington_State_Library": {
        "z3950": "sbctc-wsl.alma.exlibrisgroup.com:1921/01STATEWA_WSL"
    },
    "Wisconsin_State_Library": {
        "z3950": "sus.wiscat.net:210/wiscat"
    },
    "Arkansas_State_Library": {
        "z3950": "arks.sirsi.net:2500/UNICORN"
    },
    "California_State_Library": {
        "z3950": "csl.alma.exlibrisgroup.com:1921/01CSL_INST"
    },
    "Connecticut_State_Library": {
        "z3950": "cscu-csl.alma.exlibrisgroup.com:1921/01CSCU_CSL"
    },
    "Illinois_State_Library": {
        "z3950": "i-share-isl.alma.exlibrisgroup.com:1921/01CARLI_ISL"
    },
    "New_Hampshire_State_Library": {
        "z3950": "nhsl.nhais.bywatersolutions.com:9993/biblios"
    },
    "New_Jersey_State_Library": {
        "z3950": "nj.ipac.sirsidynix.net:19610/horizon"
    },
    "New_York_State_Library": {
        "z3950": "nyst.sirsi.net:8419/unicorn"
    },
    "Rhode_Island_State_Library": {
        "z3950": "statelibrarycatalog.sos.ri.gov:9994/biblios"
    },
    "Florida_State_Library": {
        "z3950": "fslt.sirsi.net:7019/UNICORN"
    },
    "Iowa_State_Library": {
        "z3950": "koha.silo.lib.ia.us:9989/biblios"
    },
    "Louisiana_State_Library": {
        "z3950": "ipac.state.lib.la.us:210/Horizon"
    },
    "Ohio_State_Library": {
        "z3950": "ohiolink-slo.alma.exlibrisgroup.com:1921/01OHIOLINK_SLO"
    },
    "Pennsylvania_State_Library": {
        "z3950": "na01.alma.exlibrisgroup.com:1921/01SSHELCO_STLIBPA"
    },
    "Tennessee_State_Library": {
        "z3950": "tnsla.sirsi.net:7819/Unicorn"
    },
    "Texas_State_Library": {
        "z3950": "tsla.sirsi.net:8219/UNICORN"
    },
    "BASE_Universal": {
        "sru": "https://www.base-search.net/about/en/about_sources_api.php"
    },
    "JISC_UK_Hub": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "WorldCat_Universal": {
        "rest": "https://americas.discovery.api.oclc.org/worldcat/search/v2/bibs"
    },
    "LoC_USA_Library": {
        "rest": "https://www.loc.gov/apis/search",
        "sru": "http://lx2.loc.gov/sru/lcdb",
        "z3950": "lx2.loc.gov:210/LCDB"
    },
    "DNB_Germany_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "NLA_Australia_Library": {
        "rest": "https://api.trove.nla.gov.au/v3/sru"
    },
    "Crossref_Work": {
        "rest": "https://api.crossref.org/works"
    },
    "OpenAlex_Work": {
        "rest": "https://api.openalex.org/works"
    },
    "OpenLibrary_Title": {
        "z3950": "latin1"
    },
    "Canada_Women_Writers_Person": {
        "z3950": "utf-8"
    },
    "Swedish_Lit_Bank_Place_2": {
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
    "Society_Authors_Org_2": {
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
    "Society_Authors_Org_3": {
        "z3950": "utf-8"
    },
    "Georgia_Literacy_Person": {
        "z3950": "utf-8"
    },
    "Academy_Awards_Nominee_Direct": {
        "z3950": "utf-8"
    },
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
        "z3950": "utf-8"
    },
    "Swiss_VD_Library": {
        "z3950": "utf-8"
    },
    "Library_of_the_University_of_Santiago_de_Compostela_authority_ID": {
        "z3950": "utf-8"
    },
    "National_Gallery_of_Art_Library_Bibliographic_ID": {
        "z3950": "utf-8"
    },
    "BNF_France_Library": {
        "z3950": "utf-8"
    },
    "CARLI_Illinois_Library": {
        "z3950": "utf-8"
    },
    "MnPALS_Minnesota_Library": {
        "z3950": "utf-8"
    },
    "Ontario_Legislative_Library": {
        "z3950": "utf-8"
    },
    "LIBRIS_Sweden_Library": {
        "z3950": "latin1"
    },
    "Ghana_Central_Library": {
        "z3950": "utf-8"
    },
    "Guatemala_Guatemala_Library": {
        "z3950": "utf-8"
    },
    "Israel_Central_Library": {
        "z3950": "utf-8"
    },
    "Greece_Central_Greece_Library": {
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
    "ACNP_Library": {
        "z3950": "utf-8"
    },
    "ILO_Library": {
        "z3950": "utf-8"
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
    "CastillaLeon_Library": {
        "z3950": "marc8"
    },
    "Valencia_Library": {
        "z3950": "utf-8"
    },
    "Toscana_Library": {
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
    "WorldBank_Library": {
        "z3950": "jolis.imf.org:2200/UNICORN"
    },
    "IMF_Library": {
        "z3950": "utf-8"
    },
    "Madrid_Regional_Library": {
        "z3950": "utf-8"
    },
    "Andorra_Library": {
        "z3950": "utf-8"
    },
    "France_Auvergne_Rhone_Alpes_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "France_Bourgogne_Franche_Comte_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "France_Bretagne_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "France_Corse_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "France_Grand_Est_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "France_Normandie_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "France_Nouvelle_Aquitaine_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "France_Occitanie_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "France_PACA_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Italy_Abruzzo_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Basilicata_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Calabria_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Campania_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Emilia_Romagna_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Friuli_Venezia_Giulia_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Lazio_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Liguria_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Lombardia_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Marche_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Molise_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Piemonte_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Puglia_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Sardegna_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Sicilia_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Toscana_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Trentino_Alto_Adige_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Umbria_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Valle_dAosta_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Veneto_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "UK_East_Midlands_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "UK_London_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "UK_North_East_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "UK_North_West_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "UK_Northern_Ireland_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "UK_Scotland_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "UK_South_East_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "UK_South_West_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "UK_Wales_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "UK_Yorkshire_and_the_Humber_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Chile_Arica_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Parinacota_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Iquique_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Tamarugal_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Antofagasta_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_El_Loa_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Tocopilla_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Chanaral_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Copiapo_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Huasco_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Elqui_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Limari_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Choapa_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Valparaiso_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Quillota_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_San_Antonio_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Los_Andes_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Petorca_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Marga_Marga_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Chacabuco_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Cordillera_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Maipo_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Melipilla_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Talagante_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Cachapoal_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Colchagua_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Cardenal_Caro_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Talca_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Curico_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Linares_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Cauquenes_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Diguillin_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Punilla_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Itata_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Concepcion_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Arauco_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Bio_Bio_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Nuble_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Malleco_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Cautin_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Valdivia_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Ranco_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Osorno_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Llanquihue_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Chiloe_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Palena_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Coyhaique_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Aysen_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_General_Carrera_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Capitan_Prat_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Magallanes_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Tierra_del_Fuego_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Antartica_Chilena_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Ultima_Esperanza_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Turkey_Karabuk_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Turkey_Usak_Library": {
        "rest": "https://www.loc.gov/apis/search",
        "sru": "http://lx2.loc.gov/sru/lcdb",
        "z3950": "lx2.loc.gov:210/LCDB"
    },
    "Korea_Busan_Library": {
        "rest": "https://www.loc.gov/apis/search",
        "sru": "http://lx2.loc.gov/sru/lcdb",
        "z3950": "lx2.loc.gov:210/LCDB"
    },
    "Indonesia_Maluku_Islands_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Pakistan_Sukkur_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "SouthAfrica_Frances_Baard_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "SouthAfrica_Sekhukhune_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "SouthAfrica_uThukela_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Germany_Minor_Baden_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Minor_Wuerttemberg_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Minor_Mecklenburg_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Minor_Pomerania_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Minor_Westphalia_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Minor_Palatinate_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Italy_Minor_Abruzzo_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Minor_Basilicata_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Minor_Calabria_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Minor_Molise_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Minor_Umbria_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Minor_Valle_d_Aosta_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Minor_Trentino_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Italy_Minor_Alto_Adige_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Canada_Municipal_Montreal_Library": {
        "sru": "http://amicus.collectionscanada.gc.ca:210/NLC"
    },
    "Canada_Municipal_Vancouver_Library": {
        "sru": "http://amicus.collectionscanada.gc.ca:210/NLC"
    },
    "Canada_Municipal_Calgary_Library": {
        "sru": "http://amicus.collectionscanada.gc.ca:210/NLC"
    },
    "Canada_Municipal_Edmonton_Library": {
        "sru": "http://amicus.collectionscanada.gc.ca:210/NLC"
    },
    "Canada_Municipal_Winnipeg_Library": {
        "sru": "http://amicus.collectionscanada.gc.ca:210/NLC"
    },
    "Canada_Municipal_Quebec_City_Library": {
        "sru": "http://amicus.collectionscanada.gc.ca:210/NLC"
    },
    "Portugal_Azores_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Madeira_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Pacific_French_Polynesia_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Souk_Ahras_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "PNG_New_Ireland_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Azerbaijan_Yukhari_Shirvan_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Zambia_Lusaka_Library": {
        "rest": "https://www.loc.gov/apis/search",
        "sru": "http://lx2.loc.gov/sru/lcdb",
        "z3950": "lx2.loc.gov:210/LCDB"
    },
    "Tanzania_Rukwa_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Uzbekistan_Bukhara_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Indonesia_East_Nusa_Tenggara_Library": {
        "rest": "https://www.loc.gov/apis/search",
        "sru": "http://lx2.loc.gov/sru/lcdb",
        "z3950": "lx2.loc.gov:210/LCDB"
    },
    "Indonesia_Maluku_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Indonesia_North_Maluku_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Indonesia_West_Nusa_Tenggara_Library": {
        "rest": "https://www.loc.gov/apis/search",
        "sru": "http://lx2.loc.gov/sru/lcdb",
        "z3950": "lx2.loc.gov:210/LCDB"
    },
    "Mali_Timbuktu_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "IvoryCoast_Yamoussoukro_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Cambodia_Preah_Sihanouk_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Oman_Musandam_Library": {
        "rest": "https://www.loc.gov/apis/search",
        "sru": "http://lx2.loc.gov/sru/lcdb",
        "z3950": "lx2.loc.gov:210/LCDB"
    },
    "Croatia_Vukovar_Srijem_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Albania_Kukes_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Czech_Central_Bohemian_Library": {
        "sru": "https://aleph.nkp.cz/X"
    },
    "Czech_South_Bohemian_Library": {
        "sru": "https://aleph.nkp.cz/X"
    },
    "Czech_Plzen_Library": {
        "sru": "https://aleph.nkp.cz/X"
    },
    "Czech_Karlovy_Vary_Library": {
        "sru": "https://aleph.nkp.cz/X"
    },
    "Czech_Usti_nad_Labem_Library": {
        "sru": "https://aleph.nkp.cz/X"
    },
    "Czech_Liberec_Library": {
        "sru": "https://aleph.nkp.cz/X"
    },
    "Czech_Hradec_Kralove_Library": {
        "sru": "https://aleph.nkp.cz/X"
    },
    "Czech_Pardubice_Library": {
        "sru": "https://aleph.nkp.cz/X"
    },
    "Czech_Vysocina_Library": {
        "sru": "https://aleph.nkp.cz/X"
    },
    "Czech_South_Moravian_Library": {
        "sru": "https://aleph.nkp.cz/X"
    },
    "Czech_Olomouc_Library": {
        "sru": "https://aleph.nkp.cz/X"
    },
    "Czech_Zlin_Library": {
        "sru": "https://aleph.nkp.cz/X"
    },
    "Czech_Moravian_Silesian_Library": {
        "sru": "https://aleph.nkp.cz/X"
    },
    "Iraq_Kirkuk_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Iraq_Dahuk_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Norway_Akershus_Library": {
        "rest": "https://api.nb.no/catalog/v1/items"
    },
    "Norway_Buskerud_Library": {
        "rest": "https://api.nb.no/catalog/v1/items"
    },
    "Norway_Nordland_Library": {
        "rest": "https://api.nb.no/catalog/v1/items"
    },
    "Norway_Ostfold_Library": {
        "rest": "https://api.nb.no/catalog/v1/items"
    },
    "Norway_Rogaland_Library": {
        "rest": "https://api.nb.no/catalog/v1/items"
    },
    "Norway_Telemark_Library": {
        "rest": "https://api.nb.no/catalog/v1/items"
    },
    "Norway_Trondelag_Library": {
        "rest": "https://api.nb.no/catalog/v1/items"
    },
    "Norway_Vestfold_Library": {
        "rest": "https://api.nb.no/catalog/v1/items"
    },
    "Norway_Vestland_Library": {
        "rest": "https://api.nb.no/catalog/v1/items"
    },
    "Sweden_Blekinge_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Dalarna_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Gavleborg_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Gotland_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Halland_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Jamtland_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Jonkoping_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Kalmar_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Kronoberg_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Norrbotten_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Orebro_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Ostergotland_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Skane_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Sodermanland_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Uppsala_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Varmland_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Vasterbotten_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Vasternorrland_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Vastmanland_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Sweden_Vastra_Gotaland_Library": {
        "rest": "http://libris.kb.se/xsearch"
    },
    "Denmark_Hovedstaden_Library": {
        "sru": "https://kbdk-sru.kb.dk/sru/"
    },
    "Denmark_Midtjylland_Library": {
        "sru": "https://kbdk-sru.kb.dk/sru/"
    },
    "Denmark_Nordjylland_Library": {
        "sru": "https://kbdk-sru.kb.dk/sru/"
    },
    "Denmark_Sjaelland_Library": {
        "sru": "https://kbdk-sru.kb.dk/sru/"
    },
    "Denmark_Syddanmark_Library": {
        "sru": "https://kbdk-sru.kb.dk/sru/"
    },
    "Finland_Aland_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_Central_Finland_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_Central_Ostrobothnia_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_Kainuu_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_Kanta-Hame_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_Kymenlaakso_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_Lapland_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_North_Karelia_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_North_Ostrobothnia_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_North_Savo_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_Ostrobothnia_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_Paijat-Hame_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_Pirkanmaa_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_Satakunta_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_South_Karelia_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_South_Ostrobothnia_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_South_Savo_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_Southwest_Finland_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Finland_Uusimaa_Library": {
        "sru": "https://fennica.linneanet.fi/sru"
    },
    "Ireland_Carlow_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Cavan_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Clare_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Cork_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Donegal_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Dublin_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Kerry_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Kildare_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Kilkenny_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Laois_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Leitrim_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Limerick_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Longford_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Louth_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Mayo_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Meath_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Monaghan_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Offaly_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Roscommon_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Sligo_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Tipperary_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Waterford_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Westmeath_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Wexford_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ireland_Wicklow_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "UK_England_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "UK_Greater_London_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "UK_Greater_Manchester_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "UK_West_Yorkshire_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "UK_South_Yorkshire_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "UK_Tyne_and_Wear_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "UK_Merseyside_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Portugal_Aveiro_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Beja_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Braga_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Braganca_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Castelo_Branco_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Coimbra_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Evora_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Faro_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Guarda_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Leiria_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Lisboa_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Portalegre_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Porto_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Santarem_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Setubal_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Viana_do_Castelo_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Vila_Real_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Viseu_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Portugal_Acores_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Saudi_Tabuk_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Chile_Arica_y_Parinacota_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Tarapaca_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Atacama_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Coquimbo_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Metropolitana_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_OHiggins_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Maule_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Biobio_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Araucania_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Chile_Los_Lagos_Library": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "Ukraine_Cherkasy_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Chernihiv_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Chernivtsi_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Crimea_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Dnipropetrovsk_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Donetsk_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Ivano-Frankivsk_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Kharkiv_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Kherson_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Khmelnytskyi_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Kirovohrad_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Kyiv_City_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Kyiv_Oblast_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Luhansk_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Lviv_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Mykolaiv_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Odesa_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Poltava_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Rivne_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Sevastopol_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Sumy_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Ternopil_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Vinnytsia_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Volyn_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Zakarpattia_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Zaporizhzhia_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Ukraine_Zhytomyr_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Thailand_Mukdahan_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Thailand_Phuket_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Thailand_Sukhothai_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Poland_Greater_Poland_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "Poland_Kuyavian-Pomeranian_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "Poland_Lesser_Poland_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "Poland_Lodz_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "Poland_Lower_Silesian_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "Poland_Lublin_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "Poland_Lubusz_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "Poland_Masovian_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "Poland_Opole_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "Poland_Podlaskie_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "Poland_Pomeranian_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "Poland_Silesian_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "Poland_Subcarpathian_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "Poland_Holy_Cross_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "Poland_Warmian-Masurian_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "Poland_West_Pomeranian_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "Colombia_Amazonas_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Antioquia_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Arauca_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Atlantico_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Bolivar_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Boyaca_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Caldas_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Caqueta_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Casanare_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Cauca_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Cesar_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Choco_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Cordoba_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Cundinamarca_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Guainia_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Guaviare_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Huila_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_La_Guajira_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Magdalena_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Meta_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Narino_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Putumayo_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Quindio_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Risaralda_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_San_Andres_y_Providencia_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Santander_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Sucre_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Tolima_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Vaupes_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Colombia_Vichada_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "Japan_Aichi_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Akita_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Aomori_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Chiba_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Ehime_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Fukui_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Fukuoka_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Fukushima_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Gifu_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Gunma_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Hiroshima_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Hokkaido_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Hyogo_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Ibaraki_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Ishikawa_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Iwate_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Kagawa_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Kagoshima_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Kanagawa_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Kochi_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Kumamoto_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Kyoto_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Mie_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Miyagi_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Miyazaki_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Nagano_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Nagasaki_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Nara_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Niigata_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Oita_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Okayama_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Okinawa_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Osaka_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Saga_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Saitama_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Shiga_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Shimane_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Shizuoka_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Tochigi_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Tokushima_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Tokyo_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Tottori_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Toyama_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Wakayama_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Yamagata_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Yamaguchi_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Japan_Yamanashi_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Philippines_Agusan_del_Sur_Library": {
        "rest": "https://www.loc.gov/apis/search",
        "sru": "http://lx2.loc.gov/sru/lcdb",
        "z3950": "lx2.loc.gov:210/LCDB"
    },
    "Philippines_Bukidnon_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Italy_Valle_d'Aosta_Library": {
        "sru": "http://opac.sbn.it/sru/servlet/SRU"
    },
    "Argentina_Catamarca_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Chaco_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Chubut_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Cordoba_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Corrientes_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Entre_Rios_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Formosa_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Jujuy_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_La_Pampa_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Mendoza_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Misiones_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Neuquen_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Rio_Negro_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Salta_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_San_Luis_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Santa_Cruz_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Santa_Fe_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Santiago_del_Estero_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Tierra_del_Fuego_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Argentina_Tucuman_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Australia_Northern_Territory_Library": {
        "rest": "https://api.trove.nla.gov.au/v3/sru"
    },
    "Australia_ACT_Library": {
        "rest": "https://api.trove.nla.gov.au/v3/sru"
    },
    "Russia_Chukotka_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Germany_Baden_Wuerttemberg_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Bavaria_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Berlin_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Brandenburg_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Bremen_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Hamburg_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Hesse_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Lower_Saxony_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Mecklenburg_Vorpommern_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_North_Rhine_Westphalia_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Rhineland_Palatinate_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Saarland_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Saxony_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Saxony_Anhalt_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Schleswig_Holstein_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Germany_Thuringia_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "India_Andhra_Pradesh_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Arunachal_Pradesh_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Assam_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Bihar_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Chhattisgarh_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Goa_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Gujarat_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Haryana_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Himachal_Pradesh_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Jharkhand_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Karnataka_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Kerala_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Madhya_Pradesh_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Maharashtra_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Manipur_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Meghalaya_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Mizoram_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Nagaland_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Odisha_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Punjab_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Rajasthan_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Sikkim_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Tamil_Nadu_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Telangana_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Tripura_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Uttar_Pradesh_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Uttarakhand_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_West_Bengal_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Andaman_and_Nicobar_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Chandigarh_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Dadra_and_Nagar_Haveli_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Delhi_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Jammu_and_Kashmir_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Ladakh_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Lakshadweep_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "India_Puducherry_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "Brazil_AC_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_AL_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_AM_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_AP_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_BA_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_CE_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_DF_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_ES_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_GO_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_MA_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_MG_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_MS_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_MT_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_PA_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_PB_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_PE_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_PI_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_PR_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_RJ_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_RN_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_RO_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_RR_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_RS_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_SC_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_SE_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_SP_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Brazil_TO_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Mexico_AG_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_BC_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_BS_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_CM_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_CH_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_CL_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_DG_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_GJ_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_GR_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_HG_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_JA_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_MX_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_MI_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_MO_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_NA_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_NL_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_OA_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_PU_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_QE_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_QR_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_SL_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_SI_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_SO_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_TB_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_TM_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_TX_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_VE_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_YU_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_ZA_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Japan_NationalArchives_Library": {
        "sru": "https://id.ndl.go.jp/auth/ndla/sru"
    },
    "Argentina_NL_Library": {
        "z3950": "200.123.191.9:9991/BNA01"
    },
    "Brazil_NL_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "Colombia_NL_Library": {
        "z3950": "168.176.5.96:9991/SNB01"
    },
    "National_Library_of_Chile_ID": {
        "sru": "http://200.28.148.146:210/BNC01"
    },
    "National_Library_of_Ireland_ID": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "National_Library_of_Wales_Authority_ID": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Kramerius_of_Czech_Digital_Library_UUID": {
        "sru": "https://aleph.nkp.cz/X"
    },
    "Library_Parliament_Canada": {
        "sru": "http://amicus.collectionscanada.gc.ca:210/NLC"
    },
    "Library_of_Congress_JukeBox_ID_former_scheme": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "National_Virtual_Library_of_India_ID": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "BN_Poland_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "NKP_Czech_Library": {
        "sru": "https://aleph.nkp.cz/X"
    },
    "NLI_Ireland_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "BNP_Portugal_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "NLS_Scotland_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "NLW_Wales_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "LAC_Canada_Library": {
        "sru": "http://amicus.collectionscanada.gc.ca:210/NLC"
    },
    "NLI_India_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "ZDB_Germany_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "SLNSW_Australia_Library": {
        "rest": "https://api.trove.nla.gov.au/v3/sru"
    },
    "SLV_Australia_Library": {
        "rest": "https://api.trove.nla.gov.au/v3/sru"
    },
    "K10plus_Germany_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "SWB_Germany_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "SLSA_Australia_Library": {
        "rest": "https://api.trove.nla.gov.au/v3/sru"
    },
    "SLWA_Australia_Library": {
        "rest": "https://api.trove.nla.gov.au/v3/sru"
    },
    "SLTAS_Australia_Library": {
        "rest": "https://api.trove.nla.gov.au/v3/sru"
    },
    "HeBIS_Germany_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "KOBV_Germany_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "BVB_Germany_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "HBZ_Germany_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "Ukraine_NL_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "Sudoc_France_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "NUK_Slovenia_Library": {
        "rest": "https://discover.libraryhub.jisc.ac.uk/search"
    },
    "NLM_USA_Library": {
        "rest": "https://www.loc.gov/apis/search",
        "sru": "http://lx2.loc.gov/sru/lcdb",
        "z3950": "lx2.loc.gov:210/LCDB"
    },
    "NAL_USA_Library": {
        "rest": "https://www.loc.gov/apis/search",
        "sru": "http://lx2.loc.gov/sru/lcdb",
        "z3950": "lx2.loc.gov:210/LCDB"
    },
    "LIBRUNAM_Mexico_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Pergamum_Brazil_Library": {
        "sru": "http://acervo.bn.gov.br/sophia_web/sru"
    },
    "NUKAT_Poland_Library": {
        "rest": "https://data.bn.org.pl/api/institutions/bibs.json"
    },
    "TIB_Germany_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "ZBMED_Germany_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "ZBW_Germany_Library": {
        "sru": "https://services.dnb.de/sru/dnb",
        "z3950": "z3950.dnb.de:210/dnb"
    },
    "IndCat_India_Library": {
        "sru": "http://103.19.252.137:8080/cgi-bin/koha/sru"
    },
    "Turkey_Adana_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Adiyaman_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Afyonkarahisar_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Agri_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Aksaray_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Amasya_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Ankara_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Antalya_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Ardahan_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Artvin_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Aydin_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Balikesir_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Bartin_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Batman_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Bayburt_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Bilecik_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Bingol_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Bitlis_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Bolu_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Burdur_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Bursa_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Canakkale_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Cankiri_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Corum_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Denizli_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Diyarbakir_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Duzce_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Edirne_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Elazig_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Erzincan_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Erzurum_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Eskisehir_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Gaziantep_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Giresun_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Gumushane_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Hakkari_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Hatay_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Igdir_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Isparta_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Istanbul_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Izmir_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Kahramanmaras_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Karaman_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Kars_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Kastamonu_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Kayseri_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Kilis_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Kirikkale_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Kirklareli_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Kirsehir_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Kocaeli_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Konya_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Kutahya_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Malatya_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Manisa_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Mardin_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Mersin_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Mugla_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Mus_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Nevsehir_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Nigde_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Ordu_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Osmaniye_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Rize_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Sakarya_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Samsun_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Sanliurfa_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Siirt_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Sinop_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Sirnak_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Sivas_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Tekirdag_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Tokat_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Trabzon_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Tunceli_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Van_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Yalova_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Yozgat_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Turkey_Zonguldak_Library": {
        "sru": "http://kasif.mkutup.gov.tr/sru",
        "z3950": "kasif.mkutup.gov.tr:210/biblios"
    },
    "Morocco_Beni_Mellal_Khenifra_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Morocco_Casablanca_Settat_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Morocco_Draa_Tafilalet_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Morocco_Dakhla_Oued_Ed_Dahab_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Morocco_Fes_Meknes_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Morocco_Guelmim_Oued_Noun_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Morocco_Laayoune_Sakia_El_Hamra_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Morocco_Marrakesh_Safi_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Morocco_Oriental_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Morocco_Rabat_Sale_Kenitra_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Morocco_Souss_Massa_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Morocco_Tanger_Tetouan_Al_Hoceima_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Pakistan_Bahawalpur_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Dera_Ghazi_Khan_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Faisalabad_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Gujranwala_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Lahore_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Multan_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Rawalpindi_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Sahiwal_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Sargodha_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Karachi_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Hyderabad_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Larkana_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Mirpur_Khas_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Shaheed_Benazirabad_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Bannu_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Dera_Ismail_Khan_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Hazara_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Kohat_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Malakand_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Mardan_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Peshawar_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Kalat_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Makran_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Nasirabad_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Quetta_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Sibi_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Zhob_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Nigeria_Abia_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Adamawa_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Akwa_Ibom_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Bauchi_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Bayelsa_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Benue_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Borno_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Cross_River_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Ebonyi_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Ekiti_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Gombe_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Jigawa_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Katsina_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Kebbi_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Nasarawa_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Taraba_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Yobe_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Zamfara_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "SouthAfrica_Alfred_Nzo_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Amathole_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Buffalo_City_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Cape_Winelands_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Capricorn_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Central_Karoo_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Chris_Hani_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_City_of_Johannesburg_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_City_of_Tshwane_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Dr_Kenneth_Kaunda_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Eden_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_eThekwini_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Fezile_Dabi_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Garden_Route_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Gert_Sibande_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Harry_Gwala_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Joe_Gqabi_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_John_Taolo_Gaetsewe_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Lejweleputswa_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Mangaung_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Mopani_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Namakwa_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Nelson_Mandela_Bay_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Ngaka_Modiri_Molema_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Nkangala_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_OR_Tambo_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Overberg_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Pixley_ka_Seme_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Sedibeng_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Thabo_Mofutsanyana_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_uGu_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_uMgungundlovu_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_uMkhanyakude_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_uMzinyathi_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_uThungulu_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Vhembe_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Waterberg_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_West_Coast_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Xhariep_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_ZF_Mgcawu_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Zululand_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "Algeria_Adrar_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Chlef_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Laghouat_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Oum_El_Bouaghi_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Batna_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Bejaia_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Biskra_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Bechar_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Blida_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Bouira_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Tamanghasset_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Tebessa_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Tlemcen_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Tiaret_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Tizi_Ouzou_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Alger_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Djelfa_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Jijel_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Setif_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Saida_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Skikda_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Sidi_Bel_Abbes_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Annaba_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Guelma_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Constantine_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Medea_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Mostaganem_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_M'Sila_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Mascara_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Ouargla_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Oran_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_El_Bayadh_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Illizi_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Bordj_Bou_Arreridj_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Boumerdes_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_El_Tarf_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Tindouf_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Tissemsilt_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_El_Oued_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Khenchela_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Tipaza_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Mila_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Ain_Defla_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Naama_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Ain_Temouchent_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Ghardaia_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Relizane_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Ariana_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Beja_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Ben_Arous_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Bizerte_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Gabes_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Gafsa_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Jendouba_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Kairouan_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Kasserine_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Kebili_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Kef_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Mahdia_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Manouba_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Medenine_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Monastir_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Nabeul_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Sfax_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Sidi_Bouzid_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Siliana_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Sousse_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Tataouine_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Tozeur_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Tunis_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Tunisia_Zaghouan_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Angola_Bengo_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Angola_Benguela_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Angola_Bie_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Angola_Cabinda_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Angola_Cuanza_Norte_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Angola_Cuanza_Sul_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Angola_Cunene_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Angola_Huambo_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Angola_Huila_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Angola_Luanda_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Angola_Lunda_Norte_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Angola_Lunda_Sul_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Angola_Malanje_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Angola_Moxico_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Angola_Namibe_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Angola_Uige_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "Angola_Zaire_Library": {
        "sru": "http://purl.pt/index/sru"
    },
    "DRCongo_Kinshasa_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Kongo_Central_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Kwango_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Kwilu_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Mai_Ndombe_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Equateur_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Mongala_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Nord_Ubangi_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Sud_Ubangi_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Tshuapa_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Bas_Uele_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Haut_Uele_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Ituri_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Tshopo_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Kasai_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Kasai_Central_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Kasai_Oriental_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Lomami_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Sankuru_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Haut_Katanga_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Haut_Lomami_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Lualaba_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Tanganyika_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Nord_Kivu_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Sud_Kivu_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "DRCongo_Maniema_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Uzbekistan_Andijan_Library": {
        "z3950": "u95030.eos-intl.net:210/main"
    },
    "Uzbekistan_Fergana_Library": {
        "z3950": "u95030.eos-intl.net:210/main"
    },
    "Uzbekistan_Jizzakh_Library": {
        "z3950": "u95030.eos-intl.net:210/main"
    },
    "Uzbekistan_Kashkadarya_Library": {
        "z3950": "u95030.eos-intl.net:210/main"
    },
    "Uzbekistan_Khorezm_Library": {
        "z3950": "u95030.eos-intl.net:210/main"
    },
    "Uzbekistan_Namangan_Library": {
        "z3950": "u95030.eos-intl.net:210/main"
    },
    "Uzbekistan_Navoi_Library": {
        "z3950": "u95030.eos-intl.net:210/main"
    },
    "Uzbekistan_Samarkand_Library": {
        "z3950": "u95030.eos-intl.net:210/main"
    },
    "Uzbekistan_Surkhandarya_Library": {
        "z3950": "u95030.eos-intl.net:210/main"
    },
    "Uzbekistan_Syrdarya_Library": {
        "z3950": "u95030.eos-intl.net:210/main"
    },
    "Uzbekistan_Tashkent_Library": {
        "z3950": "u95030.eos-intl.net:210/main"
    },
    "Uzbekistan_Karakalpakstan_Library": {
        "z3950": "u95030.eos-intl.net:210/main"
    },
    "Nigeria_Anambra_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Delta_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Edo_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Enugu_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Imo_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Kaduna_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Kano_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Kogi_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Kwara_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Lagos_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Niger_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Ogun_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Ondo_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Osun_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Oyo_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Plateau_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Rivers_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_Sokoto_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Nigeria_FCT_Abuja_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Uzbekistan_Tashkent_City_Library": {
        "z3950": "u95030.eos-intl.net:210/main"
    },
    "Uzbekistan_Tashkent_Region_Library": {
        "z3950": "u95030.eos-intl.net:210/main"
    },
    "Peru_Amazonas_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Ancash_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Apurimac_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Arequipa_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Ayacucho_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Cajamarca_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Callao_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Cusco_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Huancavelica_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Huanuco_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Ica_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Junin_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_La_Libertad_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Lambayeque_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Lima_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Loreto_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Madre_de_Dios_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Moquegua_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Pasco_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Piura_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Puno_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_San_Martin_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Tacna_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Tumbes_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Peru_Ucayali_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Algeria_Algiers_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_MSila_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Algeria_Oum_el_Bouaghi_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Lebanon_Beirut_Library": {
        "z3950": "libcat.aub.edu.lb:210/innopac"
    },
    "Lebanon_Akkar_Library": {
        "z3950": "libcat.aub.edu.lb:210/innopac"
    },
    "Lebanon_Baalbek_Hermel_Library": {
        "z3950": "libcat.aub.edu.lb:210/innopac"
    },
    "Lebanon_Beqaa_Library": {
        "z3950": "libcat.aub.edu.lb:210/innopac"
    },
    "Lebanon_Mount_Lebanon_Library": {
        "z3950": "libcat.aub.edu.lb:210/innopac"
    },
    "Lebanon_Nabatieh_Library": {
        "z3950": "libcat.aub.edu.lb:210/innopac"
    },
    "Lebanon_North_Library": {
        "z3950": "libcat.aub.edu.lb:210/innopac"
    },
    "Lebanon_South_Library": {
        "z3950": "libcat.aub.edu.lb:210/innopac"
    },
    "Lebanon_Keserwan_Jbeil_Library": {
        "z3950": "libcat.aub.edu.lb:210/innopac"
    },
    "Bangladesh_Barisal_Library": {
        "z3950": "library.bracu.ac.bd:9999/biblios"
    },
    "Bangladesh_Chittagong_Library": {
        "z3950": "library.bracu.ac.bd:9999/biblios"
    },
    "Bangladesh_Dhaka_Library": {
        "z3950": "library.bracu.ac.bd:9999/biblios"
    },
    "Bangladesh_Khulna_Library": {
        "z3950": "library.bracu.ac.bd:9999/biblios"
    },
    "Bangladesh_Mymensingh_Library": {
        "z3950": "library.bracu.ac.bd:9999/biblios"
    },
    "Bangladesh_Rajshahi_Library": {
        "z3950": "library.bracu.ac.bd:9999/biblios"
    },
    "Bangladesh_Rangpur_Library": {
        "z3950": "library.bracu.ac.bd:9999/biblios"
    },
    "Bangladesh_Sylhet_Library": {
        "z3950": "library.bracu.ac.bd:9999/biblios"
    },
    "Albania_Tirane_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Kenya_Baringo_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Bomet_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Bungoma_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Busia_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Elgeyo_Marakwet_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Embu_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Garissa_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Homa_Bay_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Isiolo_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Kajiado_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Kakamega_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Kericho_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Kiambu_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Kilifi_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Kirinyaga_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Kisii_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Kisumu_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Kitui_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Kwale_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Laikipia_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Lamu_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Machakos_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Makueni_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Mandera_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Marsabit_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Meru_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Migori_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Murang'a_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Nairobi_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Nakuru_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Nandi_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Narok_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Nyamira_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Nyandarua_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Nyeri_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Samburu_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Siaya_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Taita_Taveta_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Tana_River_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Tharaka_Nithi_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Trans_Nzoia_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Turkana_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Uasin_Gishu_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Vihiga_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_Wajir_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Kenya_West_Pokot_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Venezuela_Miranda_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Alborz_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Ardabil_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_East_Azerbaijan_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_West_Azerbaijan_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Bushehr_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Chaharmahal_and_Bakhtiari_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Fars_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Gilan_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Golestan_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Hamadan_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Hormozgan_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Ilam_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Isfahan_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Kerman_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Kermanshah_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_North_Khorasan_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Razavi_Khorasan_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_South_Khorasan_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Khuzestan_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Kohgiluyeh_and_Boyer-Ahmad_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Kurdistan_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Lorestan_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Markazi_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Mazandaran_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Qazvin_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Qom_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Semnan_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Sistan_and_Baluchestan_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Tehran_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Yazd_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Iran_Zanjan_Library": {
        "z3950": "80.191.10.6:210/default"
    },
    "Pakistan_Punjab_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Sindh_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Khyber_Pakhtunkhwa_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Balochistan_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Islamabad_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Pakistan_Gilgit_Baltistan_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "SouthAfrica_Eastern_Cape_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Free_State_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Gauteng_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_KwaZulu_Natal_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Limpopo_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Mpumalanga_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_North_West_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Northern_Cape_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Western_Cape_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "Russia_Adygea_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Altai_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Amur_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Arkhangelsk_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Astrakhan_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Bashkortostan_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Belgorod_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Bryansk_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Buryatia_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Chechnya_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Chelyabinsk_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Chuvashia_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Dagestan_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Ingushetia_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Irkutsk_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Ivanovo_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Jewish_Autonomous_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Kabardino_Balkaria_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Kaliningrad_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Kalmykia_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Kaluga_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Kamchatka_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Karachay_Cherkessia_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Karelia_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Kemerovo_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Khabarovsk_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Khakassia_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Khanty_Mansi_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Kirov_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Komi_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Kostroma_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Krasnodar_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Krasnoyarsk_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Kurgan_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Kursk_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Leningrad_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Lipetsk_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Magadan_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Mari_El_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Mordovia_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Moscow_City_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Moscow_Oblast_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Murmansk_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Nenets_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Nizhny_Novgorod_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_North_Ossetia_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Novgorod_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Novosibirsk_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Omsk_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Orenburg_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Oryol_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Penza_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Perm_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Primorsky_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Pskov_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Rostov_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Ryazan_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Saint_Petersburg_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Sakha_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Sakhalin_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Samara_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Saratov_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Sevastopol_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Smolensk_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Sverdlovsk_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Tambov_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Tatarstan_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Tomsk_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Tula_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Tuva_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Tver_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Tyumen_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Udmurtia_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Ulyanovsk_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Vladimir_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Volgograd_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Vologda_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Voronezh_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Yamalo_Nenets_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Yaroslavl_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_Zabaykalsky_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "China_Anhui_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Beijing_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Chongqing_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Fujian_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Gansu_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Guangdong_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Guangxi_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Guizhou_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Hainan_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Hebei_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Heilongjiang_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Henan_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Hubei_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Hunan_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Inner_Mongolia_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Jiangsu_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Jiangxi_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Jilin_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Liaoning_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Ningxia_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Qinghai_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Shaanxi_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Shandong_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Shanghai_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Shanxi_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Sichuan_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Tianjin_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Tibet_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Xinjiang_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Yunnan_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "China_Zhejiang_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "Uzbekistan_NL_Library": {
        "z3950": "u95030.eos-intl.net:210/main"
    },
    "Kenya_NationalArchives_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Nigeria_NationalArchives_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "Peru_NL_Library": {
        "z3950": "catalogo.sisbib.unmsm.edu.pe:2200/Unicorn"
    },
    "Algerian_National_Library_ID": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "National_Library_of_Nigeria_ID": {
        "rest": "https://api.crossref.org/works"
    },
    "Tunisia_NL_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Sudan_NL_Library": {
        "z3950": "ous.daphnis.opalsinfo.net:210/ous_ous"
    },
    "Morocco_NL_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "Lebanon_NL_Library": {
        "z3950": "libcat.aub.edu.lb:210/innopac"
    },
    "Algeria_NL_Library": {
        "sru": "https://gallica.bnf.fr/SRU"
    },
    "NLC_China_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    },
    "Bangladesh_NL_Library": {
        "z3950": "library.bracu.ac.bd:9999/biblios"
    },
    "Pakistan_NL_Library": {
        "z3950": "122.129.84.203:2100/biblios"
    },
    "Kenya_NL_Library": {
        "z3950": "anu.gnec.kari.opalsinfo.net:210/gnec_anu"
    },
    "Nigeria_NL_Library": {
        "rest": "https://api.crossref.org/works"
    },
    "NLSA_SouthAfrica_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "eLibrary_Russia_Library": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "CALIS_China_Library": {
        "z3950": "las.sinica.edu.tw:210/INNOPAC"
    }
}

# Inactive Regional Nodes (Discovery Pending)
INACTIVE_REGISTRY = {
    "Armenia_Aragatsotn_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Armenia_Ararat_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Armenia_Armavir_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Armenia_Gegharkunik_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Armenia_Kotayk_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Armenia_Lori_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Armenia_Shirak_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Armenia_Syunik_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Armenia_Tavush_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Armenia_Vayots_Dzor_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Georgia_Abkhazia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Georgia_Adjara_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Georgia_Guria_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Georgia_Imereti_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Georgia_Kakheti_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Georgia_Kvemo_Kartli_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Georgia_Mtskheta_Mtianeti_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Georgia_Racha_Lechkhumi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Georgia_Samegrelo_Zemo_Svaneti_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Georgia_Samtskhe_Javakheti_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Georgia_Shida_Kartli_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cuba_Camaguey_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cuba_Ciego_de_Avila_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cuba_Cienfuegos_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cuba_Granma_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cuba_Guantanamo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cuba_Holguin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cuba_Artemisa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cuba_Mayabeque_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cuba_La_Habana_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cuba_Las_Tunas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cuba_Matanzas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cuba_Sancti_Spiritus_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cuba_Villa_Clara_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jamaica_Clarendon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jamaica_Hanover_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jamaica_Kingston_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jamaica_Manchester_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jamaica_Portland_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jamaica_Saint_Andrew_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jamaica_Saint_Ann_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jamaica_Saint_Catherine_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jamaica_Saint_Elizabeth_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jamaica_Saint_James_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jamaica_Trelawny_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jamaica_Westmoreland_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Spain_Andalucia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Spain_Aragon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Spain_Asturias_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Spain_Basque_Country_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Spain_Canary_Islands_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Spain_Cantabria_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Spain_Catalonia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Spain_Extremadura_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Spain_Galicia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Spain_Murcia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Spain_Navarra_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Spain_Valencia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_Seoul_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_Daegu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_Incheon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_Gwangju_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_Daejeon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_Ulsan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_Sejong_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_Gyeonggi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_Gangwon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_North_Chungcheong_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_South_Chungcheong_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_North_Jeolla_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_South_Jeolla_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_North_Gyeongsang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_South_Gyeongsang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_Jeju_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_An_Giang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Ba_Ria_Vung_Tau_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Bac_Giang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Bac_Kan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Bac_Lieu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Bac_Ninh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Ben_Tre_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Binh_Dinh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Binh_Duong_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Binh_Phuoc_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Binh_Thuan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Ca_Mau_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Can_Tho_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Cao_Bang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Da_Nang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Dak_Lak_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Dak_Nong_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Dien_Bien_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Dong_Nai_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Dong_Thap_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Gia_Lai_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Ha_Giang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Ha_Nam_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Ha_Noi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Ha_Tinh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Hai_Duong_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Hai_Phong_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Hau_Giang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Ho_Chi_Minh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Hoa_Binh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Hung_Yen_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Khanh_Hoa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Kien_Giang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Kon_Tum_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Lai_Chau_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Lam_Dong_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Lang_Son_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Lao_Cai_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Long_An_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Nam_Dinh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Nghe_An_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Ninh_Binh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Ninh_Thuan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Phu_Tho_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Phu_Yen_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Quang_Binh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Quang_Nam_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Quang_Ngai_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Quang_Ninh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Quang_Tri_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Soc_Trang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Son_La_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Tay_Ninh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Thai_Binh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Thai_Nguyen_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Thanh_Hoa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Thua_Thien_Hue_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Tien_Giang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Tra_Vinh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Tuyen_Quang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Vinh_Long_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Vinh_Phuc_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vietnam_Yen_Bai_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Panama_Bocas_del_Toro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Panama_Chiriqui_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Panama_Cocle_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Panama_Colon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Panama_Darien_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Panama_Herrera_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Panama_Los_Santos_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Panama_Panama_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Panama_Veraguas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Panama_Panama_Oeste_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "CostaRica_Alajuela_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "CostaRica_Cartago_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "CostaRica_Guanacaste_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "CostaRica_Heredia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "CostaRica_Limon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "CostaRica_Puntarenas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ElSalvador_Ahuachapan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ElSalvador_Cabanas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ElSalvador_Chalatenango_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ElSalvador_Cuscatlan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ElSalvador_La_Libertad_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ElSalvador_La_Union_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ElSalvador_Morazan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ElSalvador_San_Salvador_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ElSalvador_Santa_Ana_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ElSalvador_Sonsonate_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ElSalvador_Usulutan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Ilocos_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Cagayan_Valley_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Central_Luzon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Calabarzon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Mimaropa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Bicol_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Western_Visayas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Central_Visayas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Eastern_Visayas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Zamboanga_Peninsula_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Northern_Mindanao_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Davao_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Soccsksargen_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Caraga_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Bangsamoro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Cordillera_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_NCR_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Sumatra_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Java_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Kalimantan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Sulawesi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Lesser_Sunda_Islands_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Papua_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Spain_Ceuta_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Spain_Melilla_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Pacific_Wallis_and_Futuna_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Pacific_Guam_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Pacific_Northern_Mariana_Islands_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Bougainville_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Central_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Chimbu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Eastern_Highlands_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_East_New_Britain_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_East_Sepik_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Enga_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Gulf_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Hela_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Jiwaka_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Madang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Manus_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Milne_Bay_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Morobe_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Oro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Sandaun_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Southern_Highlands_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_West_New_Britain_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Western_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_Western_Highlands_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Fiji_Central_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Fiji_Eastern_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Fiji_Northern_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Fiji_Western_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SolomonIslands_Central_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SolomonIslands_Choiseul_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SolomonIslands_Guadalcanal_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SolomonIslands_Isabel_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SolomonIslands_Makira_Ulawa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SolomonIslands_Malaita_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SolomonIslands_Rennell_and_Bellona_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SolomonIslands_Temotu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SolomonIslands_Western_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Armenia_Yerevan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Georgia_Tbilisi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Azerbaijan_Absheron_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Azerbaijan_Baku_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Azerbaijan_Ganja_Dashkasan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Azerbaijan_Guba_Khachmaz_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Azerbaijan_Lankaran_Astara_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Azerbaijan_Central_Aran_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Azerbaijan_Mil_Mugan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Azerbaijan_Shaki_Zaqatala_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Azerbaijan_Shamkir_Tovuz_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Azerbaijan_Nakhchivan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Angola_Cuando_Cubango_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mozambique_Cabo_Delgado_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mozambique_Gaza_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mozambique_Inhambane_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mozambique_Manica_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mozambique_Maputo_City_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mozambique_Maputo_Province_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mozambique_Nampula_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mozambique_Niassa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mozambique_Sofala_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mozambique_Tete_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mozambique_Zambezia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zambia_Central_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zambia_Copperbelt_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zambia_Eastern_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zambia_Luapula_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zambia_Muchinga_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zambia_Northern_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zambia_North_Western_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zambia_Southern_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zambia_Western_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cameroon_Adamawa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cameroon_Centre_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cameroon_East_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cameroon_Far_North_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cameroon_Littoral_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cameroon_North_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cameroon_North_West_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cameroon_South_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cameroon_South_West_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cameroon_West_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Analamanga_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Vakinankaratra_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Itasy_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Bongolava_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Sofia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Boeny_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Betsiboka_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Melaky_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Alaotra_Mangoro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Atsinanana_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Analanjirofo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Amoroni_Mania_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Haute_Matsiatra_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Vatovavy_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Fitovinany_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Atsimo_Atsinanana_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Ihorombe_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Androy_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Anosy_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Atsimo_Andrefana_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Madagascar_Menabe_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zimbabwe_Bulawayo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zimbabwe_Harare_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zimbabwe_Manicaland_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zimbabwe_Mashonaland_Central_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zimbabwe_Mashonaland_East_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zimbabwe_Mashonaland_West_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zimbabwe_Masvingo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zimbabwe_Matabeleland_North_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zimbabwe_Matabeleland_South_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Zimbabwe_Midlands_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ethiopia_Addis_Ababa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ethiopia_Afar_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ethiopia_Amhara_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ethiopia_Benishangul_Gumuz_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ethiopia_Dire_Dawa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ethiopia_Gambela_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ethiopia_Harari_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ethiopia_Oromia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ethiopia_Sidama_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ethiopia_Somali_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ethiopia_South_West_Ethiopia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ethiopia_Southern_Nations_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ethiopia_Tigray_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uganda_Central_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uganda_Eastern_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uganda_Northern_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uganda_Western_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ghana_Ahafo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ghana_Ashanti_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ghana_Bono_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ghana_Bono_East_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ghana_Eastern_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ghana_North_East_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ghana_Northern_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ghana_Oti_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ghana_Savannah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ghana_Upper_East_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ghana_Upper_West_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ghana_Volta_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ghana_Western_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ghana_Western_North_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Arusha_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Dar_es_Salaam_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Dodoma_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Geita_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Iringa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Kagera_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Katavi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Kigoma_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Kilimanjaro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Lindi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Manyara_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Mara_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Mbeya_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Morogoro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Mtwara_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Mwanza_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Njombe_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Pemba_North_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Pemba_South_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Pwani_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Ruvuma_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Shinyanga_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Simiyu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Singida_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Songwe_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Tabora_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Tanga_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Zanzibar_North_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Zanzibar_South_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Zanzibar_West_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kyrgyzstan_Batken_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kyrgyzstan_Chuy_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kyrgyzstan_Jalal_Abad_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kyrgyzstan_Naryn_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kyrgyzstan_Osh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kyrgyzstan_Talas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kyrgyzstan_Issyk_Kul_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tajikistan_Sughd_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tajikistan_Khatlon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tajikistan_Gorno_Badakhshan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tajikistan_Dushanbe_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Alta_Verapaz_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Baja_Verapaz_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Chimaltenango_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Chiquimula_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_El_Progreso_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Escuintla_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Huehuetenango_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Izabal_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Jalapa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Jutiapa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Peten_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Quetzaltenango_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Quiche_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Retalhuleu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Sacatepequez_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Santa_Rosa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Solola_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Suchitepequez_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Totonicapan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guatemala_Zacapa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Honduras_Atlantida_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Honduras_Choluteca_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Honduras_Colon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Honduras_Comayagua_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Honduras_Copan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Honduras_Cortes_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Honduras_El_Paraiso_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Honduras_Francisco_Morazan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Honduras_Gracias_a_Dios_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Honduras_Intibuca_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Honduras_Lempira_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Honduras_Ocotepeque_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Honduras_Olancho_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Honduras_Santa_Barbara_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Honduras_Valle_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Honduras_Yoro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nicaragua_Boaco_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nicaragua_Carazo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nicaragua_Chinandega_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nicaragua_Chontales_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nicaragua_Esteli_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nicaragua_Granada_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nicaragua_Jinotega_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nicaragua_Leon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nicaragua_Madriz_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nicaragua_Managua_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nicaragua_Masaya_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nicaragua_Matagalpa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nicaragua_Nueva_Segovia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nicaragua_Rivas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nicaragua_RACCN_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nicaragua_RACCS_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Pacific_Fiji_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Pacific_Kiribati_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Pacific_Marshall_Islands_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Pacific_Micronesia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Pacific_Nauru_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Pacific_Palau_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Pacific_Samoa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Pacific_Tonga_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Pacific_Tuvalu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Pacific_Vanuatu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Macedonia_Skopje_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Macedonia_Bitola_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Macedonia_Kumanovo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Macedonia_Prilep_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Macedonia_Tetovo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Macedonia_Veles_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Macedonia_Stip_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Macedonia_Ohrid_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Macedonia_Strumica_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_Abai_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_Akmola_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_Aktobe_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_Almaty_City_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_Almaty_Region_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_Atyrau_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_East_Kazakhstan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_Jetisu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_Karagandy_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_Kostanay_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_Kyzylorda_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_Mangystau_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_North_Kazakhstan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_Pavlodar_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_Shymkent_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_Turkistan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_Ulytau_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_West_Kazakhstan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_Astana_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Aceh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Bali_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Banten_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Bengkulu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Central_Java_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Central_Kalimantan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Central_Papua_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Central_Sulawesi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_East_Java_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_East_Kalimantan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_East_Papua_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Gorontalo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Highland_Papua_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Jakarta_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Jambi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Lampung_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_North_Kalimantan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_North_Papua_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_North_Sulawesi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_North_Sumatra_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Riau_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Riau_Islands_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_South_Kalimantan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_South_Papua_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_South_Sulawesi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_South_Sumatra_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Southeast_Sulawesi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Southwest_Papua_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_West_Java_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_West_Kalimantan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_West_Papua_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_West_Sulawesi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_West_Sumatra_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_Yogyakarta_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Azuay_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Bolivar_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Canar_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Carchi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Chimborazo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Cotopaxi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_El_Oro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Esmeraldas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Galapagos_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Guayas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Imbabura_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Loja_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Manabi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Morona_Santiago_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Napo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Orellana_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Pastaza_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Pichincha_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Santa_Elena_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Santo_Domingo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Sucumbios_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Tungurahua_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_Zamora_Chinchipe_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bolivia_Beni_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bolivia_Chuquisaca_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bolivia_Cochabamba_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bolivia_Oruro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bolivia_Pando_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bolivia_Potosi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bolivia_Santa_Cruz_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bolivia_Tarija_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mali_Bamako_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mali_Gao_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mali_Kayes_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mali_Kidal_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mali_Koulikoro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mali_Menaka_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mali_Mopti_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mali_Nioro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mali_Segou_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mali_Sikasso_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mali_Taoudenit_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Senegal_Dakar_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Senegal_Diourbel_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Senegal_Fatick_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Senegal_Kaffrine_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Senegal_Kaolack_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Senegal_Kedougou_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Senegal_Kolda_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Senegal_Louga_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Senegal_Matam_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Senegal_Saint_Louis_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Senegal_Sedhiou_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Senegal_Tambacounda_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Senegal_Thies_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Senegal_Ziguinchor_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "IvoryCoast_Abidjan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "IvoryCoast_Bas_Sassandra_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "IvoryCoast_Comoe_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "IvoryCoast_Denguele_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "IvoryCoast_Goh_Djiboua_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "IvoryCoast_Lacs_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "IvoryCoast_Lagunes_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "IvoryCoast_Montagnes_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "IvoryCoast_Sassandra_Marahoue_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "IvoryCoast_Savanes_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "IvoryCoast_Vallee_du_Bandama_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "IvoryCoast_Woroba_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "IvoryCoast_Zanzan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Banteay_Meanchey_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Battambang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Kampong_Cham_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Kampong_Chhnang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Kampong_Speu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Kampong_Thom_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Kampot_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Kandal_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Koh_Kong_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Kratie_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Mondulkiri_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Preah_Vihear_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Prey_Veng_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Pursat_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Ratanakiri_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Siem_Reap_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Stung_Treng_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Svay_Rieng_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Takeo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Oddar_Meanchey_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Kep_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Pailin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_Tboung_Khmum_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Attapeu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Bokeo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Bolikhamsai_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Champasak_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Houaphanh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Khammouane_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Louang_Namtha_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Louangphabang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Oudomxay_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Phongsaly_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Sayabouly_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Salavan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Savannakhet_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Sekong_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Vientiane_Capital_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Vientiane_Province_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Xaisomboun_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_Xiangkhouang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kyrgyzstan_Bishkek_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kyrgyzstan_Osh_City_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kyrgyzstan_Osh_Region_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tajikistan_Districts_of_Republican_Subordination_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Turkmenistan_Ashgabat_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Turkmenistan_Ahal_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Turkmenistan_Balkan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Turkmenistan_Dashoguz_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Turkmenistan_Lebap_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Turkmenistan_Mary_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Syria_Aleppo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Syria_Al_Hasakah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Syria_Al_Latakia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Syria_Al_Qunaytirah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Syria_Al_Raqqah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Syria_Al_Suwayda_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Syria_Daraa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Syria_Deir_ez_Zor_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Syria_Damascus_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Syria_Hama_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Syria_Homs_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Syria_Idlib_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Syria_Rif_Dimashq_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Syria_Tartus_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Oman_Ad_Dakhiliyah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Oman_Ad_Dhahirah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Oman_Al_Batinah_North_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Oman_Al_Batinah_South_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Oman_Al_Buraymi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Oman_Al_Wusta_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Oman_Ash_Sharqiyah_North_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Oman_Al_Sharqiyah_South_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Oman_Dhofar_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Oman_Muscat_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nepal_Koshi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nepal_Madhesh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nepal_Bagmati_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nepal_Gandaki_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nepal_Lumbini_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nepal_Karnali_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nepal_Sudurpashchim_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Bjelovar_Bilogora_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Brod_Posavina_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Dubrovnik_Neretva_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Istria_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Karlovac_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Koprivnica_Krizevci_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Krapina_Zagorje_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Lika_Senj_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Medjimurje_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Osijek_Baranja_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Pozega_Slavonia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Primorje_Gorski_Kotar_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Sibenik_Knin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Sisak_Moslavina_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Split_Dalmatia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Varazdin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Virovitica_Podravina_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Zadar_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Zagreb_County_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Croatia_Zagreb_City_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Bor_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Branicevo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Jablanica_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Kolubara_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Macva_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Moravica_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Nisava_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Pcinja_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Pirot_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Podunavlje_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Pomoravlje_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Rasina_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Raska_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Sumadija_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Toplica_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Zajecar_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Zlatibor_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Belgrade_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_North_Backa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Central_Banat_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_North_Banat_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_South_Backa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_South_Banat_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Srem_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_West_Backa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Kosovo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Kosovo_Pomoravlje_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Kosovska_Mitrovica_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Pec_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_Prizren_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Blagoevgrad_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Burgas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Dobrich_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Gabrovo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Haskovo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Kardzhali_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Kyustendil_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Lovech_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Montana_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Pazardzhik_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Pernik_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Pleven_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Plovdiv_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Razgrad_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Ruse_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Shumen_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Silistra_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Sliven_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Smolyan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Sofia_City_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Stara_Zagora_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Targovishte_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Varna_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Veliko_Tarnovo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Vidin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Vratsa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_Yambol_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Albania_Berat_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Albania_Diber_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Albania_Durres_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Albania_Elbasan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Albania_Fier_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Albania_Gjirokaster_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Albania_Korce_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Albania_Lezhe_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Albania_Shkoder_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Albania_Vlore_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bosnia_Federation_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bosnia_Republika_Srpska_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bosnia_Brcko_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bosnia_Unsko_Sanski_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bosnia_Posavski_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bosnia_Tuzlanski_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bosnia_Zenicko_Dobojski_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bosnia_Bosansko_Podrinjski_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bosnia_Srednjobosanski_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bosnia_Hercegovacko_Neretvanski_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bosnia_Zapadnohercegovacki_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bosnia_Sarajevski_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bosnia_Kanton_10_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Slovakia_Bratislava_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Slovakia_Trnava_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Slovakia_Trencin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Slovakia_Nitra_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Slovakia_Zilina_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Slovakia_Banska_Bystrica_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Slovakia_Presov_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Slovakia_Kosice_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Estonia_Harju_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Estonia_Hiiu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Estonia_Ida_Viru_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Estonia_Jogeva_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Estonia_Jarva_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Estonia_Laane_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Estonia_Laane_Viru_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Estonia_Polva_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Estonia_Parnu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Estonia_Rapla_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Estonia_Saare_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Estonia_Tartu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Estonia_Valga_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Estonia_Viljandi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Estonia_Voru_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Lithuania_Alytus_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Lithuania_Kaunas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Lithuania_Klaipeda_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Lithuania_Marijampole_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Lithuania_Panevezys_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Lithuania_Siauliai_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Lithuania_Taurage_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Lithuania_Telsiai_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Lithuania_Utena_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Lithuania_Vilnius_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Trinidad_Arima_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Trinidad_Chaguanas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Trinidad_Mayaro_Guayaguayare_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Trinidad_Penal_Debe_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Trinidad_Point_Fortin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Trinidad_Port_of_Spain_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Trinidad_Princes_Town_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Trinidad_Rio_Claro_Mayaro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Trinidad_San_Fernando_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Trinidad_Sangre_Grande_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Trinidad_Siparia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Trinidad_Tunapuna_Piarco_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Acklins_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Berry_Islands_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Bimini_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Cat_Island_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Central_Abaco_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Central_Andros_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Central_Eleuthera_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_City_of_Freeport_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Crooked_Island_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_East_Grand_Bahama_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Exuma_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Grand_Cay_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Harbour_Island_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Hope_Town_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Inagua_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Long_Island_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Mangrove_Cay_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Mayaguana_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Moores_Island_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_North_Abaco_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_North_Andros_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_North_Eleuthera_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Ragged_Island_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Rum_Cay_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_San_Salvador_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_South_Abaco_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_South_Andros_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_South_Eleuthera_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_Spanish_Wells_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_West_Grand_Bahama_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Azua_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Baoruco_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Barahona_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Dajabon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Distrito_Nacional_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Duarte_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Elias_Pina_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_El_Seibo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Espaillat_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Hato_Mayor_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Hermanas_Mirabal_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Independencia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_La_Altagracia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_La_Romana_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_La_Vega_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Maria_Trinidad_Sanchez_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Monsenor_Nouel_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Monte_Cristi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Monte_Plata_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Pedernales_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Peravia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Puerto_Plata_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Samana_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Sanchez_Ramirez_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_San_Cristobal_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Santiago_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Santiago_Rodriguez_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Santo_Domingo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DominicanRepublic_Valverde_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Haiti_Artibonite_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Haiti_Centre_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Haiti_GrandAnse_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Haiti_Nippes_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Haiti_Nord_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Haiti_Nord_Est_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Haiti_Nord_Ouest_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Haiti_Ouest_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Haiti_Sud_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Haiti_Sud_Est_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Alba_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Arad_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Arges_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Bacau_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Bihor_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Bistrita_Nasaud_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Botosani_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Braila_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Brasov_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Bucuresti_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Buzau_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Calarasi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Caras_Severin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Cluj_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Constanta_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Covasna_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Dambovita_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Dolj_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Galati_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Giurgiu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Gorj_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Harghita_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Hunedoara_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Ialomita_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Iasi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Ilfov_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Maramures_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Mehedinti_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Mures_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Neamt_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Olt_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Prahova_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Salaj_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Satu_Mare_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Sibiu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Suceava_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Teleorman_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Timis_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Tulcea_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Valcea_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Vaslui_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Romania_Vrancea_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Bacs_Kiskun_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Baranya_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Bekes_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Borsod_Abauj_Zemplen_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Budapest_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Csongrad_Csanad_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Fejer_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Gyor_Moson_Sopron_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Hajdu_Bihar_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Heves_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Jasz_Nagykun_Szolnok_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Komarom_Esztergom_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Nograd_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Pest_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Somogy_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Szabolcs_Szatmar_Bereg_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Tolna_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Vas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Veszprem_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hungary_Zala_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_Auckland_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_Bay_of_Plenty_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_Canterbury_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_Chatham_Islands_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_Gisborne_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_Hawke's_Bay_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_Manawatu_Wanganui_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_Marlborough_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_Nelson_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_Northland_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_Otago_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_Southland_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_Taranaki_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_Tasman_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_Waikato_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_Wellington_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NZ_West_Coast_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Myanmar_Ayeyarwady_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Myanmar_Bago_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Myanmar_Chin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Myanmar_Kachin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Myanmar_Kayah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Myanmar_Kayin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Myanmar_Magway_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Myanmar_Mandalay_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Myanmar_Mon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Myanmar_Naypyidaw_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Myanmar_Rakhine_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Myanmar_Sagaing_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Myanmar_Shan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Myanmar_Tanintharyi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Israel_Haifa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Israel_Northern_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Israel_Southern_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "UAE_Ajman_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "UAE_Dubai_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "UAE_Fujairah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "UAE_Ras_Al_Khaimah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "UAE_Sharjah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "UAE_Umm_Al_Quwain_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_Al_Anbar_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_Al_Basrah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_Al_Muthanna_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_Al_Qadisiyah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_An_Najaf_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_Arbil_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_As_Sulaymaniyah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_Babil_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_Baghdad_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_Diyala_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_Karbala_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_Maysan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_Ninawa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_Salah_ad_Din_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_Wasit_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_Halabja_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jordan_Ajloun_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jordan_Amman_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jordan_Aqaba_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jordan_Balqa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jordan_Irbid_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jordan_Jerash_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jordan_Karak_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jordan_Ma'an_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jordan_Madaba_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jordan_Mafraq_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jordan_Tafilah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jordan_Zarqa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Alto_Paraguay_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Alto_Parana_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Amambay_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Asuncion_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Boqueron_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Caaguazu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Caazapa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Canindeyu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Central_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Concepcion_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Cordillera_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Guaira_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Itapua_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Misiones_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Neembucu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Paraguari_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_Presidente_Hayes_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_San_Pedro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Artigas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Canelones_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Cerro_Largo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Colonia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Durazno_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Flores_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Florida_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Lavalleja_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Maldonado_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Montevideo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Paysandu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Rio_Negro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Rivera_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Rocha_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Salto_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Soriano_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Tacuarembo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uruguay_Treinta_y_Tres_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Amazonas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Anzoategui_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Apure_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Aragua_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Barinas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Bolivar_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Carabobo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Cojedes_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Delta_Amacuro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Falcon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Guarico_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Lara_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Merida_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Monagas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Nueva_Esparta_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Portuguesa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Sucre_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Tachira_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Trujillo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Vargas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Yaracuy_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Venezuela_Zulia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Greece_Central_Macedonia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Greece_Crete_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Greece_Eastern_Macedonia_and_Thrace_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Greece_Epirus_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Greece_Ionian_Islands_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Greece_North_Aegean_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Greece_Peloponnese_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Greece_South_Aegean_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Greece_Thessaly_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SriLanka_Central_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SriLanka_Eastern_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SriLanka_North_Central_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SriLanka_Northern_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SriLanka_North_Western_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SriLanka_Sabaragamuwa_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SriLanka_Southern_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SriLanka_Uva_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SriLanka_Western_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Belgium_Brussels_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Belgium_Flanders_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Belgium_Wallonia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Malaysia_Johor_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Malaysia_Kedah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Malaysia_Kelantan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Malaysia_Malacca_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Malaysia_Negeri_Sembilan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Malaysia_Pahang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Malaysia_Penang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Malaysia_Perak_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Malaysia_Perlis_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Malaysia_Sabah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Malaysia_Sarawak_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Malaysia_Terengganu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Malaysia_Labuan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Malaysia_Putrajaya_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Saudi_Al_Bahah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Saudi_Al_Jawf_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Saudi_Al_Hudud_al_Shamaliyah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Saudi_Al_Qassim_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Saudi_Ha'il_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Saudi_Jazan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Saudi_Madinah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Saudi_Makkah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Saudi_Najran_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Saudi_Riyadh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Saudi_Ash_Sharqiyah_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Saudi_Asir_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Alexandria_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Aswan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Asyut_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Beheira_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Beni_Suef_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Cairo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Dakahlia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Damietta_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Faiyum_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Gharbia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Giza_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Ismailia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Kafr_el-Sheikh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Luxor_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Matruh_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Minya_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Monufia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_New_Valley_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_North_Sinai_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Port_Said_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Qalyubia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Qena_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Red_Sea_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Sharqia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Sohag_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_South_Sinai_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_Suez_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Austria_Burgenland_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Austria_Carinthia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Austria_Lower_Austria_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Austria_Upper_Austria_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Austria_Salzburg_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Austria_Styria_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Austria_Tyrol_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Austria_Vorarlberg_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Austria_Vienna_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Netherlands_Drenthe_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Netherlands_Flevoland_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Netherlands_Friesland_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Netherlands_Gelderland_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Netherlands_Groningen_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Netherlands_Limburg_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Netherlands_North_Brabant_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Netherlands_North_Holland_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Netherlands_Overijssel_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Netherlands_Utrecht_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Netherlands_Zeeland_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Netherlands_South_Holland_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Amnat_Charoen_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Ang_Thong_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Bangkok_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Bueng_Kan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Buriram_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Chachoengsao_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Chai_Nat_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Chaiyaphum_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Chanthaburi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Chonburi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Chumphon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Kalasin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Kamphaeng_Phet_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Kanchanaburi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Krabi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Lampang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Lamphun_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Loei_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Lopburi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Mae_Hong_Son_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Nakhon_Nayok_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Nakhon_Pathom_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Nakhon_Phanom_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Nakhon_Ratchasima_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Nakhon_Sawan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Nakhon_Si_Thammarat_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Nan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Narathiwat_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Nong_Bua_Lamphu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Nong_Khai_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Nonthaburi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Pathum_Thani_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Pattani_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Phang_Nga_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Phatthalung_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Phayao_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Phetchabun_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Phetchaburi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Phichit_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Phitsanulok_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Phra_Nakhon_Si_Ayutthaya_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Phrae_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Prachinburi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Prachuap_Khiri_Khan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Ranong_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Ratchaburi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Rayong_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Roi_Et_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Sa_Kaeo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Sakon_Nakhon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Samut_Prakan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Samut_Sakhon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Samut_Songkhram_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Saraburi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Satun_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Sing_Buri_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Sisaket_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Songkhla_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Suphan_Buri_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Surat_Thani_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Surin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Tak_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Trang_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Trat_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Ubon_Ratchasima_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Udon_Thani_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Uthai_Thani_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Uttaradit_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Yala_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_Yasothon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Abra_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Aklan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Albay_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Antique_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Apayao_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Aurora_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Basilan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Bataan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Batanes_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Batangas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Benguet_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Biliran_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Bohol_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Bulacan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Cagayan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Camarines_Norte_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Camarines_Sur_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Camiguin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Capiz_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Catanduanes_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Cavite_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Cebu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Compostela_Valley_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Cotabato_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Davao_del_Sur_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Davao_Occidental_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Davao_Oriental_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Dinagat_Islands_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Eastern_Samar_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Guimaras_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Ifugao_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Ilocos_Norte_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Ilocos_Sur_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Iloilo_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Isabela_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Kalinga_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_La_Union_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Laguna_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Lanao_del_Sur_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Leyte_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Maguindanao_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Marinduque_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Masbate_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Misamis_Occidental_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Misamis_Oriental_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Mountain_Province_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Negros_Occidental_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Negros_Oriental_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Northern_Samar_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Nueva_Ecija_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Nueva_Vizcaya_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Occidental_Mindoro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Oriental_Mindoro_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Palawan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Pampanga_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Pangasinan_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Quezon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Quirino_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Rizal_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Romblon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Samar_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Sarangani_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Siquijor_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Sorsogon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_South_Cotabato_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Southern_Leyte_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Sultan_Kudarat_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Sulu_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Surigao_del_Sur_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Tarlac_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Tawi-Tawi_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Zambales_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Zamboanga_del_Sur_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Zamboanga_Sibugay_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Metro_Manila_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_LU_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_UR_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_SZ_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_OW_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_NW_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_GL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_ZG_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_FR_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_SO_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_BS_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_BL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_SH_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_AR_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_AI_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_SG_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_GR_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_AG_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_TG_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_TI_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_VS_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_NE_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_GE_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Swiss_JU_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Greenland_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "FaroeIslands_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PuertoRico_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guam_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NewCaledonia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Reunion_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mayotte_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "HongKong_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "CaymanIslands_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Gibraltar_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "CookIslands_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Niue_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tokelau_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kyrgyzstan_Archive_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Philippines_Archive_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Belarus_Archive_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Slovakia_Archive_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tanzania_Archive_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SriLanka_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "PNG_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Syria_Assad_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Namibia_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kazakhstan_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Azerbaijan_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Barbados_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Belize_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Guyana_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ethiopia_NationalArchives_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_NationalArchives_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Thailand_NationalArchives_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "UAE_NationalArchives_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_NationalArchives_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahamas_NationalArchives_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Fiji_NationalArchives_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "OECD_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "AZGS_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "AlexanderTurnbull_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vatican_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cyprus_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "BeirutArabUni_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "AUB_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "At_the_Circulating_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "AZGS_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ACM_Digital_Library_author_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "African_Music_Library_artist_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Alexander_Turnbull_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "At_the_Circulating_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Boris_Yeltsin_Presidential_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "British_Library_system_number": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Capitular_Library_Verona": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Chinese_Library_Classification": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "EZB_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ACM_Digital_Library_citation_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ACM_Digital_Library_event_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Central_Library_of_Volos_authority_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Digital_Library_of_Armenian_Literature_author_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Digital_Valencian_Library_author_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Digital_Library_of_Mathematical_Functions_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Digital_Mechanism_and_Gear_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "National_Library_Board_Singapore_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "National_Library_of_Albania_edition_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "National_Library_of_Indonesia_Control_Headings_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "National_Library_of_Malaysia_OPAC_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "National_Library_of_Uruguay_authority_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "National_Library_of_Israel_ID_old": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "National_Library_of_Uruguay_book_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vatican_Library_ID_former_scheme": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Vatican_Library_OPAC": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Dimitri_and_Aliki_Perrotis_Central_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Frankfurt_University_Library_Digital_Collection_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Frick_Art_Research_Library_Artist_File_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Game_Font_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Hill_Museum_and_Manuscript_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "INEGI_Digital_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ia\u0219i_Central_University_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iowa_State_University_Library_Vocabularies_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jewish_Virtual_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jisc_Library_Hub_Authority": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jisc_Library_Hub_Works": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Keratsini_Drapetsona_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kramerius_of_Moravian_Library_UUID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kramerius_of_Regional_Library_in_Pardubice_UUID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "LTI_Korea_Library_writer_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Levadia_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Library_Parliament_Riding": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Library_of_Congress_Format_Description_Document_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Library_of_Congress_providers_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Media_Library_for_Dance_and_Theatre_person_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Michigan_State_University_Library_Comic_Art_Collection_Record_Number": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Municipal_Library_of_Trikala_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "National_Marine_Biological_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Open_Library_publisher_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Open_Library_subject_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Oroklini_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Panjab_Digital_Library_ID": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "OECD_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "WTO_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "IAEA_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ERIC_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "OSTI_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cambodia_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Laos_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Mongolia_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NLI_Israel_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NLG_Greece_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "BSB_Bavaria_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SBB_Berlin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "FUB_Berlin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "HUB_Berlin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "TUB_Berlin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SLQ_Queensland_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "BC_Catalonia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "CSL_California_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SLP_Pennsylvania_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SLO_Ohio_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "OSL_Oregon_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "LVA_Virginia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SLNC_NorthCarolina_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SLF_Florida_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NYSL_NewYork_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "TSLAC_Texas_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "RERO_Swiss_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Euskariana_Basque_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "WISC_Law_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "CSL_Colorado_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "MSU_Missouri_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "BVPB_Spain_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Galiciana_Galicia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "BVA_Andalucia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Sailor_Maryland_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Serbia_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bulgaria_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "MassState_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "MichiganState_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "WashingtonState_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "GeorgiaState_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "BC_Legislative_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Syria_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "KSA_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Egypt_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jordan_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Georgia_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Korea_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Taiwan_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Singapore_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Malaysia_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Indonesia_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ArizonaState_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NevadaState_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "TennesseeState_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "KentuckyState_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ConnecticutState_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NJ_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "AL_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "AK_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "KS_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "UT_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "OK_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ME_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "VT_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NM_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NH_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "RI_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "DE_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SC_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ND_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SD_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ID_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "MT_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "WY_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "LA_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "MS_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "WV_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "HI_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "LaRioja_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Sicilia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Asturias_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "CastillaLaMancha_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Canarias_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Piemonte_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Lazio_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Campania_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Iraq_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Palestine_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kuwait_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Qatar_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Moldova_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Albania_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Montenegro_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kosovo_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jamaica_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Malta_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "AR_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "IN_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "IA_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NE_State_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "YT_Territory_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NT_Territory_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NU_Territory_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ecuador_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Paraguay_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Myanmar_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Lombardia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Gallica_BnF_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Redalyc_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SciELO_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Dialnet_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "UN_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "UNESCO_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "WHO_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NYPL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "BHL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "CiNii_Books_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Jisc_Hub_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NSZL_Hungary_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NSK_Croatia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "BL_EThOS_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "WorldLII_Law_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Trinidad_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Aruba_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Nepal_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ethiopia_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Uganda_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Ghana_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ZLB_Berlin_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tokyo_Met_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "London_Met_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ArchivesACT_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ArchivesNZ_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ArchivesBosnia_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "BarbadosArchives_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "BelizeArchives_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "JamaicaArchives_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "LC_Work_Id": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Google_Books": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "OCLC_Record": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "HathiTrust": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Murcia_Regional_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Aragon_Regional_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Cyprus_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "VIAF_Title": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Wikidata_Title": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "NationalArchives_Global_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "InternetArchive_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ISSN_International_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "ArchiveGrid_OCLC_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "RISS_Korea_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Bahrain_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Turkmenistan_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Tajikistan_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Kyrgyzstan_NL_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "SanMarino_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Armenia_Archive_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Azerbaijan_Archive_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Haiti_Archive_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    },
    "Senegal_Archive_Library": {
        "status": "inactive",
        "reason": "No verified direct endpoint discovered"
    }
}
API_REGISTRY.update(INACTIVE_REGISTRY)

# Phase 1 Discovery: High-Probability Regional Hubs
DISCOVERED_ENDPOINTS = {
    "Russia_RSL_Main": {
        "z3950": "aleph.rsl.ru:9909/RSL01"
    },
    "Russia_RSL_Foreign": {
        "z3950": "aleph.rsl.ru:9909/RSL02"
    },
    "Russia_RSL_Maps": {
        "z3950": "aleph.rsl.ru:9909/RSL03"
    },
    "Russia_RSL_Music": {
        "z3950": "aleph.rsl.ru:9909/RSL04"
    },
    "Slovenia_NL_Library": {
        "sru": "https://plus.cobiss.net/cobiss/si/en/bib/search/sru"
    },
    "Serbia_NL_Library": {
        "sru": "https://plus.cobiss.net/cobiss/sr/en/bib/search/sru"
    },
    "Bulgaria_NL_Library": {
        "sru": "https://plus.cobiss.net/cobiss/bg/en/bib/search/sru"
    },
    "Albania_NL_Library": {
        "sru": "https://plus.cobiss.net/cobiss/al/en/bib/search/sru"
    },
    "Montenegro_NL_Library": {
        "sru": "https://plus.cobiss.net/cobiss/cg/en/bib/search/sru"
    },
    "SouthAfrica_NL_Library": {
        "z3950": "sun.alma.exlibrisgroup.com:1921/27US_INST"
    },
    "SouthAfrica_Wits_Library": {
        "z3950": "wits.alma.exlibrisgroup.com:1921/27WITS_INST"
    },
    "SouthAfrica_UCT_Library": {
        "z3950": "uct.alma.exlibrisgroup.com:1921/27UCT_INST"
    },
    "Mexico_NLC_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52BN_INST"
    },
    "Mexico_UNAM_Library": {
        "z3950": "na07.alma.exlibrisgroup.com:1921/52UNAM_INST"
    }
}
API_REGISTRY.update(DISCOVERED_ENDPOINTS)

