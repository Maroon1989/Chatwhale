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
                    "根据用户输入问题，编写sql代码如下：\n```sql\n select 股东名称，持股数量 from 十大股东(历史数据)  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results
