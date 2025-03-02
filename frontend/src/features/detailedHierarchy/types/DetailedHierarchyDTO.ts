// src/features/detailedHierarchy/types/DetailedHierarchyDTO.ts

/**
 * Ресурс позиции сметы
 */
export interface ResourceItem {
  id: string;                   // Уникальный идентификатор ресурса
  code: string;                 // Код ресурса
  name: string;                 // Наименование ресурса
  type: 'material' | 'machinery' | 'labor'; // Тип ресурса
  unit: string;                 // Единица измерения
  quantity: number;             // Количество
  consumption: string;          // Расход (строка, включающая количество и единицу измерения)
  basePrice: number;            // Стоимость в базисном уровне цен
  currentPrice: number;         // Стоимость в текущем уровне цен
  indexValue: number;           // Индекс изменения цены
}

/**
 * Позиция сметы
 */
export interface EstimateItem {
  id: string;                   // Уникальный идентификатор позиции
  num: number;                  // Номер позиции
  code: string;                 // Шифр позиции (например, ФЕР 08-02-001-02)
  name: string;                 // Наименование работы
  unit: string;                 // Единица измерения
  quantity: number;             // Количество
  basePrice: {                  // Стоимость в базисном уровне цен
    direct: number;             // Прямые затраты
    total: number;              // Всего
  };
  currentPrice: {               // Стоимость в текущем уровне цен
    direct: number;
    total: number;
  };
  indexValue: number;           // Индекс изменения цены
  resources: ResourceItem[];    // Ресурсы позиции
  hasCoefficients: boolean;     // Наличие коэффициентов
  coefficients?: {              // Коэффициенты (если есть)
    name: string;               // Наименование коэффициента
    value: number;              // Значение коэффициента
  }[];
}

/**
 * Раздел сметы
 */
export interface EstimateSection {
  id: string;                   // Уникальный идентификатор раздела
  code: number;                 // Код раздела
  name: string;                 // Наименование раздела
  basePrice: number;            // Стоимость в базисном уровне цен
  currentPrice: number;         // Стоимость в текущем уровне цен
  indexValue: number;           // Индекс изменения цены
  items: EstimateItem[];        // Позиции раздела
}

/**
 * DTO для отображения иерархической структуры сметы
 * (разделы -> позиции -> ресурсы)
 */
export interface DetailedHierarchyDTO {
  /**
   * Разделы сметы
   */
  sections: EstimateSection[];

  /**
   * Общая статистика
   */
  stats: {
    sectionsCount: number;      // Количество разделов
    itemsCount: number;         // Количество позиций
    resourcesCount: number;     // Количество ресурсов
  };

  /**
   * Общие итоги
   */
  totals: {
    basePrice: number;          // Общая стоимость в базисном уровне цен
    currentPrice: number;       // Общая стоимость в текущем уровне цен
    indexValue: number;         // Общий индекс изменения цены
  };

  /**
   * Фильтры для структуры
   */
  filters: {
    availableCodes: string[];   // Доступные коды для фильтрации
    availableTypes: {           // Доступные типы для фильтрации
      code: string;
      name: string;
    }[];
  };

  /**
   * Метаданные
   */
  meta: {
    currencySymbol: string;     // Символ валюты
    dateGenerated: string;      // Дата формирования данных
    estimateName: string;       // Наименование сметы
    estimateNumber: string;     // Номер сметы
  };
}
