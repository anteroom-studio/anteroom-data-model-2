# ZAI World Data Model 🌍🤖
### Macro Market Prediction AI — Historical Data 1871 to Today

**Built by Zawwar | [@Zawwarsami16](https://github.com/Zawwarsami16)**

---

## What Is This?

I built ZAI World Data Model because I wanted to understand why markets crash — not just when they crash, but what conditions always seem to come before them.

The idea: if you download 125+ years of global financial data and find the hidden connections between markets, you can compare today's conditions to every historical crash and see which one it most resembles.

Think of it like a fingerprint database for financial crises.

---

## How It Works

```
Historical Data (1871–today)
+ Live Market Data (auto-updated every 5min)
+ World News Feed (435+ RSS sources)
         ↓
Correlation Engine
finds: "when oil spikes → inflation follows in 6–8 weeks"
         ↓
Pattern Matching
"today looks 78% like conditions before the 2008 crash"
         ↓
AI Prediction (local LLM or Claude API)
4-week, 3-month, 6-month market outlook
         ↓
Live Terminal Dashboard — runs 24/7
```

---

## Quick Start

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Add your API key** *(optional — skip if using Ollama)*

Edit `config.py`:
```python
ANTHROPIC_KEY = "your-key-here"  # console.anthropic.com
```

**3. Download historical data** *(run once — takes ~10 minutes)*
```bash
python3 data_collector.py
```

**4. Run the correlation engine**
```bash
python3 correlation_engine.py
```

**5. Launch the live dashboard**
```bash
python3 dashboard.py
```

Or use the launcher which auto-detects your hardware:
```bash
python3 zai_launcher.py
```

---

## Free Local AI (No API Costs)

If you have [Ollama](https://ollama.com) installed, ZAI will use it automatically — no API key needed.

```bash
ollama pull phi3:mini    # runs on CPU, 2GB download
```

Then set in `config.py`:
```python
USE_LOCAL_LLM = True
LOCAL_LLM_MODEL = "phi3:mini"
```

**GPU options:**
| GPU VRAM | Recommended Model |
|----------|------------------|
| 4GB+     | mistral:7b       |
| 8GB+     | llama3:8b        |
| 12GB+    | llama3:13b       |
| 24GB+    | llama3:70b       |
| No GPU   | phi3:mini (CPU)  |

---

## Data Sources (All Free)

| Source | Data | Coverage |
|--------|------|----------|
| FRED (Federal Reserve) | Inflation, GDP, Interest Rates, M2 | 1871– |
| Yahoo Finance | S&P500, NASDAQ, Gold, Oil, VIX | 1970– |
| CoinGecko | Bitcoin, Ethereum | 2010– |
| World Bank | Global GDP | 1960– |

---

## Files

| File | What It Does |
|------|-------------|
| `config.py` | Settings — the only file you need to edit |
| `data_collector.py` | Downloads all historical + live data |
| `correlation_engine.py` | Finds patterns + generates prediction |
| `news_brain.py` | Monitors world events, matches to history |
| `dashboard.py` | Live 24/7 terminal display |
| `zai_launcher.py` | Auto-detects hardware, installs what's needed |

---

## What Gets Detected

- 105 correlation pairs across 15 global markets
- 7 historical crash patterns (1929 Great Depression → 2022 Crypto Crash)
- Lead-lag relationships — which market moves before another
- Real-time similarity score: "today looks X% like [historical event]"
- Live news analysis from 435+ RSS feeds with market impact mapping

---

## Hardware Requirements

- **RAM:** 8GB minimum, 12GB+ recommended
- **Storage:** 2GB for data (I use a 1TB portable SSD)
- **GPU:** Not needed — uses API or CPU-based local model
- **Python:** 3.8+

---

## Roadmap

- [x] Historical data download (15 sources, 1871–today)
- [x] Correlation engine (105 pairs)
- [x] Crash pattern matching (7 historical events)
- [x] Claude API predictions
- [x] Local LLM support (Ollama)
- [x] Live terminal dashboard
- [x] World news monitoring (news_brain.py)
- [ ] Web-based dashboard
- [ ] Telegram alerts
- [ ] More data sources (commodities, sentiment indices)

---

*Built for research purposes. Not financial advice.*
