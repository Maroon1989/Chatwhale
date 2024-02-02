import os
from typing import List, Any, Dict

from utils import make_data_dict, ID_COUNTER
# from configs import IMG_SAVE_PATH

def classification_example(
    data: Dict[str, Any],
    classification_example: List[str] = [],
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

    # for first_component in data['components_flat'].keys():
    #     if first_component in what_are_components_flat_skipped_keys:
    #         continue
    #     results.append(
    #         make_data_dict(
    #             cur_id=str(ID_COUNTER),
    #             cur_conversations=[
    #                 f"图：<img>{img_file}</img>，图中这道菜的{first_component}怎么样？",
    #                 f"{data['components_flat'][first_component]}。"
    #             ]
    #         )
    #     )
    for i in data.keys():
        if i == 'id':
            continue
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"\n        请问“公司{data[i]}的股东类型有哪些，比如个人股东、机构股东等？”是属于下面哪个类别的问题?
                    \n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.
                    \n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.
                    \n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等. 
                    \n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.        
                    \n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.
                    \n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.\n        
                    ",
                    "C"
                ]
            )
        )
        ID_COUNTER.increment()

    return results
