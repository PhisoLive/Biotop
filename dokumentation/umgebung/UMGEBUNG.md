# Umgebung des Biotops bei der Einlagerung (abgelesen 26.09.2026 01:10:55 CEST, BIOTOP-EINLAGERUNG-01)

## Betriebssystem und Sprachen
```text
PRETTY_NAME="Ubuntu 24.04.4 LTS"
VERSION_ID="24.04"
Kernel 6.8.0-139-generic · x86_64 · CPUs 4 · RAM 3 GiB
System-Python: Python 3.12.3 (/usr/bin/python3.12)
Node: v26.8.2 (/root/.hermes/node/bin/node) · npm 11.19.1
Docker: Docker version 29.1.3, build 29.1.3-0ubuntu3~24.04.2
Git: git version 2.43.0 · pigz: pigz 2.8 · uv: uv 0.12.13 (x86_64-unknown-linux-gnu)
```

## Python-Umgebungen (pip freeze je Umgebung, über `uv pip freeze`, nur lesend)
- `/root/biotop-t3/venv`: Python 3.12.3 · 5 Pakete · Datei `pip-freeze-root-biotop-t3-venv.txt`
  - pyvenv.cfg: home = /usr/bin;implementation = CPython;uv = 0.12.13;version_info = 3.12.3;include-system-site-packages = false;
- `/root/reparatur-01/venv`: Python 3.12.3 · 5 Pakete · Datei `pip-freeze-root-reparatur-01-venv.txt`
  - pyvenv.cfg: home = /usr/bin;implementation = CPython;uv = 0.12.13;version_info = 3.12.3;include-system-site-packages = false;
- `/usr/local/lib/hermes-agent/venv`: Python 3.12.3 · 113 Pakete · Datei `pip-freeze-usr-local-lib-hermes-agent-venv.txt`
  - pyvenv.cfg: home = /usr/bin;implementation = CPython;uv = 0.12.13;version_info = 3.12.3;include-system-site-packages = false;
- Die Regression des Biotops läuft mit `/root/biotop-t3/venv/bin/python` (Runde 5: `/root/biotop-vor-t4-05/job_kette.sh` Z. 7).
- `venv`-Ordner sind nicht in den Archiven (Abhängigkeitsordner); sie werden aus den freeze-Dateien neu gebaut.

## Sperr- und Anforderungsdateien (Kopien in `sperrdateien/`)
- `/root/biotop/requirements-test.txt` · 14 B · SHA-256 `93c4ab5f175d24229e46ec70a8ecaeb6db8b36e3f54d8005808044c060acbc92` → `sperrdateien/biotop_requirements-test.txt`
- `/root/biotop/kammer/typescript/package.json` · 320 B · SHA-256 `1c74ff1dcb7dd03df8efef0b9319d1a28d5cd6251e8cefbbff05d04c034380c8` → `sperrdateien/biotop_kammer_typescript_package.json`
- `/root/biotop/kammer/typescript/package-lock.json` · 125863 B · SHA-256 `ba6dd4d05537da81b8634dd17b3bb805adf46b2ebb81e0fe08e8bb87e4840f30` → `sperrdateien/biotop_kammer_typescript_package-lock.json`
- `/root/biotop/daten/werke/versandwerk-t3-02/package.json` · 378 B · SHA-256 `82ca32479534be5813d71b645a05befb11909bdccd045aa3533361826a0f7748` → `sperrdateien/biotop_daten_werke_versandwerk-t3-02_package.json`

