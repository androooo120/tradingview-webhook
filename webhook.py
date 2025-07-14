from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "INSERISCI_IL_TUO_TOKEN"
CHAT_ID = "INSERISCI_LA_TUA_CHAT_ID"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    message = f"""
🔔 *Segnale TradingView*
🧭 Azione: {data.get("action")}
📈 Simbolo: {data.get("symbol")}
🎯 Entry: {data.get("entry")}
📉 SL: {data.get("sl")}
📍 BE: {data.get("be_trigger")}
🧲 Trailing: {data.get("trail_trigger")}
"""

    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    )

    return "ok", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
