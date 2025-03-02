// src/features/detailedHierarchy/components/DetailedHierarchy.tsx

import React, { useState, useMemo } from "react";
import {
  DetailedHierarchyDTO,
  ResourceItem,
} from "../types/DetailedHierarchyDTO";
import {
  formatCurrency,
  formatIndex,
} from "../../../utils/formatters/numberFormatters";

interface DetailedHierarchyProps {
  data: DetailedHierarchyDTO;
}

/**
 * Компонент для отображения иерархической структуры сметы
 */
const DetailedHierarchy: React.FC<DetailedHierarchyProps> = ({ data }) => {
  // Состояние для отслеживания развернутых разделов и позиций
  const [expandedSections, setExpandedSections] = useState<
    Record<string, boolean>
  >({});
  const [expandedItems, setExpandedItems] = useState<Record<string, boolean>>(
    {},
  );

  // Состояние для фильтрации
  const [codeFilter, setCodeFilter] = useState<string>("");
  const [searchQuery, setSearchQuery] = useState<string>("");

  // Функции для раскрытия/скрытия разделов и позиций
  const toggleSection = (sectionId: string) => {
    setExpandedSections((prev) => ({
      ...prev,
      [sectionId]: !prev[sectionId],
    }));
  };

  const toggleItem = (itemId: string) => {
    setExpandedItems((prev) => ({
      ...prev,
      [itemId]: !prev[itemId],
    }));
  };

  // Фильтрация данных
  const filteredSections = useMemo(() => {
    return data.sections
      .map((section) => {
        // Фильтруем позиции в разделе
        const filteredItems = section.items.filter((item) => {
          const matchesCode = codeFilter
            ? item.code.startsWith(codeFilter)
            : true;
          const matchesSearch = searchQuery
            ? item.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
              item.code.toLowerCase().includes(searchQuery.toLowerCase())
            : true;

          return matchesCode && matchesSearch;
        });

        // Возвращаем раздел с отфильтрованными позициями
        return {
          ...section,
          items: filteredItems,
        };
      })
      .filter((section) => section.items.length > 0); // Исключаем пустые разделы
  }, [data.sections, codeFilter, searchQuery]);

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <div className="flex flex-col sm:flex-row justify-between mb-6">
        <h3 className="text-lg font-semibold text-gray-800 mb-2 sm:mb-0">
          Структура сметы
        </h3>
        <div className="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-4">
          <div>
            <label htmlFor="codeFilter" className="text-sm text-gray-600 mr-2">
              Шифр:
            </label>
            <select
              id="codeFilter"
              className="border rounded p-1 text-sm"
              value={codeFilter}
              onChange={(e) => setCodeFilter(e.target.value)}
            >
              <option value="">Все</option>
              {data.filters.availableCodes.map((code) => (
                <option key={code} value={code}>
                  {code}
                </option>
              ))}
            </select>
          </div>
          <div>
            <input
              type="text"
              placeholder="Поиск..."
              className="border rounded p-1 text-sm w-full sm:w-auto"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
          </div>
        </div>
      </div>

      {/* Статистика */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6">
        <div className="bg-blue-50 rounded p-3">
          <div className="text-sm text-gray-600">Разделы</div>
          <div className="text-lg font-semibold">
            {data.stats.sectionsCount}
          </div>
        </div>
        <div className="bg-blue-50 rounded p-3">
          <div className="text-sm text-gray-600">Позиции</div>
          <div className="text-lg font-semibold">{data.stats.itemsCount}</div>
        </div>
        <div className="bg-blue-50 rounded p-3">
          <div className="text-sm text-gray-600">Ресурсы</div>
          <div className="text-lg font-semibold">
            {data.stats.resourcesCount}
          </div>
        </div>
      </div>

      {/* Иерархическая структура */}
      <div className="border rounded-lg divide-y">
        {filteredSections.map((section) => (
          <div key={section.id} className="divide-y">
            {/* Заголовок раздела */}
            <div
              className="p-3 bg-gray-50 cursor-pointer hover:bg-gray-100 transition-colors flex items-center justify-between"
              onClick={() => toggleSection(section.id)}
            >
              <div className="flex items-center">
                <span className="mr-2">
                  {expandedSections[section.id] ? (
                    <ChevronDownIcon className="h-4 w-4 text-gray-500" />
                  ) : (
                    <ChevronRightIcon className="h-4 w-4 text-gray-500" />
                  )}
                </span>
                <div>
                  <span className="font-medium">Раздел {section.code}: </span>
                  <span>{section.name}</span>
                </div>
              </div>

              <div className="flex items-center gap-4">
                <div className="text-sm hidden md:block">
                  <span className="mr-2 text-gray-600">Базисная:</span>
                  <span>{formatCurrency(section.basePrice)}</span>
                </div>
                <div className="text-sm">
                  <span className="text-gray-600 mr-2 hidden sm:inline">
                    Индекс:
                  </span>
                  <span className="text-green-600">
                    {formatIndex(section.indexValue)}
                  </span>
                </div>
              </div>
            </div>

            {/* Содержимое раздела (позиции) */}
            {expandedSections[section.id] && (
              <div className="divide-y">
                {section.items.map((item) => (
                  <div key={item.id} className="divide-y pl-4">
                    {/* Заголовок позиции */}
                    <div
                      className={`p-3 hover:bg-gray-50 transition-colors cursor-pointer flex items-center justify-between ${item.resources.length > 0 ? "" : "opacity-70"}`}
                      onClick={() =>
                        item.resources.length > 0 && toggleItem(item.id)
                      }
                    >
                      <div className="flex items-center">
                        {item.resources.length > 0 ? (
                          <span className="mr-2">
                            {expandedItems[item.id] ? (
                              <ChevronDownIcon className="h-4 w-4 text-gray-400" />
                            ) : (
                              <ChevronRightIcon className="h-4 w-4 text-gray-400" />
                            )}
                          </span>
                        ) : (
                          <span className="w-6" />
                        )}
                        <div>
                          <div className="flex items-center gap-2">
                            <span className="text-sm text-gray-500">
                              {item.num}
                            </span>
                            <span className="text-sm font-medium text-gray-700">
                              {item.code}
                            </span>
                            {item.hasCoefficients && (
                              <span className="text-xs bg-yellow-100 text-yellow-800 px-1 py-0.5 rounded">
                                К
                              </span>
                            )}
                          </div>
                          <div className="text-sm max-w-xl truncate">
                            {item.name}
                          </div>
                        </div>
                      </div>

                      <div className="flex flex-col sm:flex-row items-end sm:items-center gap-1 sm:gap-4 text-right">
                        <div className="text-xs text-gray-500">
                          {item.quantity} {item.unit}
                        </div>
                        <div className="text-sm">
                          <span className="text-gray-600 hidden lg:inline mr-1">
                            Базисная:
                          </span>
                          <span>{formatCurrency(item.basePrice.total)}</span>
                        </div>
                      </div>
                    </div>

                    {/* Ресурсы позиции */}
                    {expandedItems[item.id] && item.resources.length > 0 && (
                      <div className="bg-gray-50 pl-6 py-1 divide-y divide-gray-100">
                        {item.resources.map((resource) => (
                          <ResourceRow key={resource.id} resource={resource} />
                        ))}
                      </div>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}

        {filteredSections.length === 0 && (
          <div className="p-8 text-center text-gray-500">
            Не найдено разделов или позиций, соответствующих заданным критериям
          </div>
        )}
      </div>

      {/* Итоги */}
      <div className="mt-6 bg-blue-50 p-4 rounded-lg">
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center">
          <div className="text-gray-700 font-medium mb-2 sm:mb-0">
            Всего по смете:
          </div>
          <div className="flex flex-col sm:flex-row gap-2 sm:gap-6">
            <div>
              <span className="text-sm text-gray-600 mr-2">Базисная:</span>
              <span className="font-medium">
                {formatCurrency(data.totals.basePrice)}
              </span>
            </div>
            <div>
              <span className="text-sm text-gray-600 mr-2">Индекс:</span>
              <span className="font-medium text-green-600">
                {formatIndex(data.totals.indexValue)}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Компонент для отображения строки ресурса
const ResourceRow: React.FC<{ resource: ResourceItem }> = ({ resource }) => {
  // Определяем цвет и иконку на основе типа ресурса
  const getTypeColor = (type: string) => {
    switch (type) {
      case "material":
        return "text-amber-600";
      case "machinery":
        return "text-emerald-600";
      case "labor":
        return "text-blue-600";
      default:
        return "text-gray-600";
    }
  };

  const getTypeIcon = (type: string) => {
    switch (type) {
      case "material":
        return <MaterialIcon className="h-4 w-4" />;
      case "machinery":
        return <MachineryIcon className="h-4 w-4" />;
      case "labor":
        return <LaborIcon className="h-4 w-4" />;
      default:
        return null;
    }
  };

  return (
    <div className="p-2 flex items-center justify-between text-sm hover:bg-gray-100">
      <div className="flex items-center gap-2">
        <span className={getTypeColor(resource.type)}>
          {getTypeIcon(resource.type)}
        </span>
        <div>
          {resource.code && (
            <span className="text-xs text-gray-500 mr-1">{resource.code}</span>
          )}
          <span>{resource.name}</span>
        </div>
      </div>

      <div className="flex items-center gap-3">
        <span className="text-xs text-gray-500">{resource.consumption}</span>
        {resource.basePrice > 0 && (
          <span>{formatCurrency(resource.basePrice)}</span>
        )}
      </div>
    </div>
  );
};

// Простые SVG-иконки
const ChevronRightIcon = ({ className = "h-6 w-6" }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    className={className}
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth={2}
      d="M9 5l7 7-7 7"
    />
  </svg>
);

const ChevronDownIcon = ({ className = "h-6 w-6" }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    className={className}
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth={2}
      d="M19 9l-7 7-7-7"
    />
  </svg>
);

const MaterialIcon = ({ className = "h-6 w-6" }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    className={className}
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth={2}
      d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"
    />
  </svg>
);

const MachineryIcon = ({ className = "h-6 w-6" }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    className={className}
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth={2}
      d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
    />
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth={2}
      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
    />
  </svg>
);

const LaborIcon = ({ className = "h-6 w-6" }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    className={className}
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth={2}
      d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
    />
  </svg>
);

export default DetailedHierarchy;