## Kammer: Docker-Abbilder, Kennung und Bauweg
```text
biotop-kammer:1 · Id sha256:ce7bbe9441182aea532f147defd99ca757a95d4cb3ff7c3f5c5d9a64965643ee · erstellt 2026-09-18T23:26:54.853201859+02:00 · 55798078 B · RepoDigests [biotop-kammer@sha256:ce7bbe9441182aea532f147defd99ca757a95d4cb3ff7c3f5c5d9a64965643ee]
biotop-kammer:ts1 · Id sha256:212e6212cd165b668f5cff7a1ab12c22d739a0ab727bbedc45a87c3793754f9e · erstellt 2026-09-21T02:47:15.319791658+02:00 · 124884212 B · RepoDigests [biotop-kammer@sha256:212e6212cd165b668f5cff7a1ab12c22d739a0ab727bbedc45a87c3793754f9e]
python:3.12-slim · Id sha256:78387bc3881b8273120a12ebe6c1ab22b018ccc2c9adf565ae1ac9b536e184ea · erstellt 2026-09-01T00:12:40.129211396Z · 46192946 B · RepoDigests [python@sha256:78387bc3881b8273120a12ebe6c1ab22b018ccc2c9adf565ae1ac9b536e184ea]
node:22-bookworm-slim · Id sha256:48e4b67d85f87bd551df43704e24d252f56cc5f8e9718841aace50f19948f0f9 · erstellt 2026-09-19T00:48:56.693292887Z · 79907464 B · RepoDigests [node@sha256:48e4b67d85f87bd551df43704e24d252f56cc5f8e9718841aace50f19948f0f9]
```
- Bauweg `/root/biotop/kammer/Dockerfile` → `kammer-bauweg/kammer_Dockerfile` (SHA-256 `fb5724b68ace39ff9032800208c136d3ed6d11b3ebdb3288b48750823bad1ba3`):
```dockerfile
FROM python:3.12-slim
RUN pip install --no-cache-dir pytest==8.3.3 bandit==1.7.10 vulture==2.13 && useradd -m -u 10001 kammer
WORKDIR /werk
USER kammer
```
- Bauweg `/root/biotop/kammer/typescript/Dockerfile` → `kammer-bauweg/kammer_typescript_Dockerfile` (SHA-256 `ffdcd935b09dc54b9b5029afbe9a3f7e3d03231dd4ef56f7015f1c1a7b0dad3d`):
```dockerfile
# Werkzeugauflösung nur im Bau; Werklaeufe durch kammer --network none.
FROM node:22-bookworm-slim@sha256:48e4b67d85f87bd551df43704e24d252f56cc5f8e9718841aace50f19948f0f9 AS werkzeuge
WORKDIR /opt/biotop-ts
COPY package.json package-lock.json ./
RUN npm ci --no-audit --no-fund \
 && node node_modules/typescript/bin/tsc --version \
 && node node_modules/vitest/vitest.mjs --version \
 && node node_modules/eslint/bin/eslint.js --version \
 && node node_modules/knip/bin/knip.js --version

FROM biotop-kammer:1
USER root
COPY --from=werkzeuge /usr/local/bin/node /usr/local/bin/node
COPY --from=werkzeuge /opt/biotop-ts /opt/biotop-ts
ENV PATH="/opt/biotop-ts/node_modules/.bin:${PATH}"
RUN node --version && python -m pytest --version \
 && node /opt/biotop-ts/node_modules/tsx/dist/cli.mjs --version
USER kammer
```
- Bauschritte je Abbild: `kammer-bauweg/docker-history-*.txt`; volle Angaben: `kammer-bauweg/docker-image-inspect.json`.
- Bau (gelesen, nicht ausgeführt): `docker build -t biotop-kammer:1 /root/biotop/kammer` und danach
  `docker build -t biotop-kammer:ts1 /root/biotop/kammer/typescript` (Stufe 1 aus `node:22-bookworm-slim@sha256:48e4…`, Stufe 2 `FROM biotop-kammer:1`).
- Hinweis: `kammer/Dockerfile` nennt `FROM python:3.12-slim` ohne Digest; ein Neubau zieht womöglich ein anderes Abbild.
  Deshalb liegen die gebauten Abbilder mit `docker save` im Archiv KOMPLETT (Ordner `kammer-abbilder/`).

## Hermes Agent
```text
Hermes Agent v0.21.2 (2026.9.11) · upstream abf47063
Install directory: /usr/local/lib/hermes-agent
Install method: git
Git: abf4706384c8ab17d6f22aab0ab8c71526eac305 · Sun Sep 13 15:05:11 2026 -0700 · test(gateway): raw-output watcher messages are human-facing
Herkunft: https://github.com/NousResearch/hermes-agent.git
Lokale Änderungen (git status --short): 0 Einträge
```
- Der Quellbaum `/usr/local/lib/hermes-agent` liegt ohne `venv`, `node_modules` und `__pycache__` im Archiv KOMPLETT.

## Skills (Liste; Inhalte liegen in KOMPLETT unter root/.hermes/skills/)
64 Skills unter `/root/.hermes/skills` (abgelesen).

