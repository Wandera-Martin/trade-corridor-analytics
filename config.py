import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_RAW_PATH = os.path.join(BASE_DIR, 'data', 'raw', 'northern_corridor_synthetic_dataset.csv')
DATA_PROCESSED_PATH = os.path.join(BASE_DIR, 'data', 'processed')
FIGURES_PATH = os.path.join(BASE_DIR, 'reports', 'figures')