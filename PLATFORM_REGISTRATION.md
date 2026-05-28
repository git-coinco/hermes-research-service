# 平台注册指南

## 1. Upwork（全球最大自由职业平台）

**注册链接**: https://www.upwork.com/freelancer/signup

**注册步骤**:
1. 访问 upwork.com → 点击 Sign Up → 选择 "Work as a Freelancer"
2. 使用 coinco@qq.com 注册
3. 填写信息:
   - First Name: Hermes
   - Last Name: AI Research
   - 国家: 选择 China
4. 选择服务类别: Sales & Marketing → Market Research
5. 技能标签: AI Market Research, Industry Analysis, Strategic Advisory, Data Analysis, Competitive Analysis
6. 工作经验: Expert
7. 个人简介:
   ```
   I am an AI research agent specializing in deep industry analysis and framework construction. My work is independently conducted by AI, with human quality oversight only.

   Services:
   - Deep industry analysis and market research
   - Framework construction for complex business problems
   - Uncertainty-aware decision support
   - Competitor analysis and strategic advisory

   Portfolio:
   - AI Agent SaaS Customer Service Business Analysis: https://git-coinco.github.io/hermes-research-service/products/Hermes_研究案例_AI_Agent_SaaS客服商业闭环.pdf
   - AI Coding Tools Market Impact Analysis: https://git-coinco.github.io/hermes-research-service/products/Hermes_研究案例_AI编程工具市场影响.pdf

   All research is independently conducted by AI, with transparent methodology and uncertainty annotations.
   ```
8. 完成邮箱验证
9. 上载两份PDF研究报告到Portfolio

**注意**: Upwork可能需要身份验证（护照），请准备好。

---

## 2. 觅游（美团旗下AI技能社区）

**官网**: https://www.meyo.com（公测中）

**注册步骤**:
1. 访问觅游官网 → 注册账号
2. 选择"开发者入驻"
3. 使用curl指令上传Agent:
   ```
   curl -X POST https://api.meyo.com/agents/deploy \
     -H "Authorization: Bearer YOUR_TOKEN" \
     -d '{"name": "Hermes深度研究", "description": "AI驱动的深度行业研究与框架构建服务"}'
   ```
4. 上传技能:
   - 技能名称: AI行业深度研究与框架构建
   - 技能描述: 输入行业关键词，获得深度研究框架、市场分析和不确定性标注
   - 定价: 基础分析50元/次，深度研究200元/次，完整报告500元/次

**注意**: 觅游公测期间可能有特殊入驻流程，需关注官方公告。

---

## 3. Coze/扣子（字节旗下AI应用开发平台）

**官网**: https://www.coze.cn

**注册步骤**:
1. 访问 coze.cn → 点击注册
2. 使用手机号或邮箱注册
3. 进入"工作空间" → 创建Bot
4. Bot名称: Hermes深度研究助手
5. Bot描述: 输入行业关键词，获得AI驱动的深度研究框架和市场分析
6. 人设与回复逻辑:
   ```
   你是一个深度研究助手，擅长在信息不完整的条件下构建分析框架。
   当用户提供行业关键词时，你应该：
   1. 构建该行业的研究问题树（至少3层、10个子问题）
   2. 分析市场机会和风险
   3. 标注不确定性
   4. 给出初步判断和修正信号
   ```
7. 部署Bot → 选择"技能商店"发布
8. 定价: 免费试用，高级分析付费

**注意**: Coze支持通过GitHub链接创建Skill，可以将研究报告作为知识库上传。

---

*最后更新：2026年5月27日*
