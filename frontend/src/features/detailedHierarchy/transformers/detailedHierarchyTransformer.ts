// src/features/detailedHierarchy/transformers/detailedHierarchyTransformer.ts

import {
  DetailedHierarchyDTO,
  SectionDTO,
  ItemDTO,
  BaseItemDTO,
  CostItemDTO,
  ResourceItemDTO,
  ResourceDTO,
  ItemIconType,
} from "../types/DetailedHierarchyDTO";

/**
 * Преобразует данные из JSON формата сметы в DetailedHierarchyDTO
 *
 * @param jsonData - JSON данные сметы
 * @returns Объект DetailedHierarchyDTO
 */
export function transformToDetailedHierarchyDTO(
  jsonData: any,
): DetailedHierarchyDTO {
  // Проверяем наличие необходимых данных
  if (!jsonData || !jsonData.Object || !jsonData.Object.Estimate) {
    throw new Error("Invalid estimate data structure");
  }

  const estimate = jsonData.Object.Estimate;

  // Создаем метаданные
  const metadata = {
    constructionName: jsonData.Name || "Н/Д",
    objectName: jsonData.Object.Name || "Н/Д",
    estimateName: estimate.Name || "Н/Д",
    estimateNumber: estimate.Num || "Н/Д",
    date: formatDate(estimate.Date),
    priceBaseLevel: {
      year: Number(estimate.PriceLevelBase?.Year) || 0,
      month: Number(estimate.PriceLevelBase?.Month) || 0,
    },
    priceCurrentLevel: {
      year: Number(estimate.PriceLevelCur?.Year) || 0,
      quarter: Number(estimate.PriceLevelCur?.Quarter) || 0,
    },
  };

  // Преобразуем разделы
  const sections = transformSections(estimate.Sections?.Section || []);

  // Рассчитываем общие итоги
  const summary = estimate.EstimatePrice?.Summary || {};
  const totals = {
    basePrice: parseFloat(summary.Total?.PriceBase) || 0,
    currentPrice: parseFloat(summary.Total?.PriceCurrent) || 0,
  };

  return {
    metadata,
    sections,
    totals,
  };
}

/**
 * Преобразует JSON данные разделов в массив SectionDTO
 */
function transformSections(sectionsData: any[]): SectionDTO[] {
  if (!sectionsData || !Array.isArray(sectionsData)) {
    return [];
  }

  return sectionsData.map((section) => {
    // Преобразуем позиции
    const items = transformItems(section.Items?.Item || []);

    // Получаем итоги по разделу
    const sectionPrice = section.SectionPrice?.Summary || {};

    return {
      code: section.Code || "",
      name: section.Name || "",
      items,
      totals: {
        basePrice: parseFloat(sectionPrice.Total?.PriceBase) || 0,
        currentPrice: parseFloat(sectionPrice.Total?.PriceCurrent) || 0,
        directCosts: {
          basePrice: parseFloat(sectionPrice.Direct?.PriceBase) || 0,
          currentPrice: parseFloat(sectionPrice.Direct?.PriceCurrent) || 0,
        },
        labor: {
          basePrice: parseFloat(sectionPrice.WorkersSalary?.PriceBase) || 0,
          currentPrice:
            parseFloat(sectionPrice.WorkersSalary?.PriceCurrent) || 0,
        },
        materials: {
          basePrice: parseFloat(sectionPrice.Materials?.Total?.PriceBase) || 0,
          currentPrice:
            parseFloat(sectionPrice.Materials?.Total?.PriceCurrent) || 0,
        },
        machinery: {
          basePrice: parseFloat(sectionPrice.MachinesTotal?.PriceBase) || 0,
          currentPrice:
            parseFloat(sectionPrice.MachinesTotal?.PriceCurrent) || 0,
        },
        overhead: {
          basePrice: parseFloat(sectionPrice.Overhead?.PriceBase) || 0,
          currentPrice: parseFloat(sectionPrice.Overhead?.PriceCurrent) || 0,
        },
        profit: {
          basePrice: parseFloat(sectionPrice.Profit?.PriceBase) || 0,
          currentPrice: parseFloat(sectionPrice.Profit?.PriceCurrent) || 0,
        },
      },
    };
  });
}

/**
 * Преобразует JSON данные позиций в массив ItemDTO
 */
