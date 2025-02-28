# main.py

import logging
from validators.xml_validator import (
    load_xsd_schema,
    validate_xml_file,
    format_validation_errors
)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    # Пути к файлам
    schema_path = "xml/schema.xsd"
    xml_paths = [
        "xml/minimal_example.xml",
        "xml/multi_section_example.xml"
    ]

    try:
        # Загрузка схемы
        schema = load_xsd_schema(schema_path)
        logger.info(f"Successfully loaded XSD schema from {schema_path}")

        # Валидация каждого XML-файла
        for xml_path in xml_paths:
            logger.info(f"Validating {xml_path}...")
            is_valid, errors = validate_xml_file(xml_path, schema)

            if is_valid:
                logger.info(f"✓ {xml_path} is valid according to the schema.")
            else:
                logger.error(f"✗ {xml_path} is NOT valid:")
                logger.error(format_validation_errors(errors))

    except Exception as e:
        logger.error(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
