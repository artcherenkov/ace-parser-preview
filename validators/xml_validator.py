# validators/xml_validator.py

from lxml import etree
from typing import List, Optional, Tuple
import os
import logging

# Настройка логгера
logger = logging.getLogger(__name__)


class ValidationError:
    """Класс для представления ошибки валидации XML."""

    def __init__(self, message: str, line: Optional[int] = None, column: Optional[int] = None):
        self.message = message
        self.line = line
        self.column = column

    def __str__(self) -> str:
        location = f" at line {self.line}"
        if self.column is not None:
            location += f", column {self.column}"
        return f"Validation error{location if self.line else ''}: {self.message}"


def load_xsd_schema(schema_path: str) -> etree.XMLSchema:
    """
    Загружает XSD-схему из файла.

    Args:
        schema_path: Путь к файлу XSD-схемы

    Returns:
        Объект XMLSchema для валидации

    Raises:
        ValueError: Если файл схемы не существует или не является корректной XSD
    """
    if not os.path.exists(schema_path):
        raise ValueError(f"Schema file not found: {schema_path}")

    try:
        with open(schema_path, 'rb') as schema_file:
            schema_doc = etree.parse(schema_file)
            return etree.XMLSchema(schema_doc)
    except etree.XMLSchemaParseError as e:
        raise ValueError(f"Invalid XSD schema: {str(e)}")


def validate_xml_file(xml_path: str, schema: etree.XMLSchema) -> Tuple[bool, List[ValidationError]]:
    """
    Валидирует XML-файл по схеме XSD.

    Args:
        xml_path: Путь к XML-файлу
        schema: Объект XMLSchema для валидации

    Returns:
        Кортеж (is_valid, errors), где:
        - is_valid: True, если XML валиден, иначе False
        - errors: Список ошибок ValidationError, если есть
    """
    if not os.path.exists(xml_path):
        return False, [ValidationError(f"XML file not found: {xml_path}")]

    try:
        with open(xml_path, 'rb') as xml_file:
            xml_doc = etree.parse(xml_file)
    except etree.XMLSyntaxError as e:
        # Обработка ошибок синтаксиса XML
        line = getattr(e, 'lineno', None)
        column = getattr(e, 'position', None)
        error = ValidationError(str(e), line, column)
        logger.error(f"XML syntax error: {error}")
        return False, [error]

    # Валидация по схеме
    is_valid = schema.validate(xml_doc)

    if not is_valid:
        # Сбор и форматирование ошибок валидации
        errors = []
        for error in schema.error_log:
            errors.append(ValidationError(error.message, error.line, error.column))
        return False, errors

    return True, []


def validate_xml_string(xml_string: str, schema: etree.XMLSchema) -> Tuple[bool, List[ValidationError]]:
    """
    Валидирует XML-строку по схеме XSD.

    Args:
        xml_string: Строка с XML-данными
        schema: Объект XMLSchema для валидации

    Returns:
        Кортеж (is_valid, errors), где:
        - is_valid: True, если XML валиден, иначе False
        - errors: Список ошибок ValidationError, если есть
    """
    try:
        xml_doc = etree.fromstring(xml_string.encode('utf-8'))
        xml_tree = etree.ElementTree(xml_doc)
    except etree.XMLSyntaxError as e:
        # Обработка ошибок синтаксиса XML
        line = getattr(e, 'lineno', None)
        column = getattr(e, 'position', None)
        error = ValidationError(str(e), line, column)
        logger.error(f"XML syntax error: {error}")
        return False, [error]

    # Валидация по схеме
    is_valid = schema.validate(xml_tree)

    if not is_valid:
        # Сбор и форматирование ошибок валидации
        errors = []
        for error in schema.error_log:
            errors.append(ValidationError(error.message, error.line, error.column))
        return False, errors

    return True, []


def format_validation_errors(errors: List[ValidationError]) -> str:
    """
    Форматирует список ошибок валидации в читаемый текст.

    Args:
        errors: Список объектов ValidationError

    Returns:
        Отформатированная строка с описанием ошибок
    """
    if not errors:
        return "No validation errors."

    result = "Validation errors:\n"
    for i, error in enumerate(errors, 1):
        result += f"{i}. {str(error)}\n"

    return result
