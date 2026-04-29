# Technical Handoff: Lane-Based Identifier Integration

## 1. Mission Objective

Systematically bridge the 6,000+ implemented sources in the Identifier Harvester
Pipeline into the OpenRefine Reconciliation Service. Integration must strictly
prioritize sources that power the Five Operational Lanes:

- Winner Lane: Award winners, honorees, and prestigious fellowship recipients.
- Eponym Lane: Biographical dictionaries and namesake entities.
- Org Lane: University presses, foundations, charities, and scholarly societies.
- Prize Lane: Award databases, grant lists, and medal registries.
- Place Lane: National gazetteers and regional place-name authorities.

## 2. Workspace Architecture

- Pipeline Source: `/mnt/data7/home/davidgn/active_repos/identifier-harvesting-pipeline`
  - Registry (Source of Truth): `data/reference/harvest_source_registry.json`
  - Source Code: `src/pipeline/sources/`
- OpenRefine Service: `/mnt/data7/home/davidgn/active_repos/openrefine-reconciliation-service`
  - Strategies: `lib/strategies_*.py`
  - Manifest (Registration): `lib/schemas/manifest.py`
  - Routing (Logic): `app.py`

## 3. The Strict-Filter Audit

To select a batch, run a Python filter against the registry. Do not process
sources sequentially. Only accept sources where:

1. `implemented: true`
2. The source is not already in `manifest.py`.
3. The notes or source name contains lane keywords, e.g. foundation, prize,
   fellow, gazetteer.
4. Exclusion rule: avoid low-value niche databases like bird IDs, sports stats,
   or commercial-only catalogs.

## 4. The Implementation Lifecycle

### Step A: Verification (Smoke Test)

Before writing any OpenRefine code, verify the endpoint is live and responsive
using a shim script.

- `JsonApiSource`: Test with `requests.get(url, params={"q": name})`.
- `GenericSparqlSource`: Test via the Wikidata SPARQL proxy.
- WP-JSON: Test if the site is a WordPress API (`/wp-json/wp/v2/members`).

### Step B: Strategy Implementation (OpenRefine)

Create a new module in `lib/strategies_[source_name].py`.

- Template: Follow the pattern in `lib/strategies_helpers.py` using
  `_build_recon_dict`.
- Reuse:
  - If it is a WordPress site, use the generic `process_wp_json_query`.
  - If it is a Wikidata-mapped ID, use `process_sparql_generic_query`.
  - Otherwise, write a custom `process_[name]_query` function.

### Step C: Registration

1. Update `manifest.py`: add the unique ID and human-readable name to the
   `defaultTypes` list.
2. Update `app.py`:
   - Import the new strategy at the top.
   - Add an `if query[queryId]["type"] == "YOUR_ID":` block to the reconciliation
     route.

### Step D: Verification & Sync

1. Verify the new type appears in OpenRefine.
2. Use explicit path staging for the files changed by the batch. Do not use
   `git add .` in dirty or multi-project working trees.
3. Commit and push both repositories when both sides of the integration are
   intentionally updated.

## 5. Technical Edge Cases

- SSL Issues: For national authority servers, e.g. Spanish BNE, use
  `verify=False` in the request.
- JSON Formats: Library of Congress (LCNAF) and OpenLibrary use non-standard
  JSON arrays; use the `strategies_lcnaf.py` parsing logic as a reference.
- Dynamic Loading: The Pipeline's `SourceRegistry` loads thousands of sources
  dynamically from the JSON. If a source is missing in your test, manually
  register it in your smoke test using the appropriate protocol class
  (`JsonApiSource`, `SRUSource`, etc.).
