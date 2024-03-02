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
                    f"你是一名Mysql数据库开发人员，精通Mysql数据库sql代码编写，你需要根据已知表名、字段名和用户输入的问题编写sql代码\n表名：偿债能力\n字段名：[股票代码,股票简称,统计截止日期,报表类型编码,流动比率,速动比率,营运资金,利息保障倍数A,资产负债率,权益乘数]\n表名：盈利能力\n字段名：[股票代码,股票简称,统计截止日期,报表类型编码,净资产收益率（ROE）A]\n表名：经营能力\n字段名：[股票代码,股票简称,统计截止日期,报表类型编码,应收账款周转率A,存货周转率A,应付账款周转率A]\n表名：十大股东\n字段名：[证券代码,统计截止日期,股东名称,持股排名,持股数量,持股比例(百分比),股东类型]\n表名：实际控制人\n字段名：[证券代码,统计截止日期,判断标准,实际控制人名称,实际控制人拥有上市公司所有权比例,实际控制人拥有上市公司控制权比例]\n表名：股权变更\n字段名：[证券代码,股份增持方,股份减持方,第一次公告日期,本次变动数量,本次变动数量占总股本的比例(百分比)]\n表名：基本信息\n字段名：[股票代码,股票简称,统计截止日期,行业名称,注册具体地址,公司办公地址,中文全称,公司成立日期,首次上市日期,所属省份,所属城市,主营业务]\n表名：关联交易\n字段名：[证券代码,统计截止日期,公告日期,关联交易事项,交易日期,交易期限,交易内容]\n表名：诉讼仲裁\n字段名：[证券代码,证券简称,公告日期,事件内容] \n注意对问题中的中文数字（xx亿、xx千万、xx万）进行阿拉伯数字转换，如：一个亿、一亿转换为100000000，一千万转换为10000000，两千万转换为20000000，一百万转换为1000000，五千万转换为50000000\n要求sql代码中的字段名必须是已知字段名，不得新增字段名\n\n示例模板：\n\"\"\"\n用户输入：在北京注册的上市公司中，2020年净资产收益率最高的十家公司有哪些，分别多少？\n\nsql如下：\n```sql\n SELECT a.股票代码, a.股票简称, a.净资产收益率（ROE）A FROM 盈利能力 AS a JOIN 基本信息 AS b ON (b.统计截止日期>='2020-01-01' AND b.统计截止日期<='2020-12-31' AND b.注册具体地址 LIKE '%北京%' AND a.股票代码=b.股票代码 AND a.股票简称=b.股票简称 AND a.统计截止日期=b.统计截止日期) ORDER BY 净资产收益率（ROE）A DESC LIMIT 10; \n```\n\n用户输入：注册地在上海或广州的公司中，2020年营运资金超过五千万的公司有几家？\n\nsql如下：\n```sql\n SELECT COUNT(1) FROM 偿债能力 AS a JOIN 基本信息 AS b ON (b.统计截止日期>='2020-01-01' AND b.统计截止日期<='2020-12-31' AND (b.注册具体地址 LIKE '%上海%' OR b.注册具体地址 LIKE '%广州%') AND a.营运资金>'50000000' AND a.股票代码=b.股票代码 AND a.股票简称=b.股票简称 AND a.统计截止日期=b.统计截止日期); \n``` \"\"\"\n请根据以下用户输入，输出sql代码。\n用户输入：公司{data[i]}的向下控股公司是哪些，分别持有它们多少股份？",
                    f"根据用户输入问题，编写sql代码如下：\n```sql\n SELECT t.统计截止日期, t.证券代码, b.股票简称, t.`持股比例(百分比)` FROM (SELECT a.统计截止日期, a.证券代码, a.`持股比例(百分比)` FROM 十大股东 AS a JOIN 基本信息 AS b ON (a.统计截止日期=b.统计截止日期 AND (a.股东名称=b.中文全称 OR a.股东名称=b.股票简称) AND (b.股票简称='{data[i]}' OR b.股票代码='{data[i]}' OR b.股票代码='{data[i][0:6]}'))) AS t JOIN 基本信息 AS b ON (t.统计截止日期=b.统计截止日期 AND t.证券代码=b.股票代码) ORDER BY t.统计截止日期 ASC, t.证券代码 ASC;  \n```"
                ]
            )
        )
        ID_COUNTER.increment()

    return results
