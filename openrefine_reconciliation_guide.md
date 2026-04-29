# OpenRefine Reconciliation Implementation Guide

This document outlines how to wire the high-priority bibliographic and organizational sources into **OpenRefine** for use in the GSBPDb / ELEM identifier harvesting pipeline.

## 🚀 Pro-Tip: The Two Methods of Reconciliation
In OpenRefine, reconciliation is achieved via two distinct technical paths depending on the endpoint type. This manifest explicitly labels each service's preferred method in the `openrefine_method` field.

1.  **Standard Reconciliation (Native):** These endpoints use the standard Reconciliation API. Add them via: **Reconcile -> Start Reconciling -> Add Standard Service**.
2.  **RDF Extension (SPARQL):** These endpoints are raw SPARQL triplestores. They **must** be used with the [OpenRefine-RDF Extension](https://github.com/OpenRefine/OpenRefine-RDF-Extension). Add them via: **RDF -> Add reconciliation service -> Based on SPARQL endpoint**.

---

## 1. Global Hubs & Aggregators

### **Wikidata**
**URL:** `https://wikidata.reconci.link/en/api`
*   **Method:** Standard Reconciliation (Native)
*   **Notes:** Primary hub for cross-dataset reconciliation.

### **VIAF (Virtual International Authority File)**
**URL:** `https://refine.codefork.com/reconcile/viaf`
*   **Method:** Standard Reconciliation (Native)
*   **Property Mapping:** Map to Wikidata Property **P214**.

### **ROR (Research Organization Registry)**
**URL:** `https://reconcile.ror.org/reconcile`
*   **Method:** Standard Reconciliation (Native)
*   **Property Mapping:** Map to Wikidata Property **P6782**.

### **Open Library (Internet Archive)**
**URL:** `https://refine.codefork.com/reconcile/openlibrary`
*   **Method:** Standard Reconciliation (Native)
*   **Property Mapping:** Map to Wikidata Property **P648**.

---

## 2. National Library SPARQL Endpoints (Require RDF Extension)

| Source | SPARQL Endpoint URL | WD Property |
| :--- | :--- | :--- |
| **BnF France** | `https://data.bnf.fr/sparql` | P268 |
| **BNE Spain** | `https://datos.bne.es/sparql` | P950 |
| **DNB Germany** | `https://sparql.dnb.de` | P227 |
| **NL Hungary (OSZK)** | `http://nektar.oszk.hu/sparql` | P1184 |
| **LC Chile (BCN)** | `http://datos.bcn.cl/sparql` | P935 |
| **NL Korea (NLK)** | `http://lod.nl.go.kr/sparql` | P1015 |
| **Taiwan (NCL)** | `https://ld.ncl.edu.tw/fuseki/lod/query` | P12822 |
| **Shanghai Library** | `https://data.library.sh.cn/sparql` | P12354 |
| **Czech NL** | `https://data.gov.cz/sparql` | P691 |
| **Swissbib** | `https://data.swissbib.ch/sparql` | P5604 |

---

## 3. Specialized Authority Sources

### **ULAN (Getty Artist Names)**
**URL:** `https://vocab.getty.edu/sparql.json`
*   **Method:** RDF Extension (SPARQL)
*   **Property Mapping:** Map to Wikidata Property **P245**.

### **GND (lobid.org)**
**URL:** `https://lobid.org/gnd/reconcile`
*   **Method:** Standard Reconciliation (Native)
*   **Property Mapping:** Map to Wikidata Property **P227**.

### **OpenCorporates**
**URL:** `https://opencorporates.com/reconcile`
*   **Method:** Standard Reconciliation (Native)
*   **Property Mapping:** Map to Wikidata Property **P1320**.

---

## 4. Workflow Strategy
1.  **Reconcile** against Wikidata first to see existing coverage.
2.  **Add Column from Reconciled Values** to fetch the source-specific IDs (GND ID, BnF ARK, etc.).
3.  **Cross-Reconcile** using the specific endpoints (e.g., Lobid for GND) to fill gaps where Wikidata is sparse.
4.  **Extract Identifiers** using GREL: `cell.recon.match.id`.
