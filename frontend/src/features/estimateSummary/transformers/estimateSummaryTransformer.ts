import { EstimateSummaryDTO } from "../types/EstimateSummaryDTO";

/**
 * Преобразует данные из JSON формата сметы в EstimateSummaryDTO
 *
 * @param jsonData - JSON данные сметы
 * @returns Объект EstimateSummaryDTO
 */
export function transformToEstimateSummaryDTO(
  jsonData: any,
): EstimateSummaryDTO {
  // Проверяем наличие необходимых данных
  if (!jsonData || !jsonData.Object || !jsonData.Object.Estimate) {
    throw new Error("Invalid estimate data structure");
  }

  const estimate = jsonData.Object.Estimate;
  const summary = estimate.EstimatePrice?.Summary || {};

  return {
    metadata: {
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
    },
    totals: {
      basePrice: parseFloat(summary.Total?.PriceBase) || 0,
      currentPrice: parseFloat(summary.Total?.PriceCurrent) || 0,
      indexValue: calculateIndex(
        parseFloat(summary.Total?.PriceCurrent) || 0,
        parseFloat(summary.Total?.PriceBase) || 0,
      ),
    },
    directCosts: {
      basePrice: parseFloat(summary.Direct?.PriceBase) || 0,
      currentPrice: parseFloat(summary.Direct?.PriceCurrent) || 0,
    },
    labor: {
      basePrice: parseFloat(summary.Salary?.PriceBase) || 0,
      currentPrice: parseFloat(summary.Salary?.PriceCurrent) || 0,
    },
    materials: {
      basePrice: parseFloat(summary.Materials?.Total?.PriceBase) || 0,
      currentPrice: parseFloat(summary.Materials?.Total?.PriceCurrent) || 0,
    },
    machinery: {
      basePrice: parseFloat(summary.MachinesTotal?.PriceBase) || 0,
      currentPrice: parseFloat(summary.MachinesTotal?.PriceCurrent) || 0,
    },
    overhead: {
      basePrice: parseFloat(summary.Overhead?.PriceBase) || 0,
      currentPrice: parseFloat(summary.Overhead?.PriceCurrent) || 0,
    },
    profit: {
      basePrice: parseFloat(summary.Profit?.PriceBase) || 0,
      currentPrice: parseFloat(summary.Profit?.PriceCurrent) || 0,
    },
    transport: {
      basePrice: parseFloat(summary.TransportTotal?.PriceBase) || 0,
      currentPrice: parseFloat(summary.TransportTotal?.PriceCurrent) || 0,
    },
  };
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
 * Вычисляет индекс (соотношение текущей и базисной цены)
 */
function calculateIndex(current: number, base: number): number {
  if (!base || base === 0) return 0;
  return parseFloat((current / base).toFixed(2));
}
