// src/pages/DashboardPage.tsx

import React, { useEffect, useState } from "react";
import {
  EstimateSummary,
  transformToEstimateSummaryDTO,
} from "../features/estimateSummary";
import type { EstimateSummaryDTO } from "../features/estimateSummary";

import {
  CostStructure,
  transformToCostStructureDTO,
} from "../features/costStructure";
import type { CostStructureDTO } from "../features/costStructure";

import sampleData from "../data/sampleEstimate.json";

/**
 * Основная страница дашборда сметных расчетов
 */
const DashboardPage: React.FC = () => {
  const [estimateSummary, setEstimateSummary] =
    useState<EstimateSummaryDTO | null>(null);
  const [costStructure, setCostStructure] = useState<CostStructureDTO | null>(
    null,
  );
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // В реальном приложении здесь был бы запрос к API
    // для получения данных сметы
    try {
      const summaryData = transformToEstimateSummaryDTO(sampleData);
      setEstimateSummary(summaryData);

      const costStructureData = transformToCostStructureDTO(sampleData);
      setCostStructure(costStructureData);

      setLoading(false);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Ошибка загрузки данных");
      setLoading(false);
    }
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-full p-12">
        <div className="text-lg text-gray-600">
          <svg
            className="animate-spin h-8 w-8 text-blue-600 mr-3 inline"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle
              className="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              strokeWidth="4"
            ></circle>
            <path
              className="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            ></path>
          </svg>
          Загрузка данных...
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center h-full p-12">
        <div className="text-lg text-red-600">Произошла ошибка: {error}</div>
      </div>
    );
  }

  if (!estimateSummary) {
    return (
      <div className="flex items-center justify-center h-full p-12">
        <div className="text-lg text-gray-600">Данные сметы не найдены</div>
      </div>
    );
  }

  return (
    <div className="p-6">
      <header className="mb-6">
        <h1 className="text-2xl font-bold text-gray-800">
          Дашборд сметных расчетов
        </h1>
      </header>

      <main className="space-y-8">
        <section>
          <h2 className="text-xl font-semibold text-gray-700 mb-4">
            Общая информация
          </h2>
          <EstimateSummary data={estimateSummary} />
        </section>

        {/* Здесь будут добавлены другие компоненты для дашборда */}
        <section>
          <h2 className="text-xl font-semibold text-gray-700 mb-4">
            Структура затрат
          </h2>
          {costStructure ? (
            <CostStructure data={costStructure} />
          ) : (
            <div className="bg-gray-100 rounded-lg p-12 text-center text-gray-500">
              Данные о структуре затрат не доступны
            </div>
          )}
        </section>

        <section>
          <h2 className="text-xl font-semibold text-gray-700 mb-4">
            Разделы сметы
          </h2>
          <div className="bg-gray-100 rounded-lg p-12 text-center text-gray-500">
            Сравнение разделов сметы будет добавлено позже
          </div>
        </section>
      </main>
    </div>
  );
};

export default DashboardPage;
