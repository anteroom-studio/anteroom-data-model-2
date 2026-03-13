"""
ZAI World Model — Live Dashboard
by Zawwar (github.com/Zawwarsami16)

Runs 24/7 in your terminal.
Shows live market prices, AI predictions, historical similarity.
Auto-refreshes every 5 minutes.
Auto re-analyzes every 6 hours.

Just leave it running in the background.
"""

import os
import json
import time
import subprocess
from datetime import datetime
from config import DATA_PATH, UPDATE_INTERVAL, ANTHROPIC_KEY


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def load_latest():
    try:
        with open(f"{DATA_PATH}/predictions/latest.json") as f:
            return json.load(f)
    except:
        return None


def load_live():
    try:
        with open(f"{DATA_PATH}/live/latest.json") as f:
            return json.load(f)
    except:
        return None


def load_news():
    try:
        with open(f"{DATA_PATH}/news/latest.json") as f:
            return json.load(f)
    except:
        return None


# ================================================================
# MAIN DISPLAY
# ================================================================
def display(tick=0):
    clear()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    spin = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"][tick % 10]

    print("╔══════════════════════════════════════════════════════════╗")
    print("║          ZAI WORLD MODEL — MARKET PREDICTION AI          ║")
    print(f"║                    {now}                  ║")
    print(f"║           {spin} LIVE  by Zawwar (Zawwarsami16)              ║")
    print("╚══════════════════════════════════════════════════════════╝")

    # ── LIVE MARKETS ──────────────────────────────────────────
    live = load_live()
    if live:
        print("\n📊 LIVE MARKETS:")
        print("─" * 60)
        items = [
            ("S&P 500",   live.get("sp500")),
            ("NASDAQ",    live.get("nasdaq")),
            ("Gold",      live.get("gold")),
            ("Oil (WTI)", live.get("oil")),
            ("VIX Fear",  live.get("vix")),
            ("Bitcoin",   live.get("bitcoin")),
            ("Ethereum",  live.get("ethereum")),
        ]
        for name, d in items:
            if d:
                price = d.get("price", 0)
                chg = d.get("change_pct", 0)
                arr = "↑" if chg > 0 else "↓"
                sign = "+" if chg > 0 else ""
                print(f"  {name:<12} ${price:>12,.2f}   {arr} {sign}{chg:.2f}%")
    else:
        print("\n⚠️  No live data. Run: python3 data_collector.py")

    # ── NEWS BRAIN ────────────────────────────────────────────
    news = load_news()
    if news and news.get("triggered_categories"):
        print(f"\n📰 WORLD EVENTS (from {news.get('total_articles', 0)} articles):")
        print("─" * 60)
        for cat, info in list(news["triggered_categories"].items())[:4]:
            bar = "█" * min(info["count"], 8)
            print(f"  {cat:<16} {bar} ({info['count']})")

        if news.get("ai_analysis"):
            risk = news["ai_analysis"].get("overall_risk_level", "N/A")
            theme = news["ai_analysis"].get("dominant_theme", "N/A")
            risk_icon = {"LOW": "🟢", "MEDIUM": "🟡",
                         "HIGH": "🟠", "CRITICAL": "🔴"}.get(risk, "⚪")
            print(f"\n  Risk: {risk_icon} {risk}  |  Theme: {theme}")

    # ── AI PREDICTION ─────────────────────────────────────────
    analysis = load_latest()
    if analysis and analysis.get("ai_prediction"):
        pred = analysis["ai_prediction"]
        print("\n🤖 ZAI PREDICTION:")
        print("─" * 60)

        outlook = pred.get("overall_market_outlook", "N/A")
        conf = pred.get("confidence", 0)
        era = pred.get("current_era_similarity", "N/A")

        outlook_icon = {
            "BULLISH": "🟢", "BEARISH": "🔴",
            "NEUTRAL": "🟡", "VOLATILE": "🟠"
        }.get(outlook, "⚪")

        print(f"  Outlook:     {outlook_icon} {outlook}")
        print(f"  Confidence:  {'█' * (conf // 10)}{'░' * (10 - conf // 10)} {conf}%")
        print(f"  Similar to:  {era}")

        predictions = pred.get("predictions", {})
        if predictions:
            print("\n  📅 TIMELINE:")
            for period, p in predictions.items():
                d = p.get("direction", "?")
                m = p.get("magnitude", "?")
                icon = "↑" if d == "UP" else "↓" if d == "DOWN" else "→"
                print(f"    {period:<12} {icon} {d} ~{m}")

        crypto = pred.get("crypto_specific", {})
        if crypto:
            print(f"\n  🪙 CRYPTO:  {crypto.get('outlook', 'N/A')}")
            print(f"     Driver: {crypto.get('key_driver', 'N/A')}")

        signals = pred.get("key_signals", [])
        if signals:
            print("\n  ⚡ KEY SIGNALS:")
            for s in signals[:3]:
                print(f"    • {s}")

        warnings = pred.get("warning_signs", [])
        if warnings:
            print("\n  ⚠️  WARNINGS:")
            for w in warnings[:2]:
                print(f"    • {w}")

        summary = pred.get("summary", "")
        if summary:
            print(f"\n  💬 {summary[:120]}")

        sims = analysis.get("current_similarity", [])
        if sims:
            print("\n  📜 HISTORICAL SIMILARITY:")
            for s in sims[:3]:
                bar = "█" * int(s["similarity_pct"] / 10)
                print(f"    {s['crash'][:30]:<30} {bar} {s['similarity_pct']}%")

        gen_time = analysis.get("generated_at", "")
        if gen_time:
            print(f"\n  🕐 Last analysis: {gen_time[:19]}")

    else:
        print("\n⚠️  No prediction yet.")
        print("   Run: python3 correlation_engine.py")

    print("\n" + "─" * 60)
    print(f"  🔄 Tick #{tick}  |  Refresh in {UPDATE_INTERVAL}s  |  Ctrl+C = exit")
    print("─" * 60)


