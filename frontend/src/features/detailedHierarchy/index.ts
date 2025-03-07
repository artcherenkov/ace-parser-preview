// src/features/detailedHierarchy/index.ts

export { default as DetailedHierarchy } from "./components/DetailedHierarchy";
export { transformToDetailedHierarchyDTO } from "./transformers/detailedHierarchyTransformer";
export type {
  DetailedHierarchyDTO,
  SectionDTO,
  ItemDTO,
  ResourceDTO,
  ItemIconType,
} from "./types/DetailedHierarchyDTO";
