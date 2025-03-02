// src/layouts/DashboardLayout.tsx

import React, { ReactNode } from "react";

interface DashboardLayoutProps {
  children: ReactNode;
}

/**
 * Компонент для оформления основного макета дашборда
 */
const DashboardLayout: React.FC<DashboardLayoutProps> = ({ children }) => {
  return (
    <div className="flex min-h-screen bg-gray-50">
      {/* Боковая панель */}
      <aside className="w-64 bg-slate-800 text-white">
        <div className="p-6">
          <h1 className="text-xl font-bold">Анализ Сметы</h1>
        </div>
        <nav>
          <ul className="mt-6">
            <li className="mb-1">
              <a
                href="#"
                className="flex items-center px-6 py-3 bg-blue-600 text-white"
              >
                Обзор
              </a>
            </li>
            <li className="mb-1">
              <a
                href="#"
                className="flex items-center px-6 py-3 text-gray-300 hover:bg-slate-700 hover:text-white transition-colors"
              >
                Разделы
              </a>
            </li>
            <li className="mb-1">
              <a
                href="#"
                className="flex items-center px-6 py-3 text-gray-300 hover:bg-slate-700 hover:text-white transition-colors"
              >
                Ресурсы
              </a>
            </li>
            <li className="mb-1">
              <a
                href="#"
                className="flex items-center px-6 py-3 text-gray-300 hover:bg-slate-700 hover:text-white transition-colors"
              >
                Отчеты
              </a>
            </li>
          </ul>
        </nav>
      </aside>

      {/* Основной контент */}
      <div className="flex-1 overflow-auto">{children}</div>
    </div>
  );
};

export default DashboardLayout;
