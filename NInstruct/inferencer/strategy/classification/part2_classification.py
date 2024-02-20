import os
from typing import List, Any, Dict

from utils import make_data_dict, ID_COUNTER
# from configs import IMG_SAVE_PATH

def classification_shareholder_type(
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
                    f"\n        请问“公司{data[i]}的股东类型有哪些，比如个人股东、机构股东等？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def classification_shareholder_industry(
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
                    f"\n        请问“公司{data[i]}的股东所属的行业是什么？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def classification_industry(
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
                    f"\n        请问“公司{data[i]}所属的行业是什么？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "A"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def classification_shareholder_main_business(
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
                    f"\n        请问“公司{data[i]}股东的主营业务是什么？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def classification_main_business(
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
                    f"\n        请问“公司{data[i]}的主营业务是什么？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "A"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def classification_shareholder_public(
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
                    f"\n        请问“公司{data[i]}的股东是否存在舆情纠纷问题？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def classification_shareholder_abroad(
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
                    f"\n        请问“公司{data[i]}的股东是否存在海外实体，如果有则持股比例是多少？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def classification_shareholder_financial(
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
                    f"\n        请问“公司{data[i]}的股东财务状况如何？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def classification_financial(
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
                    f"\n        请问“公司{data[i]}的财务状况如何？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "B"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def classification_controller(
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
                    f"\n        请问“公司{data[i]}的实际控制人是谁，其拥有该公司的所有权比例和控制权比例分别多少？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def classification_shareholder_main_business_conn(
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
                    f"\n        请问“公司{data[i]}的股东主营业务和公司业务领域有何关联？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "D"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def classification_industry_status(
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
                    f"\n        请问“公司{data[i]}在所属行业中的地位如何？”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.",
                    "E"
                ]
            )
        )
        ID_COUNTER.increment()

    return results