// src/features/costStructure/types/CostStructureDTO.ts

/**
 * Элемент структуры затрат
 */
export type CostStructureElement = {
  /** Уникальный идентификатор элемента затрат */
  id: string;
  /** Наименование элемента затрат */
  name: string;
  /** Сумма в текущем уровне цен */
  value: number;
  /** Сумма в базисном уровне цен */
  baseValue: number;
  /** Процент от общей стоимости (0-100) */
  percentage: number;
  /** Цвет для отображения в диаграмме */
  color: string;
};

/**
 * DTO для отображения структуры затрат в виде круговой диаграммы.
 * Содержит данные о распределении стоимости по основным элементам затрат.
 */
export interface CostStructureDTO {
  /**
   * Общая стоимость в текущем уровне цен
   */
  totalCost: number;

  /**
   * Общая стоимость в базисном уровне цен
   */
  totalBaseCost: number;

  /**
   * Элементы структуры затрат (оплата труда, материалы, механизмы, накладные расходы, сметная прибыль и др.)
   */
  elements: CostStructureElement[];

  /**
   * Данные для построения диаграммы сравнения базисного и текущего уровней цен
   */
  comparison: {
    base: {
      total: number;
      labor: number; // Оплата труда
      machinery: number; // Машины и механизмы
      materials: number; // Материалы
      overhead: number; // Накладные расходы
      profit: number; // Сметная прибыль
      other: number; // Прочие затраты
    };
    current: {
      total: number;
      labor: number;
      machinery: number;
      materials: number;
      overhead: number;
      profit: number;
      other: number;
    };
  };

  /**
   * Индексы изменения цен по элементам затрат
   */
  indices: {
    /** Индекс для оплаты труда */
    labor: number;
    /** Индекс для машин и механизмов */
    machinery: number;
    /** Индекс для материалов */
    materials: number;
    /** Индекс для накладных расходов */
    overhead: number;
    /** Индекс для сметной прибыли */
    profit: number;
    /** Общий индекс */
    total: number;
  };

  /**
   * Дополнительные данные для анализа
   */
  meta: {
    /** Символ валюты */
    currencySymbol: string;
    /** Заголовок для диаграммы */
    chartTitle: string;
    /** Дата формирования данных */
    dateGenerated: string;
  };
}
