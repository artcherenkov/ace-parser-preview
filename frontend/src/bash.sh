#!/bin/bash

# Создаем базовую структуру директорий
mkdir -p src/components/ui
mkdir -p src/components/charts
mkdir -p src/utils/{formatters,calculations,apiClient}
mkdir -p src/shared/{types,constants,enums}
mkdir -p src/layouts
mkdir -p src/pages
mkdir -p src/data

# Создаем структуру для модуля EstimateSummary
mkdir -p src/features/estimateSummary/{types,components,transformers}

# Создаем структуру для других модулей
mkdir -p src/features/costStructure/{types,components,transformers}
mkdir -p src/features/sectionComparison/{types,components,transformers}
mkdir -p src/features/topResources/{types,components,transformers}
mkdir -p src/features/detailedHierarchy/{types,components,transformers}

# Создаем файлы для модуля EstimateSummary
touch src/features/estimateSummary/types/EstimateSummaryDTO.ts
touch src/features/estimateSummary/components/EstimateSummary.tsx
touch src/features/estimateSummary/transformers/estimateSummaryTransformer.ts
touch src/features/estimateSummary/index.ts

# Создаем файлы для других модулей (типы)
touch src/features/costStructure/types/CostStructureDTO.ts
touch src/features/sectionComparison/types/SectionComparisonDTO.ts
touch src/features/topResources/types/TopResourcesDTO.ts
touch src/features/detailedHierarchy/types/DetailedHierarchyDTO.ts

# Создаем файлы для компонентов других модулей
touch src/features/costStructure/components/CostStructure.tsx
touch src/features/sectionComparison/components/SectionComparison.tsx
touch src/features/topResources/components/TopResources.tsx
touch src/features/detailedHierarchy/components/DetailedHierarchy.tsx

# Создаем файлы для трансформеров других модулей
touch src/features/costStructure/transformers/costStructureTransformer.ts
touch src/features/sectionComparison/transformers/sectionComparisonTransformer.ts
touch src/features/topResources/transformers/topResourcesTransformer.ts
touch src/features/detailedHierarchy/transformers/detailedHierarchyTransformer.ts

# Создаем файлы для индексов других модулей
touch src/features/costStructure/index.ts
touch src/features/sectionComparison/index.ts
touch src/features/topResources/index.ts
touch src/features/detailedHierarchy/index.ts

# Создаем общие файлы утилит
touch src/utils/formatters/numberFormatters.ts
touch src/utils/formatters/dateFormatters.ts
touch src/utils/calculations/percentageCalculations.ts
touch src/utils/apiClient/apiClient.ts

# Создаем общие типы и константы
touch src/shared/types/commonTypes.ts
touch src/shared/constants/appConstants.ts
touch src/shared/enums/appEnums.ts

# Создаем файлы для layouts и pages
touch src/layouts/DashboardLayout.tsx
touch src/pages/DashboardPage.tsx

# Создаем файл с тестовыми данными
touch src/data/sampleEstimate.json

# Создаем корневые файлы приложения
touch src/App.tsx
touch src/main.tsx
touch src/vite-env.d.ts

# Сообщение об успешном создании
echo "Структура проекта успешно создана!"