| Name | Ordner | Beschreibung (Anfang) | Bytes | SHA-256 |
|---|---|---|---|---|
| apple-notes | `apple/apple-notes` | Manage Apple Notes via memo CLI: create, search, edit. | 2394 | `1ba042cb17e3aca0…` |
| apple-reminders | `apple/apple-reminders` | Apple Reminders via remindctl: add, list, complete. | 3606 | `ee5084f2d7ec1964…` |
| findmy | `apple/findmy` | Track Apple devices/AirTags via FindMy.app on macOS. | 3709 | `19ec56e3b7f9f0be…` |
| imessage | `apple/imessage` | Send and receive iMessages/SMS via the imsg CLI on macOS. | 2442 | `bc68b1648e301409…` |
| claude-code | `autonomous-ai-agents/claude-code` | Delegate coding to Claude Code CLI (features, PRs). | 34281 | `3fd7c81f2c6c19f8…` |
| codex | `autonomous-ai-agents/codex` | Delegate coding to OpenAI Codex CLI (features, PRs). | 5738 | `3ed457c2b8d5d9c3…` |
| computer-use | `autonomous-ai-agents/computer-use` | Drive the desktop background-first; escalate on signal. | 15819 | `e3d11184959bd061…` |
| hermes-agent | `autonomous-ai-agents/hermes-agent` | Use, configure, theme, extend, and orchestrate Hermes Agent. | 13289 | `e443561f1300b933…` |
| opencode | `autonomous-ai-agents/opencode` | Delegate coding to OpenCode CLI (features, PR review). | 7259 | `afb3ea1f1b430070…` |
| architecture-diagram | `creative/architecture-diagram` | Dark-themed SVG architecture/cloud/infra diagrams as HTML. | 5830 | `0e7e2736aafe052e…` |
| ascii-video | `creative/ascii-video` | ASCII video: convert video/audio to colored ASCII MP4/GIF. | 15011 | `3bd3f39985a52954…` |
| baoyu-infographic | `creative/baoyu-infographic` | Infographics: 21 layouts x 21 styles (信息图, 可视化). | 10434 | `89e25da6d8ea1cac…` |
| claude-design | `creative/claude-design` | Design one-off HTML artifacts (landing, deck, prototype). | 25117 | `1582b0d49e48bdf9…` |
| design-md | `creative/design-md` | Author/validate/export Google's DESIGN.md token spec files. | 8477 | `7ed56bba40ffc957…` |
| humanizer | `creative/humanizer` | Humanize text: strip AI-isms and add real voice. | 34463 | `887d5e3467a682da…` |
| manim-video | `creative/manim-video` | Manim CE animations: 3Blue1Brown math/algo videos. | 12150 | `467376469fc2043e…` |
| p5js | `creative/p5js` | p5.js sketches: gen art, shaders, interactive, 3D. | 27534 | `3b39b75303e082af…` |
| popular-web-designs | `creative/popular-web-designs` | 54 real design systems (Stripe, Linear, Vercel) as HTML/CSS. | 9722 | `cd89bdb86008bb30…` |
| songwriting-and-ai-music | `creative/songwriting-and-ai-music` | Songwriting craft and Suno AI music prompts. | 10963 | `5dbf92dc336e9b17…` |
| sdlc-review | `devops/sdlc-review` | Review Kanban handoffs and route verified outcomes. | 9073 | `ce90e8a3e145cce6…` |
| email-inbox-triage | `email/email-inbox-triage` | Triage an inbox: prioritize threads, draft replies safely. | 4057 | `cd57ccc9d563b518…` |
| himalaya | `email/himalaya` | Himalaya CLI: IMAP/SMTP email from terminal. | 7272 | `0f6c9bb4c0a5c4f4…` |
| gif-search | `media/gif-search` | Search/download GIFs from Tenor via curl + jq. | 2720 | `a8349043740a8805…` |
| songsee | `media/songsee` | Audio spectrograms/features (mel, chroma, MFCC) via CLI. | 2336 | `d9d8d1394c630bd8…` |
| youtube-content | `media/youtube-content` | YouTube transcripts to summaries, threads, blogs. | 3538 | `52349e30ac74a3c2…` |
| obsidian | `note-taking/obsidian` | Read, search, create, and edit notes in the Obsidian vault. | 3092 | `7aea4e8f89f94ab2…` |
| airtable | `productivity/airtable` | Airtable REST API via curl. Records CRUD, filters, upserts. | 11314 | `28253f1e20c4d250…` |
| box | `productivity/box` | Box manages cloud files, sharing, search, and metadata. | 11697 | `e9672412333de4fe…` |
| document-to-action-items | `productivity/document-to-action-items` | Extract cited obligations, deadlines, tasks from documents. | 3910 | `8a7556754aca2a7d…` |
| docx | `productivity/docx` | Create, read, edit, template, and review Word .docx files. | 10395 | `9678b14d5e7841d5…` |
| google-workspace | `productivity/google-workspace` | Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python. | 13926 | `c22194d932d9d96f…` |
| maps | `productivity/maps` | Geocode, POIs, routes, timezones via OpenStreetMap/OSRM. | 6705 | `775ef9f79be9cd14…` |
| meeting-action-items | `productivity/meeting-action-items` | Turn meeting notes into cited decisions, owners, tickets. | 3808 | `1902f782551da96e…` |
| notion | `productivity/notion` | Notion API + ntn CLI: pages, databases, markdown, Workers. | 14629 | `798ad178ead72ad3…` |
| pdf | `productivity/pdf` | PDF files: create, read, merge, fill, OCR, edit text. | 12489 | `c16b9c159a3a0b49…` |
| powerpoint | `productivity/powerpoint` | Create, read, edit .pptx decks with python-pptx. | 10781 | `b71d29d9809c4464…` |
| product-price-monitor | `productivity/product-price-monitor` | Watch product, flight, or listing prices; alert on target. | 4400 | `b87bf2102fed13d2…` |
| teams-meeting-pipeline | `productivity/teams-meeting-pipeline` | Teams meeting summaries, job replay, Graph subscriptions. | 7206 | `ae1b08f044d7dfd9…` |
| weekly-review-planning | `productivity/weekly-review-planning` | Weekly reset: commitments, stalled work, next-week plan. | 3975 | `a689257facb937cf…` |
| xlsx | `productivity/xlsx` | Create, read, edit Excel .xlsx workbooks and CSVs. | 9655 | `b302d7ac997843a7…` |
| arxiv | `research/arxiv` | Search arXiv papers by keyword, author, category, or ID. | 10061 | `9b41877bcb64166d…` |
| competitor-news-monitor | `research/competitor-news-monitor` | Watch named companies for material news; cited digests. | 4619 | `d8fd2a3a26ff4545…` |
| grounded-citations | `research/grounded-citations` | Ground answers and documents in cited, verifiable sources. | 12652 | `19fba3a4ceedf768…` |
| llm-wiki | `research/llm-wiki` | Karpathy's LLM Wiki: build/query interlinked markdown KB. | 20121 | `0229e37c1783fcac…` |
| xurl | `social-media/xurl` | X/Twitter via xurl CLI: raw post search, posting, DM, media. | 16345 | `5457319ee337284b…` |
| audit-channel-delivery | `software-development/audit-channel-delivery` | Use when delivering work to the audit channel (Prüfkanal). | 19380 | `d33963c8bf6bc825…` |
| biotop-phase-bauen | `software-development/biotop-phase-bauen` | Use when building a Biotop phase; Tor lines, Prüfkanal. | 14307 | `f1defae43b6759ef…` |
| codebase-inspection | `software-development/codebase-inspection` | Inspect codebases w/ pygount: LOC, languages, ratios. | 6033 | `015704e100160078…` |
| delegated-build-orchestration | `software-development/delegated-build-orchestration` | Use when splitting work across parallel subagents. | 8697 | `b49956693c73b1ad…` |
| dogfood | `software-development/dogfood` | Exploratory QA of web apps: find bugs, evidence, reports. | 6324 | `1b2793734493dbc6…` |
| github | `software-development/github` | GitHub via gh CLI: PRs, issues, reviews, repos, auth. | 2446 | `9d70e7c842fe7db7…` |
| hermes-agent-skill-authoring | `software-development/hermes-agent-skill-authoring` | Author in-repo SKILL.md files: frontmatter and structure. | 14432 | `3a274d5b42fa0a95…` |
| inspecting-hermes-desktop-dom | `software-development/inspecting-hermes-desktop-dom` | Read the live Hermes desktop DOM/CSS over CDP. | 6204 | `a78a5f8d277a1d6d…` |
| junit-witness-completion | `software-development/junit-witness-completion` | Use when validating JUnit evidence. Check both exit layers. | 1596 | `c52f68040d5c5d90…` |
| measurement-harness-discipline | `software-development/measurement-harness-discipline` | Use when a measured number gates a decision. | 89573 | `f6211e3fbfaa2b64…` |
| node-inspect-debugger | `software-development/node-inspect-debugger` | Debug Node.js via --inspect + Chrome DevTools Protocol CLI. | 10894 | `bc89942b76387834…` |
| python-debugpy | `software-development/python-debugpy` | Debug Python: pdb REPL + debugpy remote (DAP). | 13347 | `24258d93eb080e7b…` |
| requesting-code-review | `software-development/requesting-code-review` | Pre-commit review: security scan, quality gates, auto-fix. | 10100 | `da37c59978555c97…` |
| simplify-code | `software-development/simplify-code` | Parallel 4-agent cleanup of recent code changes. | 14696 | `9ee977c3362a1c07…` |
| spike | `software-development/spike` | Throwaway experiments to validate an idea before build. | 8723 | `573d8fc0d6699eaf…` |
| systematic-debugging | `software-development/systematic-debugging` | 4-phase root cause debugging: understand bugs before fixing. | 14059 | `bd480f51a2e9969c…` |
| test-driven-development | `software-development/test-driven-development` | TDD: enforce RED-GREEN-REFACTOR, tests before code. | 10300 | `649e6ab89bd8aaad…` |
| verified-backup-restore | `software-development/verified-backup-restore` | Use when backing up a project with a proven restore. | 8366 | `6cb0214a39a17d24…` |
| blocked-page-recovery | `web/blocked-page-recovery` | Use when a fetch fails: 403/429, paywall, WAF, bot wall. | 5156 | `7f7d321f177399ca…` |
