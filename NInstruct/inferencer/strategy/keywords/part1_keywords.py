import os
from typing import List, Any, Dict

from utils import make_data_dict, ID_COUNTER, LOGGER
# from configs import IMG_SAVE_PATH


def keywords_part1_1_1(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的股权结构是如何组织的？\""     ,
                    "股权结构"
                ]
            )
        )
        ID_COUNTER.increment()

    return results


def keywords_part1_2_1(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的十大股东是哪些？\""     ,
                    "十大股东"
                ]
            )
        )
        ID_COUNTER.increment()

    return results


def keywords_part1_2_2(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的十大股东中是否存在关联关系？\""     ,
                    "十大股东 关联关系"
                ]
            )
        )
        ID_COUNTER.increment()

    return results


def keywords_part1_2_3(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的十大股东分别持有公司多少股份？\""     ,
                    "十大股东 持有股份"
                ]
            )
        )
        ID_COUNTER.increment()

    return results


def keywords_part1_3_1(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的十大股东的持股比例？\""     ,
                    "十大股东 持股比例"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def keywords_part1_3_2(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的十大股东存在怎样的关联关系？\""     ,
                    "十大股东 关联关系"
                ]
            )
        )
        ID_COUNTER.increment()

    return results


def keywords_part1_4_1(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}近期股权变动情况有哪些？\""     ,
                    "股权变动"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def keywords_part1_4_2(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}近期是否有重要股东的增减？\""     ,
                    "股东 增减"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

