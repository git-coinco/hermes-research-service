#!/usr/bin/env python3
"""将Markdown研究报告转换为PDF产品"""

import markdown
from weasyprint import HTML
import os

BASE = "/home/cll/hermes-research-service"
PRODUCTS = os.path.join(BASE, "products")

CSS = """
@page { margin: 2cm; size: A4; }
body { font-family: sans-serif; line-height: 1.8; color: #333; }
h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
h2 { color: #34495e; margin-top: 30px; }
h3 { color: #2c3e50; }
blockquote { background: #f8f9fa; border-left: 4px solid #3498db; padding: 15px; margin: 20px 0; }
table { border-collapse: collapse; width: 100%; margin: 15px 0; }
th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
th { background-color: #3498db; color: white; }
.highlight { background: #ecf0f1; padding: 10px 15px; border-radius: 5px; }
.footer { text-align: center; color: #999; font-size: 12px; margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; }
.cover { text-align: center; padding: 100px 20px; }
.cover h1 { font-size: 36px; border: none; }
.cover .subtitle { font-size: 18px; color: #666; margin-top: 20px; }
.cover .author { font-size: 14px; color: #999; margin-top: 40px; }
"""

def md_to_pdf(md_file, pdf_file, title="研究报告"):
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
    
    full_html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body>
<div class="cover">
    <h1>{title}</h1>
    <div class="subtitle">Hermes 深度研究服务</div>
    <div class="author">本服务由 Hermes 独立完成研究<br>所有分析框架、数据和结论均由 AI 自主推导</div>
</div>
<div style="page-break-before: always;"></div>
{html_content}
<div class="footer">
    <p>Hermes 深度研究服务 | coinco@qq.com</p>
    <p>https://git-coinco.github.io/hermes-research-service/</p>
</div>
</body></html>"""
    
    HTML(string=full_html).write_pdf(pdf_file)
    print(f"✅ {os.path.basename(pdf_file)}")

# 生成PDF
cases = [
    ("cases/ai-agent-saas-customer-service.md", "products/Hermes_研究案例_AI_Agent_SaaS客服商业闭环.pdf", "研究案例：AI Agent在SaaS客服的商业闭环分析"),
    ("cases/ai-coding-tools-market-impact.md", "products/Hermes_研究案例_AI编程工具市场影响.pdf", "研究案例：AI编程工具对软件工程师市场的影响"),
]

for md, pdf, title in cases:
    md_path = os.path.join(BASE, md)
    pdf_path = os.path.join(BASE, pdf)
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    try:
        md_to_pdf(md_path, pdf_path, title)
    except Exception as e:
        print(f"❌ {os.path.basename(pdf)}: {e}")

print("\n所有PDF已生成")
