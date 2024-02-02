import os
from typing import List, Any, Dict

from utils import make_data_dict, ID_COUNTER, LOGGER
# from configs import IMG_SAVE_PATH

def keywords_example(
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

    for i in data.keys():
        if i == 'id':
            continue
        results.append(
            make_data_dict(
                cur_id=str(ID_COUNTER),
                cur_conversations=[
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.
                    \n        用户输入：
                    \n        \"公司{data[i]}的股东类型有哪些，比如个人股东、机构股东等？\""     
                    ,
                    "股东类型"
                ]
            )
        )
        ID_COUNTER.increment()

    return results
