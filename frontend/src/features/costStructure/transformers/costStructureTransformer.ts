// src/features/costStructure/transformers/costStructureTransformer.ts

import {
  CostStructureDTO,
  CostStructureElement,
} from "../types/CostStructureDTO";

/**
 * Преобразует данные из JSON формата сметы в CostStructureDTO
 *
 * @param jsonData - JSON данные сметы
 * @returns Объект CostStructureDTO
 */
export function transformToCostStructureDTO(jsonData: any): CostStructureDTO {
  // Проверяем наличие необходимых данных
  if (!jsonData || !jsonData.Object || !jsonData.Object.Estimate) {
    throw new Error("Invalid estimate data structure");
  }

  const estimate = jsonData.Object.Estimate;
  const summary = estimate.EstimatePrice?.Summary || {};

  // Извлекаем значения затрат
  const currentTotal = parseFloat(summary.Total?.PriceCurrent) || 0;
  const baseTotal = parseFloat(summary.Total?.PriceBase) || 0;

  const currentLabor = parseFloat(summary.WorkersSalary?.PriceCurrent) || 0;
  const baseLabor = parseFloat(summary.WorkersSalary?.PriceBase) || 0;

  const currentMachinery = parseFloat(summary.Machines?.PriceCurrent) || 0;
  const baseMachinery = parseFloat(summary.Machines?.PriceBase) || 0;

  const currentMaterials =
    parseFloat(summary.Materials?.Total?.PriceCurrent) || 0;
  const baseMaterials = parseFloat(summary.Materials?.Total?.PriceBase) || 0;

  const currentOverhead = parseFloat(summary.Overhead?.PriceCurrent) || 0;
  const baseOverhead = parseFloat(summary.Overhead?.PriceBase) || 0;

  const currentProfit = parseFloat(summary.Profit?.PriceCurrent) || 0;
  const baseProfit = parseFloat(summary.Profit?.PriceBase) || 0;

  // Рассчитываем прочие затраты (то, что не вошло в основные категории)
  const currentOther =
    currentTotal -
    (currentLabor +
      currentMachinery +
      currentMaterials +
      currentOverhead +
      currentProfit);
  const baseOther =
    baseTotal -
    (baseLabor + baseMachinery + baseMaterials + baseOverhead + baseProfit);

  // Формируем элементы структуры затрат
  const elements: CostStructureElement[] = [
    {
      id: "labor",
      name: "Оплата труда",
      value: currentLabor,
      baseValue: baseLabor,
      percentage: calculatePercentage(currentLabor, currentTotal),
      color: "#3B82F6", // blue-500
    },
    {
      id: "machinery",
      name: "Машины и механизмы",
      value: currentMachinery,
      baseValue: baseMachinery,
      percentage: calculatePercentage(currentMachinery, currentTotal),
      color: "#10B981", // emerald-500
    },
    {
      id: "materials",
      name: "Материалы",
      value: currentMaterials,
      baseValue: baseMaterials,
      percentage: calculatePercentage(currentMaterials, currentTotal),
      color: "#F59E0B", // amber-500
    },
    {
      id: "overhead",
      name: "Накладные расходы",
      value: currentOverhead,
      baseValue: baseOverhead,
      percentage: calculatePercentage(currentOverhead, currentTotal),
      color: "#8B5CF6", // violet-500
    },
    {
      id: "profit",
      name: "Сметная прибыль",
      value: currentProfit,
      baseValue: baseProfit,
      percentage: calculatePercentage(currentProfit, currentTotal),
      color: "#EC4899", // pink-500
    },
  ];

  // Добавляем "Прочие затраты", если они есть
  if (currentOther > 0) {
    elements.push({
      id: "other",
      name: "Прочие затраты",
      value: currentOther,
      baseValue: baseOther,
      percentage: calculatePercentage(currentOther, currentTotal),
      color: "#6B7280", // gray-500
    });
  }

  // Формируем DTO
  return {
    totalCost: currentTotal,
    totalBaseCost: baseTotal,
    elements,
    comparison: {
      base: {
        total: baseTotal,
        labor: baseLabor,
        machinery: baseMachinery,
        materials: baseMaterials,
        overhead: baseOverhead,
        profit: baseProfit,
        other: baseOther,
      },
      current: {
        total: currentTotal,
        labor: currentLabor,
        machinery: currentMachinery,
        materials: currentMaterials,
        overhead: currentOverhead,
        profit: currentProfit,
        other: currentOther,
      },
    },
    indices: {
      labor: calculateIndex(currentLabor, baseLabor),
      machinery: calculateIndex(currentMachinery, baseMachinery),
      materials: calculateIndex(currentMaterials, baseMaterials),
      overhead: calculateIndex(currentOverhead, baseOverhead),
      profit: calculateIndex(currentProfit, baseProfit),
      total: calculateIndex(currentTotal, baseTotal),
    },
    meta: {
      currencySymbol: "₽",
      chartTitle: "Структура затрат",
      dateGenerated: new Date().toISOString(),
    },
  };
}

/**
 * Вычисляет процентное соотношение части к целому
 */
function calculatePercentage(part: number, total: number): number {
  if (total === 0) return 0;
  return parseFloat(((part / total) * 100).toFixed(2));
}

/**
 * Вычисляет индекс (соотношение текущей и базисной цены)
 */
function calculateIndex(current: number, base: number): number {
  if (base === 0) return 0;
  return parseFloat((current / base).toFixed(2));
}
