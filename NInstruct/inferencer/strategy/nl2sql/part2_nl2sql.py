import os
from typing import List, Any, Dict

from utils import make_data_dict, ID_COUNTER, LOGGER
# from configs import IMG_SAVE_PATH

def nl2sql_shareholder_type(
    data: Dict[str, Any],
    what_are_components_flat_skipped_keys: List[str] = [],
    **kwargs) -> List[Any]:
    results = []
    # 请根据以下用户输入，输出sql代码。\n用户输入：“2021年注册地在重庆或深圳的上市公司中，平均的稀释每股收益是多少？”", "answer": "根据用户输入问题，编写sql代码如下：\n```sql\n select avg(稀释每股收益) from company_table where 年份 = '2021' and (注册地址 like '%重庆%' or 注册地址 like '%深圳%') and 稀释每股收益 is not null   \n```"
    for i in data.keys():
        if i == 'id':
            continue
        if i=='stock_code':
            data[i] = str(int(data[i])).zfill(6)
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的股东类型有哪些，比如个人股东、机构股东等？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.统计截止日期, a.股东名称, a.持股排名, a.股东类型 FROM 十大股东 AS a JOIN 基本信息 AS b ON (a.统计截止日期=b.统计截止日期 AND a.证券代码=b.股票代码 AND (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}')) ORDER BY a.统计截止日期 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def nl2sql_shareholder_industry(
    data: Dict[str, Any],
    what_are_components_flat_skipped_keys: List[str] = [],
    **kwargs) -> List[Any]:
    results = []
    # 请根据以下用户输入，输出sql代码。\n用户输入：“2021年注册地在重庆或深圳的上市公司中，平均的稀释每股收益是多少？”", "answer": "根据用户输入问题，编写sql代码如下：\n```sql\n select avg(稀释每股收益) from company_table where 年份 = '2021' and (注册地址 like '%重庆%' or 注册地址 like '%深圳%') and 稀释每股收益 is not null   \n```"
    for i in data.keys():
        if i == 'id':
            continue
        if i=='stock_code':
            data[i] = str(int(data[i])).zfill(6)
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的股东所属的行业是什么？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.统计截止日期, a.股东名称, c.行业名称 FROM 十大股东 AS a JOIN (SELECT t.股票代码, t.股票简称, t.统计截止日期 FROM 基本信息 AS t WHERE(t.股票简称='{data[i]}' OR t.股票代码='{data[i]}' OR t.股票代码='{data[i][0:6]}')) as b ON (a.统计截止日期=b.统计截止日期 AND a.证券代码=b.股票代码) JOIN (SELECT m.中文全称, m.行业名称, m.统计截止日期 FROM 基本信息 AS m) AS c ON (a.统计截止日期=c.统计截止日期 AND a.股东名称=c.中文全称) ORDER BY a.统计截止日期 ASC; \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def nl2sql_industry(
    data: Dict[str, Any],
    what_are_components_flat_skipped_keys: List[str] = [],
    **kwargs) -> List[Any]:
    results = []
    # 请根据以下用户输入，输出sql代码。\n用户输入：“2021年注册地在重庆或深圳的上市公司中，平均的稀释每股收益是多少？”", "answer": "根据用户输入问题，编写sql代码如下：\n```sql\n select avg(稀释每股收益) from company_table where 年份 = '2021' and (注册地址 like '%重庆%' or 注册地址 like '%深圳%') and 稀释每股收益 is not null   \n```"
    for i in data.keys():
        if i == 'id':
            continue
        if i=='stock_code':
            data[i] = str(int(data[i])).zfill(6)
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}所属的行业是什么？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.统计截止日期, a.行业名称 FROM 基本信息 AS a WHERE (a.股票简称='{data[i]}' OR a.股票代码='{data[i]}' OR a.股票代码='{data[i][0:6]}') ORDER BY a.统计截止日期 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def nl2sql_shareholder_main_business(
    data: Dict[str, Any],
    what_are_components_flat_skipped_keys: List[str] = [],
    **kwargs) -> List[Any]:
    results = []
    # 请根据以下用户输入，输出sql代码。\n用户输入：“2021年注册地在重庆或深圳的上市公司中，平均的稀释每股收益是多少？”", "answer": "根据用户输入问题，编写sql代码如下：\n```sql\n select avg(稀释每股收益) from company_table where 年份 = '2021' and (注册地址 like '%重庆%' or 注册地址 like '%深圳%') and 稀释每股收益 is not null   \n```"
    for i in data.keys():
        if i == 'id':
            continue
        if i=='stock_code':
            data[i] = str(int(data[i])).zfill(6)
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}股东的主营业务是什么？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.统计截止日期, a.股东名称, c.主营业务 FROM 十大股东 AS a JOIN (SELECT t.股票代码, t.股票简称, t.统计截止日期 FROM 基本信息 AS t WHERE(t.股票简称='{data[i]}' OR t.股票代码='{data[i]}' OR t.股票代码='{data[i][0:6]}')) as b ON (a.统计截止日期=b.统计截止日期 AND a.证券代码=b.股票代码) JOIN (SELECT m.中文全称, m.主营业务, m.统计截止日期 FROM 基本信息 AS m) AS c ON (a.统计截止日期=c.统计截止日期 AND a.股东名称=c.中文全称) ORDER BY a.统计截止日期 ASC; \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def nl2sql_main_business(
    data: Dict[str, Any],
    what_are_components_flat_skipped_keys: List[str] = [],
    **kwargs) -> List[Any]:
    results = []
    # 请根据以下用户输入，输出sql代码。\n用户输入：“2021年注册地在重庆或深圳的上市公司中，平均的稀释每股收益是多少？”", "answer": "根据用户输入问题，编写sql代码如下：\n```sql\n select avg(稀释每股收益) from company_table where 年份 = '2021' and (注册地址 like '%重庆%' or 注册地址 like '%深圳%') and 稀释每股收益 is not null   \n```"
    for i in data.keys():
        if i == 'id':
            continue
        if i=='stock_code':
            data[i] = str(int(data[i])).zfill(6)
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的主营业务是什么？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.统计截止日期, a.主营业务 FROM 基本信息 AS a WHERE (a.股票简称='{data[i]}' OR a.股票代码='{data[i]}' OR a.股票代码='{data[i][0:6]}') ORDER BY a.统计截止日期 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def nl2sql_shareholder_public(
    data: Dict[str, Any],
    what_are_components_flat_skipped_keys: List[str] = [],
    **kwargs) -> List[Any]:
    results = []
    # 请根据以下用户输入，输出sql代码。\n用户输入：“2021年注册地在重庆或深圳的上市公司中，平均的稀释每股收益是多少？”", "answer": "根据用户输入问题，编写sql代码如下：\n```sql\n select avg(稀释每股收益) from company_table where 年份 = '2021' and (注册地址 like '%重庆%' or 注册地址 like '%深圳%') and 稀释每股收益 is not null   \n```"
    for i in data.keys():
        if i == 'id':
            continue
        if i=='stock_code':
            data[i] = str(int(data[i])).zfill(6)
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的股东是否存在舆情纠纷问题？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.公告日期, a.事件内容 FROM 诉讼仲裁 AS a WHERE ((a.证券简称='{data[i]}' OR a.证券代码='{data[i]}' OR a.证券代码='{data[i][0:6]}') AND (a.事件内容 LIKE '%控股股东%' OR a.涉案缘由='股东纠纷')) ORDER BY a.公告日期 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def nl2sql_shareholder_abroad(
    data: Dict[str, Any],
    what_are_components_flat_skipped_keys: List[str] = [],
    **kwargs) -> List[Any]:
    results = []
    # 请根据以下用户输入，输出sql代码。\n用户输入：“2021年注册地在重庆或深圳的上市公司中，平均的稀释每股收益是多少？”", "answer": "根据用户输入问题，编写sql代码如下：\n```sql\n select avg(稀释每股收益) from company_table where 年份 = '2021' and (注册地址 like '%重庆%' or 注册地址 like '%深圳%') and 稀释每股收益 is not null   \n```"
    for i in data.keys():
        if i == 'id':
            continue
        if i=='stock_code':
            data[i] = str(int(data[i])).zfill(6)
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的股东是否存在海外实体，如果有则持股比例是多少？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.统计截止日期, a.股东名称, c.注册具体地址, a.`持股比例(百分比)` FROM 十大股东 AS a JOIN (SELECT t.股票代码, t.股票简称, t.统计截止日期 FROM 基本信息 AS t WHERE(t.股票简称='{data[i]}' OR t.股票代码='{data[i]}' OR t.股票代码='{data[i][0:6]}')) as b ON (a.统计截止日期=b.统计截止日期 AND a.证券代码=b.股票代码) JOIN (SELECT m.中文全称, m.注册具体地址, m.统计截止日期 FROM 基本信息 AS m) AS c ON (a.统计截止日期=c.统计截止日期 AND a.股东名称=c.中文全称) ORDER BY a.统计截止日期 ASC; \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def nl2sql_shareholder_financial(
    data: Dict[str, Any],
    what_are_components_flat_skipped_keys: List[str] = [],
    **kwargs) -> List[Any]:
    results = []
    # 请根据以下用户输入，输出sql代码。\n用户输入：“2021年注册地在重庆或深圳的上市公司中，平均的稀释每股收益是多少？”", "answer": "根据用户输入问题，编写sql代码如下：\n```sql\n select avg(稀释每股收益) from company_table where 年份 = '2021' and (注册地址 like '%重庆%' or 注册地址 like '%深圳%') and 稀释每股收益 is not null   \n```"
    for i in data.keys():
        if i == 'id':
            continue
        if i=='stock_code':
            data[i] = str(int(data[i])).zfill(6)
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的股东财务状况如何？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.统计截止日期, c.股票代码, a.股东名称, d.报表类型编码, d.流动比率, d.速动比率, d.营运资金, d.利息保障倍数A, d.资产负债率, d.权益乘数, e.应收账款周转率A, e.存货周转率A, e.应付账款周转率A  FROM 十大股东 AS a JOIN (SELECT t.股票代码, t.股票简称, t.统计截止日期 FROM 基本信息 AS t WHERE(t.股票简称='{data[i]}' OR t.股票代码='{data[i]}' OR t.股票代码='{data[i][0:6]}')) as b ON (a.统计截止日期=b.统计截止日期 AND a.证券代码=b.股票代码) JOIN (SELECT t1.股票代码, t1.统计截止日期, t1.中文全称 FROM 基本信息 AS t1) AS c ON (a.统计截止日期=c.统计截止日期 AND a.股东名称=c.中文全称) JOIN 偿债能力 AS d ON (a.统计截止日期=d.统计截止日期 AND c.股票代码=d.股票代码) JOIN 经营能力 AS e ON (a.统计截止日期=e.统计截止日期 AND c.股票代码=e.股票代码 AND d.报表类型编码=e.报表类型编码) ORDER BY a.统计截止日期 ASC, d.报表类型编码 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def nl2sql_financial(
    data: Dict[str, Any],
    what_are_components_flat_skipped_keys: List[str] = [],
    **kwargs) -> List[Any]:
    results = []
    # 请根据以下用户输入，输出sql代码。\n用户输入：“2021年注册地在重庆或深圳的上市公司中，平均的稀释每股收益是多少？”", "answer": "根据用户输入问题，编写sql代码如下：\n```sql\n select avg(稀释每股收益) from company_table where 年份 = '2021' and (注册地址 like '%重庆%' or 注册地址 like '%深圳%') and 稀释每股收益 is not null   \n```"
    for i in data.keys():
        if i == 'id':
            continue
        if i=='stock_code':
            data[i] = str(int(data[i])).zfill(6)
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的财务状况如何？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT t.统计截止日期, t1.报表类型编码, t1.流动比率, t1.速动比率, t1.营运资金, t1.利息保障倍数A, t1.资产负债率, t1.权益乘数, t2.应收账款周转率A, t2.存货周转率A, t2.应付账款周转率A, t3.净资产收益率（ROE）A FROM (SELECT a.统计截止日期, a.股票代码 FROM 基本信息 AS a WHERE (a.股票简称='{data[i]}' OR a.股票代码='{data[i]}' OR a.股票代码='{data[i][0:6]}')) AS t JOIN 偿债能力 AS t1 ON (t.统计截止日期=t1.统计截止日期 AND t.股票代码=t1.股票代码) JOIN 经营能力 AS t2 ON (t.统计截止日期=t2.统计截止日期 AND t.股票代码=t2.股票代码 AND t1.报表类型编码=t2.报表类型编码) JOIN 盈利能力 AS t3 ON (t.统计截止日期=t3.统计截止日期 AND t.股票代码=t3.股票代码 AND t1.报表类型编码=t3.报表类型编码) ORDER BY t.统计截止日期 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def nl2sql_controller(
    data: Dict[str, Any],
    what_are_components_flat_skipped_keys: List[str] = [],
    **kwargs) -> List[Any]:
    results = []
    # 请根据以下用户输入，输出sql代码。\n用户输入：“2021年注册地在重庆或深圳的上市公司中，平均的稀释每股收益是多少？”", "answer": "根据用户输入问题，编写sql代码如下：\n```sql\n select avg(稀释每股收益) from company_table where 年份 = '2021' and (注册地址 like '%重庆%' or 注册地址 like '%深圳%') and 稀释每股收益 is not null   \n```"
    for i in data.keys():
        if i == 'id':
            continue
        if i=='stock_code':
            data[i] = str(int(data[i])).zfill(6)
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的实际控制人是谁，其拥有该公司的所有权比例和控制权比例分别多少？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.统计截止日期, a.股票代码, b.判断标准, b.实际控制人名称, b.实际控制人拥有上市公司所有权比例, b.实际控制人拥有上市公司控制权比例 FROM (SELECT t.股票代码, t.股票简称, t.统计截止日期 FROM 基本信息 AS t WHERE (t.股票简称='{data[i]}' OR t.股票代码='{data[i]}' OR t.股票代码='{data[i][0:6]}')) AS a JOIN 实际控制人 AS b ON (a.股票代码=b.证券代码 AND a.统计截止日期=b.统计截止日期) ORDER BY a.统计截止日期 ASC, b.判断标准 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results