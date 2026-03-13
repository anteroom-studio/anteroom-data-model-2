# ================================================================
# ZAI WORLD MODEL - CONFIG FILE
# by Zawwar (github.com/Zawwarsami16)
#
# This is the ONLY file you need to touch.
# Everything else runs automatically.
# ================================================================

# Get your key from console.anthropic.com
# If you have Ollama installed with a local model, you don't need this
ANTHROPIC_KEY = "YOUR_ANTHROPIC_API_KEY_HERE"

# Where to store all the downloaded data
# I use my 1TB portable SSD — change this to wherever you want
# Windows: "D:/ZAI_Data"   Linux: "/mnt/ssd/ZAI_Data"
DATA_PATH = "./zai_data"

# How far back to pull data — I went with 1871, the further the better
HISTORY_FROM_YEAR = 1871

# How often live prices refresh (in seconds) — 300 = every 5 minutes
UPDATE_INTERVAL = 300

# Minimum confidence before showing a prediction — I keep it at 65
MIN_CONFIDENCE = 65

# ================================================================
# DATASETS
# Turn off anything you don't want downloaded
# ================================================================
DATASETS = {
    "sp500":        True,   # S&P 500 — the main one
    "gold":         True,   # Gold — always watch this
    "oil":          True,   # Crude oil — moves everything
    "dollar":       True,   # Dollar index — affects all markets
    "bitcoin":      True,   # Bitcoin — my main focus
    "inflation":    True,   # US CPI — goes back to 1871
    "gdp":          True,   # US GDP
    "unemployment": True,   # Unemployment rate
    "interest":     True,   # Fed interest rates
    "vix":          True,   # Fear index — very useful
    "nasdaq":       True,   # Nasdaq — tech heavy
    "dxy":          True,   # Dollar index detailed
    "bonds":        True,   # 10Y Treasury yield
    "copper":       True,   # Copper = economic health indicator
    "crypto_total": True,   # Total crypto market cap
}

# ================================================================
# LOCAL LLM (optional)
# If you have Ollama installed, set USE_LOCAL_LLM = True
# This gives you FREE predictions without any API costs
# I run phi3:mini on my machine — works fine without a GPU
# ================================================================
USE_LOCAL_LLM = True
LOCAL_LLM_MODEL = "phi3:mini"
# Other options depending on your hardware:
# "llama3:8b"   — needs 8GB+ VRAM
# "llama3:13b"  — needs 12GB+ VRAM
# "mistral:7b"  — good balance of speed and quality
