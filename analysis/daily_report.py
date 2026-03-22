# analysis/daily_report.py - 每日持倉報告生成
import pandas as pd
import yfinance as yf
from datetime import datetime

# 你的持倉
holdings = [
    {"ticker": "BCRX", "shares": 1000, "entry_price": 9.80},
    {"ticker": "02546.HK", "shares": 3000, "entry_price": 15.63}
]

def generate_report():
    report = []
    total_value = 0
    total_cost = 0

    for pos in holdings:
        ticker = pos["ticker"]
        shares = pos["shares"]
        entry = pos["entry_price"]

        current_price = 0
        error_msg = ""

        stock = yf.Ticker(ticker)
        try:
            hist = stock.history(period="1d")
            if not hist.empty:
                current_price = hist["Close"].iloc[-1]
            else:
                error_msg = "No data returned (empty DataFrame)"
        except Exception as e:
            error_msg = str(e)

        cost = shares * entry
        value = shares * current_price
        pnl = value - cost
        pnl_pct = (pnl / cost) * 100 if cost != 0 else 0

        report.append({
            "Ticker": ticker,
            "Shares": shares,
            "Entry": entry,
            "Current": round(current_price, 2),
            "Cost": round(cost, 2),
            "Value": round(value, 2),
            "P&L": round(pnl, 2),
            "P&L %": round(pnl_pct, 2),
            "Error": error_msg if error_msg else "OK"
        })

        total_cost += cost
        total_value += value

    df = pd.DataFrame(report)
    total_pnl = total_value - total_cost
    total_pnl_pct = (total_pnl / total_cost) * 100 if total_cost != 0 else 0

    today = datetime.now().strftime("%Y-%m-%d")
    md_content = f"# Daily Trade Report - {today}\n\n"
    md_content += f"**Total Cost**: ${total_cost:,.2f}\n"
    md_content += f"**Total Value**: ${total_value:,.2f}\n"
    md_content += f"**Total P&L**: ${total_pnl:,.2f} ({total_pnl_pct:.2f}%)\n\n"
    md_content += df.to_markdown(index=False)

    with open(f"reports/daily_report_{today}.md", "w") as f:
        f.write(md_content)

    print("Daily report generated!")

if __name__ == "__main__":
    generate_report()
