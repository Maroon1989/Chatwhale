import os
from typing import List, Any, Dict

from utils import make_data_dict, ID_COUNTER, LOGGER
# from configs import IMG_SAVE_PATH


def keywords_part5_1(
    data: Dict[str, Any],
    what_are_components_flat_skipped_keys: List[str] = [],
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的股权结构是否合理?\""     ,
                    "股权结构"
                ]
            )
        )
        ID_COUNTER.increment()

    return results


def keywords_part5_2(
    data: Dict[str, Any],
    what_are_components_flat_skipped_keys: List[str] = [],
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的股权集中度如何，是否存在过于集中或分散的情况?\""     ,
                    "股权集中度"
                ]
            )
        )
        ID_COUNTER.increment()

    return results


def keywords_part5_3(
    data: Dict[str, Any],
    what_are_components_flat_skipped_keys: List[str] = [],
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的关联情况如何，会对经营决策带来什么影响?\""     ,
                    "业务关联 经营决策"
                ]
            )
        )
        ID_COUNTER.increment()

    return results


def keywords_part5_4(
    data: Dict[str, Any],
    what_are_components_flat_skipped_keys: List[str] = [],
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}股权结构稳定性如何，是否经常变动?\""     ,
                    "股权结构 稳定性"
                ]
            )
        )
        ID_COUNTER.increment()

    return results


def keywords_part5_5(
    data: Dict[str, Any],
    what_are_components_flat_skipped_keys: List[str] = [],
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}不同股东的风险程度？\""     ,
                    "股东 风险程度"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

