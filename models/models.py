from dataclasses import dataclass, field
from typing import List, Dict, Optional, Union, Any
from datetime import date


@dataclass
class PriceLevel:
    """Уровень цен (базисный или текущий)"""
    year: int
    month: Optional[int] = None
    quarter: Optional[int] = None


@dataclass
class PricePair:
    """Пара значений базисной и текущей цены"""
    base: float
    current: float

    @property
    def indexValue(self) -> float:
        """Расчет индекса изменения цены"""
        if self.base == 0:
            return 0
        return self.current / self.base


@dataclass
class EstimateMeta:
    """Метаданные сметы"""
    constructionName: str
    objectName: str
    estimateName: str
    estimateNumber: str
    date: str
    priceLevelBase: PriceLevel
    priceLevelCurrent: PriceLevel


@dataclass
class Resource:
    """Ресурс (материал, машина и т.д.)"""
    id: str
    type: str  # "material", "machine", "worker"
    code: str
    name: str
    quantity: str
    cost: float


@dataclass
class ItemCost:
    """Стоимостные показатели позиции"""
    direct: float
    total: float


@dataclass
class EstimateItem:
    """Позиция сметы"""
    id: str
    num: int
    code: str
    name: str
    unit: str
    quantity: float
    base: ItemCost
    current: ItemCost
    resources: List[Resource] = field(default_factory=list)

    @property
    def indexValue(self) -> float:
        """Расчет индекса изменения цены позиции"""
        if self.base.total == 0:
            return 0
        return self.current.total / self.base.total


@dataclass
class Section:
    """Раздел сметы"""
    id: str
    code: int
    name: str
    totalCost: PricePair
    items: List[EstimateItem] = field(default_factory=list)


@dataclass
class TopResource:
    """Ценообразующий ресурс"""
    id: str
    name: str
    cost: float
    share: float


@dataclass
class EstimateSummary:
    """Итоговые показатели сметы"""
    total: PricePair
    direct: PricePair
    workersSalary: Optional[PricePair] = None
    machinistSalary: Optional[PricePair] = None
    machines: Optional[PricePair] = None
    materials: Optional[PricePair] = None
    overhead: Optional[PricePair] = None
    profit: Optional[PricePair] = None


@dataclass
class EstimateData:
    """Полные данные сметы"""
    meta: EstimateMeta
    summary: EstimateSummary
    sections: List[Section]
    topResources: List[TopResource] = field(default_factory=list)
