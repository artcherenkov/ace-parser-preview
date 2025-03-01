/**
 * Форматирует число как денежное значение в рублях
 *
 * @param value - Число для форматирования
 * @param decimalPlaces - Количество знаков после запятой (по умолчанию 2)
 * @returns Отформатированная строка с денежным значением
 */
export function formatCurrency(
  value: number,
  decimalPlaces: number = 2,
): string {
  if (isNaN(value)) return "0,00 ₽";

  return new Intl.NumberFormat("ru-RU", {
    style: "currency",
    currency: "RUB",
    minimumFractionDigits: decimalPlaces,
    maximumFractionDigits: decimalPlaces,
  }).format(value);
}

/**
 * Форматирует число с разделителями разрядов
 *
 * @param value - Число для форматирования
 * @param decimalPlaces - Количество знаков после запятой (по умолчанию 2)
 * @returns Отформатированная строка
 */
export function formatNumber(value: number, decimalPlaces: number = 2): string {
  if (isNaN(value)) return "0";

  return new Intl.NumberFormat("ru-RU", {
    minimumFractionDigits: decimalPlaces,
    maximumFractionDigits: decimalPlaces,
  }).format(value);
}

/**
 * Форматирует множитель/индекс с префиксом '×'
 *
 * @param value - Значение индекса
 * @param decimalPlaces - Количество знаков после запятой (по умолчанию 2)
 * @returns Отформатированная строка
 */
export function formatIndex(value: number, decimalPlaces: number = 2): string {
  if (isNaN(value) || value === 0) return "—";

  return `×${formatNumber(value, decimalPlaces)}`;
}
