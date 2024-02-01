from pathlib import Path

DATA_PATHS = {
    'stock_list': f'dataset'
}

JSON_SAVE_PATH_CLASSIFICATION = 'results/classification'
JSON_SAVE_PATH_KEYWORDS = 'results/keywords'
JSON_SAVE_PATH_NL2SQL = 'results/nl2sql'
IMG_SAVE_PATH = 'vllmnd/imgs'
IMG_DOWNLOAD_FAILED_LOGS = 'vllmnd/img_download_failed.csv'
Path(IMG_SAVE_PATH).mkdir(parents=True, exist_ok=True)


OPEN_AI_KEY = 'sk-' # NOTE: DO NOT UPLOAD

