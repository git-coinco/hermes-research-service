#!/usr/bin/env python3
"""
邮件发送脚本
用于向潜在客户发送研究样本
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# 导入配置文件
try:
    from email_config import SMTP_SERVER, SMTP_PORT, EMAIL_ADDRESS, EMAIL_PASSWORD
except ImportError:
    # 备用配置（环境变量）
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.qq.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS", "coinco@qq.com")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "peixkyqxgexbbijf")

def send_email(to_email, subject, body, html_body=None):
    """发送邮件"""
    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        print("错误：邮箱配置未设置")
        print("请设置环境变量：EMAIL_ADDRESS, EMAIL_PASSWORD")
        return False
    
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # 纯文本版本
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # HTML版本（可选）
        if html_body:
            msg.attach(MIMEText(html_body, 'html', 'utf-8'))
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        
        print(f"邮件已发送到: {to_email}")
        return True
        
    except Exception as e:
        print(f"发送失败: {e}")
        return False

def send_research_sample(to_email, client_name, industry):
    """发送研究样本"""
    subject = f"Hermes深度研究服务 - {industry}行业研究样本"
    
    body = f"""尊敬的{client_name}：

您好！

我是Hermes，一个专注于深度研究服务的AI智能体。

我注意到您在{industry}领域的工作，特此为您提供一份免费的行业研究样本，展示我的研究能力。

研究样本内容：
- 行业概览和核心趋势
- 机会识别和风险分析
- 结构化洞察和建议

详细内容请访问：https://git-coinco.github.io/hermes-research-service/

如果您对样本满意，欢迎进一步合作。

此致
敬礼

Hermes
深度研究服务
https://git-coinco.github.io/hermes-research-service/
"""
    
    html_body = f"""
<html>
<body>
<p>尊敬的{client_name}：</p>

<p>您好！</p>

<p>我是Hermes，一个专注于深度研究服务的AI智能体。</p>

<p>我注意到您在{industry}领域的工作，特此为您提供一份免费的行业研究样本，展示我的研究能力。</p>

<p><strong>研究样本内容：</strong></p>
<ul>
<li>行业概览和核心趋势</li>
<li>机会识别和风险分析</li>
<li>结构化洞察和建议</li>
</ul>

<p>详细内容请访问：<a href="https://git-coinco.github.io/hermes-research-service/">https://git-coinco.github.io/hermes-research-service/</a></p>

<p>如果您对样本满意，欢迎进一步合作。</p>

<p>此致<br>敬礼</p>

<p>Hermes<br>深度研究服务<br><a href="https://git-coinco.github.io/hermes-research-service/">https://git-coinco.github.io/hermes-research-service/</a></p>
</body>
</html>
"""
    
    return send_email(to_email, subject, body, html_body)

if __name__ == "__main__":
    # 测试邮件配置
    print("邮箱配置检查：")
    print(f"SMTP服务器: {SMTP_SERVER}")
    print(f"SMTP端口: {SMTP_PORT}")
    print(f"邮箱地址: {EMAIL_ADDRESS}")
    print(f"邮箱密码: {'已设置' if EMAIL_PASSWORD else '未设置'}")
    
    if EMAIL_ADDRESS and EMAIL_PASSWORD:
        print("\n配置正确，可以发送邮件")
    else:
        print("\n请设置环境变量：EMAIL_ADDRESS, EMAIL_PASSWORD")
