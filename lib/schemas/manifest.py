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
    {
      "id": "NDL_Person",
      "name": "Person -- NDL Japan"
    },
    {
      "id": "OpenCorporates_Org",
      "name": "Organization -- OpenCorporates"
    },
    {
      "id": "LCNAF_Person",
    {
      "id": "NTA_Person",
      "name": "Person -- NTA Netherlands"
    },
    {
      "id": "OpenLibrary_Author",
      "name": "Person -- Open Library Authors"
    },
      "name": "Person -- LCNAF (Library of Congress)"
    },
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
      "id": "Canada_Historic_Place",
      "name": "Location -- Canada Historic Places"
    },
    {
      "id": "ASCE_Landmark_Place",
      "name": "Location -- ASCE Civil Engineering Landmarks"
    },
    {
      "id": "ADB_Publication_Work",
      "name": "Work -- ADB Publications"
    },
    {
      "id": "AAGM_Artwork_Work",
    {
      "id": "Euro08_Winner",
      "name": "Winner -- Russian 08euro"
    },
    {
      "id": "TwoGIS_Place",
      "name": "Location -- 2GIS Gazetteer"
    },
    {
      "id": "Academy_Awards_Film",
      "name": "Award -- Academy Awards Film"
    },
    {
      "id": "AwardsWinners_Artist",
      "name": "Winner -- Awards & Winners Artist"
    },
      "name": "Work -- Munich AAGM Artwork"
    },
    {
      "id": "ASCAP_Work",
      "name": "Work -- ASCAP Musical Works"
    },
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
      "id": "SevenDays_Person",
      "name": "Person -- Russian 7 Days"
    },
    {
      "id": "AAA_UK_Org",
      "name": "Organization -- UK Literary Agents"
    },
    {
      "id": "ADAL_Spain_Org",
      "name": "Organization -- Spanish Literary Agents"
    },
    {
      "id": "Bavarian_Monument_Place",
      "name": "Location -- Bavarian Monuments"
    },
    {
      "id": "Australian_Heritage_Place_2",
      "name": "Location -- Australian Heritage"
    },
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
      "id": "ALCA_Person",
      "name": "Person -- Catalan Authors (ALCA)"
    },
    {
      "id": "ALCUIN_Person",
      "name": "Person -- Alcuin Philosophers"
    },
    {
      "id": "AMNH_Org",
      "name": "Organization -- AMNH Museum"
    },
    {
      "id": "NYC_Art_Place",
      "name": "Location -- NYC Public Art"
    },
    {
      "id": "ACNC_Org",
    {
      "id": "Georgia_Emigrants_Person",
      "name": "Person -- Georgia Emigrants Bio"
    },
    {
      "id": "CESAR_Person",
      "name": "Person -- French Theatre (CESAR)"
    },
    {
      "id": "ARC_Grant",
      "name": "Award -- Australian Research Council"
    },
    {
      "id": "OpenDOAR_Org",
    {
      "id": "RS_Memoirs_Person",
      "name": "Person -- Royal Society Memoirs"
    },
    {
      "id": "Rome_Fellow_Person",
      "name": "Person -- French Academy in Rome Fellow"
    },
    {
      "id": "Royal_Society_Person",
      "name": "Person -- Royal Society People"
    },
    {
      "id": "SAM_Gov_Org",
      "name": "Organization -- US Gov Awardees (SAM.gov)"
    },
    {
      "id": "HAL_TEL_Work",
    {
      "id": "ACM_Author_Id",
      "name": "Person -- ACM Digital Library (Author)"
    },
    {
      "id": "JapanNTA_Org",
      "name": "Organization -- Japan Corporate Number (NTA)"
    },
    {
      "id": "SherpaRomeo_Work",
      "name": "Journal -- Sherpa/Romeo Policies"
    },
    {
      "id": "IPEDS_Org",
    {
      "id": "Nobel_Person",
      "name": "Person -- Nobel Prize Laureates"
    },
    {
      "id": "SECCIK_Org",
      "name": "Organization -- Mexican Culture (SECCIK)"
    },
    {
      "id": "JTI_Org_2",
      "name": "Organization -- Japan Tech (JTI)"
    },
    {
      "id": "EU_Transparency_Org",
      "name": "Organization -- EU Transparency Register"
    },
    {
      "id": "ERIHPLUS_Journal",
      "name": "Journal -- ERIH PLUS Humanities"
    },
    {
      "id": "Crossref_Funder_Org",
      "name": "Organization -- Crossref Funder Registry"
    },
      "name": "Organization -- US Higher Ed (IPEDS)"
    },
      "name": "Work -- French Theses (HAL TEL)"
    },
      "name": "Organization -- OpenDOAR Repositories"
    },
      "name": "Organization -- Australian Charities (ACNC)"
    },
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
    {
      "id": "ISIL_Org",
      "name": "Organization -- ISIL Library Registry"
    },
    {
      "id": "ODUCAL_Org",
      "name": "Organization -- Catholic Univ (ODUCAL)"
    },
    {
      "id": "AFAS_Person",
      "name": "Person -- AFAS Science Alumni"
    },
    {
      "id": "Ads_Work",
    {
      "id": "Antarctic_Place_2",
      "name": "Location -- Australian Antarctic"
    },
    {
      "id": "IFACCA_Org",
      "name": "Organization -- Arts Councils (IFACCA)"
    },
    {
      "id": "AGORHA_Person",
      "name": "Person -- French Art History (AGORHA)"
    },
    {
      "id": "ACE_Org",
      "name": "Organization -- ASCAP Publishers (ACE)"
    },
    {
      "id": "Bombardirov_Person",
      "name": "Person -- Russian Military Honorees"
    },
      "name": "Work -- Italian Theatre (Ads)"
    },
    {
      "id": "ADB_Org_Auth",
      "name": "Organization -- ADB Australia (Authority)"
    },
    {
      "id": "AEF_Org",
      "name": "Organization -- European Foundations (AEF)"
    },
    {
      "id": "ALPSP_Org",
      "name": "Organization -- Scholarly Publishers (ALPSP)"
    },
    {
      "id": "ASALE_Org",
    {
      "id": "re3data_Org",
      "name": "Organization -- re3data Repositories"
    },
    {
      "id": "RussianDict_Person",
      "name": "Person -- 18th Cent Russian Dictionary"
    },
    {
      "id": "ChineseBio_Person",
      "name": "Person -- 20th Cent Chinese Bio"
    },
    {
      "id": "QueerScientists_Person",
      "name": "Person -- 500 Queer Scientists"
    },
      "name": "Organization -- Spanish Language Academies (ASALE)"
    },
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