function transformItems(itemsData: any[]): ItemDTO[] {
  if (!itemsData || !Array.isArray(itemsData)) {
    return [];
  }

  return itemsData.map((item) => {
    const baseItem: BaseItemDTO = {
      id: generateUniqueId(),
      summaryType: item.SummaryType || "",
      workType: item.WorkType || "",
      iconType: determineIconType(item),
      label: determineLabel(item),
      isDetailedItem: !!item.Cost,
      totals: {
        basePrice: parseFloat(item.Totals?.Base) || 0,
        currentPrice: parseFloat(item.Totals?.Current) || 0,
      },
    };

    // Добавляем накладные расходы, если есть
    if (item.Overheads) {
      baseItem.overheads = {
        reason: item.Overheads.Reason || "",
        name: item.Overheads.Name || "",
        value: parseFloat(item.Overheads.Value) || 0,
        basePrice: parseFloat(item.Overheads.PriceBase) || 0,
        currentPrice: parseFloat(item.Overheads.PriceCur) || 0,
      };
    }

    // Добавляем сметную прибыль, если есть
    if (item.Profits) {
      baseItem.profits = {
        reason: item.Profits.Reason || "",
        name: item.Profits.Name || "",
        value: parseFloat(item.Profits.Value) || 0,
        basePrice: parseFloat(item.Profits.PriceBase) || 0,
        currentPrice: parseFloat(item.Profits.PriceCur) || 0,
      };
    }

    // Если это позиция с единичной расценкой
    if (item.Cost) {
      return transformCostItem(item, baseItem);
    }
    // Если это позиция с отдельным ресурсом
    else if (
      item.Material ||
      item.Machine ||
      item.Equipment ||
      item.Transport ||
      item.Other
    ) {
      return transformResourceItem(item, baseItem);
    }

    // Если тип позиции неопределен, возвращаем базовую информацию
    return baseItem as ItemDTO;
  });
}

/**
 * Преобразует позицию с единичной расценкой
 */
function transformCostItem(item: any, baseItem: BaseItemDTO): CostItemDTO {
  const costItem: CostItemDTO = {
    ...baseItem,
    isDetailedItem: true,
    cost: {
      num: parseInt(item.Cost.Num) || 0,
      code: `${item.Cost.Prefix || ""}-${item.Cost.Code || ""}`,
      name: item.Cost.Name || "",
      quantity: parseFloat(item.Cost.Quantity) || 0,
      unit: item.Cost.Unit || "",
      perUnit: {
        base: {
          direct: parseFloat(item.Cost.PerUnit?.Base?.Direct) || 0,
          machines: parseFloat(item.Cost.PerUnit?.Base?.Machines) || 0,
          workersSalary:
            parseFloat(item.Cost.PerUnit?.Base?.WorkersSalary) || 0,
          machinistSalary:
            parseFloat(item.Cost.PerUnit?.Base?.MachinistSalary) || 0,
          salary: parseFloat(item.Cost.PerUnit?.Base?.Salary) || 0,
          materials: parseFloat(item.Cost.PerUnit?.Base?.Materials) || 0,
        },
        current: item.Cost.PerUnit?.Current
          ? {
              direct: parseFloat(item.Cost.PerUnit.Current.Direct) || 0,
              machines: parseFloat(item.Cost.PerUnit.Current.Machines) || 0,
              workersSalary:
                parseFloat(item.Cost.PerUnit.Current.WorkersSalary) || 0,
              machinistSalary:
                parseFloat(item.Cost.PerUnit.Current.MachinistSalary) || 0,
              salary: parseFloat(item.Cost.PerUnit.Current.Salary) || 0,
              materials: parseFloat(item.Cost.PerUnit.Current.Materials) || 0,
            }
          : undefined,
        natural: item.Cost.PerUnit?.Natural
          ? {
              laborCosts: parseFloat(item.Cost.PerUnit.Natural.LaborCosts) || 0,
              machinistLaborCosts:
                parseFloat(item.Cost.PerUnit.Natural.MachinistLaborCosts) || 0,
            }
          : undefined,
      },
      totals: {
        base: {
          direct: parseFloat(item.Cost.Totals?.Base?.Direct) || 0,
          machines: parseFloat(item.Cost.Totals?.Base?.Machines) || 0,
          workersSalary: parseFloat(item.Cost.Totals?.Base?.WorkersSalary) || 0,
          machinistSalary:
            parseFloat(item.Cost.Totals?.Base?.MachinistSalary) || 0,
          salary: parseFloat(item.Cost.Totals?.Base?.Salary) || 0,
          materials: parseFloat(item.Cost.Totals?.Base?.Materials) || 0,
        },
        current: item.Cost.Totals?.Current
          ? {
              direct: parseFloat(item.Cost.Totals.Current.Direct) || 0,
              machines: parseFloat(item.Cost.Totals.Current.Machines) || 0,
              workersSalary:
                parseFloat(item.Cost.Totals.Current.WorkersSalary) || 0,
              machinistSalary:
                parseFloat(item.Cost.Totals.Current.MachinistSalary) || 0,
              salary: parseFloat(item.Cost.Totals.Current.Salary) || 0,
              materials: parseFloat(item.Cost.Totals.Current.Materials) || 0,
            }
          : undefined,
        natural: item.Cost.Totals?.Natural
          ? {
              laborCosts: parseFloat(item.Cost.Totals.Natural.LaborCosts) || 0,
              machinistLaborCosts:
                parseFloat(item.Cost.Totals.Natural.MachinistLaborCosts) || 0,
            }
          : undefined,
      },
    },
  };

  // Добавляем внутренние ресурсы, если есть
  if (item.Cost.ResourcesInternal) {
    costItem.cost.resourcesInternal = transformResources(
      item.Cost.ResourcesInternal,
    );
  }

  // Добавляем внешние ресурсы, если есть
  if (item.Cost.Resources) {
    costItem.cost.resources = transformResources(item.Cost.Resources);
  }

  return costItem;
}

