import os
from typing import List, Any, Dict

from utils import make_data_dict, ID_COUNTER, LOGGER
# from configs import IMG_SAVE_PATH

def nl2sql_part1_1_1(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的股权结构是如何组织的？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.统计截止日期, a.股东名称, a.持股排名, a.`持股比例(百分比)`, a.股份性质 FROM 十大股东 AS a JOIN 基本信息 AS b ON (a.统计截止日期=b.统计截止日期 AND a.证券代码=b.股票代码 AND (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}')) ORDER BY a.统计截止日期 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def nl2sql_part1_2_1(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的十大股东是哪些？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.统计截止日期, a.股东名称, a.持股排名, a.`持股比例(百分比)` FROM 十大股东 AS a JOIN 基本信息 AS b ON (a.统计截止日期=b.统计截止日期 AND a.证券代码=b.股票代码 AND (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}')) ORDER BY a.统计截止日期 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def nl2sql_part1_2_2(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的十大股东分别持有公司多少股份？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.统计截止日期, a.股东名称, a.持股排名, a.`持股比例(百分比)` FROM 十大股东 AS a JOIN 基本信息 AS b ON (a.统计截止日期=b.统计截止日期 AND a.证券代码=b.股票代码 AND (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}')) ORDER BY a.统计截止日期 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def nl2sql_part1_2_3(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的十大股东的持股比例？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.统计截止日期, a.股东名称, a.持股排名, a.`持股比例(百分比)` FROM 十大股东 AS a JOIN 基本信息 AS b ON (a.统计截止日期=b.统计截止日期 AND a.证券代码=b.股票代码 AND (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}')) ORDER BY a.统计截止日期 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def nl2sql_part1_3_1(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的十大股东中是否存在关联关系？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.统计截止日期, a.股东名称, c.公告日期, c.关联交易事项, c.交易日期, c.交易期限, c.交易内容 FROM 十大股东 AS a JOIN 基本信息 AS b ON (a.统计截止日期=b.统计截止日期 AND a.证券代码=b.股票代码 AND (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}')) JOIN 关联交易 AS c ON (a.证券代码=c.证券代码 AND a.统计截止日期=c.统计截止日期 AND a.股东名称=c.关联方) ORDER BY a.统计截止日期 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def nl2sql_part1_3_2(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的十大股东存在怎样的关联关系？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.统计截止日期, a.股东名称, c.公告日期, c.关联交易事项, c.交易日期, c.交易期限, c.交易内容 FROM 十大股东 AS a JOIN 基本信息 AS b ON (a.统计截止日期=b.统计截止日期 AND a.证券代码=b.股票代码 AND (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}')) JOIN 关联交易 AS c ON (a.证券代码=c.证券代码 AND a.统计截止日期=c.统计截止日期 AND a.股东名称=c.关联方) ORDER BY a.统计截止日期 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def nl2sql_part1_4_1(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}近期股权变动情况有哪些？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT t.统计截止日期, a.第一次公告日期, a.股份增持方, a.股份减持方, a.本次变动数量, a.`本次变动数量占总股本的比例(百分比)` FROM 股权变更 AS a JOIN (SELECT b.股票代码, b.股票简称, b.统计截止日期 FROM 基本信息 AS b WHERE (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}')) AS t ON (a.证券代码=t.股票代码 AND SUBSTR(a.第一次公告日期,1,4)=SUBSTR(t.统计截止日期,1,4)) ORDER BY a.第一次公告日期 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def nl2sql_part1_4_2(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}近期是否有重要股东的增减？”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT t.统计截止日期, a.第一次公告日期, a.股份增持方, a.股份减持方, a.本次变动数量, a.`本次变动数量占总股本的比例(百分比)` FROM 股权变更 AS a JOIN (SELECT b.股票代码, b.股票简称, b.统计截止日期 FROM 基本信息 AS b WHERE (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}')) AS t ON (a.证券代码=t.股票代码 AND SUBSTR(a.第一次公告日期,1,4)=SUBSTR(t.统计截止日期,1,4)) ORDER BY a.第一次公告日期 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results