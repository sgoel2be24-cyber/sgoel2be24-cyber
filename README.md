<div align="center">

# Shikhar Goel

**Software Engineer** · distributed systems, static analysis, native apps — and the AI layer on top

<sub>Open to software engineering internships · Summer 2027</sub>

<a href="https://portfolio-website-zeta-dun-27.vercel.app/">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=21&duration=3200&pause=900&color=38BDAF&center=true&vCenter=true&width=700&lines=Crash-safe+by+construction%3A+WAL%2C+fencing+tokens%2C+F_FULLFSYNC.;627+regexes+benchmarked.+0+false+positives%2C+0+misses.;Merged+into+NumPy%2C+Apache+Magpie%2C+Google+ADK+and+Cognee.;Deterministic+code+decides.+Models+only+observe." alt="Typing SVG" />
</a>

<br/>

<a href="https://portfolio-website-zeta-dun-27.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white" /></a>
<a href="https://www.linkedin.com/in/shikhar-goel01/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<a href="mailto:shikhardeepgoel@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" /></a>
<img src="https://komarev.com/ghpvc/?username=sgoel2be24-cyber&style=for-the-badge&color=38BDAF&label=PROFILE+VIEWS" />

</div>

---

### `whoami`

```go
type Shikhar struct {
    Role     string   // "Software Engineer"
    Studying string   // "B.E. Computer Engineering @ Thapar Institute (2024–2028)"
    Depth    []string // {"distributed systems", "static analysis", "native macOS", "AI agents"}
    Thesis   string   // "A claim isn't real until something measures it."
}
```

I write systems that hold up when things go wrong — crash-safe storage, fault-tolerant dispatch,
analyzers that prove an exploit rather than flagging a smell. The AI work sits on the same
foundation: models emit typed observations, deterministic code makes the decisions, and every
claim ships with the evidence that produced it.

---

## Systems &amp; software

