// src/features/detailedHierarchy/transformers/detailedHierarchyTransformer.ts

import {
  DetailedHierarchyDTO,
  EstimateSection,
  EstimateItem,
  ResourceItem,
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
  const summary = estimate.EstimatePrice?.Summary || {};
  const jsonSections = Array.isArray(estimate.Sections?.Section)
    ? estimate.Sections.Section
    : [estimate.Sections?.Section].filter(Boolean);

  // Общие счетчики для статистики
  let totalItemsCount = 0;
  let totalResourcesCount = 0;
  const allCodes = new Set<string>();
  const allTypes = new Map<string, string>();

  // Преобразуем разделы
  const sections: EstimateSection[] = jsonSections.map(
    (jsonSection: any, index: number) => {
      const sectionId = jsonSection.Code || String(index + 1);

      // Преобразуем позиции раздела
      const jsonItems = Array.isArray(jsonSection.Items?.Item)
        ? jsonSection.Items.Item
        : [jsonSection.Items?.Item].filter(Boolean);

      const items: EstimateItem[] = jsonItems.map(
        (jsonItem: any, itemIndex: number) => {
          totalItemsCount++;

          // Получаем шифр и добавляем в список всех шифров
          const code = jsonItem.Cost?.Code || "";
          if (code) {
            allCodes.add(code.split("-")[0]);
          }

          // Если указан тип работ, добавляем его в список типов
          const workType = jsonItem.WorkType || "";
          if (workType) {
            allTypes.set(workType, workType);
          }

          // Преобразуем ресурсы позиции
          const resources: ResourceItem[] = [];

          // Добавляем материалы
          if (jsonItem.Material) {
            const material = jsonItem.Material;
            totalResourcesCount++;

            resources.push({
              id: `${sectionId}-${itemIndex + 1}-material-${material.Num || 1}`,
              code: material.Code || "",
              name: material.Name || "",
              type: "material",
              unit: material.Unit || "",
              quantity: parseFloat(material.ConsumptionTotal) || 0,
              consumption: `${material.ConsumptionTotal || 0} ${material.Unit || ""}`,
              basePrice: parseFloat(material.PriceTotalBase) || 0,
              currentPrice: calculateCurrentPrice(
                material.PriceTotalBase,
                7.28,
              ), // Используем средний индекс для материалов
              indexValue: 7.28, // Средний индекс для материалов
            });
          }

          // Добавляем ресурсы из Cost.ResourcesInternal при наличии
          if (jsonItem.Cost?.ResourcesInternal) {
            // Обрабатываем материалы
            const materials = Array.isArray(
              jsonItem.Cost.ResourcesInternal.Material,
            )
              ? jsonItem.Cost.ResourcesInternal.Material
              : [jsonItem.Cost.ResourcesInternal.Material].filter(Boolean);

            materials.forEach((material: any, resIndex: number) => {
              if (!material) return;
              totalResourcesCount++;

              resources.push({
                id: `${sectionId}-${itemIndex + 1}-material-int-${resIndex + 1}`,
                code: material.Code || "",
                name: material.Name || "",
                type: "material",
                unit: material.Unit || "",
                quantity: parseFloat(material.ConsumptionTotal) || 0,
                consumption: `${material.ConsumptionTotal || 0} ${material.Unit || ""}`,
                basePrice: parseFloat(material.PriceTotalBase) || 0,
                currentPrice: calculateCurrentPrice(
                  material.PriceTotalBase,
                  7.28,
                ),
                indexValue: 7.28,
              });
            });

            // Обрабатываем машины и механизмы
            const machines = Array.isArray(
              jsonItem.Cost.ResourcesInternal.Machine,
            )
              ? jsonItem.Cost.ResourcesInternal.Machine
              : [jsonItem.Cost.ResourcesInternal.Machine].filter(Boolean);

            machines.forEach((machine: any, resIndex: number) => {
              if (!machine) return;
              totalResourcesCount++;

              resources.push({
                id: `${sectionId}-${itemIndex + 1}-machine-${resIndex + 1}`,
                code: machine.Code || "",
                name: machine.Name || "",
                type: "machinery",
                unit: machine.Unit || "",
                quantity: parseFloat(machine.ConsumptionTotal) || 0,
                consumption: `${machine.ConsumptionTotal || 0} ${machine.Unit || ""}`,
                basePrice: parseFloat(machine.PriceTotalBase) || 0,
                currentPrice: calculateCurrentPrice(
                  machine.PriceTotalBase,
                  12.83,
                ),
                indexValue: 12.83,
              });
            });

            // Обрабатываем трудовые ресурсы
            const workers = Array.isArray(
              jsonItem.Cost.ResourcesInternal.Worker,
            )
              ? jsonItem.Cost.ResourcesInternal.Worker
              : [jsonItem.Cost.ResourcesInternal.Worker].filter(Boolean);

            workers.forEach((worker: any, resIndex: number) => {
              if (!worker) return;
              totalResourcesCount++;

              resources.push({
                id: `${sectionId}-${itemIndex + 1}-worker-${resIndex + 1}`,
                code: worker.Code || "",
                name: worker.Name || "",
                type: "labor",
                unit: worker.Unit || "",
                quantity: parseFloat(worker.ConsumptionTotal) || 0,
                consumption: `${worker.ConsumptionTotal || 0} ${worker.Unit || ""}`,
                basePrice: 0, // Обычно не указывается
                currentPrice: 0, // Обычно не указывается
                indexValue: 38.59,
              });
            });
          }

          // Обрабатываем коэффициенты
          const hasCoefficients = !!jsonItem.Cost?.Coefficients;
          let coefficients = undefined;

          if (hasCoefficients && jsonItem.Cost?.Coefficients?.Coefficient) {
            const jsonCoefficients = Array.isArray(
              jsonItem.Cost.Coefficients.Coefficient,
            )
              ? jsonItem.Cost.Coefficients.Coefficient
              : [jsonItem.Cost.Coefficients.Coefficient].filter(Boolean);

            coefficients = jsonCoefficients.map((coef: any) => ({
              name: coef.Name || "",
              value: parseCoefficient(coef),
            }));
          }

          // Создаем объект позиции
          return {
            id: `${sectionId}-${itemIndex + 1}`,
            num: jsonItem.Cost?.Num || itemIndex + 1,
            code: jsonItem.Cost?.Code || "",
            name: jsonItem.Cost?.Name || "",
            unit: jsonItem.Cost?.Unit || "",
            quantity: parseFloat(jsonItem.Cost?.Quantity) || 0,
            basePrice: {
              direct: parseFloat(jsonItem.Cost?.Totals?.Base?.Direct) || 0,
              total: parseFloat(jsonItem.Cost?.Totals?.Base) || 0,
            },
            currentPrice: {
              direct: parseFloat(jsonItem.Cost?.Totals?.Current?.Direct) || 0,
              total:
                parseFloat(jsonItem.Current?.total) ||
                calculateCurrentPrice(
                  jsonItem.Cost?.Totals?.Base,
                  jsonItem.indexValue || 12.79,
                ),
            },
            indexValue: parseFloat(jsonItem.indexValue) || 12.79,
            resources,
            hasCoefficients,
            coefficients,
          };
        },
      );

      // Получаем итоги по разделу
      const sectionPrice = jsonSection.SectionPrice || {};
      const sectionSummary = sectionPrice.Summary || {};

      return {
        id: String(sectionId),
        code: parseInt(sectionId, 10) || index + 1,
        name: jsonSection.Name || `Раздел ${sectionId}`,
        basePrice: parseFloat(sectionSummary.Total?.PriceBase) || 0,
        currentPrice: parseFloat(sectionSummary.Total?.PriceCurrent) || 0,
        indexValue: calculateIndex(
          parseFloat(sectionSummary.Total?.PriceCurrent) || 0,
          parseFloat(sectionSummary.Total?.PriceBase) || 0,
        ),
        items,
      };
    },
  );

  return {
    sections,
    stats: {
      sectionsCount: sections.length,
      itemsCount: totalItemsCount,
      resourcesCount: totalResourcesCount,
    },
    totals: {
      basePrice: parseFloat(summary.Total?.PriceBase) || 0,
      currentPrice: parseFloat(summary.Total?.PriceCurrent) || 0,
      indexValue: calculateIndex(
        parseFloat(summary.Total?.PriceCurrent) || 0,
        parseFloat(summary.Total?.PriceBase) || 0,
      ),
    },
    filters: {
      availableCodes: Array.from(allCodes),
      availableTypes: Array.from(allTypes.entries()).map(([code, name]) => ({
        code,
        name,
      })),
    },
    meta: {
      currencySymbol: "₽",
      dateGenerated: new Date().toISOString(),
      estimateName: estimate.Name || "",
      estimateNumber: estimate.Num || "",
    },
  };
}

/**
 * Вычисляет индекс (соотношение текущей и базисной цены)
 */
function calculateIndex(current: number, base: number): number {
  if (base === 0) return 0;
  return parseFloat((current / base).toFixed(2));
}

/**
 * Вычисляет текущую цену на основе базисной и индекса
 */
function calculateCurrentPrice(
  basePrice: string | number,
  index: number,
): number {
  const base =
    typeof basePrice === "string" ? parseFloat(basePrice) : basePrice;
  if (isNaN(base)) return 0;
  return parseFloat((base * index).toFixed(2));
}

/**
 * Извлекает значение коэффициента из объекта коэффициента
 */
function parseCoefficient(coef: any): number {
  try {
    if (coef.Values?.Value) {
      const values = Array.isArray(coef.Values.Value)
        ? coef.Values.Value
        : [coef.Values.Value];

      // Ищем значение коэффициента
      for (const val of values) {
        if (val.CoefValue) {
          return parseFloat(val.CoefValue);
        }
      }
    }
    return 1.0;
  } catch (e) {
    return 1.0;
  }
}
