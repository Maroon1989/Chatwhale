from inferencer.base import BaseInferencer
from inferencer.stock_list import StockInferencer
__all__ = [
    'BaseInferencer',
    'StockInferencer'
    ]

EXP_STR2CLASS_NAME = {
    'stock_list': 'StockInferencer',  
}
