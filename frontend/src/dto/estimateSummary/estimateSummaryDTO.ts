import { formatCurrency, roundValue } from "../../utils/utils.ts";
import { EstimateSummaryDTO } from "./types.ts";

/**
 * Извлекает пару значений базового и текущего уровня цен
 * и вычисляет индекс изменения
 * @param costItem Элемент затрат из исходного JSON
 * @returns Объект с базовым, текущим значением и индексом
 */
function extractCostPair(costItem: any): {
  base: number;
  current: number;
  indexValue: number;
} {
  // Парсим базовое и текущее значение из строк в числа
  const base = parseFloat(costItem.PriceBase || "0");
  const current = parseFloat(costItem.PriceCurrent || "0");

  // Вычисляем индекс (отношение текущей цены к базовой)
  // Избегаем деления на ноль
  const indexValue = base > 0 ? roundValue(current / base, 2) : 0;

  return { base, current, indexValue };
}

/**
 * Рассчитывает процентное соотношение элементов затрат
 * @param costs Объект с значениями различных элементов затрат
 * @returns Объект с процентным соотношением каждого элемента
 */
function calculateCostStructure(costs: {
  workersSalary: number;
  machines: number;
  materials: number;
  overhead: number;
  profit: number;
}): {
  workersSalary: number;
  machines: number;
  materials: number;
  overhead: number;
  profit: number;
} {
  // Считаем общую сумму
  const total = Object.values(costs).reduce((sum, value) => sum + value, 0);

  // Если общая сумма нулевая, возвращаем нули во избежание деления на ноль
  if (total === 0) {
    return {
      workersSalary: 0,
      machines: 0,
      materials: 0,
      overhead: 0,
      profit: 0,
    };
  }

  // Вычисляем доли и округляем до двух знаков после запятой
  return {
    workersSalary: roundValue((costs.workersSalary / total) * 100, 2),
    machines: roundValue((costs.machines / total) * 100, 2),
    materials: roundValue((costs.materials / total) * 100, 2),
    overhead: roundValue((costs.overhead / total) * 100, 2),
    profit: roundValue((costs.profit / total) * 100, 2),
  };
}

/**
 * Преобразует исходные данные JSON-сметы в формат EstimateSummaryDTO
 * @param rawData Исходные данные JSON
 * @returns Объект EstimateSummaryDTO с агрегированными показателями
 */
export function transformToEstimateSummary(rawData: any): EstimateSummaryDTO {
  // Получаем ссылку на данные сводных показателей сметы
  const estimatePrice = rawData.Object.Estimate.EstimatePrice;
  const summary = estimatePrice.Summary;

  // Извлекаем базовые показатели
  const total = extractCostPair(summary.Total);
  const direct = extractCostPair(summary.Direct);
  const workersSalary = extractCostPair(summary.WorkersSalary);
  const machines = extractCostPair(summary.Machines);
  const machinistSalary = extractCostPair(summary.MachinistSalary);
  const materials = extractCostPair(summary.Materials.Total);
  const overhead = extractCostPair(summary.Overhead);
  const profit = extractCostPair(summary.Profit);

  // Рассчитываем структуру затрат (процентные соотношения)
  const costStructure = calculateCostStructure({
    workersSalary: workersSalary.current,
    machines: machines.current,
    materials: materials.current,
    overhead: overhead.current,
    profit: profit.current,
  });

  // Возвращаем сформированный DTO
  return {
    total,
    direct,
    workersSalary,
    machines,
    machinistSalary,
    materials,
    overhead,
    profit,
    costStructure,
    display: {
      formattedTotalCurrent: formatCurrency(total.current),
      formattedTotalBase: formatCurrency(total.base),
    },
  };
}
