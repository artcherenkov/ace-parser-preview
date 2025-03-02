// src/features/detailedHierarchy/components/DetailedHierarchy.tsx

import React, { useState } from "react";
import {
  DetailedHierarchyDTO,
  SectionDTO,
  ItemDTO,
  CostItemDTO,
  ResourceItemDTO,
  ResourceDTO,
  ItemIconType,
} from "../types/DetailedHierarchyDTO";
import {
  formatCurrency,
  formatNumber,
} from "../../../utils/formatters/numberFormatters";

// Иконки для различных типов элементов
const ItemIcons: Record<ItemIconType, React.ReactNode> = {
  [ItemIconType.Material]: (
    <svg
      className="w-5 h-5 text-amber-500"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
    >
      <path d="M3.375 3C2.339 3 1.5 3.84 1.5 4.875v.75c0 1.036.84 1.875 1.875 1.875h17.25c1.035 0 1.875-.84 1.875-1.875v-.75C22.5 3.839 21.66 3 20.625 3H3.375z" />
      <path
        fillRule="evenodd"
        d="M3.087 9l.54 9.176A3 3 0 006.62 21h10.757a3 3 0 002.995-2.824L20.913 9H3.087zM12 10.5a.75.75 0 01.75.75v4.94l1.72-1.72a.75.75 0 111.06 1.06l-3 3a.75.75 0 01-1.06 0l-3-3a.75.75 0 111.06-1.06l1.72 1.72v-4.94a.75.75 0 01.75-.75z"
        clipRule="evenodd"
      />
    </svg>
  ),
  [ItemIconType.Work]: (
    <svg
      className="w-5 h-5 text-blue-500"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
    >
      <path d="M21.731 2.269a2.625 2.625 0 00-3.712 0l-1.157 1.157 3.712 3.712 1.157-1.157a2.625 2.625 0 000-3.712zM19.513 8.199l-3.712-3.712-12.15 12.15a5.25 5.25 0 00-1.32 2.214l-.8 2.685a.75.75 0 00.933.933l2.685-.8a5.25 5.25 0 002.214-1.32L19.513 8.2z" />
    </svg>
  ),
  [ItemIconType.Transport]: (
    <svg
      className="w-5 h-5 text-green-500"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
    >
      <path d="M3.375 4.5C2.339 4.5 1.5 5.34 1.5 6.375V13.5h12V6.375c0-1.036-.84-1.875-1.875-1.875h-8.25zM13.5 15h-12v2.625c0 1.035.84 1.875 1.875 1.875h.375a3 3 0 116 0h3a.75.75 0 00.75-.75V15z" />
      <path d="M8.25 19.5a1.5 1.5 0 10-3 0 1.5 1.5 0 003 0zM15.75 6.75a.75.75 0 00-.75.75v11.25c0 .087.015.17.042.248a3 3 0 015.958.464c.853-.175 1.522-.935 1.464-1.883a18.659 18.659 0 00-3.732-10.104 1.837 1.837 0 00-1.47-.725H15.75z" />
      <path d="M19.5 19.5a1.5 1.5 0 10-3 0 1.5 1.5 0 003 0z" />
    </svg>
  ),
  [ItemIconType.Machine]: (
    <svg
      className="w-5 h-5 text-teal-500"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
    >
      <path d="M18.75 12.75h1.5a.75.75 0 000-1.5h-1.5a.75.75 0 000 1.5zM12 6a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5A.75.75 0 0112 6zM12 18a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5A.75.75 0 0112 18zM3.75 6.75h1.5a.75.75 0 100-1.5h-1.5a.75.75 0 000 1.5zM5.25 18.75h-1.5a.75.75 0 010-1.5h1.5a.75.75 0 010 1.5zM3 12a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5A.75.75 0 013 12zM9 3.75a2.25 2.25 0 100 4.5 2.25 2.25 0 000-4.5zM12.75 12a2.25 2.25 0 114.5 0 2.25 2.25 0 01-4.5 0zM9 15.75a2.25 2.25 0 100 4.5 2.25 2.25 0 000-4.5z" />
    </svg>
  ),
  [ItemIconType.Equipment]: (
    <svg
      className="w-5 h-5 text-purple-500"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
    >
      <path
        fillRule="evenodd"
        d="M12 6.75a5.25 5.25 0 016.775-5.025.75.75 0 01.313 1.248l-3.32 3.319c.063.475.276.934.641 1.299.365.365.824.578 1.3.64l3.318-3.319a.75.75 0 011.248.313 5.25 5.25 0 01-5.472 6.756c-1.018-.086-1.87.1-2.309.634L7.344 21.3A3.298 3.298 0 112.7 16.657l8.684-7.151c.533-.44.72-1.291.634-2.309A5.342 5.342 0 0112 6.75zM4.117 19.125a.75.75 0 01.75-.75h.008a.75.75 0 01.75.75v.008a.75.75 0 01-.75.75h-.008a.75.75 0 01-.75-.75v-.008z"
        clipRule="evenodd"
      />
    </svg>
  ),
  [ItemIconType.Other]: (
    <svg
      className="w-5 h-5 text-gray-500"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
    >
      <path
        fillRule="evenodd"
        d="M2.25 13.5a8.25 8.25 0 018.25-8.25.75.75 0 01.75.75v6.75H18a.75.75 0 01.75.75 8.25 8.25 0 01-16.5 0z"
        clipRule="evenodd"
      />
      <path
        fillRule="evenodd"
        d="M12.75 3a.75.75 0 01.75-.75 8.25 8.25 0 018.25 8.25.75.75 0 01-.75.75h-7.5a.75.75 0 01-.75-.75V3z"
        clipRule="evenodd"
      />
    </svg>
  ),
};

