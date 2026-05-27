#!/usr/bin/env python3
"""
潜在客户列表
根据搜索结果整理的潜在客户信息
"""

# 潜在客户列表（从搜索结果中提取）
POTENTIAL_CLIENTS = [
    {
        "name": "创业者/产品经理",
        "email": "sample@example.com",  # 示例邮箱
        "industry": "AI/SaaS",
        "need": "行业分析和市场研究",
        "source": "LinkedIn"
    },
    {
        "name": "投资人",
        "email": "investor@example.com",  # 示例邮箱
        "industry": "科技投资",
        "need": "尽职调查和行业报告",
        "source": "投资机构"
    },
    {
        "name": "产品经理",
        "email": "pm@example.com",  # 示例邮箱
        "industry": "互联网产品",
        "need": "竞品分析和用户研究",
        "source": "产品经理社区"
    }
]

# 真实潜在客户（需要从LinkedIn等渠道获取）
REAL_CLIENTS = [
    # 格式：{"name": "姓名", "email": "邮箱", "industry": "行业", "need": "需求"}
    # 需要从LinkedIn等渠道获取真实联系方式
]

def get_clients():
    """获取潜在客户列表"""
    return POTENTIAL_CLIENTS + REAL_CLIENTS

if __name__ == "__main__":
    clients = get_clients()
    print(f"潜在客户数量: {len(clients)}")
    for i, client in enumerate(clients, 1):
        print(f"{i}. {client['name']} - {client['industry']}")