/**
 * Преобразует позицию с отдельным ресурсом
 */
function transformResourceItem(
  item: any,
  baseItem: BaseItemDTO,
): ResourceItemDTO {
  let resourceData;

  // Определяем, какой тип ресурса используется
  if (item.Material) resourceData = item.Material;
  else if (item.Machine) resourceData = item.Machine;
  else if (item.Equipment) resourceData = item.Equipment;
  else if (item.Transport) resourceData = item.Transport;
  else if (item.Other) resourceData = item.Other;
  else resourceData = {}; // Если ничего не найдено

  return {
    ...baseItem,
    isDetailedItem: false,
    code: resourceData.Code || "",
    name: resourceData.Name || "",
    consumption: parseFloat(resourceData.Consumption) || 0,
    unit: resourceData.Unit || "",
    pricePerUnitBase: parseFloat(resourceData.PricePerUnitBase) || 0,
    pricePerUnitCurrent: parseFloat(resourceData.PricePerUnitCur) || 0,
  };
}

/**
 * Преобразует ресурсы внутри расценки в массив ResourceDTO
 */
function transformResources(resourcesData: any): ResourceDTO[] {
  const resources: ResourceDTO[] = [];

  // Обработка различных типов ресурсов
  processResourceArray(resourcesData.Worker, "worker", resources);
  processResourceArray(resourcesData.Machine, "machine", resources);
  processResourceArray(resourcesData.Material, "material", resources);
  processResourceArray(resourcesData.Equipment, "equipment", resources);

  return resources;
}

/**
 * Обрабатывает массив ресурсов определённого типа
 */
function processResourceArray(
  resourceArray: any,
  type: "worker" | "machine" | "material" | "equipment",
  resultArray: ResourceDTO[],
): void {
  if (!resourceArray) return;

  const resources = Array.isArray(resourceArray)
    ? resourceArray
    : [resourceArray];

  resources.forEach((resource) => {
    resultArray.push({
      num: parseInt(resource.Num) || undefined,
      code: resource.Code || "",
      name: resource.Name || "",
      consumption: parseFloat(resource.Consumption) || 0,
      unit: resource.Unit || "",
      consumptionTotal: parseFloat(resource.ConsumptionTotal) || 0,
      pricePerUnitBase: parseFloat(resource.PricePerUnitBase) || 0,
      priceTotalBase: parseFloat(resource.PriceTotalBase) || 0,
      type,
    });
  });
}

/**
 * Определяет тип иконки для позиции
 */
function determineIconType(item: any): ItemIconType {
  if (item.Cost) {
    return ItemIconType.Work; // Если есть Cost, это расценка (работа)
  } else if (item.Material) {
    return ItemIconType.Material;
  } else if (item.Machine) {
    return ItemIconType.Machine;
  } else if (item.Equipment) {
    return ItemIconType.Equipment;
  } else if (item.Transport) {
    return ItemIconType.Transport;
  } else {
    return ItemIconType.Other;
  }
}

/**
 * Определяет метку (лейбл) для позиции
 */
function determineLabel(item: any): string {
  if (item.Cost) {
    return "Расценка";
  } else if (item.Material) {
    return "Материал";
  } else if (item.Machine) {
    return "Машины и механизмы";
  } else if (item.Equipment) {
    return "Оборудование";
  } else if (item.Transport) {
    return "Транспорт";
  } else {
    return "Прочее";
  }
}

/**
 * Форматирует дату из объекта с полями Year, Month, Day в строку
 */
function formatDate(dateObj: any): string {
  if (!dateObj) return "Н/Д";

  const year = dateObj.Year || "";
  const month = dateObj.Month ? String(dateObj.Month).padStart(2, "0") : "";
  const day = dateObj.Day ? String(dateObj.Day).padStart(2, "0") : "";

  if (year && month && day) {
    return `${day}.${month}.${year}`;
  }

  return "Н/Д";
}

/**
 * Генерирует уникальный идентификатор
 */
function generateUniqueId(): string {
  return Date.now().toString(36) + Math.random().toString(36).substr(2);
}