| Project | What it is |
|---|---|
| **[conveyor-job-queue](https://github.com/sgoel2be24-cyber/conveyor-job-queue)**<br/>`Go` `Connect RPC` `Protobuf` `Prometheus` | Durable distributed job queue built around crash-safety: CRC32C-checksummed, length-prefixed WAL with torn-write detection and `F_FULLFSYNC` flushing; fencing tokens against zombie-worker acks; lease-based streaming dispatch with bounded concurrency and dead-lettering. **50 trials of `kill -9` with zero job loss**, 32,232 submissions/sec group-commit throughput, 7.7 ms recovery for 100K records. |
| **[redoscope](https://github.com/sgoel2be24-cyber/redoscope)**<br/>`TypeScript` `Node ≥22.18` `zero deps` | ReDoS static analysis that verifies its own findings. Parses the full ECMAScript regex grammar, compiles to an NFA modelling real backtracking, and detects exponential and polynomial paths via product automata — then generates witness attack strings and times them in killable child processes. Benchmarked on **627 real-world regexes**: a star-height heuristic gave 10 false positives and missed 14 real vulnerabilities; this pipeline hit **0 false positives and 0 misses**. |
| **LiveEnv** — *private repo*<br/>`Next.js` `SQLite` `WebSocket` `IndexedDB` `MapLibre` | Local-first, decay-based geospatial social platform across four surfaces. Geohash-partitioned SQLite serving a hot TTL-swept table alongside durable transactional tables; paid placements settled through an append-only double-entry ledger so money never moves without minting the pin; IndexedDB offline outbox with idempotent client-ID-keyed sync. |
| **AgentBar** — *private repo*<br/>`Swift` `Xcode` `Keychain` `SQLite` | Native macOS menu bar app unifying usage tracking across six AI coding agents into one stacked bar with per-service metrics. Secure credential handling through macOS Keychain across heterogeneous sources; shipped as a signed `.dmg` under MIT. |

---

## AI engineering

| Project | What it is |
|---|---|
| **[modelgauntlet](https://github.com/sgoel2be24-cyber/modelgauntlet)**<br/>`Next.js` `Zod` `Ajv` `Vitest` | Pre-release testing platform that stress-tests structured AI tasks across open-source models and returns a deterministic **SHIP / FIX / BLOCK** verdict. One rule enforced end to end: AI proposes, deterministic TypeScript code decides — AI never grades AI. 23 automated tests across parsing, assertion, schema-validation and verdict boundaries. |
| **[multimodal-evidence-review](https://github.com/sgoel2be24-cyber/multimodal-evidence-review-orchestrate)**<br/>`Python` `Gemini 2.5 Flash` | Multimodal damage-claim adjudication pipeline — model output validated and repaired against a strict 14-column schema with tightly constrained enums. Semantic consistency rules lifted **claim-status accuracy from 70% to 85%** with zero additional model calls. SHA-256 content-addressed caching, resumable batch pipeline, graceful stop on quota errors. **Ranked #37 of 1,773.** |
| **[kaamtwin](https://github.com/sgoel2be24-cyber/kaamtwin)**<br/>`Next.js` `TypeScript` | Causal digital-twin simulator that reorders manufacturing order queues by deadline priority — 62 → 59 late deliveries in the demonstrated scenario, verified by **15 anti-hardcoding causal tests** (reversed-input, capacity, duration, immutable-hash) that rule out a hardcoded result. 67 automated tests at 88%+ coverage, 8/8 Chromium e2e, zero critical a11y findings, hardened CSP. |
| **[zero-token-router](https://github.com/sgoel2be24-cyber/zero-token-router)**<br/>`Python` | Hybrid router resolving deterministic tasks locally and escalating only genuinely hard work to LLMs. Passed **19/19 simulated evaluations** shipped as a public Linux/amd64 image under 4 GB RAM / 2 vCPU. |

---

## Open source

Patches landed in projects I actually use, plus work in flight. Counts below are generated daily from GitHub search, not typed:

| Project | PR | What it did |
|---|---|---|
| **[numpy/numpy](https://github.com/numpy/numpy)** | [#32386](https://github.com/numpy/numpy/pull/32386) ✅ **merged** | `BUG: close duplicated file descriptor if fdopen fails` — C-level fix closing a descriptor leak in NumPy's error path, with regression tests handling WASM/musl. All 91 required CI checks passed. |
| **[apache/magpie](https://github.com/apache/magpie)** | [#1089](https://github.com/apache/magpie/pull/1089) ✅ **merged** | `fix(license-compliance-audit): handle large blobs and canonical SPDX` — files over ~1 MiB return without inline content, so the audit silently mis-flagged them as non-compliant. Fetches via raw-media API, separates *uninspected* from *violating*, enforces canonical `Apache-2.0`. Closed issue #944. |
| **[google/adk-python](https://github.com/google/adk-python)** | [#6419](https://github.com/google/adk-python/pull/6419) ✅ **landed** | `fix: handle Windows paths in adk eval` — the eval-case parser read the colon in `C:\` as a case selector. Google lands patches through Copybara, so the PR shows closed while the change is on `main` as [`6f6106f`](https://github.com/google/adk-python/commit/6f6106f), authored by me and shipped in `v2.6.0` and `v2.8.0`. |
| **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | [#4126](https://github.com/topoteretes/cognee/pull/4126) ✅ **merged** | `fix(cli): reject dry runs in API dispatch mode` — `--dry-run` was silently ignored when `--api-url` was set, executing real remote operations. |
| **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | [#4161](https://github.com/topoteretes/cognee/pull/4161) 🔄 open | `fix(api): scope configuration lookup to authenticated owner` — any authenticated user could read any config by UUID. |
| **[corsairdev/corsair](https://github.com/corsairdev/corsair)** | [#1200](https://github.com/corsairdev/corsair/pull/1200) 🔄 open | `feat(pinecone): production-grade integration` — 48 operations across four API surfaces, typed Zod schemas, dynamic host routing. |
| **[google/adk-python](https://github.com/google/adk-python)** | [#6705](https://github.com/google/adk-python/pull/6705) 🔄 open | `test: pin EvalCase session state injection` — regression test locking state injection into instruction templates. |

---

## What I chose not to do

Output is easy to list; restraint isn't. Three decisions I'd want a reviewer to see:

| Decision | Reasoning |
|---|---|
| **Stood down on [cognee#4131](https://github.com/topoteretes/cognee/issues/4131)** | Investigated the defect, then found four active PRs already covering the concrete fix. A duplicate PR spends a maintainer's review budget without adding anything, so I closed my branch instead of opening it. |
| **Called the Facillima rebuild** | I'd shipped the platform end to end in Next.js when the company asked for a WordPress version to match their main site. I didn't have the runway to do that properly, and said so rather than hand over something half-migrated. |
| **Kept the review note on [corsair#1200](https://github.com/corsairdev/corsair/pull/1200)** | Review found input schemas weren't validated at runtime before request construction. It's a real gap in my patch — catching it pre-merge is what review is for, and it stays open until it's fixed. |

The same instinct shows up in the code: Conveyor's invariants were verified by
mutation — reintroduce the bug, confirm a test fails — because a test nobody has
seen fail isn't evidence of anything.

---

## Experience

**AI Intern — Bharat Electronics Limited, Bengaluru** · Jul – Aug 2026
Backend API integrations in FastAPI, a React/Vite analytics dashboard turning application data into
usage, latency and performance views, and improvements to the project's RAG pipeline.

**Remote AI Intern — Facillima** · May – Jun 2026
Shipped an AI-native EdTech platform end to end in Next.js/TypeScript — technical SEO, structured
data, analytics instrumentation, third-party LMS integration — and led evaluation of the company's
LLM observability stack.

---

## Toolkit

**Languages**

<p align="center">
<img src="https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white" />
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
<img src="https://img.shields.io/badge/Swift-F05138?style=for-the-badge&logo=swift&logoColor=white" />
<img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" />
<img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" />
<img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
</p>

**AI &amp; agents** — *where most of my work sits*

<p align="center">
<img src="https://img.shields.io/badge/Model_Context_Protocol-D97757?style=for-the-badge&logo=anthropic&logoColor=white" />
<img src="https://img.shields.io/badge/Google_ADK-4285F4?style=for-the-badge&logo=google&logoColor=white" />
<img src="https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" />
<img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white" />
<img src="https://img.shields.io/badge/Cognee-1B1F23?style=for-the-badge" />
<img src="https://img.shields.io/badge/Featherless-5B4B8A?style=for-the-badge" />
</p>

**Concepts:** RAG · autonomous agents · multi-agent orchestration · deterministic verification · model evaluation &amp; benchmarking · release gating · prompt engineering · LLM observability

**Tools:** LangSmith · Braintrust · Zod · Ajv · Vitest · agent skills &amp; persistent memory

**Machine learning &amp; data**

<p align="center">
<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
<img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white" />
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" />
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
<img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge" />
</p>

**Concepts:** ensemble methods · CNNs &amp; Grad-CAM explainability · feature engineering · model calibration · ROC-AUC / permutation importance

**Systems &amp; infrastructure**

<p align="center">
<img src="https://img.shields.io/badge/Connect_RPC-244C5A?style=for-the-badge" />
<img src="https://img.shields.io/badge/Protocol_Buffers-4285F4?style=for-the-badge" />
<img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" />
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" />
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" />
<img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" />
<img src="https://img.shields.io/badge/Xcode-147EFB?style=for-the-badge&logo=xcode&logoColor=white" />
</p>

**Concepts:** write-ahead logging · crash recovery &amp; durability · fencing tokens · lease-based dispatch · group commit · static analysis / automata · local-first &amp; offline sync

**Backend, frontend &amp; stores**

<p align="center">
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" />
<img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
<img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" />
<img src="https://img.shields.io/badge/Node.js-5FA04E?style=for-the-badge&logo=nodedotjs&logoColor=white" />
<img src="https://img.shields.io/badge/Express-000000?style=for-the-badge&logo=express&logoColor=white" />
</p>

<p align="center">
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
<img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" />
<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
<img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
<img src="https://img.shields.io/badge/IndexedDB-4B5563?style=for-the-badge" />
</p>

**Core CS:** data structures &amp; algorithms · DBMS · object-oriented programming · distributed systems · software testing (pytest, Vitest, Ruff)

---

## Track record

<div align="center">

[![merged upstream](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fsgoel2be24-cyber%2Fsgoel2be24-cyber%2Fbadges%2Fpr-merged.json&style=for-the-badge)](https://github.com/sgoel2be24-cyber/sgoel2be24-cyber/actions/workflows/pr-counts.yml)
[![in review](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fsgoel2be24-cyber%2Fsgoel2be24-cyber%2Fbadges%2Fpr-open.json&style=for-the-badge)](https://github.com/sgoel2be24-cyber/sgoel2be24-cyber/actions/workflows/pr-counts.yml)
![Orchestrate](https://img.shields.io/badge/HackerRank_Orchestrate-%2337_of_1,773-38BDAF?style=for-the-badge)

</div>

Code landed in **NumPy**, **Apache Magpie** (Apache Software Foundation), **Google's Agent
Development Kit** and **Cognee**. Open review threads across **Apache Airflow**, **pandas**,
**LiteLLM**, **Buzz**, **Microsoft Agent Framework**, **corsair**, **cognee** and **ADK**.
Anthropic certified across AI Fluency, MCP, Agent Skills and Subagents; Walmart Global Tech
Advanced Software Engineering and Deloitte Cyber job simulations.

<div align="center">

<sub><i>A claim isn't real until something measures it.</i></sub>

</div>
