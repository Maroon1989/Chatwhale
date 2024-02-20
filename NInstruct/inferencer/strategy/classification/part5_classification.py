import os
from typing import List, Any, Dict

from utils import make_data_dict, ID_COUNTER
# from configs import IMG_SAVE_PATH
#评价公司的股权结构是否合理?
def part5_1_evaluate_structure(
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
                    f"\n        请问“公司{data[i]}的股权结构是否合理?”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "E"
                ]
            )
        )
        ID_COUNTER.increment()


    return results
#公司的股权集中度如何，是否存在过于集中或分散的情况?
def part5_2_ownership_con(
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
                    f"\n        请问“公司{data[i]}的股权集中度如何，是否存在过于集中或分散的情况?”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "E"
                ]
            )
        )
        ID_COUNTER.increment()


    return results

#公司的关联情况如何，会对经营决策带来什么影响?
def part5_3_com_connection(
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
                    f"\n        请问“公司{data[i]}的关联情况如何，会对经营决策带来什么影响?”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "D"
                ]
            )
        )
        ID_COUNTER.increment()


    return results

#股权结构稳定性如何，是否经常变动?
def part5_4_ownership_stable(
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
                    f"\n        请问“公司{data[i]}股权结构稳定性如何，是否经常变动?”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "E"
                ]
            )
        )
        ID_COUNTER.increment()


    return results
#评估不同股东的风险程度?
def part5_5_risk(
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
                    f"\n        请问“公司{data[i]}不同股东的风险程度？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "E"
                ]
            )
        )
        ID_COUNTER.increment()


    return results