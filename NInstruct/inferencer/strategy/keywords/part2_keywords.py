import os
from typing import List, Any, Dict

from utils import make_data_dict, ID_COUNTER, LOGGER
# from configs import IMG_SAVE_PATH

def keywords_shareholder_type(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的股东类型有哪些，比如个人股东、机构股东等？\""     ,
                    "股东类型"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def keywords_shareholder_industry(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的股东所属的行业是什么？\""     ,
                    "股东 所属行业"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def keywords_shareholder_public(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的股东是否存在舆情纠纷问题？\""     ,
                    "股东 纠纷"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def keywords_industry(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}所属的行业是什么？\""     ,
                    "所属行业"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def keywords_public(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}是否存在舆情纠纷问题？\""     ,
                    "纠纷"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def keywords_shareholder_abroad(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的股东是否存在海外实体，如果有则持股比例多少？\""     ,
                    "股东 海外实体 持股比例"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def keywords_shareholder_financial(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}股东的财务状况如何？\""     ,
                    "股东 财务"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def keywords_financial(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的财务状况如何？\""     ,
                    "财务"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def keywords_controller(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的实际控制人是谁，其拥有该公司的所有权和控制权分别为多少？\""     ,
                    "实际控制人 所有权 控制权"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def keywords_shareholder_industry_conn(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}股东的主营业务和公司业务领域有何关联？\""     ,
                    "股东 业务关联"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

def keywords_industry_status(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}在所属行业中的地位如何？\""     ,
                    "行业地位"
                ]
            )
        )
        ID_COUNTER.increment()

    return results