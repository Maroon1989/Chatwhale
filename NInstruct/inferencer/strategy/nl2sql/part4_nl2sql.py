import os
from typing import List, Any, Dict

from utils import make_data_dict, ID_COUNTER, LOGGER
# from configs import IMG_SAVE_PATH

# 主要向下控股公司所在行业是什么 持股比例>0.3 反向查询
def nl2sql_down_industry(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}主要向下控股公司所属的行业是什么”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT t.统计截止日期, t.证券代码, b.股票简称, t.持股比例(%), b.行业名称 FROM (SELECT a.统计截止日期, a.证券代码, a.持股比例(%) FROM 十大股东 AS a JOIN 上市公司基本信息年度表 AS b ON (a.统计截止日期=b.统计截止日期 AND (a.股东名称=b.中文全称 OR a.股东名称=b.股票简称) AND (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}') AND a.持股比例(%)>30)) AS t JOIN 上市公司基本信息年度表 AS b ON (t.统计截止日期=b.统计截止日期 AND t.证券代码=b.股票代码) ORDER BY t.统计截止日期 ASC AND t.持股比例(%) DESC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 主要子公司所在的行业是什么 持股比例>0.3
def nl2sql_sub_industry(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}主要的子公司所在的行业是什么”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT t.统计截止日期, t.证券代码, b.股票简称, t.持股比例(%), b.行业名称 FROM (SELECT a.统计截止日期, a.证券代码, a.持股比例(%) FROM 十大股东 AS a JOIN 上市公司基本信息年度表 AS b ON (a.统计截止日期=b.统计截止日期 AND (a.股东名称=b.中文全称 OR a.股东名称=b.股票简称) AND (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}') AND a.持股比例(%)>30)) AS t JOIN 上市公司基本信息年度表 AS b ON (t.统计截止日期=b.统计截止日期 AND t.证券代码=b.股票代码) ORDER BY t.统计截止日期 ASC AND t.持股比例(%) DESC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

'''子公司和原公司业务领域有何关联？'''
# 业务关联表暂缺？改为文本类问题

# 向下控股公司是否存在纠纷问题 此处包括联营合营 直接筛选诉讼仲裁内容
def nl2sql_down_public(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的向下控股公司是否存在纠纷问题”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.公告日期, a.事件内容 FROM 诉讼仲裁 AS a WHERE ((a.证券简称='{data[i]}' OR a.证券代码='{data[i]}' OR a.证券代码='{data[i][0:6]}') AND ((a.事件内容 LIKE '%子公司%') OR (a.事件内容 LIKE '%联营%') OR (a.事件内容 LIKE '%合营%'))) ORDER BY a.公告日期 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 子公司是否存在纠纷问题
def nl2sql_sub_public(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的子公司是否存在纠纷问题”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT a.公告日期, a.事件内容 FROM 诉讼仲裁 AS a WHERE ((a.证券简称='{data[i]}' OR a.证券代码='{data[i]}' OR a.证券代码='{data[i][0:6]}') AND (a.事件内容 LIKE '%子公司%')) ORDER BY a.公告日期 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 主要向下控股公司是否为海外实体
def nl2sql_down_abroad(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}主要向下控股公司是否为海外实体”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT t.统计截止日期, t.证券代码, b.股票简称, t.持股比例(%), b.注册具体地址 FROM (SELECT a.统计截止日期, a.证券代码, a.持股比例(%) FROM 十大股东 AS a JOIN 上市公司基本信息年度表 AS b ON (a.统计截止日期=b.统计截止日期 AND (a.股东名称=b.中文全称 OR a.股东名称=b.股票简称) AND (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}') AND a.持股比例(%)>30)) AS t JOIN 上市公司基本信息年度表 AS b ON (t.统计截止日期=b.统计截止日期 AND t.证券代码=b.股票代码) ORDER BY t.统计截止日期 ASC AND t.持股比例(%) DESC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 主要子公司是否为海外实体
def nl2sql_sub_abroad(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}主要子公司是否为海外实体”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT t.统计截止日期, t.证券代码, b.股票简称, t.持股比例(%), b.注册具体地址 FROM (SELECT a.统计截止日期, a.证券代码, a.持股比例(%) FROM 十大股东 AS a JOIN 上市公司基本信息年度表 AS b ON (a.统计截止日期=b.统计截止日期 AND (a.股东名称=b.中文全称 OR a.股东名称=b.股票简称) AND (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}') AND a.持股比例(%)>30)) AS t JOIN 上市公司基本信息年度表 AS b ON (t.统计截止日期=b.统计截止日期 AND t.证券代码=b.股票代码) ORDER BY t.统计截止日期 ASC AND t.持股比例(%) DESC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 列举主要向下控股公司的重要财务信息
def nl2sql_down_financial(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“请列举公司{data[i]}主要向下控股公司的重要财务信息”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT t.统计截止日期, t.证券代码, b.股票简称, t.持股比例(%), t1.流动比率, t1.速动比率, t1.营运资金, t1.利息保障倍数A, t1.资产负债率, t1.权益乘数, t2.可持续增长率, t3.净资产收益率（ROE）A, t4.应收账款周转率A, t4.存货周转率A, t4.应付账款周转率A FROM (SELECT a.统计截止日期, a.证券代码, a.持股比例(%) FROM 十大股东 AS a JOIN 上市公司基本信息年度表 AS b ON (a.统计截止日期=b.统计截止日期 AND (a.股东名称=b.中文全称 OR a.股东名称=b.股票简称) AND (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}') AND a.持股比例(%)>30)) AS t JOIN 上市公司基本信息年度表 AS b ON (t.统计截止日期=b.统计截止日期 AND t.证券代码=b.股票代码) JOIN 偿债能力 AS t1 ON (t.统计截止日期=t1.统计截止日期 AND t.证券代码=t1.股票代码) JOIN 发展能力 AS t2 ON (t.统计截止日期=t2.统计截止日期 AND t.证券代码=t2.股票代码) JOIN 盈利能力 AS t3 ON (t.统计截止日期=t3.统计截止日期 AND t.证券代码=t3.股票代码) JOIN 经营能力 AS t4 ON (t.统计截止日期=t4.统计截止日期 AND t.证券代码=t4.股票代码) ORDER BY t.统计截止日期 ASC AND t.持股比例(%) DESC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 列举主要子公司的重要财务信息
def nl2sql_sub_financial(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“请列举公司{data[i]}主要子公司的重要财务信息”",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT t.统计截止日期, t.证券代码, b.股票简称, t.持股比例(%), t1.流动比率, t1.速动比率, t1.营运资金, t1.利息保障倍数A, t1.资产负债率, t1.权益乘数, t2.可持续增长率, t3.净资产收益率（ROE）A, t4.应收账款周转率A, t4.存货周转率A, t4.应付账款周转率A FROM (SELECT a.统计截止日期, a.证券代码, a.持股比例(%) FROM 十大股东 AS a JOIN 上市公司基本信息年度表 AS b ON (a.统计截止日期=b.统计截止日期 AND (a.股东名称=b.中文全称 OR a.股东名称=b.股票简称) AND (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}') AND a.持股比例(%)>30)) AS t JOIN 上市公司基本信息年度表 AS b ON (t.统计截止日期=b.统计截止日期 AND t.证券代码=b.股票代码) JOIN 偿债能力 AS t1 ON (t.统计截止日期=t1.统计截止日期 AND t.证券代码=t1.股票代码) JOIN 发展能力 AS t2 ON (t.统计截止日期=t2.统计截止日期 AND t.证券代码=t2.股票代码) JOIN 盈利能力 AS t3 ON (t.统计截止日期=t3.统计截止日期 AND t.证券代码=t3.股票代码) JOIN 经营能力 AS t4 ON (t.统计截止日期=t4.统计截止日期 AND t.证券代码=t4.股票代码) ORDER BY t.统计截止日期 ASC AND t.持股比例(%) DESC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results