<div align="center">

# Shikhar Goel

**AI &amp; Systems Engineer**

<a href="https://portfolio-website-zeta-dun-27.vercel.app/">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=3000&pause=900&color=38BDAF&center=true&vCenter=true&width=650&lines=Deterministic+code+decides.+Models+only+observe.;Agents+with+stopping+conditions%2C+not+vibes.;Go+job+queues%2C+Python+routers%2C+TypeScript+debuggers.;Shipping+at+Thapar+%E2%80%A2+B.E.+CSE+'28" alt="Typing SVG" />
</a>

<br/>

<a href="https://portfolio-website-zeta-dun-27.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white" /></a>
<a href="mailto:shikhardeepgoel@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" /></a>
<img src="https://komarev.com/ghpvc/?username=sgoel2be24-cyber&style=for-the-badge&color=38BDAF&label=PROFILE+VIEWS" />

</div>

---

### `whoami`

```python
class Shikhar:
    role      = "AI & Software Developer"
    studying  = "B.E. Computer Engineering @ Thapar Institute (2024–2028)"
    focus     = ["agentic systems", "RAG", "deterministic evals", "distributed systems"]
    thesis    = "LLMs emit typed observations. Deterministic code makes the decisions."
    currently = "Go internals, agent evaluation harnesses, and shipping things that survive judges"
```

I build AI systems that are **auditable** — every agent has a stopping condition, a verifier, a
budget, and a fallback path. Most of my repos exist because I wanted evidence that something
actually worked, not a demo that worked once.

---

## Selected work

| Project | What it is | Stack |
|---|---|---|
| **[conveyor-job-queue](https://github.com/sgoel2be24-cyber/conveyor-job-queue)** | Durable distributed job queue — crash-safe WAL, at-least-once delivery with fencing tokens, lease-timeout reclaim, jittered-backoff retries, dead-letter queue | `Go` |
| **[modelgauntlet](https://github.com/sgoel2be24-cyber/modelgauntlet)** | Break your AI before users do. Deterministic, reproducible release evidence across open models | `TypeScript` |
| **[multimodal-evidence-review](https://github.com/sgoel2be24-cyber/multimodal-evidence-review-orchestrate)** | Multimodal damage-claim verification pipeline — **ranked #37 of 1,773** at HackerRank Orchestrate | `Python` |
| **[kaamtwin](https://github.com/sgoel2be24-cyber/kaamtwin)** | Evidence-linked workflow debugger for microbusinesses: observations compile to a process twin, deterministic code simulates the failure, patches it, and re-verifies the identical scenario | `TypeScript` |
| **[zero-token-router](https://github.com/sgoel2be24-cyber/zero-token-router)** | Hybrid token-efficient LLM router — keeps cheap tasks local, escalates only what needs it. `v0.2.0` passed 10/10 retired + 19/19 simulated eval under 4 GB RAM / 2 CPUs | `Python` |
| **[hospital-readmission-risk](https://github.com/sgoel2be24-cyber/hospital-readmission-risk)** | Readmission-risk modelling with a focus on calibration and explainability, not leaderboard accuracy | `Python` |

---

## Open source

Contributions merged into projects I actually use:

| Project | PR | What it fixed |
|---|---|---|
| **[google/adk-python](https://github.com/google/adk-python)** | [#6419](https://github.com/google/adk-python/pull/6419) ✅ **merged** | `fix: handle Windows paths in adk eval` — the eval-case parser was reading the colon in `C:\` as a case selector |
| **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | [#4126](https://github.com/topoteretes/cognee/pull/4126) ✅ **merged** | `fix(cli): reject dry runs in API dispatch mode` — `--dry-run` was silently ignored when `--api-url` was set, executing real remote operations |
| **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | [#4161](https://github.com/topoteretes/cognee/pull/4161) 🔄 open | `fix(api): scope configuration lookup to authenticated owner` — any authenticated user could read any config by UUID |
| **[corsairdev/corsair](https://github.com/corsairdev/corsair)** | [#1200](https://github.com/corsairdev/corsair/pull/1200) 🔄 open | `feat(pinecone): production-grade Pinecone integration` — 48 operations across four API surfaces, typed Zod schemas, dynamic host routing |
| **[google/adk-python](https://github.com/google/adk-python)** | [#6705](https://github.com/google/adk-python/pull/6705) 🔄 open | `test: pin EvalCase session state injection` — regression test locking in state injection into instruction templates |

---

## Toolkit

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)

![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![MCP](https://img.shields.io/badge/Model_Context_Protocol-D97757?style=flat-square&logo=anthropic&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

</div>

---

## Track record

<div align="center">

![Orchestrate](https://img.shields.io/badge/HackerRank_Orchestrate-%2337_of_1,773-38BDAF?style=for-the-badge)
![Merged](https://img.shields.io/badge/Upstream_PRs_merged-2-38BDAF?style=for-the-badge)
![Open](https://img.shields.io/badge/Upstream_PRs_open-3-203A43?style=for-the-badge)

</div>

Merged into **google/adk-python** and **topoteretes/cognee** — both projects I use daily. Open work in
flight on **corsairdev/corsair** (a 48-operation Pinecone integration) and a regression test back in ADK.

---

## Elsewhere

- 🏆 **HackerRank Orchestrate 2026** — #37 / 1,773
- 🧪 Hackathons: Codex 2026 · Goldman Sachs India · Bharatiya Antariksh (exoplanet transit detection) · SBI @ GFF · Vibe2Ship by Google for Developers · AMD Developer Hackathon
- 📜 Anthropic AI Fluency series · MCP · Agent Skills · Walmart Global Tech SWE Simulation · Deloitte Cyber Simulation
- 💼 AI internships across a FastAPI + React analytics stack and RAG pipeline work

<div align="center">

<sub><i>If a loop runs more than once, it needs a verifier and a budget.</i></sub>

</div>
