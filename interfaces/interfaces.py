from abc import ABC, abstractmethod
from typing import Optional, BinaryIO, Union, Dict, Any

from models.models import EstimateData


class EstimateParser(ABC):
    """Интерфейс для парсера смет"""

    @abstractmethod
    def validate_xml(self, xml_content: Union[str, bytes]) -> bool:
        """
        Проверяет соответствие XML файла XSD-схеме.

        Args:
            xml_content: Содержимое XML файла

        Returns:
            bool: True, если XML соответствует схеме, иначе False
        """
        pass

    @abstractmethod
    def parse_xml(self, xml_content: Union[str, bytes]) -> EstimateData:
        """
        Разбирает XML и возвращает структурированные данные.

        Args:
            xml_content: Содержимое XML файла

        Returns:
            EstimateData: Структурированные данные сметы
        """
        pass

    @abstractmethod
    def parse_file(self, file_path: str) -> EstimateData:
        """
        Разбирает XML файл и возвращает структурированные данные.

        Args:
            file_path: Путь к XML файлу

        Returns:
            EstimateData: Структурированные данные сметы
        """
        pass

    @abstractmethod
    def parse_file_like(self, file_like: BinaryIO) -> EstimateData:
        """
        Разбирает файлоподобный объект и возвращает структурированные данные.

        Args:
            file_like: Файлоподобный объект с XML содержимым

        Returns:
            EstimateData: Структурированные данные сметы
        """
        pass


class EstimateTransformer(ABC):
    """Интерфейс для преобразования данных сметы в формат для фронтенда"""

    @abstractmethod
    def to_frontend_format(self, estimate_data: EstimateData) -> Dict[str, Any]:
        """
        Преобразует данные сметы в формат для фронтенда.

        Args:
            estimate_data: Данные сметы

        Returns:
            Dict[str, Any]: Данные в формате для фронтенда
        """
        pass
