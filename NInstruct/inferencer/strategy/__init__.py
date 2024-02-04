from .classification.classification_example import classification_example
from .keywords.keywords_example import keywords_example
from .nl2sql.nl2sql_example import nl2sql_example

STRATEGIES = {
    'classification_example': {'func':classification_example,'type':'classification'},
    'keywords_example':{'func':keywords_example,'type':'keywords'},
    'nl2sql_example':{'func':nl2sql_example,'type':'nl2sql'}
}