import json
import os

from .logger import Logger

_logger = Logger(logger_name=__name__).logger


class DataContext:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def load_data(self):
        if not os.path.exists(self.data_path):
            _logger.error(f"Arquivo não encontrado: {self.data_path}")
            raise FileNotFoundError(f"Arquivo não encontrado: {self.data_path}")
        with open(self.data_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        _logger.info(f"Dados carregados com sucesso de {self.data_path}")
        return json_data
