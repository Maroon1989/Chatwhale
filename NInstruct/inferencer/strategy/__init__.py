# from .what_is_dish import what_is_dish
# from .what_is_step_img_doing import what_is_step_img_doing
# from .what_are_step_imgs_doing import what_are_step_imgs_doing
# from .what_are_components_nested import what_are_components_nested
# from .what_are_components_flat import what_are_components_flat
# from .how_to_sort_step_imgs import how_to_sort_step_imgs
# from .generated_by_GPT import generated_by_GPT
from .classification.classification_example import classification_example
from .keywords.keywords_example import keywords_example
from .nl2sql.nl2sql_example import nl2sql_example

STRATEGIES = {
    'classification_example': {'func':classification_example,'type':'classification'},
    'keywords_example':{'func':keywords_example,'type':'keywords'},
    'nl2sql_example':{'func':nl2sql_example,'type':'nl2sql'}
}