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
 * Иконки для различных типов элементов и ресурсов
 */
const ItemIcons = {
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
        d="M3.087 9l.54 9.176A3 3 0 006.62 21h10.757a3 3 0 002.995-2.824L20.913 9H3.087zm8.913 1.5a.75.75 0 01.75.75v4.94l1.72-1.72a.75.75 0 111.06 1.06l-3 3a.75.75 0 01-1.06 0l-3-3a.75.75 0 111.06-1.06l1.72 1.72v-4.94a.75.75 0 01.75-.75z"
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
      <path d="M5.566 4.657A4.505 4.505 0 016.75 4.5h10.5c.41 0 .806.055 1.183.157A3 3 0 0015.75 3h-7.5a3 3 0 00-2.684 1.657zM2.25 12a3 3 0 013-3h13.5a3 3 0 013 3v6a3 3 0 01-3 3H5.25a3 3 0 01-3-3v-6zM5.25 7.5c-.41 0-.806.055-1.184.157A3 3 0 016.75 6h10.5a3 3 0 012.683 1.657A4.505 4.505 0 0018.75 7.5H5.25z" />
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
      <path d="M19.906 9c.382 0 .749.057 1.094.162V9a3 3 0 00-3-3h-3.879a.75.75 0 01-.53-.22L11.47 3.66A2.25 2.25 0 009.879 3H6a3 3 0 00-3 3v3.162A3.756 3.756 0 014.094 9h15.812zM4.094 10.5a2.25 2.25 0 00-2.227 2.568l.857 6A2.25 2.25 0 004.951 21H19.05a2.25 2.25 0 002.227-1.932l.857-6a2.25 2.25 0 00-2.227-2.568H4.094z" />
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

/**
 * Иконки для типов ресурсов в таблице
 */
const ResourceIcons = {
  worker: (
    <svg
      className="w-5 h-5 text-blue-500"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
    >
      <path
        fillRule="evenodd"
        d="M7.5 6a4.5 4.5 0 119 0 4.5 4.5 0 01-9 0zM3.751 20.105a8.25 8.25 0 0116.498 0 .75.75 0 01-.437.695A18.683 18.683 0 0112 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 01-.437-.695z"
        clipRule="evenodd"
      />
    </svg>
  ),
  machine: (
    <svg
      className="w-5 h-5 text-teal-500"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
    >
      <path d="M12.75 12.75a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM7.5 15.75a.75.75 0 100-1.5.75.75 0 000 1.5zM8.25 17.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM9.75 15.75a.75.75 0 100-1.5.75.75 0 000 1.5zM10.5 17.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM12 15.75a.75.75 0 100-1.5.75.75 0 000 1.5zM12.75 17.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM14.25 15.75a.75.75 0 100-1.5.75.75 0 000 1.5zM15 17.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM16.5 15.75a.75.75 0 100-1.5.75.75 0 000 1.5zM15 12.75a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM16.5 13.5a.75.75 0 100-1.5.75.75 0 000 1.5z" />
      <path
        fillRule="evenodd"
        d="M6.75 2.25A.75.75 0 017.5 3v1.5h9V3A.75.75 0 0118 3v1.5h.75a3 3 0 013 3v11.25a3 3 0 01-3 3H5.25a3 3 0 01-3-3V7.5a3 3 0 013-3H6V3a.75.75 0 01.75-.75zm13.5 9a1.5 1.5 0 00-1.5-1.5H5.25a1.5 1.5 0 00-1.5 1.5v7.5a1.5 1.5 0 001.5 1.5h13.5a1.5 1.5 0 001.5-1.5v-7.5z"
        clipRule="evenodd"
      />
    </svg>
  ),
  material: (
    <svg
      className="w-5 h-5 text-amber-500"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
    >
      <path d="M12.378 1.602a.75.75 0 00-.756 0L3 6.632l9 5.25 9-5.25-8.622-5.03zM21.75 7.93l-9 5.25v9l8.628-5.032a.75.75 0 00.372-.648V7.93zM11.25 22.18v-9l-9-5.25v8.57a.75.75 0 00.372.648l8.628 5.033z" />
    </svg>
  ),
  equipment: (
    <svg
      className="w-5 h-5 text-purple-500"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
    >
      <path d="M17.004 10.407c.138.435-.216.842-.672.842h-3.465a.75.75 0 01-.65-.375l-1.732-3c-.229-.396-.053-.907.393-1.004a5.252 5.252 0 016.126 3.537zM8.12 8.464c.307-.338.838-.235 1.066.16l1.732 3a.75.75 0 010 .75l-1.732 3.001c-.229.396-.76.498-1.067.16A5.231 5.231 0 016.75 12c0-1.362.519-2.603 1.37-3.536zM10.878 17.13c-.447-.097-.623-.608-.394-1.003l1.733-3.003a.75.75 0 01.65-.375h3.465c.457 0 .81.408.672.843a5.252 5.252 0 01-6.126 3.538z" />
      <path
        fillRule="evenodd"
        d="M21 12.75a.75.75 0 000-1.5h-.783a8.22 8.22 0 00-.237-1.357l.734-.267a.75.75 0 10-.513-1.41l-.735.268a8.24 8.24 0 00-.689-1.191l.6-.504a.75.75 0 10-.964-1.149l-.6.504a8.3 8.3 0 00-1.054-.885l.391-.678a.75.75 0 10-1.299-.75l-.39.677a8.188 8.188 0 00-1.295-.471l.136-.77a.75.75 0 00-1.477-.26l-.136.77a8.364 8.364 0 00-1.377 0l-.136-.77a.75.75 0 10-1.477.26l.136.77c-.448.121-.88.28-1.294.47l-.39-.676a.75.75 0 00-1.3.75l.392.678a8.29 8.29 0 00-1.054.885l-.6-.504a.75.75 0 00-.965 1.149l.6.503a8.243 8.243 0 00-.689 1.192L3.8 8.217a.75.75 0 10-.513 1.41l.735.267a8.222 8.222 0 00-.238 1.355h-.783a.75.75 0 000 1.5h.783c.042.464.122.917.238 1.356l-.735.268a.75.75 0 10.513 1.41l.735-.268c.197.417.428.816.69 1.192l-.6.504a.75.75 0 10.963 1.149l.601-.505c.326.323.679.62 1.054.885l-.392.68a.75.75 0 101.3.75l.39-.679c.414.192.847.35 1.294.471l-.136.771a.75.75 0 101.477.26l.137-.772a8.376 8.376 0 001.376 0l.136.773a.75.75 0 101.477-.26l-.136-.772a8.19 8.19 0 001.294-.47l.391.677a.75.75 0 101.3-.75l-.393-.679a8.282 8.282 0 001.054-.885l.601.504a.75.75 0 10.964-1.15l-.6-.503a8.24 8.24 0 00.69-1.191l.735.268a.75.75 0 10.512-1.41l-.734-.268c.115-.438.195-.892.237-1.356h.784zm-2.657-3.06a6.744 6.744 0 00-1.19-2.053 6.784 6.784 0 00-1.82-1.51A6.704 6.704 0 0012 5.25a6.801 6.801 0 00-1.225.11 6.7 6.7 0 00-2.092.872 6.784 6.784 0 00-2.866 3.458 6.784 6.784 0 000 5.18 6.784 6.784 0 002.866 3.458 6.7 6.7 0 002.092.872 6.801 6.801 0 001.225.11 6.704 6.704 0 003.334-.877 6.784 6.784 0 001.82-1.51 6.744 6.744 0 001.19-2.053 6.784 6.784 0 000-4.11z"
        clipRule="evenodd"
      />
    </svg>
  ),
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
    <div
      className={`rounded-lg overflow-hidden shadow-sm ${getBgColorClass()}`}
    >
      <div
        className="p-3 flex items-center justify-between cursor-pointer hover:bg-opacity-80 transition-colors"
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
        <div className="p-4 border-t border-gray-100 bg-white">
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

      {cost.totals.natural && (
        <div className="bg-gray-50 p-3 rounded-lg mb-4">
          <h4 className="text-sm font-medium text-gray-700 mb-2">
            Общие трудозатраты
          </h4>
          <div className="grid grid-cols-2 gap-4 text-sm">
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
          </div>
        </div>
      )}

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
            <div className="rounded-lg overflow-hidden">
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
          {resources.map((resource, index) => (
            <tr
              key={`resource-${resource.code}-${index}`}
              className="hover:bg-gray-50 transition-colors"
            >
              <td className="px-3 py-2">
                {ResourceIcons[resource.type] || (
                  <svg
                    className="w-5 h-5 text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="currentColor"
                  >
                    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z" />
                  </svg>
                )}
              </td>
              <td className="px-3 py-2 whitespace-nowrap text-gray-600">
                {resource.code}
              </td>
              <td className="px-3 py-2 text-gray-800">
                {resource.name}
                {resource.code === "1.1" && (
                  <span className="text-xs text-gray-500 ml-1">
                    (справочно)
                  </span>
                )}
              </td>
              <td className="px-3 py-2 whitespace-nowrap text-gray-600">
                {resource.unit}
              </td>
              <td className="px-3 py-2 text-right whitespace-nowrap text-gray-800">
                {resource.code === "1.1"
                  ? resource.consumption
                  : formatNumber(resource.consumption)}
              </td>
              <td className="px-3 py-2 text-right whitespace-nowrap text-gray-800">
                {resource.pricePerUnitBase
                  ? formatCurrency(resource.pricePerUnitBase)
                  : "—"}
              </td>
              <td className="px-3 py-2 text-right whitespace-nowrap">
                {resource.priceTotalBase ? (
                  <div>
                    <div className="font-medium text-gray-800">
                      {formatCurrency(resource.priceTotalBase)}
                    </div>
                  </div>
                ) : (
                  "—"
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DetailedHierarchy;
