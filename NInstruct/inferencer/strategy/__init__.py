from .classification.classification_example import classification_example
from .keywords.keywords_example import keywords_example
from .nl2sql.nl2sql_example import nl2sql_example
from .classification.part1_classification import *
from .classification.part2_classification import *
from .classification.part3_1classification import part3_1classification
from .classification.part3_2classification import part3_2classification
from .classification.part4_classification import *
from .classification.part5_classification import *
from .classification.part6_classification import *
from .classification.oversea_classification import oversea_classification
from .keywords.part1_keywords import *
from .keywords.part2_keywords import *
from .keywords.part3_1keywords import part3_1keywords
from .keywords.part3_2keywords import part3_2keywords
from .keywords.part4_keywords import *
from .keywords.part5_keywords import *
from .keywords.part6_keywords import *
from .keywords.oversea_keywords import oversea_keywords
from .nl2sql.part1_nl2sql import *
from .nl2sql.part2_nl2sql import *
from .nl2sql.part3_1nl2sql import part3_1nl2sql
from .nl2sql.part3_2nl2sql import part3_2nl2sql
from .nl2sql.oversea_nl2sql import oversea_nl2sql
from .nl2sql.part4_nl2sql import *





STRATEGIES = {
    # 'classification_example': {'func':classification_example,'type':'classification'},
    'part1_1_1classification':{'func':part1_1_1classification,'type':'classification'},
    'part1_2_1classification':{'func':part1_2_1classification,'type':'classification'},
    'part1_2_2classification':{'func':part1_2_2classification,'type':'classification'},
    'part1_2_3classification':{'func':part1_2_3classification,'type':'classification'},
    'part1_3_1classification':{'func':part1_3_1classification,'type':'classification'},
    'part1_3_2classification':{'func':part1_3_2classification,'type':'classification'},
    'part1_4_1classification':{'func':part1_4_1classification,'type':'classification'},
    'part1_4_2classification':{'func':part1_4_2classification,'type':'classification'},
    'part2_classification_shareholder_type':{'func':classification_shareholder_type,'type':'classification'},
    'part2_classification_shareholder_industry':{'func':classification_shareholder_industry,'type':'classification'},
    'part2_classification_industry':{'func':classification_industry,'type':'classification'},
    'part2_classification_shareholder_main_business':{'func':classification_shareholder_main_business,'type':'classification'},
    'part2_classification_main_business':{'func':classification_main_business,'type':'classification'},
    'part2_classification_shareholder_public':{'func':classification_shareholder_public,'type':'classification'},
    'part2_classification_shareholder_abroad':{'func':classification_shareholder_abroad,'type':'classification'},
    'part2_classification_shareholder_financial':{'func':classification_shareholder_financial,'type':'classification'},
    'part2_classification_financial':{'func':classification_financial,'type':'classification'},
    'part2_classification_controller':{'func':classification_controller,'type':'classification'},
    'part2_classification_shareholder_main_business_conn':{'func':classification_shareholder_main_business_conn,'type':'classification'},
    'part2_classification_industry_status':{'func':classification_industry_status,'type':'classification'},
    'part3_1classification':{'func':part3_1classification,'type':'classification'},
    'part3_1classification':{'func':part3_1classification,'type':'classification'},
    'part3_2classification':{'func':part3_2classification,'type':'classification'},
    'part4_classification_down_industry':{'func':classification_down_industry,'type':'classification'},
    'part4_classification_sub_industry':{'func':classification_sub_industry,'type':'classification'},
    'part4_classification_down_industry_conn':{'func':classification_down_industry_conn,'type':'classification'},
    'part4_classification_sub_industry_conn':{'func':classification_sub_industry_conn,'type':'classification'},
    'part4_classification_down_public':{'func':classification_down_public,'type':'classification'},
    'part4_classification_sub_public':{'func':classification_sub_public,'type':'classification'},
    'part4_classification_down_abroad':{'func':classification_down_abroad,'type':'classification'},
    'part4_classification_sub_abroad':{'func':classification_sub_abroad,'type':'classification'},
    'part4_classification_down_financial':{'func':classification_down_financial,'type':'classification'},
    'part4_classification_sub_financial':{'func':classification_sub_financial,'type':'classification'},
    'part5_classification_evaluate_structure':{'func':part5_1_evaluate_structure,'type':'classification'},
    'part5_classification_ownership_con':{'func':part5_2_ownership_con,'type':'classification'},
    'part5_classification_com_connection':{'func':part5_3_com_connection,'type':'classification'},
    'part5_classification_ownership_stable':{'func':part5_4_ownership_stable,'type':'classification'},
    'part5_classification_risk':{'func':part5_5_risk,'type':'classification'},
    'part6_classification_shareholders_support':{'func':classification_shareholders_support,'type':'classification'},
    'part6_classification_evaluate_control_structure':{'func':classification_evaluate_control_structure,'type':'classification'},
    'part6_classification_down_company_risk_status':{'func':classification_down_company_risk_status,'type':'classification'},
    'part6_classification_down_company_finance_status':{'func':classification_down_company_finance_status,'type':'classification'},
    'part6_classification_down_company_industry_potential':{'func':classification_down_company_industry_potential,'type':'classification'},
    'oversea_classification':{'func':oversea_classification,'type':'classification'},

    # 'keywords_example':{'func':keywords_example,'type':'keywords'},
    'part1_1_1keywords':{'func':keywords_part1_1_1,'type':'keywords'},
    'part1_2_1keywords':{'func':keywords_part1_2_1,'type':'keywords'},
    'part1_2_2keywords':{'func':keywords_part1_2_2,'type':'keywords'},
    'part1_2_3keywords':{'func':keywords_part1_2_3,'type':'keywords'},
    'part1_3_1keywords':{'func':keywords_part1_3_1,'type':'keywords'},
    'part1_3_2keywords':{'func':keywords_part1_3_2,'type':'keywords'},
    'part1_4_1keywords':{'func':keywords_part1_4_1,'type':'keywords'},
    'part1_4_2keywords':{'func':keywords_part1_4_2,'type':'keywords'},
    'part2_keywords_shareholder_type':{'func':keywords_shareholder_type,'type':'keywords'},
    'part2_keywords_shareholder_industry':{'func':keywords_shareholder_industry,'type':'keywords'},
    'part2_keywords_industry':{'func':keywords_industry,'type':'keywords'},
    'part2_keywords_shareholder_main_business':{'func':keywords_shareholder_main_business,'type':'keywords'},
    'part2_keywords_main_business':{'func':keywords_main_business,'type':'keywords'},
    'part2_keywords_shareholder_public':{'func':keywords_shareholder_public,'type':'keywords'},
    'part2_keywords_shareholder_abroad':{'func':keywords_shareholder_abroad,'type':'keywords'},
    'part2_keywords_shareholder_financial':{'func':keywords_shareholder_financial,'type':'keywords'},
    'part2_keywords_financial':{'func':keywords_financial,'type':'keywords'},
    'part2_keywords_controller':{'func':keywords_controller,'type':'keywords'},
    'part2_keywords_shareholder_main_business_conn':{'func':keywords_shareholder_main_business_conn,'type':'keywords'},
    'part2_keywords_industry_status':{'func':keywords_industry_status,'type':'keywords'},
    'part3_1keywords':{'func':part3_1keywords,'type':'keywords'},
    'part3_2keywords':{'func':part3_2keywords,'type':'keywords'},
    'part4_keywords_down_industry':{'func':keywords_down_industry,'type':'keywords'},
    'part4_keywords_sub_industry':{'func':keywords_sub_industry,'type':'keywords'},
    'part4_keywords_down_industry_conn':{'func':keywords_down_industry_conn,'type':'keywords'},
    'part4_keywords_sub_industry_conn':{'func':keywords_sub_industry_conn,'type':'keywords'},
    'part4_keywords_down_public':{'func':keywords_down_public,'type':'keywords'},
    'part4_keywords_sub_public':{'func':keywords_sub_public,'type':'keywords'},
    'part4_keywords_down_abroad':{'func':keywords_down_abroad,'type':'keywords'},
    'part4_keywords_sub_abroad':{'func':keywords_sub_abroad,'type':'keywords'},
    'part4_keywords_down_financial':{'func':keywords_down_financial,'type':'keywords'},
    'part4_keywords_sub_financial':{'func':keywords_sub_financial,'type':'keywords'},
    'part5_1keywords':{'func':keywords_part5_1,'type':'keywords'},
    'part5_2keywords':{'func':keywords_part5_2,'type':'keywords'},
    'part5_3keywords':{'func':keywords_part5_3,'type':'keywords'},
    'part5_4keywords':{'func':keywords_part5_4,'type':'keywords'},
    'part5_5keywords':{'func':keywords_part5_5,'type':'keywords'},
    'part6_keywords_shareholders_support':{'func':keywords_shareholders_support,'type':'keywords'},
    'part6_keywords_evaluate_control_structure':{'func':keywords_evaluate_control_structure,'type':'keywords'},
    'part6_keywords_down_company_risk_status':{'func':keywords_down_company_risk_status,'type':'keywords'},
    'part6_keywords_down_company_finance_status':{'func':keywords_down_company_finance_status,'type':'keywords'},
    'part6_keywords_down_company_industry_potential':{'func':keywords_down_company_industry_potential,'type':'keywords'},
    'oversea_keywords':{'func':oversea_keywords,'type':'keywords'},

    # 'nl2sql_example':{'func':nl2sql_example,'type':'nl2sql'},
    'part1_1_1nl2sql':{'func':nl2sql_part1_1_1,'type':'nl2sql'},
    'part1_2_1nl2sql':{'func':nl2sql_part1_2_1,'type':'nl2sql'},
    'part1_2_2nl2sql':{'func':nl2sql_part1_2_2,'type':'nl2sql'},
    'part1_2_3nl2sql':{'func':nl2sql_part1_2_3,'type':'nl2sql'},
    'part1_3_1nl2sql':{'func':nl2sql_part1_3_1,'type':'nl2sql'},
    'part1_3_2nl2sql':{'func':nl2sql_part1_3_2,'type':'nl2sql'},
    'part1_4_1nl2sql':{'func':nl2sql_part1_4_1,'type':'nl2sql'},
    'part1_4_2nl2sql':{'func':nl2sql_part1_4_2,'type':'nl2sql'},
    'part2_nl2sql_shareholder_type':{'func':nl2sql_shareholder_type,'type':'nl2sql'},
    'part2_nl2sql_shareholder_industry':{'func':nl2sql_shareholder_industry,'type':'nl2sql'},
    'part2_nl2sql_industry':{'func':nl2sql_industry,'type':'nl2sql'},
    'part2_nl2sql_shareholder_main_business':{'func':nl2sql_shareholder_main_business,'type':'nl2sql'},
    'part2_nl2sql_main_business':{'func':nl2sql_main_business,'type':'nl2sql'},
    'part2_nl2sql_shareholder_public':{'func':nl2sql_shareholder_public,'type':'nl2sql'},
    'part2_nl2sql_shareholder_abroad':{'func':nl2sql_shareholder_abroad,'type':'nl2sql'},
    'part2_nl2sql_shareholder_financial':{'func':nl2sql_shareholder_financial,'type':'nl2sql'},
    'part2_nl2sql_financial':{'func':nl2sql_financial,'type':'nl2sql'},
    'part2_nl2sql_controller':{'func':nl2sql_controller,'type':'nl2sql'},
    'part3_1nl2sql':{'func':part3_1nl2sql,'type':'nl2sql'},
    'part3_2nl2sql':{'func':part3_2nl2sql,'type':'nl2sql'},
    'part4_nl2sql_down_industry':{'func':nl2sql_down_industry,'type':'nl2sql'},
    'part4_nl2sql_sub_industry':{'func':nl2sql_sub_industry,'type':'nl2sql'},
    'part4_nl2sql_down_public':{'func':nl2sql_down_public,'type':'nl2sql'},
    'part4_nl2sql_sub_public':{'func':nl2sql_sub_public,'type':'nl2sql'},
    'part4_nl2sql_down_abroad':{'func':nl2sql_down_abroad,'type':'nl2sql'},
    'part4_nl2sql_sub_abroad':{'func':nl2sql_sub_abroad,'type':'nl2sql'},
    'part4_nl2sql_down_financial':{'func':nl2sql_down_financial,'type':'nl2sql'},
    'part4_nl2sql_sub_financial':{'func':nl2sql_sub_financial,'type':'nl2sql'},
    'oversea_nl2sql':{'func':oversea_nl2sql,'type':'nl2sql'}
}