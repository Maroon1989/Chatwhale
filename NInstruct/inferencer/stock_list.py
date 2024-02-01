from typing import Dict, Any, List

from utils import load_pickle, preprocess_text
from inferencer import BaseInferencer
import numpy as np

class StockInferencer(BaseInferencer):
    def __init__(self,
                 types: List[str],
                 **kwargs) -> None:
        super().__init__(types=types)
        ...

    def load(self,
             file_name: str,
             **kwargs) -> Dict[str, Any]:
        cur_data = load_pickle(file_name)
        cur_data = {
            'id':cur_data['id'],
            'security_code' : cur_data['security_code'],
            'stock_name': cur_data['stock_name'],
            'stock_code': cur_data['stock_code'],
        }

        # NOTE: 完善类型检查
        assert isinstance(cur_data['title'], str)
        assert isinstance(cur_data['id'],int)
        assert isinstance(cur_data['stock_name'],str)
        assert isinstance(cur_data['stock_code'],np.float64)
        assert isinstance(cur_data['security_code'],str)

        # 文本预处理
        # cur_data['title'] = preprocess_text(cur_data['title'])
        # cur_data['description'] = preprocess_text(cur_data['description'])
        # for key1, inner_dict in cur_data['components_nested'].items():
        #     for key2, value in inner_dict.items():
        #         cur_data['components_nested'][key1][key2] = preprocess_text(value)
        # for key in cur_data['components_flat'].keys():
        #     cur_data['components_flat'][key] = preprocess_text(cur_data['components_flat'][key])
        # for i in range(len(cur_data['steps'])):
        #     cur_data['steps'][i]['description'] = preprocess_text(cur_data['steps'][i]['description'])

        return cur_data

