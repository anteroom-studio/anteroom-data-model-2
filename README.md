# Anteroom Data Model

**Macro data intelligence system for historical market analysis, event monitoring, and scenario research.**

Anteroom Data Model is a Python-based research system that collects long-range market and macroeconomic data, monitors world-event signals, compares current conditions against historical stress periods, and produces structured scenario summaries through local or API-based language models.

> Built by **Anteroom Studio** as part of its research systems and intelligence tooling.

---

## Overview

This project was designed to study market regimes as connected systems rather than isolated charts. It combines historical financial data, live market snapshots, world-event monitoring, lead-lag analysis, and historical similarity matching.

It helps explore questions such as:

- Which indicators historically move before others?
- Which historical stress periods resemble current conditions?
- What categories of news are most relevant to market risk?
- How do equities, commodities, rates, currencies, and crypto behave across similar regimes?

This is a research and analysis tool, not a trading signal service.

---

## System Flow

```text
Historical Data + Live Market Data + World News Feeds
                         ↓
Data Normalization and Storage
                         ↓
Correlation and Lead-Lag Engine
                         ↓
Historical Stress-Period Matching
                         ↓
Optional Local/API Model Summary
                         ↓
Terminal Dashboard
```

---

## Core Capabilities

- Historical market and macro data collection
- Live market refresh cycle
- Cross-asset correlation analysis
- Lead-lag relationship detection
- Historical stress-period comparison
- RSS-based world-event monitoring
- Local LLM support through Ollama
- Optional Anthropic API fallback
- Terminal dashboard for live review
- Hardware-aware launcher

---

## Data Sources

| Source | Coverage |
|---|---|
| FRED | Inflation, GDP, rates, unemployment, treasury data |
| Yahoo Finance | Equities, commodities, volatility, market indices |
| CoinGecko | Bitcoin and Ethereum market data |
| World Bank | Global macroeconomic data |
| RSS feeds | World events, market news, energy, crypto, policy, technology |

---

## Requirements

- Python 3.8+
- 8GB RAM minimum; 12GB+ recommended
- Around 2GB+ local storage for datasets
- Optional Ollama installation for local summaries
- Optional Anthropic API key for cloud model summaries

---

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create local environment settings:

```bash
cp .env.example .env
```

Optional local configuration:

```env
ANTHROPIC_API_KEY=
ANTEROOM_DATA_PATH=./anteroom_data
ANTEROOM_USE_LOCAL_LLM=true
ANTEROOM_LOCAL_LLM_MODEL=phi3:mini
```

Never commit `.env` or real credentials.

---

## Usage

Download historical data:

```bash
python3 data_collector.py
```

Run the analysis engine:

```bash
python3 correlation_engine.py
```

Run world-event analysis:

```bash
python3 news_brain.py
```

Launch the live dashboard:

```bash
python3 dashboard.py
```

Use the hardware-aware launcher:

```bash
python3 zai_launcher.py
```

> The launcher file name is retained for compatibility. It can be renamed later after repository migration.

---

## Local Model Support

If Ollama is installed, the system can use a local model without API costs.

```bash
ollama pull phi3:mini
```

Recommended starting configuration:

```env
ANTEROOM_USE_LOCAL_LLM=true
ANTEROOM_LOCAL_LLM_MODEL=phi3:mini
```

Larger systems can use models such as `mistral:7b`, `llama3:8b`, or larger variants depending on available RAM/VRAM.

---

## Project Structure

| File | Purpose |
|---|---|
| `config.py` | Safe runtime configuration and environment loading |
| `data_collector.py` | Historical and live market data collection |
| `correlation_engine.py` | Correlation, lead-lag, and historical similarity analysis |
| `news_brain.py` | RSS-based world-event monitoring and market-impact mapping |
| `dashboard.py` | Terminal dashboard for live review |
| `zai_launcher.py` | Hardware-aware launcher retained for compatibility |
| `.env.example` | Safe local environment template |
| `.gitignore` | Keeps local datasets, caches, and secrets out of Git |

---

## Safety and Scope

Anteroom Data Model is intended for research, education, and internal experimentation. Its outputs may be incomplete, stale, or incorrect depending on data-source availability, local configuration, and model behavior.

This project does not provide financial, investment, legal, or professional advice. Always verify outputs independently before using them in any real-world decision.

---

## Studio

**Anteroom Studio**  
Research systems, intelligence interfaces, and experimental software.
