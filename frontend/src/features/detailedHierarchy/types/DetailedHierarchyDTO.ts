// src/features/detailedHierarchy/types/DetailedHierarchyDTO.ts

/**
 * Типы иконок для различных элементов сметы
 */
export enum ItemIconType {
  Material = "material", // Материалы
  Work = "work", // Работы (расценки)
  Transport = "transport", // Транспорт
  Machine = "machine", // Машины и механизмы
  Equipment = "equipment", // Оборудование
  Other = "other", // Прочее
}

/**
 * Основная структура DTO для иерархического отображения сметы
 */
export interface DetailedHierarchyDTO {
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
  sections: SectionDTO[]; // Разделы сметы
  totals: {
    basePrice: number; // Общая стоимость в базисном уровне
    currentPrice: number; // Общая стоимость в текущем уровне
  };
}

/**
 * Раздел сметы содержащий позиции
 */
export interface SectionDTO {
  code: number | string; // Код раздела
  name: string; // Название раздела
  items: ItemDTO[]; // Позиции в разделе
  totals: {
    basePrice: number; // Общая стоимость в базисном уровне
    currentPrice: number; // Общая стоимость в текущем уровне
    directCosts: {
      // Прямые затраты
      basePrice: number;
      currentPrice: number;
    };
    labor: {
      // Оплата труда
      basePrice: number;
      currentPrice: number;
    };
    materials: {
      // Материалы
      basePrice: number;
      currentPrice: number;
    };
    machinery: {
      // Машины и механизмы
      basePrice: number;
      currentPrice: number;
    };
    overhead: {
      // Накладные расходы
      basePrice: number;
      currentPrice: number;
    };
    profit: {
      // Сметная прибыль
      basePrice: number;
      currentPrice: number;
    };
  };
}

/**
 * Базовый тип позиции сметы с общими свойствами
 */
export interface BaseItemDTO {
  id: string; // Уникальный идентификатор позиции
  summaryType: string; // Графа объектной сметы (Строительные, Монтажные, Оборудование, Прочее)
  workType: string; // Тип работ
  iconType: ItemIconType; // Тип иконки для отображения
  label: string; // Лейбл для отображения типа позиции
  isDetailedItem: boolean; // Флаг, указывающий является ли это развернутой позицией (с Cost) или единичным ресурсом
  totals: {
    // Итоговые суммы по позиции
    basePrice: number;
    currentPrice?: number;
  };
  overheads?: {
    // Накладные расходы
    reason: string; // Обоснование
    name: string; // Наименование
    value: number; // Значение в %
    basePrice: number; // Стоимость в базисном уровне
    currentPrice?: number; // Стоимость в текущем уровне
  };
  profits?: {
    // Сметная прибыль
    reason: string; // Обоснование
    name: string; // Наименование
    value: number; // Значение в %
    basePrice: number; // Стоимость в базисном уровне
    currentPrice?: number; // Стоимость в текущем уровне
  };
}

/**
 * Тип позиции с единичной расценкой (содержит Cost)
 */
export interface CostItemDTO extends BaseItemDTO {
  isDetailedItem: true; // Это расширенная позиция с Cost
  cost: {
    num: number; // Порядковый номер
    code: string; // Шифр
    name: string; // Наименование
    quantity: number; // Количество
    unit: string; // Единица измерения
    perUnit: {
      // Показатели за единицу
      base: {
        direct?: number; // Прямые затраты
        machines?: number; // Машины
        workersSalary?: number; // Оплата труда рабочих
        machinistSalary?: number; // Оплата труда машинистов
        salary?: number; // Общая оплата труда
        materials?: number; // Материалы
      };
      current?: {
        // То же, но в текущем уровне цен
        direct?: number;
        machines?: number;
        workersSalary?: number;
        machinistSalary?: number;
        salary?: number;
        materials?: number;
      };
      natural?: {
        // Натуральные показатели
        laborCosts?: number; // Затраты труда рабочих
        machinistLaborCosts?: number; // Затраты труда машинистов
      };
    };
    totals: {
      // Итоговые стоимости
      base: {
        direct?: number;
        machines?: number;
        workersSalary?: number;
        machinistSalary?: number;
        salary?: number;
        materials?: number;
      };
      current?: {
        direct?: number;
        machines?: number;
        workersSalary?: number;
        machinistSalary?: number;
        salary?: number;
        materials?: number;
      };
      natural?: {
        laborCosts?: number;
        machinistLaborCosts?: number;
      };
    };
    resourcesInternal?: ResourceDTO[]; // Внутренние ресурсы (в расценке)
    resources?: ResourceDTO[]; // Внешние ресурсы (требуемые дополнительно)
  };
}

/**
 * Тип для отдельного ресурса (не содержит Cost)
 */
export interface ResourceItemDTO extends BaseItemDTO {
  isDetailedItem: false; // Это единичный ресурс
  code: string; // Шифр
  name: string; // Наименование
  consumption: number; // Расход
  unit: string; // Единица измерения
  pricePerUnitBase?: number; // Цена за единицу в базисном уровне
  pricePerUnitCurrent?: number; // Цена за единицу в текущем уровне
}

/**
 * Ресурс, используемый в расценке
 */
export interface ResourceDTO {
  num?: number; // Порядковый номер
  code: string; // Шифр
  name: string; // Наименование
  consumption: number; // Расход на единицу расценки
  unit: string; // Единица измерения
  consumptionTotal: number; // Расход на весь объем
  pricePerUnitBase?: number; // Цена за единицу в базисном уровне
  priceTotalBase?: number; // Общая стоимость в базисном уровне
  type: "worker" | "machine" | "material" | "equipment"; // Тип ресурса
}

/**
 * Объединение типов позиций
 */
export type ItemDTO = CostItemDTO | ResourceItemDTO;
