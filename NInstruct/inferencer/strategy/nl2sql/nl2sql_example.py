import os
from typing import List, Any, Dict

from utils import make_data_dict, ID_COUNTER, LOGGER
# from configs import IMG_SAVE_PATH

def nl2sql_example(
    data: Dict[str, Any],
    what_are_components_flat_skipped_keys: List[str] = [],
    **kwargs) -> List[Any]:
    results = []
    # img_file = os.path.join(IMG_SAVE_PATH, f"{data['id']}_{str(ID_COUNTER)}_{what_are_components_flat.__name__}.jpg")

    # if os.path.isfile(img_file):
    #     LOGGER.warning(f'img has been downloaded in {what_are_components_flat.__name__}: [{img_file}]')

    # if not download_img(
    #     data['img'],
    #     img_file
    #     ):
    #     LOGGER.debug(f"img download failed, url: [{data['img']}]")
    #     log_failed_img(str(ID_COUNTER), data['img'], img_file)
    #     # return results
    # 请根据以下用户输入，输出sql代码。\n用户输入：“2021年注册地在重庆或深圳的上市公司中，平均的稀释每股收益是多少？”", "answer": "根据用户输入问题，编写sql代码如下：\n```sql\n select avg(稀释每股收益) from company_table where 年份 = '2021' and (注册地址 like '%重庆%' or 注册地址 like '%深圳%') and 稀释每股收益 is not null   \n```"
    for i in data.keys():
        if i == 'id':
            continue
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"请根据以下用户输入，输出sql代码。\n用户输入：“公司{data[i]}十大股东是哪些，他们分别持有公司多少股份?”",
                    "根据用户输入问题，编写sql代码如下：\n```sql\n select 股东名称，持股数量 from 十大股东(历史数据)  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results
