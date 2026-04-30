"""
Anteroom Data Model - Intelligence Terminal

Terminal dashboard for live market data, world-event signals, historical similarity,
and optional scenario summaries.
"""

import json
import os
import time
from datetime import datetime

from config import DATA_PATH, UPDATE_INTERVAL


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def load_json(path):
    try:
        with open(path, encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return None


def load_latest():
    return load_json(f"{DATA_PATH}/predictions/latest.json")


def load_live():
    return load_json(f"{DATA_PATH}/live/latest.json")


def load_news():
    return load_json(f"{DATA_PATH}/news/latest.json")


def render_header(tick):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    spin = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"][tick % 10]
    print("╔══════════════════════════════════════════════════════════╗")
    print("║        ANTEROOM DATA MODEL — INTELLIGENCE TERMINAL       ║")
    print(f"║                    {now}                  ║")
    print(f"║              {spin} Live research dashboard              ║")
    print("╚══════════════════════════════════════════════════════════╝")


def render_live_markets():
    live = load_live()
    if not live:
        print("\n⚠️  No live market snapshot found. Run: python3 data_collector.py")
        return

    print("\n📊 LIVE MARKETS")
    print("─" * 60)
    items = [
        ("S&P 500", live.get("sp500")),
        ("NASDAQ", live.get("nasdaq")),
        ("Gold", live.get("gold")),
        ("Oil (WTI)", live.get("oil")),
        ("VIX", live.get("vix")),
        ("Bitcoin", live.get("bitcoin")),
        ("Ethereum", live.get("ethereum")),
    ]
    for name, data in items:
        if data:
            price = data.get("price", 0)
            change = data.get("change_pct", 0)
            arrow = "↑" if change > 0 else "↓"
            sign = "+" if change > 0 else ""
            print(f"  {name:<12} ${price:>12,.2f}   {arrow} {sign}{change:.2f}%")


def render_world_events():
    news = load_news()
    if not news or not news.get("triggered_categories"):
        return

    print(f"\n📰 WORLD EVENT SIGNALS ({news.get('total_articles', 0)} articles)")
    print("─" * 60)
    for category, info in list(news["triggered_categories"].items())[:4]:
        bar = "█" * min(info.get("count", 0), 8)
        print(f"  {category:<16} {bar} ({info.get('count', 0)})")

    analysis = news.get("ai_analysis") or {}
    if analysis:
        risk = analysis.get("overall_risk_level", "N/A")
        theme = analysis.get("dominant_theme", "N/A")
        icon = {"LOW": "🟢", "MEDIUM": "🟡", "HIGH": "🟠", "CRITICAL": "🔴"}.get(risk, "⚪")
        print(f"\n  Risk: {icon} {risk}  |  Theme: {theme}")


def render_scenario_summary():
    analysis = load_latest()
    if not analysis or not analysis.get("ai_prediction"):
        print("\n⚠️  No scenario summary found. Run: python3 correlation_engine.py")
        return

    summary = analysis["ai_prediction"]
    print("\n🤖 SCENARIO SUMMARY")
    print("─" * 60)

    outlook = summary.get("overall_market_outlook", "N/A")
    confidence = int(summary.get("confidence", 0) or 0)
    era = summary.get("current_era_similarity", "N/A")
    icon = {"BULLISH": "🟢", "BEARISH": "🔴", "NEUTRAL": "🟡", "VOLATILE": "🟠"}.get(outlook, "⚪")

    print(f"  Outlook:     {icon} {outlook}")
    print(f"  Confidence:  {'█' * (confidence // 10)}{'░' * (10 - confidence // 10)} {confidence}%")
    print(f"  Similar to:  {era}")

    predictions = summary.get("predictions", {})
    if predictions:
        print("\n  📅 RESEARCH HORIZONS")
        for period, item in predictions.items():
            direction = item.get("direction", "?")
            magnitude = item.get("magnitude", "?")
            arrow = "↑" if direction == "UP" else "↓" if direction == "DOWN" else "→"
            print(f"    {period:<12} {arrow} {direction} ~{magnitude}")

    signals = summary.get("key_signals", [])
    if signals:
        print("\n  ⚡ KEY SIGNALS")
        for signal in signals[:3]:
            print(f"    • {signal}")

    text = summary.get("summary", "")
    if text:
        print(f"\n  💬 {text[:140]}")

    similarities = analysis.get("current_similarity", [])
    if similarities:
        print("\n  📜 HISTORICAL SIMILARITY")
        for item in similarities[:3]:
            bar = "█" * int(item.get("similarity_pct", 0) / 10)
            print(f"    {item['crash'][:30]:<30} {bar} {item.get('similarity_pct', 0)}%")

    generated_at = analysis.get("generated_at", "")
    if generated_at:
        print(f"\n  🕐 Last analysis: {generated_at[:19]}")


def display(tick=0):
    clear()
    render_header(tick)
    render_live_markets()
    render_world_events()
    render_scenario_summary()
    print("\n" + "─" * 60)
    print(f"  🔄 Tick #{tick}  |  Refresh in {UPDATE_INTERVAL}s  |  Ctrl+C = exit")
    print("─" * 60)


def run_update_cycle():
    from data_collector import update_live_data
    from correlation_engine import (
        compare_current_to_history,
        extract_crash_patterns,
        find_correlations,
        find_lead_lag_relationships,
        get_ai_prediction,
        load_all_data,
        merge_data,
        save_analysis,
    )

    print("\n🔄 Running scheduled update cycle...")
    update_live_data()

    data = load_all_data()
    if data:
        frame = merge_data(data)
        correlations = find_correlations(frame)
        relationships = find_lead_lag_relationships(frame)
        crash_patterns = extract_crash_patterns(frame)
        similarities = compare_current_to_history(frame, crash_patterns)
        prediction = get_ai_prediction(correlations, relationships, similarities, frame)
        save_analysis(correlations, relationships, crash_patterns, similarities, prediction)

    try:
        from news_brain import analyze_articles, fetch_all_news, get_news_ai_analysis, match_to_history, save_news_analysis

        articles = fetch_all_news(max_feeds=10)
        if articles:
            triggered = analyze_articles(articles)
            historical = match_to_history(triggered)
            news_summary, _source = get_news_ai_analysis(triggered, historical, articles)
            save_news_analysis(triggered, historical, news_summary, articles)
    except Exception:
        pass


if __name__ == "__main__":
    print("🚀 Starting Anteroom Data Model dashboard...")

    if not os.path.exists(f"{DATA_PATH}/historical"):
        print("❌ Historical data not found. Run first: python3 data_collector.py")
        raise SystemExit(1)

    tick = 0
    last_analysis = 0
    analysis_interval = 21600

    while True:
        try:
            display(tick)
            time.sleep(UPDATE_INTERVAL)
            tick += 1

            from data_collector import update_live_data
            update_live_data()

            if time.time() - last_analysis > analysis_interval:
                run_update_cycle()
                last_analysis = time.time()

        except KeyboardInterrupt:
            print("\n\n👋 Dashboard stopped.")
            break
        except Exception as exc:
            print(f"\n❌ Dashboard error: {exc}")
            time.sleep(30)
