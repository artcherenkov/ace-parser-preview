// src/features/costStructure/components/CostStructure.tsx

import React from "react";
import { CostStructureDTO } from "../types/CostStructureDTO";
import {
  formatCurrency,
  formatNumber,
} from "../../../utils/formatters/numberFormatters";

interface CostStructureProps {
  data: CostStructureDTO;
}

/**
 * Компонент для отображения структуры затрат в виде круговой диаграммы
 */
const CostStructure: React.FC<CostStructureProps> = ({ data }) => {
  // Вычисляем размеры диаграммы
  const size = 240; // размер svg в пикселях
  const radius = size / 2;
  const center = { x: radius, y: radius };

  // Вычисляем сегменты диаграммы
  const segments = createPieSegments(data.elements, center, radius * 0.8);

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <div className="flex flex-col lg:flex-row">
        {/* Круговая диаграмма */}
        <div className="flex-shrink-0 mb-6 lg:mb-0 lg:mr-8">
          <div
            className="relative"
            style={{ width: `${size}px`, height: `${size}px` }}
          >
            <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
              {segments.map((segment, index) => (
                <path
                  key={`segment-${index}`}
                  d={segment.path}
                  fill={data.elements[index].color}
                  stroke="#fff"
                  strokeWidth="1"
                />
              ))}

              {/* Центральный круг с общей суммой */}
              <circle
                cx={center.x}
                cy={center.y}
                r={radius * 0.4}
                fill="#fff"
              />
              <text
                x={center.x}
                y={center.y - 10}
                textAnchor="middle"
                className="text-xs font-medium"
                fill="#6B7280"
              >
                Всего
              </text>
              <text
                x={center.x}
                y={center.y + 10}
                textAnchor="middle"
                className="text-sm font-semibold"
                fill="#1F2937"
              >
                {formatCurrency(data.totalCost, 0)}
              </text>
            </svg>
          </div>
        </div>

        {/* Легенда */}
        <div className="flex-1">
          <div className="grid grid-cols-1 md:grid-cols-[auto_auto] gap-3 gap-x-10 justify-start">
            {data.elements.map((element) => (
              <div key={element.id} className="flex items-center w-60">
                <div
                  className="w-4 h-4 mr-2 rounded-sm"
                  style={{ backgroundColor: element.color }}
                />
                <div className="flex-1">
                  <div className="flex justify-between items-center">
                    <span className="text-sm text-gray-600">
                      {element.name}
                    </span>
                    <span className="text-sm font-medium">
                      {formatNumber(element.percentage, 1)}%
                    </span>
                  </div>
                  <div className="text-sm font-medium text-gray-900">
                    {formatCurrency(element.value)}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Сравнение индексов по элементам затрат */}
      <div className="mt-8">
        <h4 className="text-base font-medium text-gray-700 mb-3">
          Индексы по элементам затрат
        </h4>
        <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
          {Object.entries(data.indices).map(
            ([key, value]) =>
              key !== "total" && (
                <div key={key} className="bg-gray-50 p-3 rounded">
                  <div className="text-sm text-gray-600">
                    {getElementName(key)}
                  </div>
                  <div className="text-lg font-medium">
                    ×{formatNumber(value, 2)}
                  </div>
                </div>
              ),
          )}
        </div>
      </div>
    </div>
  );
};

/**
 * Преобразует ключ элемента в понятное название
 */
function getElementName(key: string): string {
  const names: Record<string, string> = {
    labor: "Оплата труда",
    machinery: "Машины и механизмы",
    materials: "Материалы",
    overhead: "Накладные расходы",
    profit: "Сметная прибыль",
    other: "Прочие затраты",
    total: "Всего",
  };

  return names[key] || key;
}

/**
 * Создает сегменты круговой диаграммы
 */
function createPieSegments(
  elements: CostStructureDTO["elements"],
  center: { x: number; y: number },
  radius: number,
) {
  const total = elements.reduce((sum, el) => sum + el.percentage, 0);
  let startAngle = 0;

  return elements.map((element) => {
    // Вычисляем угол для сегмента на основе процентного соотношения
    const angle = (element.percentage / total) * 360;
    const endAngle = startAngle + angle;

    // Преобразуем углы в радианы
    const startRad = ((startAngle - 90) * Math.PI) / 180;
    const endRad = ((endAngle - 90) * Math.PI) / 180;

    // Вычисляем координаты для создания дуги
    const x1 = center.x + radius * Math.cos(startRad);
    const y1 = center.y + radius * Math.sin(startRad);
    const x2 = center.x + radius * Math.cos(endRad);
    const y2 = center.y + radius * Math.sin(endRad);

    // Флаг для больших дуг (более 180 градусов)
    const largeArcFlag = angle > 180 ? 1 : 0;

    // Создаем SVG-путь для сегмента
    const path = `
      M ${center.x},${center.y}
      L ${x1},${y1}
      A ${radius},${radius} 0 ${largeArcFlag},1 ${x2},${y2}
      Z
    `;

    // Обновляем начальный угол для следующего сегмента
    startAngle = endAngle;

    return { path };
  });
}

export default CostStructure;
