# tests/test_xml_validator.py
import pytest
from lxml import etree

from validators.xml_validator import load_xsd_schema, validate_xml_file, validate_xml_string, ValidationError

# Пути к тестовым файлам
SCHEMA_PATH = "xml/schema.xsd"
VALID_XML_PATH = "xml/minimal_example.xml"
INVALID_XML = """
<?xml version="1.0"?>
<InvalidRoot>
  <InvalidElement>This is not valid</InvalidElement>
</InvalidRoot>
"""


def test_load_xsd_schema():
    """Тест загрузки XSD-схемы."""
    schema = load_xsd_schema(SCHEMA_PATH)
    assert schema is not None
    assert isinstance(schema, etree.XMLSchema)


def test_load_xsd_schema_not_found():
    """Тест ошибки при отсутствии файла схемы."""
    with pytest.raises(ValueError) as excinfo:
        load_xsd_schema("nonexistent_schema.xsd")
    assert "Schema file not found" in str(excinfo.value)


def test_validate_xml_file():
    """Тест валидации корректного XML-файла."""
    schema = load_xsd_schema(SCHEMA_PATH)
    is_valid, errors = validate_xml_file(VALID_XML_PATH, schema)
    assert is_valid is True
    assert len(errors) == 0


def test_validate_xml_file_not_found():
    """Тест ошибки при отсутствии XML-файла."""
    schema = load_xsd_schema(SCHEMA_PATH)
    is_valid, errors = validate_xml_file("nonexistent.xml", schema)
    assert is_valid is False
    assert len(errors) == 1
    assert "XML file not found" in str(errors[0])


def test_validate_xml_string():
    """Тест валидации некорректной XML-строки."""
    schema = load_xsd_schema(SCHEMA_PATH)
    is_valid, errors = validate_xml_string(INVALID_XML, schema)
    assert is_valid is False
    assert len(errors) > 0
