from .classification.classification_example import classification_example
from .keywords.keywords_example import keywords_example
from .nl2sql.nl2sql_example import nl2sql_example
from .classification.part3_1classification import part3_1classification
from .classification.part3_2classification import part3_2classification
from .classification.part4_classification import *
from .keywords.part3_1keywords import part3_1keywords
from .keywords.part3_2keywords import part3_2keywords
from .keywords.part4_keywords import *
from .nl2sql.part3_1nl2sql import part3_1nl2sql
from .nl2sql.part3_2nl2sql import part3_2nl2sql
from .nl2sql.part4_nl2sql import *
from .classification.part1_classification import *
from .classification.part6_classification import *
from .keywords.part1_keywords import *
from .keywords.part6_keywords import *

STRATEGIES = {
    'classification_example': {'func':classification_example,'type':'classification'},
    'part1_1_1classification':{'func':part1_1_1classification,'type':'classification'},
    'part1_2_1classification':{'func':part1_2_1classification,'type':'classification'},
    'part1_2_2classification':{'func':part1_2_2classification,'type':'classification'},
    'part1_2_3classification':{'func':part1_2_3classification,'type':'classification'},
    'part1_3_1classification':{'func':part1_3_1classification,'type':'classification'},
    'part1_3_2classification':{'func':part1_3_2classification,'type':'classification'},
    'part1_4_1classification':{'func':part1_4_1classification,'type':'classification'},
    'part1_4_2classification':{'func':part1_4_2classification,'type':'classification'},
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
    'part6_classification_shareholders_support':{'func':classification_shareholders_support,'type':'classification'},
    'part6_classification_evaluate_control_structure':{'func':classification_evaluate_control_structure,'type':'classification'},
    'part6_classification_down_company_risk_status':{'func':classification_down_company_risk_status,'type':'classification'},
    'part6_classification_down_company_finance_status':{'func':classification_down_company_finance_status,'type':'classification'},
    'part6_classification_down_company_industry_potential':{'func':classification_down_company_industry_potential,'type':'classification'},

    'keywords_example':{'func':keywords_example,'type':'keywords'},
    'keywords_part1_1_1':{'func':keywords_part1_1_1,'type':'keywords'},
    'keywords_part1_2_1':{'func':keywords_part1_2_1,'type':'keywords'},
    'keywords_part1_2_2':{'func':keywords_part1_2_2,'type':'keywords'},
    'keywords_part1_2_3':{'func':keywords_part1_2_3,'type':'keywords'},
    'keywords_part1_3_1':{'func':keywords_part1_3_1,'type':'keywords'},
    'keywords_part1_3_2':{'func':keywords_part1_3_2,'type':'keywords'},
    'keywords_part1_4_2':{'func':keywords_part1_4_2,'type':'keywords'},
    'keywords_part1_4_1':{'func':keywords_part1_4_1,'type':'keywords'},
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
    'part6_keywords_shareholders_support':{'func':keywords_shareholders_support,'type':'keywords'},
    'part6_keywords_evaluate_control_structure':{'func':keywords_evaluate_control_structure,'type':'keywords'},
    'part6_keywords_down_company_risk_status':{'func':keywords_down_company_risk_status,'type':'keywords'},
    'part6_keywords_down_company_finance_status':{'func':keywords_down_company_finance_status,'type':'keywords'},
    'part6_keywords_down_company_industry_potential':{'func':keywords_down_company_industry_potential,'type':'keywords'},

    'nl2sql_example':{'func':nl2sql_example,'type':'nl2sql'},
    'part3_1nl2sql':{'func':part3_1nl2sql,'type':'nl2sql'},
    'part3_2nl2sql':{'func':part3_2nl2sql,'type':'nl2sql'},
    'part4_nl2sql_down_industry':{'func':nl2sql_down_industry,'type':'nl2sql'},
    'part4_nl2sql_sub_industry':{'func':nl2sql_sub_industry,'type':'nl2sql'},
    'part4_nl2sql_down_public':{'func':nl2sql_down_public,'type':'nl2sql'},
    'part4_nl2sql_sub_public':{'func':nl2sql_sub_public,'type':'nl2sql'},
    'part4_nl2sql_down_abroad':{'func':nl2sql_down_abroad,'type':'nl2sql'},
    'part4_nl2sql_sub_abroad':{'func':nl2sql_sub_abroad,'type':'nl2sql'},
    'part4_nl2sql_down_financial':{'func':nl2sql_down_financial,'type':'nl2sql'},
    'part4_nl2sql_sub_financial':{'func':nl2sql_sub_financial,'type':'nl2sql'}
}