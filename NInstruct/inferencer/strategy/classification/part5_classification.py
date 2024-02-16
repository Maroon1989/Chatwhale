import os
from typing import List, Any, Dict

from utils import make_data_dict, ID_COUNTER
# from configs import IMG_SAVE_PATH

# 不同股东对公司的支持程度如何，是否有利于公司的发展？
def classification_shareholders_support(
    data: Dict[str, Any],
    classification_example: List[str] = [],
    **kwargs) -> List[Any]:
    results = []
    for i in data.keys():
        if i == 'id':
            continue
        if i=='stock_code':
            data[i] = str(int(data[i])).zfill(6)
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"\n        请问“不同股东对公司{data[i]}的支持程度如何，是否有利于公司的发展？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "D"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 对公司的向下控股结构进行评价，是否有助于提高公司的竞争力和发展？
def classification_evaluate_control_structure(
    data: Dict[str, Any],
    classification_example: List[str] = [],
    **kwargs) -> List[Any]:
    results = []
    for i in data.keys():
        if i == 'id':
            continue
        if i=='stock_code':
            data[i] = str(int(data[i])).zfill(6)
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"\n        请问“对公司{data[i]}的向下控股结构进行评价，是否有助于提高公司的竞争力和发展？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "E"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 评估向下控股公司的风险状况，财务状况，行业前景
def classification_down_company_risk_status(
    data: Dict[str, Any],
    classification_example: List[str] = [],
    **kwargs) -> List[Any]:
    results = []
    for i in data.keys():
        if i == 'id':
            continue
        if i=='stock_code':
            data[i] = str(int(data[i])).zfill(6)
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"\n        请问“评估公司{data[i]}向下控股公司的风险状况?”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "D"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 主要子公司行业和公司业务领域有何关联
def classification_down_company_finance_status(
    data: Dict[str, Any],
    classification_example: List[str] = [],
    **kwargs) -> List[Any]:
    results = []
    for i in data.keys():
        if i == 'id':
            continue
        if i=='stock_code':
            data[i] = str(int(data[i])).zfill(6)
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"\n        请问“评估公司{data[i]}向下控股公司的财务状况?”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "D"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 向下控股公司是否存在纠纷问题 此处包括联营合营 直接筛选诉讼仲裁内容
def classification_down_company_industry_potential(
    data: Dict[str, Any],
    classification_example: List[str] = [],
    **kwargs) -> List[Any]:
    results = []
    for i in data.keys():
        if i == 'id':
            continue
        if i=='stock_code':
            data[i] = str(int(data[i])).zfill(6)
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"\n        请问“评估公司{data[i]}向下控股公司的行业前景?”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "D"
                ]
            )
        )
        ID_COUNTER.increment()

    return results
