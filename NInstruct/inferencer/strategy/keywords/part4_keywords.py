import os
from typing import List, Any, Dict

from utils import make_data_dict, ID_COUNTER, LOGGER
# from configs import IMG_SAVE_PATH

# 主要向下控股公司所在行业是什么 持股比例>0.3
def keywords_down_industry(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的主要向下控股公司所属的行业是什么？\""     ,
                    "向下控股公司 所在行业"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 主要子公司所在的行业是什么 持股比例>0.3
def keywords_sub_industry(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}主要的子公司所在的行业是什么？\""     ,
                    "子公司 所在行业"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 主要向下控股公司行业和公司业务领域有何关联
def keywords_down_industry_conn(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的主要向下控股公司所属的行业和公司业务领域有何关联？\""     ,
                    "向下控股公司 业务关联"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 主要子公司行业和公司业务领域有何关联
def keywords_sub_industry_conn(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}主要的子公司所属的行业和公司业务领域有何关联？\""     ,
                    "子公司 业务关联"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 向下控股公司是否存在纠纷问题 此处包括联营合营 直接筛选诉讼仲裁内容
def keywords_down_public(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的向下控股公司是否存在纠纷问题？\""     ,
                    "向下控股公司 纠纷"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 子公司是否存在纠纷问题
def keywords_sub_public(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}的子公司是否存在纠纷问题？\""     ,
                    "子公司 纠纷"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 主要向下控股公司是否为海外实体
def keywords_down_abroad(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}主要的向下控股公司是否为海外实体？\""     ,
                    "向下控股公司 海外实体"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 主要子公司是否为海外实体
def keywords_sub_abroad(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"公司{data[i]}主要的子公司是否为海外实体？\""     ,
                    "子公司 海外实体"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 列举主要向下控股公司的重要财务信息
def keywords_down_financial(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"请列举公司{data[i]}主要向下控股公司的重要财务信息？\""     ,
                    "向下控股公司 财务"
                ]
            )
        )
        ID_COUNTER.increment()

    return results

# 列举主要子公司的重要财务信息
def keywords_sub_financial(
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
                    f"\n        请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词,你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.\n        用户输入：\n        \"请列举公司{data[i]}主要子公司的重要财务信息？\""     ,
                    "子公司 财务"
                ]
            )
        )
        ID_COUNTER.increment()

    return results