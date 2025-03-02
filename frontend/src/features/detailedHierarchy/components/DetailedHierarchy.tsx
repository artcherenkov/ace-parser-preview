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
    <div className={`bg-white rounded-lg shadow-md ${className}`}>
      <div className="p-6 border-b border-gray-100">
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

      <div className="divide-y divide-gray-100">
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
          <div className="mr-2 text-gray-400">
            {isExpanded ? (
              <svg
                className="w-5 h-5"
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
                className="w-5 h-5"
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
          <div>
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
 * Иконки для различных типов элементов и ресурсов
 * (используем outline варианты иконок)
 */
const ItemIcons = {
  [ItemIconType.Material]: (
    <svg
      className="w-5 h-5 text-amber-500"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={1.5}
        d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"
      />
    </svg>
  ),
  [ItemIconType.Work]: (
    <svg
      className="w-5 h-5 text-blue-500"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={1.5}
        d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"
      />
    </svg>
  ),
  [ItemIconType.Transport]: (
    <svg
      className="w-5 h-5 text-green-500"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={1.5}
        d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"
      />
    </svg>
  ),
  [ItemIconType.Machine]: (
    <svg
      className="w-5 h-5 text-teal-500"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={1.5}
        d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
      />
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={1.5}
        d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
      />
    </svg>
  ),
  [ItemIconType.Equipment]: (
    <svg
      className="w-5 h-5 text-purple-500"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={1.5}
        d="M11 4a2 2 0 114 0v1a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-1a2 2 0 100 4h1a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-1a2 2 0 10-4 0v1a1 1 0 01-1 1H7a1 1 0 01-1-1v-3a1 1 0 00-1-1H4a2 2 0 110-4h1a1 1 0 001-1V7a1 1 0 011-1h3a1 1 0 001-1V4z"
      />
    </svg>
  ),
  [ItemIconType.Other]: (
    <svg
      className="w-5 h-5 text-gray-500"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={1.5}
        d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
      />
    </svg>
  ),
};

/**
 * Иконки для типов ресурсов в таблице (outline варианты)
 */
const ResourceIcons = {
  worker: (
    <svg
      className="w-5 h-5 text-blue-500"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      {/* Icon representing a construction worker with helmet */}
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={1.5}
        d="M16 7a4 4 0 11-8 0 4 4 0 018 0z"
      />
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={1.5}
        d="M12 14c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"
      />
    </svg>
  ),
  machine: (
    <svg
      className="w-5 h-5 text-teal-500"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      {/* Gear icon representing construction machinery */}
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={1.5}
        d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
      />
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={1.5}
        d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
      />
    </svg>
  ),
  material: (
    <svg
      className="w-5 h-5 text-amber-500"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={1.5}
        d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"
      />
    </svg>
  ),
  equipment: (
    <svg
      className="w-5 h-5 text-purple-500"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={1.5}
        d="M11 4a2 2 0 114 0v1a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-1a2 2 0 100 4h1a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-1a2 2 0 10-4 0v1a1 1 0 01-1 1H7a1 1 0 01-1-1v-3a1 1 0 00-1-1H4a2 2 0 110-4h1a1 1 0 001-1V7a1 1 0 011-1h3a1 1 0 001-1V4z"
      />
    </svg>
  ),
};

/**
 * Компонент для отображения позиции сметы
 */
const ItemComponent: React.FC<{ item: ItemDTO }> = ({ item }) => {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <div className="border-b border-gray-100">
      <div
        className="p-3 flex items-center justify-between cursor-pointer hover:bg-gray-50 transition-colors"
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
        <div className="p-4 bg-gray-50 border-t border-gray-100">
          {/* Разное содержимое в зависимости от типа */}
          {item.isDetailedItem ? (
            <DetailedItemContent item={item as CostItemDTO} />
          ) : (
            <ResourceItemContent item={item as ResourceItemDTO} />
          )}

          {/* Накладные расходы и прибыль, если есть */}
          {(item.overheads || item.profits) && (
            <div className="mt-4 pt-4 border-t border-gray-100">
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

  // Функция для форматирования количества с предлогом при необходимости
  const formatQuantityWithUnit = (quantity: number, unit: string) => {
    if (unit.includes("100 ")) {
      return `${formatNumber(quantity)} × ${unit}`;
    }
    return `${formatNumber(quantity)} ${unit}`;
  };

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
            {formatQuantityWithUnit(cost.quantity, cost.unit)}
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
          {/* Add labor costs to "Total Cost" section */}
          {cost.totals.natural && (
            <>
              <div>
                <div className="text-gray-600">Затраты труда рабочих:</div>
                <div className="font-medium">
                  {formatNumber(cost.totals.natural.laborCosts || 0)} чел-ч
                </div>
              </div>
              <div>
                <div className="text-gray-600">Затраты труда машинистов:</div>
                <div className="font-medium">
                  {formatNumber(cost.totals.natural.machinistLaborCosts || 0)}{" "}
                  чел-ч
                </div>
              </div>
            </>
          )}
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
            <div className="rounded-lg overflow-hidden bg-white border border-gray-100">
              {cost.resourcesInternal && cost.resourcesInternal.length > 0 && (
                <div className="p-3">
                  <h5 className="text-sm font-medium text-gray-700 mb-2">
                    Внутренние ресурсы (учтены в расценке)
                  </h5>
                  <ResourcesTable resources={cost.resourcesInternal} />
                </div>
              )}

              {cost.resources && cost.resources.length > 0 && (
                <div className="p-3 border-t border-gray-100">
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
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full text-sm">
        <thead className="bg-gray-50">
          <tr>
            <th className="px-3 py-2 text-left">Тип</th>
            <th className="px-3 py-2 text-left">Код</th>
            <th className="px-3 py-2 text-left">Наименование</th>
            <th className="px-3 py-2 text-left">Ед. изм.</th>
            <th className="px-3 py-2 text-right">Количество</th>
            <th className="px-3 py-2 text-right">Цена</th>
            <th className="px-3 py-2 text-right">Стоимость</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-100">
          {resources.map((resource, index) => {
            // Format "средний разряд работы" with value included in name
            let displayName = resource.name;
            let displayConsumption = formatNumber(resource.consumption);

            if (resource.code === "1.1") {
              displayName = `${resource.name} – ${resource.consumption}`;
              displayConsumption = "";
            }

            return (
              <tr
                key={`resource-${resource.code}-${index}`}
                className="hover:bg-gray-50 transition-colors"
              >
                <td className="px-3 py-2">
                  {ResourceIcons[resource.type] || (
                    <svg
                      className="w-5 h-5 text-gray-400"
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <circle cx="12" cy="12" r="10" strokeWidth="1.5" />
                      <line x1="12" y1="8" x2="12" y2="12" strokeWidth="1.5" />
                      <line
                        x1="12"
                        y1="16"
                        x2="12.01"
                        y2="16"
                        strokeWidth="1.5"
                      />
                    </svg>
                  )}
                </td>
                <td className="px-3 py-2 whitespace-nowrap text-gray-600">
                  {resource.code}
                </td>
                <td className="px-3 py-2 text-gray-800">{displayName}</td>
                <td className="px-3 py-2 whitespace-nowrap text-gray-600">
                  {resource.unit}
                </td>
                <td className="px-3 py-2 text-right whitespace-nowrap text-gray-800">
                  {displayConsumption}
                </td>
                <td className="px-3 py-2 text-right whitespace-nowrap text-gray-800">
                  {resource.pricePerUnitBase
                    ? formatCurrency(resource.pricePerUnitBase)
                    : "—"}
                </td>
                <td className="px-3 py-2 text-right whitespace-nowrap">
                  {resource.priceTotalBase ? (
                    <div className="font-medium text-gray-800">
                      {formatCurrency(resource.priceTotalBase)}
                    </div>
                  ) : (
                    "—"
                  )}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

export default DetailedHierarchy;
