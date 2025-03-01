// Пример использования в React-компоненте

import React from "react";
import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Legend,
  Tooltip,
} from "recharts";
import { EstimateSummaryDTO } from "./estimateSummary/types.ts";

interface EstimateSummaryCardProps {
  summary: EstimateSummaryDTO;
}

const EstimateSummaryCard: React.FC<EstimateSummaryCardProps> = ({
  summary,
}) => {
  // Подготавливаем данные для диаграммы структуры затрат
  const costStructureData = [
    { name: "Оплата труда", value: summary.costStructure.workersSalary },
    { name: "Механизмы", value: summary.costStructure.machines },
    { name: "Материалы", value: summary.costStructure.materials },
    { name: "Накладные расходы", value: summary.costStructure.overhead },
    { name: "Сметная прибыль", value: summary.costStructure.profit },
  ];

  // Цвета для диаграммы
  const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042", "#8884d8"];

  return (
    <div className="estimate-summary-card">
      <h3>Итоги по смете</h3>

      <div className="summary-values">
        <div className="summary-item">
          <span className="label">Общая стоимость (текущий уровень)</span>
          <span className="value">{summary.display.formattedTotalCurrent}</span>
        </div>

        <div className="summary-item">
          <span className="label">Базисный уровень</span>
          <span className="value">{summary.display.formattedTotalBase}</span>
        </div>

        <div className="summary-item">
          <span className="label">Индекс</span>
          <span className="value">×{summary.total.indexValue}</span>
        </div>
      </div>

      <h4>Структура затрат</h4>
      <div className="cost-structure-chart" style={{ height: 300 }}>
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie
              data={costStructureData}
              cx="50%"
              cy="50%"
              labelLine={false}
              outerRadius={80}
              fill="#8884d8"
              dataKey="value"
              label={({ name, percent }) =>
                `${name}: ${(percent * 100).toFixed(0)}%`
              }
            >
              {costStructureData.map((_entry, index) => (
                <Cell
                  key={`cell-${index}`}
                  fill={COLORS[index % COLORS.length]}
                />
              ))}
            </Pie>
            <Tooltip formatter={(value) => `${value.toFixed(2)}%`} />
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default EstimateSummaryCard;
