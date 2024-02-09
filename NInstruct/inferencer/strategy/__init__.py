from .classification.classification_example import classification_example
from .keywords.keywords_example import keywords_example
from .nl2sql.nl2sql_example import nl2sql_example
from .classification.part3_1classification import part3_1classification
from .classification.part3_2classification import part3_2classification
from .keywords.part3_1keywords import part3_1keywords
from .keywords.part3_2keywords import part3_2keywords
from .nl2sql.part3_1nl2sql import part3_1nl2sql
from .nl2sql.part3_2nl2sql import part3_2nl2sql

STRATEGIES = {
    'classification_example': {'func':classification_example,'type':'classification'},
    'part3_1classification':{'func':part3_1classification,'type':'classification'},
    'part3_2classification':{'func':part3_2classification,'type':'classification'},
    'keywords_example':{'func':keywords_example,'type':'keywords'},
    'part3_1keywords':{'func':part3_1keywords,'type':'keywords'},
    'part3_2keywords':{'func':part3_2keywords,'type':'keywords'},
    'part3_1nl2sql':{'func':part3_1nl2sql,'type':'nl2sql'},
    'part3_2nl2sql':{'func':part3_2nl2sql,'type':'nl2sql'},
    'nl2sql_example':{'func':nl2sql_example,'type':'nl2sql'}
}