# ================================================================
# BACKGROUND UPDATE CYCLE
# Runs full re-analysis every 6 hours automatically
# ================================================================
def run_update_cycle():
    from data_collector import update_live_data
    from correlation_engine import (load_all_data, merge_data, find_correlations,
                                     find_lead_lag_relationships, extract_crash_patterns,
                                     compare_current_to_history, get_ai_prediction,
                                     save_analysis)

    print("\n🔄 Running full update cycle...")
    update_live_data()

    data = load_all_data()
    if data:
        df = merge_data(data)
        correlations = find_correlations(df)
        relationships = find_lead_lag_relationships(df)
        crash_patterns = extract_crash_patterns(df)
        similarities = compare_current_to_history(df, crash_patterns)
        prediction = get_ai_prediction(correlations, relationships, similarities, df)
        if prediction:
            save_analysis(correlations, relationships, crash_patterns, similarities, prediction)

    # News update too if available
    try:
        from news_brain import fetch_all_news, analyze_articles, match_to_history
        from news_brain import get_news_ai_analysis, save_news_analysis
        articles = fetch_all_news(max_feeds=10)
        if articles:
            triggered = analyze_articles(articles)
            hist_matches = match_to_history(triggered)
            ai_analysis, _ = get_news_ai_analysis(triggered, hist_matches, articles)
            save_news_analysis(triggered, hist_matches, ai_analysis, articles)
    except:
        pass


# ================================================================
# RUN
# ================================================================
if __name__ == "__main__":
    print("🚀 ZAI Dashboard starting...")

    if not os.path.exists(f"{DATA_PATH}/historical"):
        print("❌ No data found. Run first: python3 data_collector.py")
        exit()

    tick = 0
    last_analysis = 0
    ANALYSIS_INTERVAL = 21600  # 6 hours

    while True:
        try:
            display(tick)
            time.sleep(UPDATE_INTERVAL)
            tick += 1

            from data_collector import update_live_data
            update_live_data()

            if time.time() - last_analysis > ANALYSIS_INTERVAL:
                run_update_cycle()
                last_analysis = time.time()

        except KeyboardInterrupt:
            print("\n\n👋 ZAI Dashboard stopped. — Zawwar")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            time.sleep(30)
