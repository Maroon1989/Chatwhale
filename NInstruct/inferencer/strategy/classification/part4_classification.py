import os
from typing import List, Any, Dict

from utils import make_data_dict, ID_COUNTER
# from configs import IMG_SAVE_PATH

# 主要向下控股公司所在行业是什么 持股比例>0.3
def classification_down_industry(
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
                    f"\n        请问“公司{data[i]}的主要向下控股公司所属的行业是什么？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 主要子公司所在的行业是什么 持股比例>0.3
def classification_sub_industry(
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
                    f"\n        请问“公司{data[i]}的主要子公司所在的行业是什么？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 主要向下控股公司行业和公司业务领域有何关联
def classification_down_industry_conn(
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
                    f"\n        请问“公司{data[i]}的主要向下控股公司所属的行业和公司业务领域有何关联？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 主要子公司行业和公司业务领域有何关联
def classification_sub_industry_conn(
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
                    f"\n        请问“公司{data[i]}的主要子公司所属的行业和公司业务领域有何关联？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 向下控股公司是否存在纠纷问题 此处包括联营合营 直接筛选诉讼仲裁内容
def classification_down_public(
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
                    f"\n        请问“公司{data[i]}的向下控股公司是否存在纠纷问题？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 子公司是否存在纠纷问题
def classification_sub_public(
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
                    f"\n        请问“公司{data[i]}的子公司是否存在纠纷问题？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 主要向下控股公司是否为海外实体
def classification_down_abroad(
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
                    f"\n        请问“公司{data[i]}主要的向下控股公司是否为海外实体？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 主要子公司是否为海外实体
def classification_sub_abroad(
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
                    f"\n        请问“公司{data[i]}主要的子公司是否为海外实体？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 列举主要向下控股公司的重要财务信息
def classification_down_financial(
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
                    f"\n        请问“请列举公司{data[i]}主要向下控股公司的重要财务信息？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 列举主要子公司的重要财务信息
def classification_sub_financial(
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
                    f"\n        请问“请列举公司{data[i]}主要子公司的重要财务信息？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results