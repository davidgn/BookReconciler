from os import environ

use_endpoint_address = "http://127.0.0.1:5001"
if environ.get('OR_IP') is not None:
  use_endpoint_address = environ.get('OR_IP')


manifest = {
  "versions": ["0.2"],
  "defaultTypes": [
    {
      "id": "ROR_Org",
      "name": "Organization -- ROR"
    },
    {
      "id": "OpenAlex_Org",
    {
      "id": "ISNI_Person",
      "name": "Person -- ISNI"
    },
    {
      "id": "GND_Person",
    {
      "id": "BnF_Person",
      "name": "Person -- BnF"
    },
    {
      "id": "BNE_Person",
      "name": "Person -- BNE"
    },
    {
      "id": "AAT_Award",
      "name": "Award -- Getty AAT"
    },
    {
      "id": "DataCite_Award",
    {
      "id": "GeoNames_Location",
      "name": "Location -- GeoNames"
    },
    {
      "id": "TGN_Location",
    {
      "id": "Academy_Award",
      "name": "Award -- Academy Awards"
    },
    {
      "id": "NSF_Award",
      "name": "Award -- NSF (US National Science Foundation)"
    },
    {
      "id": "PEN_Org",
      "name": "Organization -- PEN Centres"
    },
    {
      "id": "Members_Org",
    {
      "id": "ACLS_Org",
      "name": "Organization -- ACLS Societies"
    },
    {
      "id": "IFLA_Org",
      "name": "Organization -- IFLA Members"
    },
    {
      "id": "ISC_Org",
      "name": "Organization -- ISC Members"
    },
    {
      "id": "Alberta_Place",
      "name": "Location -- Alberta Historic Places"
    },
    {
      "id": "OpenLibrary_Work",
    {
      "id": "SF_Awards_Person",
      "name": "Person -- Sci-Fi Awards Database"
    },
    {
      "id": "ACM_Awards_Person",
      "name": "Person -- ACM Awards"
    },
    {
      "id": "RSC_Fellow",
      "name": "Person -- Fellow Royal Society Canada"
    },
    {
      "id": "TWAS_Fellow",
      "name": "Person -- TWAS Fellow"
    },
    {
      "id": "EBU_Org",
      "name": "Organization -- EBU Members"
    },
    {
      "id": "EUNIC_Org",
    {
      "id": "ADB_Person",
      "name": "Person -- ADB Australia"
    },
    {
      "id": "ACM_Person",
      "name": "Person -- ACM Digital Library"
    },
    {
      "id": "BNMX_Person",
      "name": "Person -- BNMX Mexico"
    },
    {
      "id": "AIATSIS_Place",
    {
      "id": "HAL_Org",
      "name": "Organization -- French HAL (Research Units)"
    },
    {
      "id": "AwardsWinners_Person",
    {
      "id": "ALS_Org",
      "name": "Organization -- Alliance of Literary Societies"
    },
    {
      "id": "AAA_Org",
      "name": "Organization -- AAA UK Literary Agents"
    },
    {
      "id": "JTI_Org",
      "name": "Organization -- JTI Japan Registry"
    },
    {
      "id": "AEDA_Place",
    {
      "id": "MedalHonor_Person",
      "name": "Person -- Medal of Honor Recipients"
    },
    {
      "id": "AINM_Place",
      "name": "Location -- Irish Place Names (AINM)"
    },
    {
      "id": "ACER_Org",
      "name": "Organization -- ACER Code"
    },
    {
      "id": "ACUM_Org",
    {
      "id": "Euro08_Person",
      "name": "Person -- Euro08 Biography"
    },
    {
      "id": "HebrewTheatre_Person",
      "name": "Person -- Hebrew Theatre Guide"
    },
    {
      "id": "AMPAS_Item",
      "name": "Work -- AMPAS Film Collection"
    },
    {
      "id": "ANPI_Place",
    {
      "id": "AILA_Org",
      "name": "Organization -- Indigenous Publishers (AILA)"
    },
    {
      "id": "Altexto_Org",
      "name": "Organization -- Mexican Univ Presses (Altexto)"
    },
    {
      "id": "Sloan_Prize",
      "name": "Award -- Sloan Foundation Grants"
    },
    {
      "id": "AMPAS_Person_2",
    {
      "id": "AJOL_Org",
      "name": "Organization -- African Journals (AJOL)"
    },
    {
      "id": "AJUP_Org",
      "name": "Organization -- Japanese Univ Presses (AJUP)"
    },
    {
      "id": "AtomicHeritage_Org",
      "name": "Organization -- Atomic Heritage Foundation"
    },
    {
      "id": "Antarctic_Place",
      "name": "Location -- Antarctic Gazetteer"
    },
    {
      "id": "BaneNOR_Place",
    {
      "id": "ABEU_Org",
      "name": "Organization -- Brazilian Univ Presses (ABEU)"
    },
    {
      "id": "AfricanMinds_Org",
      "name": "Organization -- African Minds Mapping"
    },
    {
      "id": "AlbinMichel_Person",
      "name": "Person -- Albin Michel Authors"
    },
    {
      "id": "GrantNav_Prize",
    {
      "id": "AFNIL_Org",
      "name": "Organization -- French Publishers (AFNIL)"
    },
    {
      "id": "ASEUC_Org",
      "name": "Organization -- Colombian Univ Presses (ASEUC)"
    },
    {
      "id": "AlternativaTeatral_Place",
      "name": "Location -- Alternativa Teatral"
    },
    {
      "id": "BHF_Person",
      "name": "Person -- BHF Authors"
    },
    {
      "id": "REUN_Org",
    {
      "id": "AAGM_Org",
      "name": "Organization -- Munich AAGM"
    },
    {
      "id": "ReliefWeb_Org",
      "name": "Organization -- ReliefWeb UN/NGOs"
    },
    {
      "id": "AmericanHeritage_Place",
      "name": "Location -- American Heritage"
    },
      "name": "Organization -- Argentine Univ Presses (REUN)"
    },
      "name": "Award -- GrantNav (360Giving)"
    },
      "name": "Location -- Norway Bane NOR"
    },
      "name": "Person -- AMPAS Academy Awards"
    },
      "name": "Location -- Italian ANPI Places"
    },
      "name": "Organization -- ACUM Creator/Publisher"
    },
      "name": "Location -- AEDA Subject/Place"
    },
    {
      "id": "AAMC_Org",
      "name": "Organization -- AAMC Art Museums"
    },
    {
      "id": "AALA_Org",
      "name": "Organization -- AALA Literary Agents"
    },
    {
      "id": "BabelNet_Entity",
      "name": "Concept -- BabelNet"
    },
    {
      "id": "CODEN_Work",
      "name": "Work -- CODEN (Science Journals)"
    },
      "name": "Person -- Awards & Winners"
    },
      "name": "Location -- AIATSIS Australia"
    },
      "name": "Organization -- EUNIC Members"
    },
    {
      "id": "EuropePMC_Work",
      "name": "Work -- Europe PMC"
    },
    {
      "id": "OpenCitations_Work",
      "name": "Work -- OpenCitations"
    },
      "name": "Work -- Open Library Search"
    },
      "name": "Organization -- Member/Affiliate Search"
    },
    {
      "id": "ThreeSixtyGiving_Org",
      "name": "Organization -- 360Giving (UK Charity)"
    },
    {
      "id": "Grammy_Award",
      "name": "Award -- Grammy Awards"
    },
    {
      "id": "Sirene_Org",
      "name": "Organization -- French SIRENE"
    },
    {
      "id": "DOAJ_Journal",
      "name": "Journal -- DOAJ"
    },
    {
      "id": "IdRef_Person",
      "name": "Person -- IdRef"
    },
    {
      "id": "SBN_Work",
    {
      "id": "BVMC_Person",
      "name": "Person -- BVMC"
    },
    {
      "id": "GCD_Publisher",
      "name": "Publisher -- Grand Comics Database"
    },
    {
      "id": "SIC_Mexico",
      "name": "Organization -- SIC Mexico"
    },
    {
      "id": "GRID_Historical",
    {
      "id": "ProPublica_Org",
      "name": "Organization -- ProPublica (US Foundation)"
    },
      "name": "Organization -- GRID Historical"
    },
    {
      "id": "NLA_Person",
      "name": "Person -- NLA/Trove"
    },
      "name": "Work -- Italian SBN"
    },
      "name": "Location -- Getty TGN"
    },
      "name": "Award -- DataCite"
    },
      "name": "Person -- GND"
    },
      "name": "Organization -- OpenAlex"
    },
    {
      "id": "LC_Work_Id",
      "name": "Title -- id.loc.gov"
    },

    {
      "id": "Google_Books",
      "name": "Title -- Google Books"
    },  

    {
      "id": "OCLC_Record",
      "name": "Title -- Worldcat"
    },
    {
      "id": "HathiTrust",
      "name": "Title -- HathiTrust"
    },
    {
      "id": "VIAF_Title",
      "name": "Title -- VIAF Work"
    },
    {
      "id": "Wikidata_Title",
      "name": "Title -- Wikidata Work"
    }, 
    {
      "id": "OpenLibrary_Title",
      "name": "Title -- Open Library Work"
    },    
    {
      "id": "VIAF_Personal",
      "name": "Name -- VIAF Personal"
    }
  ],
  "identifierSpace": "/doc/#identifierSpace",
  "schemaSpace": "/doc/#schemaSpace",

  "name": "BookReconciler Service",
  "batchSize": 1,
  "preview": {
    "height": 200,
    "url": use_endpoint_address + "/api/v1/preview?id={{id}}",
    "width": 500
  },

  "view": {
    "url": use_endpoint_address + "/api/v1/redirect?id={{id}}"
  },

  "suggest": {
    "property": {
      "service_url": use_endpoint_address + "/api/v1/reconcile",
      "service_path": "/suggest/property"
    },

  },
  "extend": {
    "propose_properties": {
      "service_url": use_endpoint_address + "/api/v1/reconcile",
      "service_path": "/extend_suggest"
    }
  }

}