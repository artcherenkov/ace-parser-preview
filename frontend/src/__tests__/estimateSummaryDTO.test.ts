// estimateSummary.test.ts
import { expect } from "jest";

// Мокаем входные данные для тестов
const mockRawData = {
  Object: {
    Estimate: {
      EstimatePrice: {
        Summary: {
          Total: {
            PriceBase: "645565.33",
            PriceCurrent: "8254549.76",
          },
          Direct: {
            PriceBase: "572557.75",
            PriceCurrent: "5610127.81",
          },
          WorkersSalary: {
            PriceBase: "43191.48",
            PriceCurrent: "1666759.2",
          },
          Machines: {
            PriceBase: "16140.93",
            PriceCurrent: "207088.13",
          },
          MachinistSalary: {
            PriceBase: "2742.85",
            PriceCurrent: "0",
          },
          Materials: {
            Total: {
              PriceBase: "513225.34",
              PriceCurrent: "3736280.48",
            },
          },
          Overhead: {
            PriceBase: "44830.96",
            PriceCurrent: "1621892.2",
          },
          Profit: {
            PriceBase: "28176.62",
            PriceCurrent: "1022529.75",
          },
        },
      },
    },
  },
};

describe("EstimateSummary Transformer", () => {
  // Тест трансформации исходных данных в DTO
  test("transformToEstimateSummary transforms raw data correctly", () => {
    const result = transformToEstimateSummary(mockRawData);

    // Проверяем общую стоимость
    expect(result.total.base).toBe(645565.33);
    expect(result.total.current).toBe(8254549.76);
    expect(result.total.indexValue).toBe(12.79);

    // Проверяем прямые затраты
    expect(result.direct.base).toBe(572557.75);
    expect(result.direct.current).toBe(5610127.81);

    // Проверяем структуру затрат
    expect(result.costStructure.workersSalary).toBeCloseTo(20.19, 1);
    expect(result.costStructure.materials).toBeCloseTo(45.26, 1);

    // Проверяем форматированные строки
    expect(result.display.formattedTotalCurrent).toBe("8 254 549,76 ₽");
  });

  // Тест извлечения пары значений стоимостей
  test("extractCostPair calculates index value correctly", () => {
    const testItem = {
      PriceBase: "100",
      PriceCurrent: "250",
    };

    const result = extractCostPair(testItem);

    expect(result.base).toBe(100);
    expect(result.current).toBe(250);
    expect(result.indexValue).toBe(2.5);
  });

  // Тест обработки нулевых значений
  test("extractCostPair handles zero base value", () => {
    const testItem = {
      PriceBase: "0",
      PriceCurrent: "250",
    };

    const result = extractCostPair(testItem);

    expect(result.base).toBe(0);
    expect(result.current).toBe(250);
    expect(result.indexValue).toBe(0);
  });

  // Тест расчета структуры затрат
  test("calculateCostStructure calculates percentages correctly", () => {
    const costs = {
      workersSalary: 1000,
      machines: 500,
      materials: 3000,
      overhead: 400,
      profit: 100,
    };

    const result = calculateCostStructure(costs);

    // Общая сумма: 5000
    expect(result.workersSalary).toBe(20); // 1000/5000 * 100
    expect(result.machines).toBe(10); // 500/5000 * 100
    expect(result.materials).toBe(60); // 3000/5000 * 100
    expect(result.overhead).toBe(8); // 400/5000 * 100
    expect(result.profit).toBe(2); // 100/5000 * 100
  });

  // Тест форматирования валюты
  test("formatCurrency formats number correctly", () => {
    expect(formatCurrency(1234567.89)).toBe("1 234 567,89 ₽");
    expect(formatCurrency("9876.54")).toBe("9 876,54 ₽");
    expect(formatCurrency(0)).toBe("0,00 ₽");
  });
});
