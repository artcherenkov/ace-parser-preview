import xmlschema
import json
from decimal import Decimal

# Пути к файлам
xsd_file = '../xml/schema/schema.xsd'  # Путь к вашему XSD-файлу
xml_file = '../xml/estimates-examples/full_example.xml'  # Путь к вашему XML-файл
json_file = '../frontend/src/data/sampleEstimate.json'  # Путь к файлу, куда будут сохранены данные в JSON


# Определение кастомного энкодера для Decimal
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)  # Преобразуем Decimal в строку для точности
        return super().default(obj)


try:
    # Загрузка XSD-схемы
    schema = xmlschema.XMLSchema(xsd_file)

    # Преобразование XML в Python-словарь с валидацией
    data = schema.to_dict(xml_file)

    # Сериализация в JSON
    json_data = json.dumps(data, indent=4, ensure_ascii=False, cls=DecimalEncoder)
    print("XML успешно провалидирован и преобразован в JSON.")
    # Сохранение данных в JSON-файл
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False, cls=DecimalEncoder)

    # Пример доступа к данным (значения будут строками)
    quantity = data.get('Item', {}).get('Cost', {}).get('Quantity')
    if quantity is not None:
        print(f"Количество (Quantity): {quantity} (тип: {type(quantity)})")

except xmlschema.XMLSchemaValidationError as e:
    print(f"Ошибка валидации XML: {e}")
except xmlschema.XMLSchemaDecodeError as e:
    print(f"Ошибка декодирования XML: {e}")
except FileNotFoundError as e:
    print(f"Файл не найден: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
