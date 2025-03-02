// src/features/estimateSummary/components/EstimateSummary.tsx

import React from "react";
import { EstimateSummaryDTO } from "../types/EstimateSummaryDTO";
import {
  formatCurrency,
  formatIndex,
} from "../../../utils/formatters/numberFormatters";

interface EstimateSummaryProps {
  data: EstimateSummaryDTO;
}

/**
 * Компонент для отображения сводной информации по смете
 */
const EstimateSummary: React.FC<EstimateSummaryProps> = ({ data }) => {
  return (
    <div className="bg-gray-50 rounded-lg shadow p-6">
      <div className="mb-6">
        <h1 className="text-2xl font-semibold text-gray-800 mb-2">
          {data.metadata.constructionName}
        </h1>
        <h2 className="text-xl text-gray-700 mb-4">
          {data.metadata.objectName}
        </h2>
        <div className="flex flex-col md:flex-row gap-2 md:gap-4 text-sm text-gray-600 mb-2">
          <p>{data.metadata.estimateName}</p>
          <p>№ {data.metadata.estimateNumber}</p>
          <p>от {data.metadata.date}</p>
        </div>
        <div className="flex flex-col md:flex-row gap-2 md:gap-4 text-sm text-gray-600">
          <p>
            Базисный уровень цен: {data.metadata.priceBaseLevel.year}.
            {data.metadata.priceBaseLevel.month}
          </p>
          <p>
            Текущий уровень цен: {data.metadata.priceCurrentLevel.year} кв.
            {data.metadata.priceCurrentLevel.quarter}
          </p>
        </div>
      </div>

      <div className="space-y-4">
        {/* Общая стоимость */}
        <div className="bg-white rounded-lg shadow border-l-4 border-blue-600 p-4">
          <h3 className="text-lg font-medium text-gray-700 mb-3">
            Общая стоимость
          </h3>
          <div className="space-y-3">
            <div className="flex justify-between items-center">
              <span className="text-gray-600 text-sm">Базисный уровень</span>
              <span className="font-medium">
                {formatCurrency(data.totals.basePrice)}
              </span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-gray-600 text-sm">Текущий уровень</span>
              <span className="font-medium text-blue-600">
                {formatCurrency(data.totals.currentPrice)}
              </span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-gray-600 text-sm">Индекс</span>
              <span className="font-medium text-green-600">
                {formatIndex(data.totals.indexValue)}
              </span>
            </div>
          </div>
        </div>

        {/* Прямые затраты */}
        <div className="bg-white rounded-lg shadow border-l-4 border-green-600 p-4">
          <h3 className="text-lg font-medium text-gray-700 mb-3">
            Прямые затраты
          </h3>
          <div className="space-y-3">
            <div className="flex justify-between items-center">
              <span className="text-gray-600 text-sm">Базисный уровень</span>
              <span className="font-medium">
                {formatCurrency(data.directCosts.basePrice)}
              </span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-gray-600 text-sm">Текущий уровень</span>
              <span className="font-medium">
                {formatCurrency(data.directCosts.currentPrice)}
              </span>
            </div>
          </div>
        </div>

        {/* Сетка с элементами затрат */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {/* Оплата труда */}
          <div className="bg-white rounded-lg shadow p-4">
            <h3 className="text-base font-medium text-gray-700 mb-3">
              Оплата труда
            </h3>
            <div className="flex justify-between items-center">
              <span className="text-gray-600 text-sm">Текущий уровень</span>
              <span className="font-medium">
                {formatCurrency(data.labor.currentPrice)}
              </span>
            </div>
          </div>

          {/* Материалы */}
          <div className="bg-white rounded-lg shadow p-4">
            <h3 className="text-base font-medium text-gray-700 mb-3">
              Материалы
            </h3>
            <div className="flex justify-between items-center">
              <span className="text-gray-600 text-sm">Текущий уровень</span>
              <span className="font-medium">
                {formatCurrency(data.materials.currentPrice)}
              </span>
            </div>
          </div>

          {/* Машины и механизмы */}
          <div className="bg-white rounded-lg shadow p-4">
            <h3 className="text-base font-medium text-gray-700 mb-3">
              Машины и механизмы
            </h3>
            <div className="flex justify-between items-center">
              <span className="text-gray-600 text-sm">Текущий уровень</span>
              <span className="font-medium">
                {formatCurrency(data.machinery.currentPrice)}
              </span>
            </div>
          </div>

          {/* Накладные расходы */}
          <div className="bg-white rounded-lg shadow p-4">
            <h3 className="text-base font-medium text-gray-700 mb-3">
              Накладные расходы
            </h3>
            <div className="flex justify-between items-center">
              <span className="text-gray-600 text-sm">Текущий уровень</span>
              <span className="font-medium">
                {formatCurrency(data.overhead.currentPrice)}
              </span>
            </div>
          </div>

          {/* Сметная прибыль */}
          <div className="bg-white rounded-lg shadow p-4">
            <h3 className="text-base font-medium text-gray-700 mb-3">
              Сметная прибыль
            </h3>
            <div className="flex justify-between items-center">
              <span className="text-gray-600 text-sm">Текущий уровень</span>
              <span className="font-medium">
                {formatCurrency(data.profit.currentPrice)}
              </span>
            </div>
          </div>

          {/* Транспорт */}
          <div className="bg-white rounded-lg shadow p-4">
            <h3 className="text-base font-medium text-gray-700 mb-3">
              Транспорт
            </h3>
            <div className="flex justify-between items-center">
              <span className="text-gray-600 text-sm">Текущий уровень</span>
              <span className="font-medium">
                {formatCurrency(data.transport.currentPrice)}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default EstimateSummary;
