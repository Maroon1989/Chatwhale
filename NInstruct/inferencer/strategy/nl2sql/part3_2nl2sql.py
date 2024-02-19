import os
from typing import List, Any, Dict

from utils import make_data_dict, ID_COUNTER, LOGGER
# from configs import IMG_SAVE_PATH

def part3_2nl2sql(
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
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}的主要向下控股公司是哪些，分别持有它们多少股份？”",
                    "根据用户输入问题，编写sql代码如下：\n```sql\n SELECT t.统计截止日期, t.证券代码, b.股票简称, t.持股比例(%) FROM (SELECT a.统计截止日期, a.证券代码, a.持股比例(%) FROM 十大股东 AS a JOIN 上市公司基本信息年度表 AS b ON (a.统计截止日期=b.统计截止日期 AND (a.股东名称=b.中文全称 OR a.股东名称=b.股票简称) AND (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}') AND a.持股比例(%)>30)) AS t JOIN 上市公司基本信息年度表 AS b ON (t.统计截止日期=b.统计截止日期 AND t.证券代码=b.股票代码) ORDER BY t.统计截止日期 ASC AND t.持股比例(%) DESC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results
