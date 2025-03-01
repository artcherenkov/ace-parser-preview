/**
 * Форматирует число в строку с разделителями групп разрядов и символом валюты
 * @param value Число для форматирования
 * @returns Отформатированная строка
 */
export function formatCurrency(value: number | string): string {
  const numValue = typeof value === "string" ? parseFloat(value) : value;

  return new Intl.NumberFormat("ru-RU", {
    style: "currency",
    currency: "RUB",
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  }).format(numValue);
}

/**
 * Округляет число до указанного количества знаков после запятой
 * @param value Исходное число
 * @param decimals Количество знаков после запятой
 * @returns Округленное число
 */
export function roundValue(value: number, decimals: number): number {
  const factor = Math.pow(10, decimals);
  return Math.round(value * factor) / factor;
}
