import os
from pathlib import Path

# ============================================================
# ANTEROOM DATA MODEL - CONFIGURATION
# ============================================================


def load_env(path: str = ".env"):
    env = Path(path)
    if not env.exists():
        return
    for line in env.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


load_env()

ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY", "")
DATA_PATH = os.getenv("ANTEROOM_DATA_PATH", "./anteroom_data")
HISTORY_FROM_YEAR = int(os.getenv("ANTEROOM_HISTORY_FROM_YEAR", "1871"))
UPDATE_INTERVAL = int(os.getenv("ANTEROOM_UPDATE_INTERVAL", "300"))
MIN_CONFIDENCE = int(os.getenv("ANTEROOM_MIN_CONFIDENCE", "65"))

USE_LOCAL_LLM = os.getenv("ANTEROOM_USE_LOCAL_LLM", "true").lower() == "true"
LOCAL_LLM_MODEL = os.getenv("ANTEROOM_LOCAL_LLM_MODEL", "phi3:mini")

DATASETS = {
    "sp500": True,
    "gold": True,
    "oil": True,
    "dollar": True,
    "bitcoin": True,
    "inflation": True,
    "gdp": True,
    "unemployment": True,
    "interest": True,
    "vix": True,
    "nasdaq": True,
    "dxy": True,
    "bonds": True,
    "copper": True,
    "crypto_total": True,
}
