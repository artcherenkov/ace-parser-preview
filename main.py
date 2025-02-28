from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import Dict, Any
from interfaces.interfaces import EstimateParser, EstimateTransformer

app = FastAPI(title="Смета API", description="API для парсинга и анализа смет строительных работ")


@app.post("/parse-estimate/", summary="Разбор XML файла сметы")
async def parse_estimate(
        file: UploadFile = File(...),
        parser: EstimateParser = None,
        transformer: EstimateTransformer = None
) -> Dict[str, Any]:
    """
    Разбирает загруженный XML файл сметы и возвращает структурированные данные.

    Args:
        file: Загруженный XML файл

    Returns:
        Dict[str, Any]: Структурированные данные для фронтенда

    Raises:
        HTTPException: При ошибке парсинга или валидации
    """
    try:
        # Чтение содержимого файла
        content = await file.read()

        # Валидация XML
        if not parser.validate_xml(content):
            raise HTTPException(status_code=400, detail="Некорректный формат XML-файла")

        # Парсинг XML
        estimate_data = parser.parse_xml(content)

        # Преобразование данных для фронтенда
        frontend_data = transformer.to_frontend_format(estimate_data)

        return frontend_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при обработке файла: {str(e)}")
