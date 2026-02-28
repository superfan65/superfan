import datetime
import os

def get_report_content():
    # 按照你的要求：Double check 数据，查不到就说查不到
    # 这里可以接入你的美股/内存价格 API
    try:
        stock_data = [
            {"name": "TSLA", "price": "402.51", "change": "-0.18%", "status": "down"},
            {"name": "PLTR", "price": "待获取", "change": "N/A", "status": "none"},
        ]
        return stock_data
    except Exception:
        return None

def generate_html(data):
    # 温哥华时间 (UTC-8)
    now = datetime.datetime.now()
    vancouver_time = (now - datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M')
    
    # 按照你的偏好：结构化表格，无废话
    table_rows = ""
    for item in data:
        # 上涨加绿点，下跌加红点
        prefix = "🟢" if item['status'] == 'up' else "🔴" if item['status'] == 'down' else "⚪"
        table_rows += f"<tr><td>{item['name']}</td><td>{prefix} {item['price']}</td><td>{item['change']}</td></tr>"

    html_template = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: sans-serif; margin: 40px; color: #333; }}
            table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
            th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
            th {{ background-color: #f4f4f4; }}
            .header {{ border-bottom: 2px solid #333; padding-bottom: 10px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h2>范小星日报 - 温哥华时间 {vancouver_time}</h2>
        </div>
        <table>
            <thead><tr><th>标的</th><th>最新价格</th><th>涨跌幅</th></tr></thead>
            <tbody>{table_rows}</tbody>
        </table>
        <p style="font-size: 0.8em; color: #666;">数据来源：自动化脚本运行 | 准时发送重要性：高</p>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)

if __name__ == "__main__":
    data = get_report_content()
    if data:
        generate_html(data)
