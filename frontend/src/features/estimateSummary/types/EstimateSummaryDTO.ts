/**
 * Тип данных для отображения общего обзора сметы с ключевыми показателями.
 * Содержит метаданные и основные финансовые показатели.
 */
export interface EstimateSummaryDTO {
  metadata: {
    constructionName: string; // Название стройки
    objectName: string; // Название объекта
    estimateName: string; // Название сметы
    estimateNumber: string; // Номер сметы
    date: string; // Дата составления
    priceBaseLevel: {
      year: number;
      month: number;
    }; // Базисный уровень цен
    priceCurrentLevel: {
      year: number;
      quarter: number;
    }; // Текущий уровень цен
  };
  totals: {
    basePrice: number; // Общая стоимость в базисном уровне
    currentPrice: number; // Общая стоимость в текущем уровне
    indexValue: number; // Индекс изменения цен
  };
  directCosts: {
    basePrice: number; // Прямые затраты в базисном уровне
    currentPrice: number; // Прямые затраты в текущем уровне
  };
  labor: {
    basePrice: number; // Оплата труда в базисном уровне
    currentPrice: number; // Оплата труда в текущем уровне
  };
  materials: {
    basePrice: number; // Материалы в базисном уровне
    currentPrice: number; // Материалы в текущем уровне
  };
  machinery: {
    basePrice: number; // Машины и механизмы в базисном уровне
    currentPrice: number; // Машины и механизмы в текущем уровне
  };
  overhead: {
    basePrice: number; // Накладные расходы в базисном уровне
    currentPrice: number; // Накладные расходы в текущем уровне
  };
  profit: {
    basePrice: number; // Сметная прибыль в базисном уровне
    currentPrice: number; // Сметная прибыль в текущем уровне
  };
  sectionsCount: number; // Количество разделов в смете
}
