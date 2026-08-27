<div align="center">

# Shikhar Goel

**Software Engineer** · distributed systems, static analysis, native apps — and the AI layer on top

<a href="https://portfolio-website-zeta-dun-27.vercel.app/">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=21&duration=3200&pause=900&color=38BDAF&center=true&vCenter=true&width=700&lines=Crash-safe+by+construction%3A+WAL%2C+fencing+tokens%2C+F_FULLFSYNC.;627+regexes+benchmarked.+0+false+positives%2C+0+misses.;Merged+into+NumPy%2C+Apache+Magpie%2C+Google+ADK+and+Cognee.;Deterministic+code+decides.+Models+only+observe." alt="Typing SVG" />
</a>

<br/>

<a href="https://portfolio-website-zeta-dun-27.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white" /></a>
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

Four merges into projects I actually use, plus work in flight:

| Project | PR | What it did |
|---|---|---|
| **[numpy/numpy](https://github.com/numpy/numpy)** | [#32386](https://github.com/numpy/numpy/pull/32386) ✅ **merged** | `BUG: close duplicated file descriptor if fdopen fails` — C-level fix closing a descriptor leak in NumPy's error path, with regression tests handling WASM/musl. All 91 required CI checks passed. |
| **[apache/magpie](https://github.com/apache/magpie)** | [#1089](https://github.com/apache/magpie/pull/1089) ✅ **merged** | `fix(license-compliance-audit): handle large blobs and canonical SPDX` — files over ~1 MiB return without inline content, so the audit silently mis-flagged them as non-compliant. Fetches via raw-media API, separates *uninspected* from *violating*, enforces canonical `Apache-2.0`. Closed issue #944. |
| **[google/adk-python](https://github.com/google/adk-python)** | [#6419](https://github.com/google/adk-python/pull/6419) ✅ **merged** | `fix: handle Windows paths in adk eval` — the eval-case parser read the colon in `C:\` as a case selector. |
| **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | [#4126](https://github.com/topoteretes/cognee/pull/4126) ✅ **merged** | `fix(cli): reject dry runs in API dispatch mode` — `--dry-run` was silently ignored when `--api-url` was set, executing real remote operations. |
| **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | [#4161](https://github.com/topoteretes/cognee/pull/4161) 🔄 open | `fix(api): scope configuration lookup to authenticated owner` — any authenticated user could read any config by UUID. |
| **[corsairdev/corsair](https://github.com/corsairdev/corsair)** | [#1200](https://github.com/corsairdev/corsair/pull/1200) 🔄 open | `feat(pinecone): production-grade integration` — 48 operations across four API surfaces, typed Zod schemas, dynamic host routing. |
| **[google/adk-python](https://github.com/google/adk-python)** | [#6705](https://github.com/google/adk-python/pull/6705) 🔄 open | `test: pin EvalCase session state injection` — regression test locking state injection into instruction templates. |

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

<div align="center">

![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Swift](https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)

![gRPC](https://img.shields.io/badge/gRPC_/_Connect-244C5A?style=flat-square&logo=grpc&logoColor=white)
![Protobuf](https://img.shields.io/badge/Protocol_Buffers-4285F4?style=flat-square&logo=googlecloud&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![Vitest](https://img.shields.io/badge/Vitest-6E9F18?style=flat-square&logo=vitest&logoColor=white)
![Xcode](https://img.shields.io/badge/Xcode-147EFB?style=flat-square&logo=xcode&logoColor=white)
![MCP](https://img.shields.io/badge/Model_Context_Protocol-D97757?style=flat-square&logo=anthropic&logoColor=white)
![PyTorch](https://img.shields.io/badge/TensorFlow_/_Keras-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)

</div>

---

## Track record

<div align="center">

![Merged](https://img.shields.io/badge/Upstream_PRs_merged-4-38BDAF?style=for-the-badge)
![Open](https://img.shields.io/badge/In_review-3-203A43?style=for-the-badge)
![Orchestrate](https://img.shields.io/badge/HackerRank_Orchestrate-%2337_of_1,773-38BDAF?style=for-the-badge)

</div>

Merged into **NumPy**, **Apache Magpie** (Apache Software Foundation), **Google's Agent Development
Kit** and **Cognee**. Anthropic certified across AI Fluency, MCP, Agent Skills and Subagents;
Walmart Global Tech Advanced Software Engineering and Deloitte Cyber job simulations.

<div align="center">

<sub><i>A claim isn't real until something measures it.</i></sub>

</div>