// Основной интерфейс для компонента
interface DetailedHierarchyProps {
  data: DetailedHierarchyDTO;
  className?: string;
}

/**
 * Компонент для отображения детальной иерархии сметы
 */
const DetailedHierarchy: React.FC<DetailedHierarchyProps> = ({
  data,
  className = "",
}) => {
  return (
    <div className={`bg-white rounded-lg shadow ${className}`}>
      <div className="p-6 border-b">
        <h2 className="text-xl font-semibold text-gray-800">
          Детальная структура сметы
        </h2>
        <div className="text-sm text-gray-600 mt-2">
          {data.metadata.constructionName} / {data.metadata.objectName}
        </div>
        <div className="text-sm text-gray-500 mt-1">
          Смета № {data.metadata.estimateNumber} от {data.metadata.date}
        </div>
      </div>

      <div className="divide-y">
        {data.sections.map((section, index) => (
          <SectionComponent key={`section-${index}`} section={section} />
        ))}
      </div>

      <div className="p-6 bg-gray-50 rounded-b-lg">
        <div className="flex justify-between items-center">
          <span className="font-semibold text-gray-700">Итого по смете:</span>
          <div className="text-right">
            <div className="text-sm text-gray-600">
              Базисный уровень: {formatCurrency(data.totals.basePrice)}
            </div>
            <div className="font-semibold text-gray-800">
              Текущий уровень: {formatCurrency(data.totals.currentPrice)}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

/**
 * Компонент для отображения раздела сметы
 */
const SectionComponent: React.FC<{ section: SectionDTO }> = ({ section }) => {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <div className="section">
      <div
        className="p-4 bg-gray-50 cursor-pointer hover:bg-gray-100 transition-colors flex justify-between items-center"
        onClick={() => setIsExpanded(!isExpanded)}
      >
        <div className="flex items-center">
          <div className="mr-2">
            {isExpanded ? (
              <svg
                className="w-5 h-5 text-gray-500"
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
            ) : (
              <svg
                className="w-5 h-5 text-gray-500"
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
            )}
          </div>
          <h3 className="font-medium text-gray-800">
            {section.code}. {section.name}
          </h3>
        </div>
        <div className="text-right">
          <div className="text-sm text-gray-600">
            Базисный: {formatCurrency(section.totals.basePrice)}
          </div>
          <div className="font-medium">
            Текущий: {formatCurrency(section.totals.currentPrice)}
          </div>
        </div>
      </div>

      {isExpanded && (
        <div className="px-4 py-2">
          {/* Сводная информация по разделу */}
          <div className="mb-4 bg-gray-50 p-3 rounded-lg text-sm">
            <div className="grid grid-cols-3 gap-4">
              <div>
                <div className="text-gray-600">Прямые затраты:</div>
                <div className="font-medium">
                  {formatCurrency(section.totals.directCosts.basePrice)}
                </div>
              </div>
              <div>
                <div className="text-gray-600">Оплата труда:</div>
                <div className="font-medium">
                  {formatCurrency(section.totals.labor.basePrice)}
                </div>
              </div>
              <div>
                <div className="text-gray-600">Материалы:</div>
                <div className="font-medium">
                  {formatCurrency(section.totals.materials.basePrice)}
                </div>
              </div>
              <div>
                <div className="text-gray-600">Механизмы:</div>
                <div className="font-medium">
                  {formatCurrency(section.totals.machinery.basePrice)}
                </div>
              </div>
              <div>
                <div className="text-gray-600">Накладные расходы:</div>
                <div className="font-medium">
                  {formatCurrency(section.totals.overhead.basePrice)}
                </div>
              </div>
              <div>
                <div className="text-gray-600">Сметная прибыль:</div>
                <div className="font-medium">
                  {formatCurrency(section.totals.profit.basePrice)}
                </div>
              </div>
            </div>
          </div>

          {/* Список позиций */}
          <div className="space-y-3">
            {section.items.map((item, index) => (
              <ItemComponent key={`item-${item.id}-${index}`} item={item} />
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

/**
 * Компонент для отображения позиции сметы
 */
const ItemComponent: React.FC<{ item: ItemDTO }> = ({ item }) => {
  const [isExpanded, setIsExpanded] = useState(false);

  // Определяем цвет фона в зависимости от типа позиции
  const getBgColorClass = () => {
    if (item.isDetailedItem) return "bg-blue-50";

    switch (item.iconType) {
      case ItemIconType.Material:
        return "bg-amber-50";
      case ItemIconType.Machine:
        return "bg-teal-50";
      case ItemIconType.Equipment:
        return "bg-purple-50";
      case ItemIconType.Transport:
        return "bg-green-50";
      default:
        return "bg-gray-50";
    }
  };

  return (
    <div className={`border rounded-lg overflow-hidden ${getBgColorClass()}`}>
      <div
        className="p-3 flex items-center justify-between cursor-pointer hover:bg-opacity-80"
        onClick={() => setIsExpanded(!isExpanded)}
      >
        <div className="flex items-center">
          <div className="mr-3">{ItemIcons[item.iconType]}</div>
          <div>
            <div className="text-xs text-gray-500">{item.label}</div>
            <div className="font-medium text-gray-800">
              {item.isDetailedItem
                ? `${(item as CostItemDTO).cost.code} ${(item as CostItemDTO).cost.name}`
                : `${(item as ResourceItemDTO).code} ${(item as ResourceItemDTO).name}`}
            </div>
          </div>
        </div>
        <div className="flex items-center">
          <div className="text-right mr-4">
            <div className="text-sm">
              {formatCurrency(item.totals.basePrice)}
            </div>
          </div>
          <div>
            {isExpanded ? (
              <svg
                className="w-5 h-5 text-gray-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M5 15l7-7 7 7"
                />
              </svg>
            ) : (
              <svg
                className="w-5 h-5 text-gray-400"
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
            )}
          </div>
        </div>
      </div>

      {isExpanded && (
        <div className="p-4 border-t bg-white">
          {/* Разное содержимое в зависимости от типа */}
          {item.isDetailedItem ? (
            <DetailedItemContent item={item as CostItemDTO} />
          ) : (
            <ResourceItemContent item={item as ResourceItemDTO} />
          )}

          {/* Накладные расходы и прибыль, если есть */}
          {(item.overheads || item.profits) && (
            <div className="mt-4 pt-4 border-t border-gray-200">
              <h4 className="text-sm font-medium text-gray-700 mb-2">
                Накладные расходы и прибыль
              </h4>
              <div className="grid grid-cols-2 gap-4">
                {item.overheads && (
                  <div className="text-sm">
                    <div className="text-gray-600">
                      Накладные расходы ({item.overheads.value}%):
                    </div>
                    <div className="font-medium">
                      {formatCurrency(item.overheads.basePrice)}
                    </div>
                    <div className="text-xs text-gray-500">
                      {item.overheads.name}
                    </div>
                  </div>
                )}
                {item.profits && (
                  <div className="text-sm">
                    <div className="text-gray-600">
                      Сметная прибыль ({item.profits.value}%):
                    </div>
                    <div className="font-medium">
                      {formatCurrency(item.profits.basePrice)}
                    </div>
                    <div className="text-xs text-gray-500">
                      {item.profits.name}
                    </div>
                  </div>
                )}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

/**
 * Компонент для отображения содержимого детальной позиции (с расценкой)
 */
const DetailedItemContent: React.FC<{ item: CostItemDTO }> = ({ item }) => {
  const { cost } = item;
  const [showResources, setShowResources] = useState(false);

  return (
    <div>
      <div className="grid grid-cols-2 gap-x-4 gap-y-2 mb-4">
        <div>
          <div className="text-sm text-gray-600">Шифр:</div>
          <div className="font-medium">{cost.code}</div>
        </div>
        <div>
          <div className="text-sm text-gray-600">Количество:</div>
          <div className="font-medium">
            {formatNumber(cost.quantity)} {cost.unit}
          </div>
        </div>

        <div className="col-span-2">
          <div className="text-sm text-gray-600">Наименование:</div>
          <div className="font-medium">{cost.name}</div>
        </div>
      </div>

      <div className="bg-gray-50 p-3 rounded-lg mb-4">
        <h4 className="text-sm font-medium text-gray-700 mb-2">
          Стоимость единицы
        </h4>
        <div className="grid grid-cols-3 gap-4 text-sm">
          <div>
            <div className="text-gray-600">Прямые затраты:</div>
            <div className="font-medium">
              {formatCurrency(cost.perUnit.base.direct || 0)}
            </div>
          </div>
          <div>
            <div className="text-gray-600">Оплата труда:</div>
            <div className="font-medium">
              {formatCurrency(cost.perUnit.base.workersSalary || 0)}
            </div>
          </div>
          <div>
            <div className="text-gray-600">Механизмы:</div>
            <div className="font-medium">
              {formatCurrency(cost.perUnit.base.machines || 0)}
            </div>
          </div>
          <div>
            <div className="text-gray-600">Материалы:</div>
            <div className="font-medium">
              {formatCurrency(cost.perUnit.base.materials || 0)}
            </div>
          </div>
          {cost.perUnit.natural && (
            <>
              <div>
                <div className="text-gray-600">Затраты труда рабочих:</div>
                <div className="font-medium">
                  {formatNumber(cost.perUnit.natural.laborCosts || 0)} чел-ч
                </div>
              </div>
              <div>
                <div className="text-gray-600">Затраты труда машинистов:</div>
                <div className="font-medium">
                  {formatNumber(cost.perUnit.natural.machinistLaborCosts || 0)}{" "}
                  чел-ч
                </div>
              </div>
            </>
          )}
        </div>
      </div>

      <div className="bg-gray-50 p-3 rounded-lg mb-4">
        <h4 className="text-sm font-medium text-gray-700 mb-2">
          Стоимость всего
        </h4>
        <div className="grid grid-cols-3 gap-4 text-sm">
          <div>
            <div className="text-gray-600">Прямые затраты:</div>
            <div className="font-medium">
              {formatCurrency(cost.totals.base.direct || 0)}
            </div>
          </div>
          <div>
            <div className="text-gray-600">Оплата труда:</div>
            <div className="font-medium">
              {formatCurrency(cost.totals.base.workersSalary || 0)}
            </div>
          </div>
          <div>
            <div className="text-gray-600">Механизмы:</div>
            <div className="font-medium">
              {formatCurrency(cost.totals.base.machines || 0)}
            </div>
          </div>
          <div>
            <div className="text-gray-600">Материалы:</div>
            <div className="font-medium">
              {formatCurrency(cost.totals.base.materials || 0)}
            </div>
          </div>
        </div>
      </div>

      {/* Ресурсы, если они есть */}
      {(cost.resourcesInternal || cost.resources) && (
        <div>
          <button
            className="flex items-center text-blue-600 hover:text-blue-800 transition-colors mb-3"
            onClick={() => setShowResources(!showResources)}
          >
            {showResources ? (
              <svg
                className="w-4 h-4 mr-1"
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
            ) : (
              <svg
                className="w-4 h-4 mr-1"
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
            )}
            {showResources ? "Скрыть ресурсы" : "Показать ресурсы"}
          </button>

          {showResources && (
            <div className="border rounded-lg overflow-hidden">
              {cost.resourcesInternal && cost.resourcesInternal.length > 0 && (
                <div className="p-3">
                  <h5 className="text-sm font-medium text-gray-700 mb-2">
                    Внутренние ресурсы (учтены в расценке)
                  </h5>
                  <ResourcesTable resources={cost.resourcesInternal} />
                </div>
              )}

              {cost.resources && cost.resources.length > 0 && (
                <div className="p-3 border-t">
                  <h5 className="text-sm font-medium text-gray-700 mb-2">
                    Внешние ресурсы (не учтены в расценке)
                  </h5>
                  <ResourcesTable resources={cost.resources} />
                </div>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
};

/**
 * Компонент для отображения содержимого ресурсной позиции
 */
const ResourceItemContent: React.FC<{ item: ResourceItemDTO }> = ({ item }) => {
  return (
    <div className="grid grid-cols-2 gap-x-4 gap-y-2">
      <div>
        <div className="text-sm text-gray-600">Шифр:</div>
        <div className="font-medium">{item.code}</div>
      </div>
      <div>
        <div className="text-sm text-gray-600">Единица измерения:</div>
        <div className="font-medium">{item.unit}</div>
      </div>
      <div>
        <div className="text-sm text-gray-600">Количество:</div>
        <div className="font-medium">{formatNumber(item.consumption)}</div>
      </div>
      <div>
        <div className="text-sm text-gray-600">Цена за единицу:</div>
        <div className="font-medium">
          {formatCurrency(item.pricePerUnitBase || 0)}
        </div>
      </div>
      <div className="col-span-2">
        <div className="text-sm text-gray-600">Наименование:</div>
        <div className="font-medium">{item.name}</div>
      </div>
    </div>
  );
};

/**
 * Компонент для отображения таблицы ресурсов
 */
const ResourcesTable: React.FC<{ resources: ResourceDTO[] }> = ({
  resources,
}) => {
  // Группируем ресурсы по типу
  const groupedResources = resources.reduce(
    (acc, resource) => {
      if (!acc[resource.type]) {
        acc[resource.type] = [];
      }
      acc[resource.type].push(resource);
      return acc;
    },
    {} as Record<string, ResourceDTO[]>,
  );

  // Заголовки для групп ресурсов
  const typeHeaders = {
    worker: "Затраты труда рабочих",
    machine: "Машины и механизмы",
    material: "Материалы",
    equipment: "Оборудование",
  };

  return (
    <div className="space-y-4">
      {Object.entries(groupedResources).map(([type, typeResources]) => (
        <div key={`resource-group-${type}`}>
          <h6 className="text-xs font-medium text-gray-700 mb-2">
            {typeHeaders[type as keyof typeof typeHeaders] || "Прочее"}
          </h6>
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200 text-sm">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-3 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Код
                  </th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Наименование
                  </th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Ед. изм.
                  </th>
                  <th className="px-3 py-2 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Количество
                  </th>
                  <th className="px-3 py-2 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Цена
                  </th>
                  <th className="px-3 py-2 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Стоимость
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {typeResources.map((resource, index) => (
                  <tr key={`resource-${resource.code}-${index}`}>
                    <td className="px-3 py-2 whitespace-nowrap text-gray-600">
                      {resource.code}
                    </td>
                    <td className="px-3 py-2 text-gray-800">{resource.name}</td>
                    <td className="px-3 py-2 whitespace-nowrap text-gray-600">
                      {resource.unit}
                    </td>
                    <td className="px-3 py-2 text-right whitespace-nowrap text-gray-800">
                      {formatNumber(resource.consumption)}
                    </td>
                    <td className="px-3 py-2 text-right whitespace-nowrap text-gray-800">
                      {resource.pricePerUnitBase
                        ? formatCurrency(resource.pricePerUnitBase)
                        : "—"}
                    </td>
                    <td className="px-3 py-2 text-right whitespace-nowrap font-medium text-gray-800">
                      {resource.priceTotalBase
                        ? formatCurrency(resource.priceTotalBase)
                        : "—"}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      ))}
    </div>
  );
};

export default DetailedHierarchy;
