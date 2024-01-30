from typing import List, Callable

from langchain.document_loaders.unstructured import UnstructuredFileLoader
from unstructured.partition.text import partition_text
import os
# import fitz
# from PyMuPDF import fitz
import fitz
from tqdm import tqdm
from typing import Union, Any
import numpy as np
import base64
from paddleocr import PaddleOCR
def pdf_ocr_txt(filepath, dir_path="tmp_files"):
    ocr_engine = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=True, show_log=False)
    full_dir_path = os.path.join(os.path.dirname(filepath), dir_path)
    if not os.path.exists(full_dir_path):
        os.makedirs(full_dir_path)
    doc = fitz.open(filepath)
    txt_file_path = os.path.join(full_dir_path, "{}.txt".format(os.path.split(filepath)[-1]))
    img_name = os.path.join(full_dir_path, 'tmp.png')
    with open(txt_file_path, 'w', encoding='utf-8') as fout:
        for i in tqdm(range(doc.page_count)):
            page = doc.load_page(i)
            pix = page.get_pixmap()
            img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.h, pix.w, pix.n))

            img_data = {"img64": base64.b64encode(img).decode("utf-8"), "height": pix.h, "width": pix.w,
                        "channels": pix.n}
            result = ocr_engine(img)
            # print(result)
            result = [line for line in result if line]
            ocr_result = [i[1][0] for line in result for i in line if isinstance(i, list) and len(i) > 1 and isinstance(i[1], list) and len(i[1]) > 0]
            fout.write("\n".join(ocr_result))
    if os.path.exists(img_name):
        os.remove(img_name)
    return txt_file_path
pdf_ocr_txt(filepath=r'Chatwhale\pdf_parser\paddle_ocr\data_process\data\平安银行：2022年年度报告 (1).PDF')