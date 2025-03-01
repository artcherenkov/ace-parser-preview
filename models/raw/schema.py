from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional


class EstimateEstimateType(Enum):
    CYRILLIC_CAPITAL_LETTER_ES_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_I_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_EL_CYRILLIC_SMALL_LETTER_SOFT_SIGN_CYRILLIC_SMALL_LETTER_ES_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_VE_CYRILLIC_SMALL_LETTER_O = "Строительство"
    CYRILLIC_CAPITAL_LETTER_ER_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_ES_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_VE_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_TSE_CYRILLIC_SMALL_LETTER_I_CYRILLIC_SMALL_LETTER_YA = "Реставрация"


class EstimateIndexType(Enum):
    CYRILLIC_CAPITAL_LETTER_O_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_ES_CYRILLIC_SMALL_LETTER_U_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_ES_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_VE_CYRILLIC_SMALL_LETTER_U_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_TE = "Отсутствует"
    CYRILLIC_CAPITAL_LETTER_I_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_DE_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_KA_CYRILLIC_SMALL_LETTER_ES_CYRILLIC_SMALL_LETTER_YERU_SPACE_CYRILLIC_SMALL_LETTER_KA_SPACE_CYRILLIC_CAPITAL_LETTER_ES_CYRILLIC_CAPITAL_LETTER_EM_CYRILLIC_CAPITAL_LETTER_ER = "Индексы к СМР"
    CYRILLIC_CAPITAL_LETTER_I_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_DE_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_KA_CYRILLIC_SMALL_LETTER_ES_CYRILLIC_SMALL_LETTER_YERU_SPACE_CYRILLIC_SMALL_LETTER_KA_SPACE_CYRILLIC_SMALL_LETTER_E_CYRILLIC_SMALL_LETTER_EL_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_EM_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_EM_SPACE_CYRILLIC_SMALL_LETTER_PE_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_YA_CYRILLIC_SMALL_LETTER_EM_CYRILLIC_SMALL_LETTER_YERU_CYRILLIC_SMALL_LETTER_HA_SPACE_CYRILLIC_SMALL_LETTER_ZE_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_TE = "Индексы к элементам прямых затрат"
    CYRILLIC_CAPITAL_LETTER_I_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_DE_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_KA_CYRILLIC_SMALL_LETTER_ES_CYRILLIC_SMALL_LETTER_YERU_SPACE_CYRILLIC_SMALL_LETTER_KA_SPACE_CYRILLIC_SMALL_LETTER_E_CYRILLIC_SMALL_LETTER_EL_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_EM_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_EM_SPACE_CYRILLIC_SMALL_LETTER_PE_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_YA_CYRILLIC_SMALL_LETTER_EM_CYRILLIC_SMALL_LETTER_YERU_CYRILLIC_SMALL_LETTER_HA_SPACE_CYRILLIC_SMALL_LETTER_ZE_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_TE_SPACE_CYRILLIC_SMALL_LETTER_VE_SPACE_CYRILLIC_SMALL_LETTER_PE_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_ZE_CYRILLIC_SMALL_LETTER_I_CYRILLIC_SMALL_LETTER_TSE_CYRILLIC_SMALL_LETTER_I_CYRILLIC_SMALL_LETTER_I = "Индексы к элементам прямых затрат в позиции"


class TaccessLevel(Enum):
    CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_BE_CYRILLIC_SMALL_LETTER_SHCHA_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_DE_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_ES_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_U_CYRILLIC_SMALL_LETTER_PE_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_YA_SPACE_CYRILLIC_SMALL_LETTER_I_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_EF_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_EM_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_TSE_CYRILLIC_SMALL_LETTER_I_CYRILLIC_SMALL_LETTER_YA = "общедоступная информация"
    CYRILLIC_SMALL_LETTER_DE_CYRILLIC_SMALL_LETTER_EL_CYRILLIC_SMALL_LETTER_YA_SPACE_CYRILLIC_SMALL_LETTER_ES_CYRILLIC_SMALL_LETTER_EL_CYRILLIC_SMALL_LETTER_U_CYRILLIC_SMALL_LETTER_ZHE_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_BE_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_GHE_CYRILLIC_SMALL_LETTER_O_SPACE_CYRILLIC_SMALL_LETTER_PE_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_EL_CYRILLIC_SMALL_LETTER_SOFT_SIGN_CYRILLIC_SMALL_LETTER_ZE_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_VE_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_I_CYRILLIC_SMALL_LETTER_YA = "для служебного пользования"
    CYRILLIC_SMALL_LETTER_KA_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_EM_CYRILLIC_SMALL_LETTER_EM_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_CHE_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_ES_CYRILLIC_SMALL_LETTER_KA_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_YA_SPACE_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_SHORT_I_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_A = "коммерческая тайна"


@dataclass
class Tbimdata:
    """
    Базовый тип для передачи данных об элементе BIM.

    :ivar file_id: Ссылка на порядковый номер файла см. BIMFiles
    :ivar ifc_guid: Идентификатор элемента в IFC файле
    :ivar ifc_quantity: Объем данного элемента в позиции, в единицах
        измерения позиции
    """

    class Meta:
        name = "TBIMData"

    file_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "FileId",
            "type": "Element",
            "required": True,
        },
    )
    ifc_guid: Optional[str] = field(
        default=None,
        metadata={
            "name": "IfcGuid",
            "type": "Element",
            "required": True,
        },
    )
    ifc_quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IfcQuantity",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Tcoefficients:
    """
    Поправочные коэффициенты.

    :ivar final: Итоговое значение коэффициента учета условий
        производства работ. Округление до 7-ми знаков. Округление
        производится один раз после всех математических операций.
    :ivar coefficient: Поправочный коэффициент
    """

    class Meta:
        name = "TCoefficients"

    final: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    coefficient: list["Tcoefficients.Coefficient"] = field(
        default_factory=list,
        metadata={
            "name": "Coefficient",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Coefficient:
        """
        :ivar name: Наименование коэффициента
        :ivar reason: Обоснование коэффициента
        :ivar num: Порядковый номер коэффициента
        :ivar value: Значение коэффициента
        """

        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Element",
                "required": True,
            },
        )
        reason: Optional[str] = field(
            default=None,
            metadata={
                "name": "Reason",
                "type": "Element",
                "required": True,
            },
        )
        num: Optional[int] = field(
            default=None,
            metadata={
                "name": "Num",
                "type": "Element",
                "required": True,
            },
        )
        value: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Element",
                "required": True,
            },
        )


@dataclass
class Tcomissioning:
    """
    :ivar code: <text xmlns="">Обоснование доли ПНР.</text> <links
        xmlns="">Приложение № 8 к Методике определения сметной стоимости
        строительства, реконструкции, капитального ремонта, сноса
        объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденной приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр </links>
    :ivar name: <text xmlns="">Наименование сборника сметных норм
        (единичных расценок) на пусконаладочные работы.</text> <links
        xmlns="">Приложение № 8 к Методике определения сметной стоимости
        строительства, реконструкции, капитального ремонта, сноса
        объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденной приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр </links>
    :ivar unit: <text xmlns="">Единица измерения доли ПНР (%).</text>
        <links xmlns="">Приложение № 8 к Методике определения сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденной приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр </links>
    :ivar quantity: <text xmlns="">Доля пусконаладочных работ</text>
        <links xmlns="">Приложение № 8 к Методике определения сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденной приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр </links>
    :ivar base_price: <text xmlns="">Стоимость пусконаладочных работ по
        доле и обоснованию в базовом уровне цен.</text> <formula
        xmlns="">BasePrice (Стоимость пусконаладочных работ по доле и
        обоснованию в базовом уровне цен) =Item.Totals.Base (Итоговые
        суммарные показатели по позиции ЛСР ПНР (ФЕРп, ТЕРп) с
        одинаковым обоснованием в базовом уровне цен)* Quantity (Доля
        пусконаладочных работ)/100 Округление до 2-х знаков. Округление
        производится один раз после всех математических операций
        </formula> <links xmlns="">Приложение № 8 к Методике определения
        сметной стоимости строительства, реконструкции, капитального
        ремонта, сноса объектов капитального строительства, работ по
        сохранению объектов культурного наследия (памятников истории и
        культуры) народов Российской Федерации на территории Российской
        Федерации, утвержденной приказом Министерства строительства и
        жилищно-коммунального хозяйства Российской Федерации от 4
        августа 2020 г. № 421/пр </links>
    :ivar current_price: <text xmlns="">Стоимость пусконаладочных работ
        по доле и обоснованию в текущем уровне цен.</text> <formula
        xmlns="">CurrentPrice (Стоимость пусконаладочных работ по доле и
        обоснованию в текущем уровне цен) =Item.Totals.Current (Итоговые
        суммарные показатели по позиции ЛСР ПНР (ФЕРп, ТЕРп) с
        одинаковым обоснованием в текущем уровне цен)* Quantity (Доля
        пусконаладочных работ)/100 Округление до 2-х знаков. Округление
        производится один раз после всех математических операций
        </formula> <links xmlns="">Приложение № 8 к Методике определения
        сметной стоимости строительства, реконструкции, капитального
        ремонта, сноса объектов капитального строительства, работ по
        сохранению объектов культурного наследия (памятников истории и
        культуры) народов Российской Федерации на территории Российской
        Федерации, утвержденной приказом Министерства строительства и
        жилищно-коммунального хозяйства Российской Федерации от 4
        августа 2020 г. № 421/пр </links>
    """

    class Meta:
        name = "TComissioning"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "required": True,
        },
    )
    quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        },
    )
    base_price: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Element",
            "required": True,
        },
    )
    current_price: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CurrentPrice",
            "type": "Element",
            "required": True,
        },
    )


class TcostIndexValueTarget(Enum):
    CYRILLIC_CAPITAL_LETTER_O_CYRILLIC_CAPITAL_LETTER_TE = "ОТ"
    CYRILLIC_CAPITAL_LETTER_O_CYRILLIC_CAPITAL_LETTER_TE_CYRILLIC_CAPITAL_LETTER_EM = "ОТМ"
    CYRILLIC_CAPITAL_LETTER_E_CYRILLIC_CAPITAL_LETTER_EM = "ЭМ"
    CYRILLIC_CAPITAL_LETTER_EM = "М"


@dataclass
class Tdate:
    """
    Дата составления локального сметного расчета.

    :ivar year: Год
    :ivar month: Месяц
    :ivar day: День
    """

    class Meta:
        name = "TDate"

    year: Optional[int] = field(
        default=None,
        metadata={
            "name": "Year",
            "type": "Element",
            "required": True,
        },
    )
    month: Optional[int] = field(
        default=None,
        metadata={
            "name": "Month",
            "type": "Element",
            "required": True,
        },
    )
    day: Optional[int] = field(
        default=None,
        metadata={
            "name": "Day",
            "type": "Element",
            "required": True,
        },
    )


class TfileFormatType(Enum):
    CYRILLIC_CAPITAL_LETTER_EL_CYRILLIC_CAPITAL_LETTER_ES = "ЛС"


class TitemSummaryType(Enum):
    CYRILLIC_CAPITAL_LETTER_ES_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_I_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_EL_CYRILLIC_SMALL_LETTER_SOFT_SIGN_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_YERU_CYRILLIC_SMALL_LETTER_IE = "Строительные"
    CYRILLIC_CAPITAL_LETTER_EM_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_ZHE_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_YERU_CYRILLIC_SMALL_LETTER_IE = "Монтажные"
    CYRILLIC_CAPITAL_LETTER_O_CYRILLIC_SMALL_LETTER_BE_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_U_CYRILLIC_SMALL_LETTER_DE_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_VE_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_I_CYRILLIC_SMALL_LETTER_IE = "Оборудование"
    CYRILLIC_CAPITAL_LETTER_PE_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_CHE_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_IE = "Прочее"


class TitemWorkType(Enum):
    CYRILLIC_CAPITAL_LETTER_ES_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_I_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_EL_CYRILLIC_SMALL_LETTER_SOFT_SIGN_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_YERU_CYRILLIC_SMALL_LETTER_IE = "Строительные"
    CYRILLIC_CAPITAL_LETTER_EM_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_ZHE_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_YERU_CYRILLIC_SMALL_LETTER_IE = "Монтажные"
    CYRILLIC_CAPITAL_LETTER_O_CYRILLIC_SMALL_LETTER_BE_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_U_CYRILLIC_SMALL_LETTER_DE_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_VE_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_I_CYRILLIC_SMALL_LETTER_IE = "Оборудование"
    CYRILLIC_CAPITAL_LETTER_PE_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_CHE_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_IE = "Прочее"
    CYRILLIC_CAPITAL_LETTER_PE_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_IE_CYRILLIC_SMALL_LETTER_VE_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_ZE_CYRILLIC_SMALL_LETTER_KA_CYRILLIC_SMALL_LETTER_A = "Перевозка"


class TlegalType(Enum):
    CYRILLIC_CAPITAL_LETTER_GHE_CYRILLIC_CAPITAL_LETTER_ES_CYRILLIC_CAPITAL_LETTER_EN = "ГСН"
    CYRILLIC_CAPITAL_LETTER_O_CYRILLIC_CAPITAL_LETTER_ES_CYRILLIC_CAPITAL_LETTER_EN = "ОСН"
    CYRILLIC_CAPITAL_LETTER_TE_CYRILLIC_CAPITAL_LETTER_IE_CYRILLIC_CAPITAL_LETTER_ER = "ТЕР"
    CYRILLIC_CAPITAL_LETTER_I_CYRILLIC_CAPITAL_LETTER_ES_CYRILLIC_CAPITAL_LETTER_EN = "ИСН"
    CYRILLIC_CAPITAL_LETTER_ES_CYRILLIC_SMALL_LETTER_PE_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_VE_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_CHE_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_YA_SPACE_CYRILLIC_SMALL_LETTER_I_CYRILLIC_SMALL_LETTER_EN_CYRILLIC_SMALL_LETTER_EF_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_ER_CYRILLIC_SMALL_LETTER_EM_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_TSE_CYRILLIC_SMALL_LETTER_I_CYRILLIC_SMALL_LETTER_YA = "Справочная информация"


class ToverheadTarget(Enum):
    CYRILLIC_CAPITAL_LETTER_PE_CYRILLIC_CAPITAL_LETTER_ZE = "ПЗ"
    CYRILLIC_CAPITAL_LETTER_O_CYRILLIC_CAPITAL_LETTER_TE = "ОТ"
    CYRILLIC_CAPITAL_LETTER_O_CYRILLIC_CAPITAL_LETTER_TE_CYRILLIC_CAPITAL_LETTER_EM = "ОТМ"
    CYRILLIC_CAPITAL_LETTER_EF_CYRILLIC_CAPITAL_LETTER_O_CYRILLIC_CAPITAL_LETTER_TE = "ФОТ"


@dataclass
class TpriceLevel:
    """
    Уровень цен локального сметного расчета.

    :ivar year: Год
    :ivar month: Месяц
    :ivar quarter: Квартал
    :ivar note: Примечание
    """

    class Meta:
        name = "TPriceLevel"

    year: Optional[int] = field(
        default=None,
        metadata={
            "name": "Year",
            "type": "Element",
            "required": True,
            "min_inclusive": 1964,
            "max_inclusive": 2100,
        },
    )
    month: Optional[int] = field(
        default=None,
        metadata={
            "name": "Month",
            "type": "Element",
            "min_inclusive": 1,
            "max_inclusive": 12,
        },
    )
    quarter: Optional[int] = field(
        default=None,
        metadata={
            "name": "Quarter",
            "type": "Element",
            "min_inclusive": 1,
            "max_inclusive": 4,
        },
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
        },
    )


@dataclass
class TpriceParameters:
    """
    Стоимостные показатели позиции локального сметного расчёта.

    :ivar direct: <text xmlns="">Итого по единичной расценке - Прямые
        затраты, учитывающие стоимость ресурсов, необходимых для
        выполнения работ: материальных (материалов, изделий,
        конструкций, оборудования, мебели, инвентаря); технических
        (эксплуатации строительных машин и механизмов); трудовых
        (средства на оплату труда рабочих, а также машинистов,
        учитываемые в стоимости эксплуатации строительных машин и
        механизмов). Прямые затраты определяются при составлении сметной
        документации на строительство, реконструкцию, капитальный ремонт
        объектов капитального строительства </text> <formula xmlns="">
        За единицу измерения расценки Базовые:
        PerUnit.Base.Direct(Прямые затраты в базовом уровне на ед. изм.
        расценки) = PerUnit.Base.WorkersSalary(Оплата труда рабочих в
        базовом уровне на ед. изм. расценки) +
        PerUnit.Base.Machines(Сметные затраты на эксплуатацию
        строительных машин в базовом уровне на ед. изм. расценки) +
        PerUnit.Base.Materials(Сметные затраты на материальные ресурсы в
        базовом уровне на ед. изм. расценки) +
        PerUnit.Base.Equipment(Сметные затраты на оборудование в базовом
        уровне на ед. изм. расценки) Итоговые Базовые:
        Totals.Base.Direct (Итоговые прямые затраты в базовом уровне) =
        Totals.Base.WorkersSalary (Итоговая оплата труда рабочих в
        базовом уровне) + Totals.Base.Machines (Итоговые сметные затраты
        на эксплуатацию строительных машин в базовом уровне) +
        Totals.Base.Materials (Итоговые сметные затраты на материальные
        ресурсы в базовом уровне) + Totals.Base.Equipment (Итоговые
        сметные затраты на оборудование в базовом уровне)) Округление до
        2-х знаков. Округление производится один раз после всех
        математических операций. </formula> <links xmlns="">Методика
        определения сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        работ по сохранению объектов культурного наследия (памятников
        истории и культуры) народов Российской Федерации на территории
        Российской Федерации, утвержденная приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 4 августа 2020 г. № 421/пр. </links>
    :ivar machines: <text xmlns="">Сметные затраты на эксплуатацию
        строительных машин, автотранспортных средств, механизированных
        инструментов и механизмов определяемые при составлении сметной
        документации на строительство, реконструкцию, капитальный ремонт
        объектов капитального строительства. </text> <formula xmlns="">
        За единицу измерения расценки Базовые: PerUnit.Base.Machines
        (Сметные затраты на эксплуатацию строительных машин в базовом
        уровне на ед. изм. расценки) = значение из единичной расценки
        Итоговые Базовые: Totals.Base.Machines (Итоговые сметные затраты
        на эксплуатацию строительных машин в базовом уровне) =
        QuantityTotal(Объем работ с учетом поправочных коэффициентов)*
        ((PerUnit.Base.Machines (Сметные затраты на эксплуатацию
        строительных машин в базовом уровне на ед. изм. расценки) -
        PerUnit.Base.MachinistSalary (Оплата труда машинистов в базовом
        уровне на ед. изм. расценки)) * Coefficient(Поправочный
        коэффициент к ЭМ) + PerUnit.Base.MachinistSalary (Оплата труда
        машинистов в базовом уровне на ед. изм. расценки) *
        Coefficient(Поправочный коэффициент к ОТМ)) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций. </formula> <links xmlns="">Методические
        рекомендации по определению сметных цен на эксплуатацию машин и
        механизмов утвержденные приказом Министерства строительства и
        жилищно-коммунального хозяйства Российской Федерации от 4
        сентября 2019 г. № 513/пр. </links>
    :ivar workers_salary: <text xmlns="">Оплата труда рабочих
        непосредственно занятых в процессе создания материальных
        ценностей при выполнении строительных работ и работников-
        исполнителей пусконаладочных работ. </text> <formula xmlns="">
        За единицу измерения расценки Базовые:
        PerUnit.Base.WorkersSalary (Оплата труда рабочих в базовом
        уровне на ед. изм. расценки) = значение из единичной расценки
        Итоговые Базовые: Totals.Base.WorkersSalary (Итоговая оплата
        труда рабочих в базовом уровне) = QuantityTotal(Объем работ с
        учетом поправочных коэффициентов) * PerUnit.Base.WorkersSalary
        (Оплата труда рабочих в базовом уровне на ед. изм. расценки) *
        Coefficient (Поправочный коэффициент к ОТ) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций. Итоговые Текущие:
        Totals.Price.WorkersSalary (Итоговая оплата труда рабочих в
        текущем уровне) = Totals.Base.WorkersSalary (Итоговая оплата
        труда рабочих в базовом уровне)* Index (Индекс к ОТ) Округление
        до 2-х знаков. Округление производится один раз после всех
        математических операций. </formula> <links xmlns="">Методические
        рекомендации по определению сметных цен на затраты труда в
        строительстве, утвержденные приказом Министерства строительства
        и жилищно-коммунального хозяйства Российской Федерации от 4
        сентября 2019 г. № 515/пр. </links>
    :ivar machinist_salary: <text xmlns="">Оплата труда машинистов
        (рабочих, управляющих машинами), включенная в состав затрат на
        эксплуатацию строительных машин. Рассчитывается в составе
        стоимости маш.–ч машин. </text> <formula xmlns=""> За единицу
        измерения расценки Базовые: PerUnit.Base.MachinistSalary (Оплата
        труда машинистов в базовом уровне на ед. изм. расценки) =
        значение из единичной расценки Итоговые Базовые:
        Totals.Base.MachinistSalary(Итоговая оплата труда машинистов в
        базовом уровне) = QuantityTotal(Объем работ с учетом поправочных
        коэффициентов) * PerUnit.Base.MachinistSalary (Оплата труда
        машинистов в базовом уровне на ед. изм. расценки)*
        Coefficient(Поправочный коэффициент к ОТМ) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций. Итоговые Текущие:
        Totals.Price.MachinistSalary (Итоговая оплата труда машинистов в
        текущем уровне) = Totals.Base. MachinistSalary (Итоговая оплата
        труда машинистов в базовом уровне) * Index (Индекс к ОТМ)
        Округление до 2-х знаков. Округление производится один раз после
        всех математических операций. </formula> <links
        xmlns="">Методические рекомендации по определению сметных цен на
        эксплуатацию машин и механизмов утвержденные приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 сентября 2019 г. № 513/пр. </links>
    :ivar salary: <text xmlns="">Фонд оплаты труда рабочих-строителей и
        машинистов (ФОТ). Для определения накладных расходов и размера
        сметной прибыли. Определяется как сумма итоговых значений оплаты
        труда рабочих и машинистов </text> <formula xmlns=""> Итоговый
        Базовый: Base.Salary (ФОТ в базовом уровне) = Base.WorkersSalary
        (Итоговая оплата труда рабочих в базовом уровне) +
        Base.MachinistSalary(Итоговая оплата труда машинистов в базовом
        уровне) Округление до 2-х знаков. Округление производится один
        раз после всех математических операций. Итоговый Текущий:
        Base.Salary (ФОТ в текущем уровне) = Current.WorkersSalary
        (Итоговая оплата труда рабочих в текущем уровне) +
        Current.MachinistSalary(Итоговая оплата труда машинистов в
        текущем уровне) Округление до 2-х знаков. Округление
        производится один раз после всех математических операций.
        </formula> <links xmlns="">Методика определения сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр. </links>
    :ivar materials: <text xmlns="">Сметные затраты на материальные
        ресурсы определяемые при составлении сметной документации на
        строительство, реконструкцию, капитальный ремонт объектов
        капитального строительства. </text> <formula xmlns=""> За
        единицу измерения расценки Базовые:
        PerUnit.Base.Materials(Сметные затраты на материальные ресурсы в
        базовом уровне на ед. изм. расценки) = значение из единичной
        расценки Итоговые Базовые: Totals.Base.Materials(Итоговые
        сметные затраты на материальные ресурсы в базовом уровне) =
        QuantityTotal(Объем работ с учетом поправочных коэффициентов) *
        PerUnit.Base.Materials (Сметные затраты на материальные ресурсы
        в базовом уровне на ед. изм. расценки) * Coefficient(Поправочный
        коэффициент к МР) Округление до 2-х знаков. Округление
        производится один раз после всех математических операций.
        </formula> <links xmlns="">Методические рекомендации по
        определению сметных цен на материалы, изделия, конструкции,
        оборудование, утвержденные приказом Министерства строительства и
        жилищно-коммунального хозяйства Российской Федерации от 4
        сентября 2019 г. № 517/пр. </links>
    :ivar equipment: <text xmlns="">Сметные затраты на оборудование,
        мебель, инвентарь определяемые при составлении сметной
        документации на строительство, реконструкцию, капитальный ремонт
        объектов капитального строительства. </text> <formula xmlns="">
        За единицу измерения расценки Базовые:
        PerUnit.Base.Equipment(Сметные затраты на оборудование в базовом
        уровне на ед. изм. расценки) = значение из единичной расценки
        Итоговые Базовые: Totals.Base.Equipment (Итоговые сметные
        затраты на оборудование в базовом уровне)= QuantityTotal(Объем
        работ с учетом поправочных коэффициентов) *
        PerUnit.Base.Equipment(Сметные затраты на оборудование в базовом
        уровне на ед. изм. расценки) * Coefficient (Поправочный
        коэффициент к ОБ) Округление до 2-х знаков. Округление
        производится один раз после всех математических операций.
        </formula> <links xmlns="">Методические рекомендации по
        определению сметных цен на материалы, изделия, конструкции,
        оборудование, утвержденные приказом Министерства строительства и
        жилищно-коммунального хозяйства Российской Федерации от 4
        сентября 2019 г. № 517/пр. </links>
    """

    class Meta:
        name = "TPriceParameters"

    direct: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Direct",
            "type": "Element",
        },
    )
    machines: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Machines",
            "type": "Element",
        },
    )
    workers_salary: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WorkersSalary",
            "type": "Element",
        },
    )
    machinist_salary: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MachinistSalary",
            "type": "Element",
        },
    )
    salary: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Salary",
            "type": "Element",
        },
    )
    materials: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Materials",
            "type": "Element",
        },
    )
    equipment: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Element",
        },
    )


@dataclass
class Tregion:
    """
    Субъект РФ (регион)

    :ivar code: Цифровой код субъекта РФ (региона)
    :ivar name: Наименование субъекта Российской Федерации
    """

    class Meta:
        name = "TRegion"

    code: Optional[int] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 99,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Tsignatures:
    """
    Подписи локального сметного расчета.

    :ivar compose_fio: Cоставил (должность, подпись (инициалы, фамилия))
    :ivar verify_fio: Проверил (должность, подпись (инициалы, фамилия))
    """

    class Meta:
        name = "TSignatures"

    compose_fio: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComposeFIO",
            "type": "Element",
        },
    )
    verify_fio: Optional[str] = field(
        default=None,
        metadata={
            "name": "VerifyFIO",
            "type": "Element",
        },
    )


class ValueTarget(Enum):
    CYRILLIC_CAPITAL_LETTER_ES_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_I_CYRILLIC_SMALL_LETTER_EM_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_ES_CYRILLIC_SMALL_LETTER_TE_CYRILLIC_SMALL_LETTER_SOFT_SIGN = "Стоимость"
    CYRILLIC_CAPITAL_LETTER_ER_CYRILLIC_SMALL_LETTER_A_CYRILLIC_SMALL_LETTER_ES_CYRILLIC_SMALL_LETTER_HA_CYRILLIC_SMALL_LETTER_O_CYRILLIC_SMALL_LETTER_DE = "Расход"


@dataclass
class TcostCoefficients:
    """
    Поправочные коэффициенты к элементам затрат и объему работ.

    :ivar values: Значения коэффициента
    """

    class Meta:
        name = "TCostCoefficients"

    values: Optional["TcostCoefficients.Values"] = field(
        default=None,
        metadata={
            "name": "Values",
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class Values:
        """
        :ivar value: Значение коэффициента
        """

        value: list["TcostCoefficients.Values.Value"] = field(
            default_factory=list,
            metadata={
                "name": "Value",
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass
        class Value:
            """
            :ivar target: К чему применяются
            :ivar coef_value: Значение коэффициента
            """

            target: Optional[ValueTarget] = field(
                default=None,
                metadata={
                    "name": "Target",
                    "type": "Element",
                    "required": True,
                },
            )
            coef_value: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "CoefValue",
                    "type": "Element",
                    "required": True,
                },
            )


@dataclass
class TfileFormat:
    """
    Комплексный тип для описания типа и версии передаваемого файла.

    :ivar type_value: <text xmlns=""> Тип передаваемого файла: ЛC -
        Локальная смета; </text>
    :ivar version: Номер версии схемы
    """

    class Meta:
        name = "TFileFormat"

    type_value: Optional[TfileFormatType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "required": True,
        },
    )
    version: Decimal = field(
        default=Decimal("1.01"),
        metadata={
            "name": "Version",
            "type": "Element",
            "required": True,
            "fraction_digits": 2,
        },
    )


@dataclass
class TindexValue:
    """
    Индексы изменения сметной стоимости.

    :ivar final: Итоговое значение индекса, полученное в результате
        перемножения всех значений (индексы и поправочные коэффициенты).
        Округление до 2-х знаков. Округление производится один раз после
        всех математических операций
    :ivar value: Исходное значение индекса
    :ivar coefficients: Коэффициенты, применяемые к значению индекса
    """

    class Meta:
        name = "TIndexValue"

    final: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    coefficients: Optional[Tcoefficients] = field(
        default=None,
        metadata={
            "name": "Coefficients",
            "type": "Element",
        },
    )


@dataclass
class TitemParameters:
    """
    Уровень цен стоимостных показателей позиции локального сметного и натуральные
    показатели позиции.

    :ivar base: Стоимостные показатели позиции локального сметного
        расчета в базисном уровне цен
    :ivar current: Стоимостные показатели позиции локального сметного
        расчета в текущем уровне цен
    :ivar natural: Натуральные показатели позиции локального сметного
        расчета
    """

    class Meta:
        name = "TItemParameters"

    base: Optional[TpriceParameters] = field(
        default=None,
        metadata={
            "name": "Base",
            "type": "Element",
        },
    )
    current: Optional[TpriceParameters] = field(
        default=None,
        metadata={
            "name": "Current",
            "type": "Element",
        },
    )
    natural: Optional["TitemParameters.Natural"] = field(
        default=None,
        metadata={
            "name": "Natural",
            "type": "Element",
        },
    )

    @dataclass
    class Natural:
        """
        :ivar labor_costs: <text xmlns="">Затраты труда рабочих
            непосредственно занятых в процессе создания материальных
            ценностей при выполнении строительных работ и работников-
            исполнителей пусконаладочных работ не занятых обслуживанием
            машин) </text> <formula xmlns=""> На единицу измерения
            расценки: LaborCosts (Затраты труда рабочих на ед. изм.
            расценки) = значение из единичной расценки Итоговые:
            LaborCosts (Затраты труда рабочих на ед. изм. расценки) *
            QuantityTotal(Объем работ с учетом поправочных
            коэффициентов) * Coefficients.Final(Итоговое произведение
            коэффициентов) Округление до 7-ми знаков. Округление
            производится один раз после всех математических операций.
            </formula> <links xmlns="">Методические рекомендации по
            определению сметных цен на затраты труда в строительстве,
            утвержденные приказом Министерства строительства и жилищно-
            коммунального хозяйства Российской Федерации от 4 сентября
            2019 г. № 515/пр. </links>
        :ivar machinist_labor_costs: <text xmlns="">Затраты труда
            машинистов (рабочих, управляющих машинами)</text> <formula
            xmlns=""> На единицу измерения расценки: MachinistLaborCosts
            (Затраты труда машинистов на ед. изм. расценки) = значение
            из единичной расценки Итоговые: MachinistLaborCosts (Затраты
            труда машинистов на ед. изм. расценки) * QuantityTotal(Объем
            работ с учетом поправочных коэффициентов) *
            Coefficients.Final(Итоговое произведение коэффициентов)
            Округление до 7-ми знаков. Округление производится один раз
            после всех математических операций. </formula> <links
            xmlns="">Методические рекомендации по определению сметных
            цен на затраты труда в строительстве, утвержденные приказом
            Министерства строительства и жилищно-коммунального хозяйства
            Российской Федерации от 4 сентября 2019 г. № 515/пр.
            </links>
        """

        labor_costs: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "LaborCosts",
                "type": "Element",
            },
        )
        machinist_labor_costs: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "MachinistLaborCosts",
                "type": "Element",
            },
        )


@dataclass
class Tlegal:
    """
    Описание данных, используемых для определения стоимости работ и затрат в
    локальном сметном расчете (сметные нормативы, индексы, и др.)

    :ivar name: Наименование редакции (наименование, редакция, приказ)
    :ivar type_value: Тип нормативов из федерального реестра сметных
        нормативов
    :ivar date: Дата включения в федеральный реестр сметных нормативов
    :ivar num: Регистрационный номер в федеральном реестре сметных
        нормативов
    :ivar orders: Реквизиты приказов об утверждении
    """

    class Meta:
        name = "TLegal"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    type_value: Optional[TlegalType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "required": True,
        },
    )
    date: Optional[Tdate] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
        },
    )
    num: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num",
            "type": "Element",
            "required": True,
        },
    )
    orders: Optional[str] = field(
        default=None,
        metadata={
            "name": "Orders",
            "type": "Element",
        },
    )


@dataclass
class Toverhead:
    """
    Накладные расходы.

    :ivar reason: <text xmlns="">Обоснование нормы (шифр строки
        нормы)</text> <formula xmlns=""> Шифр для строки нормы сметной
        прибыли имеет следующий вид - "Пр/ППП-ХХХ.Х" где ППП – числовое
        обозначение номера приказа; ХХХ.Х – шифр, состоящий из двух
        частей: номер пункта (три знака) и номер подпункта,
        соответствующие приложению Методики к приказу; Шифр для строки
        нормы накладных расходов имеет следующий вид - "Пр/ППП-ХХХ.Х-Т"
        где ППП – числовое обозначение номера приказа; ХХХ.Х – шифр,
        состоящий из двух частей: номер пункта (три знака) и номер
        подпункта, соответствующие приложению Методики к приказу; Т -
        обозначение территории расположения объекта строительства: - не
        относящейся к районам Крайнего Севера и местностям, приравненным
        к ним (Территория) - 1; - относящейся к местностям, приравненным
        к районам Крайнего Севера (МПРКС) - 2; - относящейся к районам
        Крайнего Севера (РКС) - 3 </formula> <links xmlns="">Методика по
        разработке и применению нормативов сметной прибыли при
        определении сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 11.12.2020 №
        774/пр (с учетом изменений от 22.04.2022 № 317/пр). Методика по
        разработке и применению нормативов накладных расходов при
        определении сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 21.12.2020 №
        812/пр (с учетом изменений от 02.09.2021 № 636/пр). </links>
    :ivar name: <text xmlns="">Наименование по видам строительных,
        монтажных и ремонтно-строительных работ, определяемых в
        соответствии с наименованием сборников расценок и сметных
        нормативов </text> <links xmlns="">Методика по разработке и
        применению нормативов сметной прибыли при определении сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 11.12.2020 № 774/пр (с учетом изменений
        от 22.04.2022 № 317/пр). Методика по разработке и применению
        нормативов накладных расходов при определении сметной стоимости
        строительства, реконструкции, капитального ремонта, сноса
        объектов капитального строительства, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 21.12.2020 № 812/пр (с учетом изменений
        от 02.09.2021 № 636/пр). </links>
    :ivar target: <text xmlns="">К чему применяются: ФОТ- фонд оплаты
        труда рабочих не занятых обслуживанием машин и оплаты труда
        машинистов (механизаторов) </text> <links xmlns="">Методика по
        разработке и применению нормативов сметной прибыли при
        определении сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 11.12.2020 №
        774/пр (с учетом изменений от 22.04.2022 № 317/пр). Методика по
        разработке и применению нормативов накладных расходов при
        определении сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 21.12.2020 №
        812/пр (с учетом изменений от 02.09.2021 № 636/пр). </links>
    :ivar value: <text xmlns="">Значение норматива в %</text> <links
        xmlns="">Методика по разработке и применению нормативов сметной
        прибыли при определении сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, утвержденная приказом Министерства строительства
        и жилищно-коммунального хозяйства Российской Федерации от
        11.12.2020 № 774/пр (с учетом изменений от 22.04.2022 № 317/пр).
        Методика по разработке и применению нормативов накладных
        расходов при определении сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, утвержденная приказом Министерства строительства
        и жилищно-коммунального хозяйства Российской Федерации от
        21.12.2020 № 812/пр (с учетом изменений от 02.09.2021 № 636/пр).
        </links>
    :ivar value_total: <text xmlns="">Значение норматива в % с учетом
        коэффициента. Округление до 7-ми знаков. Округление производится
        один раз после всех математических операций. </text> <links
        xmlns="">Методика по разработке и применению нормативов сметной
        прибыли при определении сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, утвержденная приказом Министерства строительства
        и жилищно-коммунального хозяйства Российской Федерации от
        11.12.2020 № 774/пр (с учетом изменений от 22.04.2022 № 317/пр).
        Методика по разработке и применению нормативов накладных
        расходов при определении сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, утвержденная приказом Министерства строительства
        и жилищно-коммунального хозяйства Российской Федерации от
        21.12.2020 № 812/пр (с учетом изменений от 02.09.2021 № 636/пр).
        </links>
    :ivar price_base: <text xmlns="">Итоговая стоимость</text> <formula
        xmlns="">Базисный уровень цен Base=(Totals.Base.WorkersSalary
        (Итоговая оплата труда рабочих в базисном уровне цен)+
        Totals.Base. MachinistSalary(Итоговая оплата труда машинистов в
        базисном уровне цен))* Value(Значение норматива в
        %)*Coefficients (Коэффициенты к норме) Округление до 2-х знаков
        после запятой. Округление производится один раз после всех
        математических операций. Текущий уровень цен Price =
        (Totals.Price.WorkersSalary (Итоговая оплата труда рабочих в
        текущем уровне цен)+ Totals.Price. MachinistSalary(Итоговая
        оплата труда машинистов в текущем уровне цен))* Value(Значение
        норматива в %)*Coefficients (Коэффициенты к норме) Округление до
        2-х знаков после запятой. Округление производится один раз после
        всех математических операций. </formula> <links
        xmlns="">Методика по разработке и применению нормативов сметной
        прибыли при определении сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, утвержденная приказом Министерства строительства
        и жилищно-коммунального хозяйства Российской Федерации от
        11.12.2020 № 774/пр (с учетом изменений от 22.04.2022 № 317/пр).
        Методика по разработке и применению нормативов накладных
        расходов при определении сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, утвержденная приказом Министерства строительства
        и жилищно-коммунального хозяйства Российской Федерации от
        21.12.2020 № 812/пр (с учетом изменений от 02.09.2021 № 636/пр).
        </links>
    :ivar coefficients: <text xmlns="">Коэффициенты к норме, учитывающие
        изменения. Округление до 7-ми знаков. Округление производится
        один раз после всех математических операций. </text> <links
        xmlns="">Методика по разработке и применению нормативов сметной
        прибыли при определении сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, утвержденная приказом Министерства строительства
        и жилищно-коммунального хозяйства Российской Федерации от
        11.12.2020 № 774/пр (с учетом изменений от 22.04.2022 № 317/пр).
        Методика по разработке и применению нормативов накладных
        расходов при определении сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, утвержденная приказом Министерства строительства
        и жилищно-коммунального хозяйства Российской Федерации от
        21.12.2020 № 812/пр (с учетом изменений от 02.09.2021 № 636/пр).
        </links>
    :ivar price_cur: <text xmlns="">Итоговая стоимость</text> <formula
        xmlns="">Текущий уровень цен
        Current=(Totals.Current.WorkersSalary (Итоговая оплата труда
        рабочих в текущем уровне цен)+ Totals.Current.
        MachinistSalary(Итоговая оплата труда машинистов в текущем
        уровне цен))* Value(Значение норматива в %)*Coefficients
        (Коэффициенты к норме) Округление до 2-х знаков после запятой.
        Округление производится один раз после всех математических
        операций. Текущий уровень цен Price =
        (Totals.Price.WorkersSalary (Итоговая оплата труда рабочих в
        текущем уровне цен)+ Totals.Price. MachinistSalary(Итоговая
        оплата труда машинистов в текущем уровне цен))* Value(Значение
        норматива в %)*Coefficients (Коэффициенты к норме) Округление до
        2-х знаков после запятой. Округление производится один раз после
        всех математических операций. </formula> <links
        xmlns="">Методика по разработке и применению нормативов сметной
        прибыли при определении сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, утвержденная приказом Министерства строительства
        и жилищно-коммунального хозяйства Российской Федерации от
        11.12.2020 № 774/пр (с учетом изменений от 22.04.2022 № 317/пр).
        Методика по разработке и применению нормативов накладных
        расходов при определении сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, утвержденная приказом Министерства строительства
        и жилищно-коммунального хозяйства Российской Федерации от
        21.12.2020 № 812/пр (с учетом изменений от 02.09.2021 № 636/пр).
        </links>
    """

    class Meta:
        name = "TOverhead"

    reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    target: Optional[ToverheadTarget] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    value_total: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValueTotal",
            "type": "Element",
            "required": True,
        },
    )
    price_base: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PriceBase",
            "type": "Element",
            "required": True,
        },
    )
    coefficients: Optional[Tcoefficients] = field(
        default=None,
        metadata={
            "name": "Coefficients",
            "type": "Element",
        },
    )
    price_cur: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PriceCur",
            "type": "Element",
        },
    )


@dataclass
class TresCoefficient:
    """
    Поправочный коэффициент, учитывающий усложняющие факторы и (или) условия
    производства работ, применяемый к количеству или к стоимости.

    :ivar values: Значение коэффициента
    """

    class Meta:
        name = "TResCoefficient"

    values: Optional["TresCoefficient.Values"] = field(
        default=None,
        metadata={
            "name": "Values",
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class Values:
        """
        :ivar value: Значение коэффициента
        """

        value: list["TresCoefficient.Values.Value"] = field(
            default_factory=list,
            metadata={
                "name": "Value",
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass
        class Value:
            """
            :ivar target: К чему применяются
            :ivar coef_value: Значение коэффициента
            """

            target: Optional[ValueTarget] = field(
                default=None,
                metadata={
                    "name": "Target",
                    "type": "Element",
                    "required": True,
                },
            )
            coef_value: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "CoefValue",
                    "type": "Element",
                    "required": True,
                },
            )


@dataclass
class TcostIndexValue(TindexValue):
    """
    Комплексный тип для передачи значения индекса изменения стоимости оплаты труда
    (EstimateType="Строительство") или значений индексов изменений стоимости
    элементов прямых затрат (EstimateType="Реставрация")

    :ivar target: К чему применяется индекс. Для типа определения
        сметной стоимости "Строительство"
        (EstimateType="Строительство"): к оплате труда основных рабочих
        (ОТ) и машинистов (ОТМ). Для типа определения сметной стоимости
        "Реставрация" (EstimateType="Реставрация"): к оплате труда
        основных рабочих (ОТ) и машинистов (ОТМ), к эксплуатации машин
        (ЭМ) и материальным ресурсам (М).
    """

    class Meta:
        name = "TCostIndexValue"

    target: Optional[TcostIndexValueTarget] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Tmeta:
    """
    Информация о программном комплексе и версии формата.

    :ivar soft: Программный комплекс
    :ivar file:
    """

    class Meta:
        name = "TMeta"

    soft: Optional["Tmeta.Soft"] = field(
        default=None,
        metadata={
            "name": "Soft",
            "type": "Element",
            "required": True,
        },
    )
    file: Optional[TfileFormat] = field(
        default=None,
        metadata={
            "name": "File",
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class Soft:
        """
        :ivar name: Наименование программного комплекса
        :ivar version: Версия программного комплекса
        """

        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Element",
                "required": True,
            },
        )
        version: Optional[str] = field(
            default=None,
            metadata={
                "name": "Version",
                "type": "Element",
                "required": True,
            },
        )


@dataclass
class TpriceIndex(TindexValue):
    """<text xmlns="">Индекс изменения сметной стоимости к элементам прямых затрат
    локального сметного расчета или к виду работ (СМР, Реставрация, Оборудование,
    Прочие, ПНР, Перевозка). От вида индексации зависит применение индексов в ЛСР:
    в позициях или в итогах сметы.

    БИМ с применением индексов к элементам прямых затрат:
    1. "Строительство" - индекс к ОТ и ОТМ в позициях ЛСР; индекс к МР, ЭМ в итогах ЛСР; индекс по видам
    работ Оборудование, Прочие в итогах ЛСР; индекс к Перевозке в позициях ЛСР; индекс к Прочим
    затратам, учитываемым в соответствии с пунктом 184 Методики, в позициях ЛСР.
    2. "Реставрация" - индекс к ОТ, ОТМ, ЭМ, М в позициях ЛСР; индекс к Прочим затратам, учитываемым в
    соответствии с пунктом 184 Методики, в позициях ЛСР.
    БИМ с применением индекса СМР:
    1. "Строительство" - индекс по видам работ СМР, Оборудование, Прочие, ПНР в итогах ЛСР; индекс к
    Перевозке в позициях ЛСР; индекс к Прочим затратам, учитываемым в соответствии с пунктом 184
    Методики в позициях ЛСР.
    2. "Реставрация" - индекс к ремонтно-реставрационным работам в базисном уровне цен 1984 года с
    пересчетом в уровень цен СНБ 2001 года в итогах ЛСР; индекс к ремонтно-реставрационным работам в
    уровне цен СНБ 2001 года с пересчетом в текущий уровень цен в итогах ЛСР; индекс к Прочим затратам,
    учитываемым в соответствии с пунктом 184 Методики, в позициях ЛСР.
    Округление до 2-х знаков. Округление производится один раз после всех математических операций
    </text>

    :ivar index_name: Наименование индекса изменения сметной стоимости к
        элементам затрат локального сметного расчета или единого индекса
        пересчета по локальному сметному расчету по виду работ (СМР,
        Реставрация)
    """

    class Meta:
        name = "TPriceIndex"

    index_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndexName",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Tprofit(Toverhead):
    """
    Сметная прибыль.
    """

    class Meta:
        name = "TProfit"


@dataclass
class TresCoefficientDetail(TresCoefficient):
    """Результирующее значение коэффициента для учета усложняющих факторов и (или)
    условий производства работ, применяемый к стоимости или к количеству.

    Определяется как произведение всех коэффициентов к количеству и
    произведение коэффициентов к стоимости. Округление до 7-ми знаков.
    Округление производится один раз после всех математических операций.

    :ivar name: Наименование коэффициента. Указывается наименование,
        величина, а также составляющие единичных расценок, к которым
        коэффициент применяется
    :ivar reason: Обоснование коэффициента (шифр коэффициента (при
        наличии) или ссылка на положения сметных нормативов и (или)
        пункты разделов сборников единичных расценок)
    """

    class Meta:
        name = "TResCoefficientDetail"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Element",
        },
    )


@dataclass
class TresIndex:
    """
    Индекс изменения сметной стоимости.

    :ivar name: Наименование индекса изменения сметной стоимости
    :ivar reason: Обоснование индекса изменения сметной стоимости
    :ivar num: Порядковый номер индекса изменения сметной стоимости
    :ivar value:
    """

    class Meta:
        name = "TResIndex"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Element",
        },
    )
    num: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num",
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[TindexValue] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Tmachinist:
    """<text xmlns="">Оплата труда машинистов (рабочих, управляющих машинами),
    включенная в состав затрат на эксплуатацию строительных машин.

    Рассчитывается в составе стоимости маш.–ч машин. Приводится
    справочно, для определения ФОТ </text> <links xmlns=""> Методические
    рекомендации по определению сметных цен на эксплуатацию машин и
    механизмов утвержденные приказом Министерства строительства и
    жилищно-коммунального хозяйства Российской Федерации от 4 сентября
    2019 г. № 513/пр. Методика определения сметной стоимости
    строительства, реконструкции, капитального ремонта, сноса объектов
    капитального строительства, работ по сохранению объектов культурного
    наследия (памятников истории и культуры) народов Российской
    Федерации на территории Российской Федерации, утвержденная приказом
    Министерства строительства и жилищно-коммунального хозяйства
    Российской Федерации от 4 августа 2020 г. № 421/пр </links>

    :ivar num: <text xmlns="">Порядковый номер строки в совокупности с
        единичной расценкой или позиции в разделе локального сметного
        расчета. Номер строки в совокупности с единичной расценкой
        связан с ней, состоит из трёх групп цифр, разделенных точкой:
        первая группа цифр соответствует номеру позиции (единичной
        расценки), вторая - соответствует номеру позиции ресурса,
        третья– порядковому номеру строки в позиции </text>
    :ivar code: <text xmlns="">Шифр (код) затрат на оплату труда
        машиниста в локальном сметном расчете</text> <links
        xmlns="">Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 августа 2020 г. № 421/пр </links>
    :ivar name: <text xmlns="">Наименование затрат на оплата труда
        машиниста. Указывается полностью, без сокращений в соответствии
        с данными, включенными в ФРСН или в соответствии с проектной и
        иной технической документацией </text> <links xmlns="">Методика
        определения сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        работ по сохранению объектов культурного наследия (памятников
        истории и культуры) народов Российской Федерации на территории
        Российской Федерации, утвержденная приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 4 августа 2020 г. № 421/пр </links>
    :ivar consumption: <text xmlns="">Количество в соответствии с
        проектной и (или) иной технической документацией и с учетом
        единицы измерения позиции </text> <links xmlns="">Методика
        определения сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        работ по сохранению объектов культурного наследия (памятников
        истории и культуры) народов Российской Федерации на территории
        Российской Федерации, утвержденная приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 4 августа 2020 г. № 421/пр </links>
    :ivar unit: <text xmlns="">Единица измерения позиции</text> <links
        xmlns="">Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 августа 2020 г. № 421/пр </links>
    :ivar price_per_unit_cur: <text xmlns="">Сметная цена оплаты труда
        машинистов за единицу измерения в текущем уровне цен</text>
        <formula xmlns="">PricePerUnitCur = PricePerUnitBase(Сметная
        цена оплаты труда машинистов за единицу измерения в базисном
        уровне цен) * Indexes (Индексы изменения сметной стоимости,
        применяемые к оплате труда машинистов) Округление до 2-х знаков.
        Округление производится один раз после всех математических
        операций </formula> <links xmlns="">Методика определения сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр </links>
    :ivar price_total_cur: <text xmlns="">Итоговая стоимость оплаты
        труда машинистов в текущем уровне цен с учетом количества по
        позиции </text> <formula xmlns="">PriceTotalCur =
        PriceTotalBase(Итоговая стоимость оплаты труда машинистов в
        базисном уровне цен с учетом количества по позиции)*
        Indexes(Индексы изменения сметной стоимости, применяемые к
        оплате труда машинистов) Округление до 2-х знаков. Округление
        производится один раз после всех математических операций
        </formula> <links xmlns="">Методика определения сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр </links>
    :ivar consumption_total: <text xmlns="">Результирующее количество на
        весь объем и с учетом коэффициентов к количеству</text>
    :ivar price_per_unit_base: <text xmlns="">Сметная цена оплаты труда
        машинистов за единицу измерения в базисном уровне цен в
        соответствии с данными, включенными в ФРСН или в соответствии с
        проектной и иной технической документацией </text> <links
        xmlns="">Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 августа 2020 г. № 421/пр </links>
    :ivar price_total_base: <text xmlns="">Итоговая стоимость оплаты
        труда машинистов в базисном уровне цен </text> <formula
        xmlns="">PriceTotalBase=PricePerUnitBase(Сметная цена оплату
        труда машинистов за единицу измерения в базисном уровне
        цен)*Consumption (Количество с учетом единицы измерения
        позиции)* Coefficients(Коэффициенты, для учета в сметной
        документации влияния условий производства работ, применяемые к
        стоимости и к количеству) Округление до 2-х знаков. Округление
        производится один раз после всех математических операций
        </formula> <links xmlns="">Методика определения сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр </links>
    :ivar coefficients: <text xmlns="">Коэффициенты учета условий
        производства работ, применяемые к стоимости и к количеству
        Округление до 7-ми знаков. Округление производится один раз
        после всех математических операций </text> <links
        xmlns="">Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 августа 2020 г. № 421/пр </links>
    :ivar index: <text xmlns="">Индекс изменения сметной стоимости,
        применяемый к оплате труда</text>
    """

    class Meta:
        name = "TMachinist"

    num: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num",
            "type": "Element",
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    consumption: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Consumption",
            "type": "Element",
            "required": True,
        },
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "required": True,
        },
    )
    price_per_unit_cur: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricePerUnitCur",
            "type": "Element",
        },
    )
    price_total_cur: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PriceTotalCur",
            "type": "Element",
        },
    )
    consumption_total: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ConsumptionTotal",
            "type": "Element",
            "required": True,
        },
    )
    price_per_unit_base: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricePerUnitBase",
            "type": "Element",
            "required": True,
        },
    )
    price_total_base: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PriceTotalBase",
            "type": "Element",
            "required": True,
        },
    )
    coefficients: Optional["Tmachinist.Coefficients"] = field(
        default=None,
        metadata={
            "name": "Coefficients",
            "type": "Element",
        },
    )
    index: Optional[TresIndex] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
        },
    )

    @dataclass
    class Coefficients:
        """
        :ivar final: <text xmlns="">Итоговое значение коэффициента учета
            условий производства работ, применяемое к стоимости и к
            расходу ресурса. Округление до 7-ми знаков. Округление
            производится один раз после всех математических операций
            </text> <links xmlns="">Методические рекомендации по
            применению федеральных единичных расценок на строительные,
            специальные строительные, ремонтно-строительные, монтаж
            оборудования и пусконаладочные работы, утвержденные приказом
            Министерства строительства и жилищно-коммунального хозяйства
            Российской Федерации от 4 сентября 2019 г. № 519/пр.
            Методические рекомендации по определению сметных цен на
            эксплуатацию машин и механизмов, утвержденные приказом
            Министерства строительства и жилищно-коммунального хозяйства
            Российской Федерации от 4 сентября 2019 г. № 513/пр.
            </links>
        :ivar coefficient: <text xmlns="">Коэффициент учета условий
            производства работ, применяемый к стоимости и к расходу
            ресурса </text> <links xmlns="">Методические рекомендации по
            применению федеральных единичных расценок на строительные,
            специальные строительные, ремонтно-строительные, монтаж
            оборудования и пусконаладочные работы, утвержденные приказом
            Министерства строительства и жилищно-коммунального хозяйства
            Российской Федерации от 4 сентября 2019 г. № 519/пр.
            Методические рекомендации по определению сметных цен на
            эксплуатацию машин и механизмов, утвержденные приказом
            Министерства строительства и жилищно-коммунального хозяйства
            Российской Федерации от 4 сентября 2019 г. № 513/пр.
            </links>
        """

        final: Optional[TresCoefficient] = field(
            default=None,
            metadata={
                "name": "Final",
                "type": "Element",
                "required": True,
            },
        )
        coefficient: list[TresCoefficientDetail] = field(
            default_factory=list,
            metadata={
                "name": "Coefficient",
                "type": "Element",
                "min_occurs": 1,
            },
        )


@dataclass
class TpriceElement:
    """
    Уровень цен итоговой сметной стоимости локального сметного расчета по элементам
    или по видам основных работ.

    :ivar price_base: <text xmlns="">Стоимость в базисном уровне
        цен</text>
    :ivar price_index: <text xmlns="">Индекс изменения сметной стоимости
        к элементам затрат локального сметного расчета или единый индекс
        пересчета по локальному сметному расчету по виду работ (СМР,
        Реставрация, ПНР, Прочие работы и затраты) </text>
    :ivar price_current: <text xmlns="">Стоимость в текущем уровне
        цен</text>
    """

    class Meta:
        name = "TPriceElement"

    price_base: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PriceBase",
            "type": "Element",
        },
    )
    price_index: Optional[TpriceIndex] = field(
        default=None,
        metadata={
            "name": "PriceIndex",
            "type": "Element",
        },
    )
    price_current: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PriceCurrent",
            "type": "Element",
        },
    )


@dataclass
class Ttransportation:
    """<text xmlns="">Затраты на перевозку грузов автомобильным или иным видом
    транспорта</text> <links xmlns="">Методика определения сметной стоимости
    строительства, реконструкции, капитального ремонта, сноса объектов капитального
    строительства, работ по сохранению объектов культурного наследия (памятников
    истории и культуры) народов Российской Федерации на территории Российской
    Федерации, утвержденная приказом Министерства строительства и жилищно-
    коммунального хозяйства Российской Федерации от 4 августа 2020 г.

    № 421/пр </links>

    :ivar num: <text xmlns="">Порядковый номер строки в совокупности с
        единичной расценкой или позиции в разделе локального сметного
        расчета. Номер строки в совокупности с единичной расценкой
        связан с ней, состоит из трёх групп цифр, разделенных точкой:
        первая группа цифр соответствует номеру позиции (единичной
        расценки), вторая - соответствует номеру позиции ресурса,
        третья– порядковому номеру строки в позиции </text>
    :ivar prefix: <text xmlns="">Префикс шифра цены на материалы,
        изделия, конструкции и оборудования, расценки на эксплуатацию
        строительных машин и автотранспортных средств, цены на перевозку
        грузов </text> <links xmlns="">Методика определения сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр. Методические рекомендации по определению сметных
        цен на материалы, изделия, конструкции, оборудование,
        утвержденные приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 сентября 2019
        г. № 517/пр. </links>
    :ivar code: <text xmlns="">Шифр (код) затрат на переовзку грузов в
        локальном сметном расчете</text> <links xmlns="">Методика
        определения сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        работ по сохранению объектов культурного наследия (памятников
        истории и культуры) народов Российской Федерации на территории
        Российской Федерации, утвержденная приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 4 августа 2020 г. № 421/пр </links>
    :ivar name: <text xmlns="">Наименование затрат на перевозку грузов
        автомобильным или иным видом транспорта в локальном сметном
        расчете, содержит шифр материального ресурса или оборудования, к
        которому относиться. Указывается полностью, без сокращений в
        соответствии с данными, включенными в ФРСН или в соответствии с
        проектной и иной технической документацией </text> <links
        xmlns="">Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 августа 2020 г. № 421/пр </links>
    :ivar consumption: <text xmlns="">Количество в соответствии с
        проектной и (или) иной технической документацией и с учетом
        единицы измерения позиции (затрат на перевозку) </text> <links
        xmlns="">Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 августа 2020 г. № 421/пр </links>
    :ivar unit: <text xmlns="">Единица измерения позиции (затрат на
        перевозку)</text> <links xmlns="">Методика определения сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр </links>
    :ivar price_per_unit_cur: <text xmlns="">Сметная цена на перевозку
        грузов за единицу измерения в текущем уровне цен</text> <formula
        xmlns="">PricePerUnitCur = PricePerUnitBase(Сметная цена на
        перевозку грузов за единицу измерения в базисном уровне цен) *
        Indexes (Индексы изменения сметной стоимости, применяемые к
        стоимости перевозки грузов) Округление до 2-х знаков. Округление
        производится один раз после всех математических операций
        </formula> <links xmlns="">Методика определения сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр </links>
    :ivar price_total_cur: <text xmlns="">Итоговая стоимость перевозки
        грузов в текущем уровне цен с учетом количества по позиции
        </text> <formula xmlns="">PriceTotalCur =
        PriceTotalBase(Итоговая стоимость перевозки грузов в базисном
        уровне цен с учетом количества по позиции)* Indexes(Индексы
        изменения сметной стоимости, применяемые к сметным ценам на
        перевозку) Округление до 2-х знаков. Округление производится
        один раз после всех математических операций </formula> <links
        xmlns="">Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 августа 2020 г. № 421/пр </links>
    :ivar consumption_total: <text xmlns="">Результирующее количество на
        весь объем и с учетом коэффициентов к количеству</text>
    :ivar price_per_unit_base: <text xmlns="">Сметная цена на перевозку
        грузов за единицу измерения в базисном уровне цен в соответствии
        с данными, включенными в ФРСН или в соответствии с проектной и
        иной технической документацией </text> <links xmlns="">Методика
        определения сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        работ по сохранению объектов культурного наследия (памятников
        истории и культуры) народов Российской Федерации на территории
        Российской Федерации, утвержденная приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 4 августа 2020 г. № 421/пр </links>
    :ivar price_total_base: <text xmlns="">Итоговая стоимость перевозки
        грузов в базисном уровне цен </text> <formula
        xmlns="">PriceTotalBase=PricePerUnitBase(Сметная цена на
        перевозку грузов за единицу измерения в базисном уровне
        цен)*Consumption (Количество с учетом единицы измерения позиции
        (затрат на перевозку))* Coefficients(Коэффициенты, для учета в
        сметной документации влияния условий производства работ,
        применяемые к стоимости и к количеству) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций </formula> <links xmlns="">Методика
        определения сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        работ по сохранению объектов культурного наследия (памятников
        истории и культуры) народов Российской Федерации на территории
        Российской Федерации, утвержденная приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 4 августа 2020 г. № 421/пр </links>
    :ivar coefficients: <text xmlns="">Коэффициенты учета условий
        производства работ, применяемые к стоимости и к количеству
        Округление до 7-ми знаков. Округление производится один раз
        после всех математических операций </text> <links
        xmlns="">Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 августа 2020 г. № 421/пр </links>
    :ivar index: <text xmlns="">Индекс изменения сметной
        стоимости</text>
    """

    class Meta:
        name = "TTransportation"

    num: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num",
            "type": "Element",
        },
    )
    prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prefix",
            "type": "Element",
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    consumption: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Consumption",
            "type": "Element",
            "required": True,
        },
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "required": True,
        },
    )
    price_per_unit_cur: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricePerUnitCur",
            "type": "Element",
        },
    )
    price_total_cur: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PriceTotalCur",
            "type": "Element",
        },
    )
    consumption_total: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ConsumptionTotal",
            "type": "Element",
            "required": True,
        },
    )
    price_per_unit_base: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricePerUnitBase",
            "type": "Element",
            "required": True,
        },
    )
    price_total_base: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PriceTotalBase",
            "type": "Element",
            "required": True,
        },
    )
    coefficients: Optional["Ttransportation.Coefficients"] = field(
        default=None,
        metadata={
            "name": "Coefficients",
            "type": "Element",
        },
    )
    index: Optional[TresIndex] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
        },
    )

    @dataclass
    class Coefficients:
        """
        :ivar final: <text xmlns="">Итоговое значение коэффициента учета
            условий производства работ, применяемое к стоимости и к
            расходу ресурса Округление до 7-ми знаков. Округление
            производится один раз после всех математических операций
            </text> <links xmlns="">Методические рекомендации по
            применению федеральных единичных расценок на строительные,
            специальные строительные, ремонтно-строительные, монтаж
            оборудования и пусконаладочные работы, утвержденные приказом
            Министерства строительства и жилищно-коммунального хозяйства
            Российской Федерации от 4 сентября 2019 г. № 519/пр.
            Методические рекомендации по определению сметных цен на
            эксплуатацию машин и механизмов, утвержденные приказом
            Министерства строительства и жилищно-коммунального хозяйства
            Российской Федерации от 4 сентября 2019 г. № 513/пр.
            </links>
        :ivar coefficient: <text xmlns="">Коэффициент учета условий
            производства работ, применяемый к стоимости и к расходу
            ресурса </text> <links xmlns="">Методические рекомендации по
            применению федеральных единичных расценок на строительные,
            специальные строительные, ремонтно-строительные, монтаж
            оборудования и пусконаладочные работы, утвержденные приказом
            Министерства строительства и жилищно-коммунального хозяйства
            Российской Федерации от 4 сентября 2019 г. № 519/пр.
            Методические рекомендации по определению сметных цен на
            эксплуатацию машин и механизмов, утвержденные приказом
            Министерства строительства и жилищно-коммунального хозяйства
            Российской Федерации от 4 сентября 2019 г. № 513/пр.
            </links>
        """

        final: Optional[TresCoefficient] = field(
            default=None,
            metadata={
                "name": "Final",
                "type": "Element",
                "required": True,
            },
        )
        coefficient: list[TresCoefficientDetail] = field(
            default_factory=list,
            metadata={
                "name": "Coefficient",
                "type": "Element",
                "min_occurs": 1,
            },
        )


@dataclass
class Tresource:
    """
    Базовый комплексный тип для передачи данных ресурсов локального сметного
    расчета.

    :ivar num: <text xmlns="">Порядковый номер ресурса в единичной
        расценке или позиции в локальном сметном расчете. Номер
        неучтенного строительного ресурса (связанный с единичной
        расценкой(позицией)) состоит из двух групп цифр, разделенных
        точкой: первая группа цифр которого соответствует номеру
        позиции, вторая – порядковому номеру строки в позиции. </text>
    :ivar prefix: <text xmlns="">Префикс шифра цены на материалы,
        изделия, конструкции и оборудования, расценки на эксплуатацию
        строительных машин и автотранспортных средств, цены на перевозку
        грузов </text> <links xmlns="">Методика определения сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр. Методические рекомендации по определению сметных
        цен на материалы, изделия, конструкции, оборудование,
        утвержденные приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 сентября 2019
        г. № 517/пр. </links>
    :ivar code: <text xmlns="">Шифр (код) строительного ресурса в
        соответствии с Классификатором строительных ресурсов,
        сформированным приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации. Строительным
        ресурсам, цена которых определена в результате конъюнктурного
        анализа, присваивается шифр (код) в соответствии с описанием в
        Методике. </text> <links xmlns="">Методические рекомендации по
        определению сметных цен на материалы, изделия, конструкции,
        оборудование и цен услуг на перевозку грузов для строительства,
        утвержденные приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 сентября 2019
        г. № 517/пр. Методические рекомендации по определению сметных
        цен на эксплуатацию машин и механизмов, утвержденные приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 сентября 2019 г. № 513/пр. </links>
    :ivar name: <text xmlns="">Наименование ресурса в соответствии с
        Классификатором строительных ресурсов, сформированным приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации. Указывается полностью, без сокращений в
        соответствии с данными, включенными в ФРСН или в соответствии с
        проектной и иной технической документацией, а также
        обосновывающими сметную цену строительных ресурсов документами.
        Для материалов, изделий, конструкций и оборудования,
        отсутствующих в ФРСН, указывается максимально полное их описание
        с указанием характеристик. </text> <links xmlns="">Методические
        рекомендации по определению сметных цен на материалы, изделия,
        конструкции, оборудование и цен услуг на перевозку грузов для
        строительства, утвержденные приказом Министерства строительства
        и жилищно-коммунального хозяйства Российской Федерации от 4
        сентября 2019 г. № 517/пр. Методические рекомендации по
        определению сметных цен на эксплуатацию машин и механизмов,
        утвержденные приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 сентября 2019
        г. № 513/пр. </links>
    :ivar comment: Примечание к элементу в локальном сметном расчете
    :ivar consumption: <text xmlns="">Количество строительного ресурса
        на единицу измерения единичной расценки</text> <links
        xmlns="">Методические рекомендации по определению сметных цен на
        материалы, изделия, конструкции, оборудование и цен услуг на
        перевозку грузов для строительства, утвержденные приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 сентября 2019 г. № 517/пр.
        Методические рекомендации по определению сметных цен на
        эксплуатацию машин и механизмов, утвержденные приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 сентября 2019 г. № 513/пр. </links>
    :ivar unit: <text xmlns="">Единица измерения расхода ресурса.</text>
        <links xmlns="">Классификатор строительных ресурсов,
        сформированный приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации. Методические
        рекомендации по определению сметных цен на эксплуатацию машин и
        механизмов, утвержденные приказом Министерства строительства и
        жилищно-коммунального хозяйства Российской Федерации от 4
        сентября 2019 г. № 513/пр. </links>
    :ivar price_per_unit_cur: <text xmlns="">Сметная цена ресурса за
        единицу измерения в текущем уровне цен. Для строительных
        ресурсов, отсутствующих в ФРСН, сметная цена в текущем уровне
        цен (без учета НДС) определяется по результатам конъюнктурного
        анализа в соответствии с описанием в Методике. Для остальных
        строительных ресурсов параметр отсутствует </text> <links
        xmlns="">Методические рекомендации по определению сметных цен на
        материалы, изделия, конструкции, оборудование и цен услуг на
        перевозку грузов для строительства, утвержденные приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 сентября 2019 г. № 517/пр.
        Методические рекомендации по определению сметных цен на
        эксплуатацию машин и механизмов, утвержденные приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 сентября 2019 г. № 513/пр. </links>
    :ivar price_total_cur: <text xmlns="">Итоговая стоимость ресурса в
        текущем уровне цен с учетом объема работ по расценке и
        примененных коэффициентов. Определяется для ресурсов,
        отсутствующих в ФРСН, для остальных строительных ресурсов
        параметр отсутствует. </text> <formula xmlns=""> Для ресурсов,
        отсутствующих в ФРСН: PriceTotalCur (Итоговая стоимость ресурса
        в текущем уровне цен) = ConsumptionTotal (Результирующее
        количество строительного ресурса на весь объем единичной
        расценки с учетом коэффициентов к количеству)*PricePerUnitCur
        (Сметная цена за единицу измерения в текущем уровне цен)*
        Coefficients (Результирующий коэффициент к стоимости ресурса)
        Округление до 2-х знаков. Округление производится один раз после
        всех математических операций. </formula> <links
        xmlns="">Методические рекомендации по определению сметных цен на
        материалы, изделия, конструкции, оборудование и цен услуг на
        перевозку грузов для строительства, утвержденные приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 сентября 2019 г. № 517/пр.
        Методические рекомендации по определению сметных цен на
        эксплуатацию машин и механизмов, утвержденные приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 сентября 2019 г. № 513/пр. </links>
    :ivar consumption_total: <text xmlns="">Результирующее количество
        строительного ресурса на весь объем единичной расценки и с
        учетом коэффициентов к количеству. Не используется в ресурсах не
        входящих в единичную расценку. </text> <formula
        xmlns="">ConsumptionTotal (Результирующее количество
        строительного ресурса на весь объем единичной расценки с учетом
        коэффициентов к количеству) = Consumption (Количество ресурса на
        единицу измерения расценки) * QuantityTotal(Результирующий объем
        работ по расценке) * Coefficients(Коэффициенты, применяемые к
        количеству) Округление до 7-ми знаков. Округление производится
        один раз после всех математических операций. </formula> <links
        xmlns="">Методические рекомендации по определению сметных цен на
        материалы, изделия, конструкции, оборудование и цен услуг на
        перевозку грузов для строительства, утвержденные приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 сентября 2019 г. № 517/пр.
        Методические рекомендации по определению сметных цен на
        эксплуатацию машин и механизмов, утвержденные приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 сентября 2019 г. № 513/пр. </links>
    :ivar price_per_unit_base: <text xmlns="">Сметная цена ресурса за
        единицу измерения в базисном уровне цен. Для строительных
        ресурсов, отсутствующих в ФРСН параметр не определяется </text>
        <links xmlns="">Методические рекомендации по определению сметных
        цен на эксплуатацию машин и механизмов, утвержденные приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 сентября 2019 г. № 513/пр. </links>
    :ivar price_total_base: <text xmlns="">Итоговая стоимость ресурса в
        базисном уровне цен с учетом объема работ по расценке и
        примененных коэффициентов Для строительных ресурсов,
        отсутствующих в ФРСН, указывается сметная стоимость всего в
        базисном уровне цен, полученная как частное от деления итоговой
        текущей стоимости ресурса и индекса к ресурсу </text> <formula
        xmlns=""> PriceTotalBase (Итоговая стоимость ресурса в базисном
        уровне цен) = PricePerUnitBase(Сметная цена ресурса за единицу
        измерения в базисном уровне цен)*ConsumptionTotal
        (Результирующее количество строительного ресурса на весь объем
        единичной расценки с учетом коэффициентов к количеству)*
        Coefficients(Коэффициенты, для учета в сметной документации
        влияния условий производства работ, применяемые к стоимости
        ресурса) Для ресурсов, отсутствующих в ФРСН: PriceTotalBase
        (Итоговая стоимость ресурса в базисном уровне цен) =
        PriceTotalCur(Итоговая стоимость ресурса в текущем уровне цен с
        учетом объема работ по расценке и примененных коэффициентов) /
        Indexes(Индекс изменения сметной стоимости, применяемый к
        стоимости ресурса) Округление до 2-х знаков. Округление
        производится один раз после всех математических операций.
        </formula> <links xmlns="">Методические рекомендации по
        определению сметных цен на материалы, изделия, конструкции,
        оборудование и цен услуг на перевозку грузов для строительства,
        утвержденные приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 сентября 2019
        г. № 517/пр. Методические рекомендации по определению сметных
        цен на эксплуатацию машин и механизмов, утвержденные приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 сентября 2019 г. № 513/пр. </links>
    :ivar coefficients: <text xmlns="">Коэффициенты учета условий
        производства работ, применяемые к стоимости и к количеству
        ресурса. Округление производится до семи знаков после запятой по
        итогу перемножения. </text> <links xmlns="">Методические
        рекомендации по применению федеральных единичных расценок на
        строительные, специальные строительные, ремонтно-строительные,
        монтаж оборудования и пусконаладочные работы, утвержденные
        приказом Министерства строительства и жилищно-коммунального
        хозяйства Российской Федерации от 4 сентября 2019 г. № 519/пр.
        </links>
    :ivar index: <text xmlns="">Индекс изменения сметной стоимости,
        применяемый к стоимости ресурса</text>
    :ivar transport: <text xmlns="">Затраты на перевозку грузов
        автомобильным или иным видом транспорта</text> <links
        xmlns="">Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 августа 2020 г. № 421/пр </links>
    :ivar warehouse_cur: <text xmlns="">Заготовительно-складские расходы
        (в текущем уровне цен). Определяются при составлении сметной
        документации в порядке, установленном в Методике применения
        сметных цен строительных ресурсов </text> <links
        xmlns="">Методические рекомендации по определению сметных цен на
        материалы, изделия, конструкции, оборудование, утвержденные
        приказом Министерства строительства и жилищно-коммунального
        хозяйства Российской Федерации от 4 сентября 2019 г. № 517/пр.
        Методика применения сметных цен строительных ресурсов,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 8 февраля 2017
        г. № 77/пр. </links>
    :ivar warehouse_base: <text xmlns="">Заготовительно-складские
        расходы (в базовом уровне цен). Определяются при составлении
        сметной документации в порядке, установленном в Методике
        применения сметных цен строительных ресурсов </text> <links
        xmlns="">Методические рекомендации по определению сметных цен на
        материалы, изделия, конструкции, оборудование, утвержденные
        приказом Министерства строительства и жилищно-коммунального
        хозяйства Российской Федерации от 4 сентября 2019 г. № 517/пр.
        Методика применения сметных цен строительных ресурсов,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 8 февраля 2017
        г. № 77/пр. </links>
    """

    class Meta:
        name = "TResource"

    num: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num",
            "type": "Element",
        },
    )
    prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prefix",
            "type": "Element",
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
        },
    )
    consumption: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Consumption",
            "type": "Element",
            "required": True,
        },
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "required": True,
        },
    )
    price_per_unit_cur: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricePerUnitCur",
            "type": "Element",
        },
    )
    price_total_cur: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PriceTotalCur",
            "type": "Element",
        },
    )
    consumption_total: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ConsumptionTotal",
            "type": "Element",
            "required": True,
        },
    )
    price_per_unit_base: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricePerUnitBase",
            "type": "Element",
        },
    )
    price_total_base: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PriceTotalBase",
            "type": "Element",
        },
    )
    coefficients: Optional["Tresource.Coefficients"] = field(
        default=None,
        metadata={
            "name": "Coefficients",
            "type": "Element",
        },
    )
    index: Optional[TresIndex] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
        },
    )
    transport: list[Ttransportation] = field(
        default_factory=list,
        metadata={
            "name": "Transport",
            "type": "Element",
        },
    )
    warehouse_cur: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WarehouseCur",
            "type": "Element",
        },
    )
    warehouse_base: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WarehouseBase",
            "type": "Element",
        },
    )

    @dataclass
    class Coefficients:
        """
        :ivar final: <text xmlns="">Итоговое значение коэффициента учета
            условий производства работ, применяемое к стоимости и к
            расходу ресурса. Округление до 7-ми знаков. Округление
            производится один раз после всех математических операций
            </text> <links xmlns="">Методические рекомендации по
            применению федеральных единичных расценок на строительные,
            специальные строительные, ремонтно-строительные, монтаж
            оборудования и пусконаладочные работы, утвержденные приказом
            Министерства строительства и жилищно-коммунального хозяйства
            Российской Федерации от 4 сентября 2019 г. № 519/пр.
            Методические рекомендации по определению сметных цен на
            эксплуатацию машин и механизмов, утвержденные приказом
            Министерства строительства и жилищно-коммунального хозяйства
            Российской Федерации от 4 сентября 2019 г. № 513/пр.
            </links>
        :ivar coefficient: <text xmlns="">Коэффициент учета условий
            производства работ, применяемый к стоимости и к расходу
            ресурса </text> <links xmlns="">Методические рекомендации по
            применению федеральных единичных расценок на строительные,
            специальные строительные, ремонтно-строительные, монтаж
            оборудования и пусконаладочные работы, утвержденные приказом
            Министерства строительства и жилищно-коммунального хозяйства
            Российской Федерации от 4 сентября 2019 г. № 519/пр.
            Методические рекомендации по определению сметных цен на
            эксплуатацию машин и механизмов, утвержденные приказом
            Министерства строительства и жилищно-коммунального хозяйства
            Российской Федерации от 4 сентября 2019 г. № 513/пр.
            </links>
        """

        final: Optional[TresCoefficient] = field(
            default=None,
            metadata={
                "name": "Final",
                "type": "Element",
                "required": True,
            },
        )
        coefficient: list[TresCoefficientDetail] = field(
            default_factory=list,
            metadata={
                "name": "Coefficient",
                "type": "Element",
                "min_occurs": 1,
            },
        )


@dataclass
class TsummaryDetails:
    """
    Комплексный тип для передачи итоговых показателей отдельных элементов сметной
    стоимости локального сметного расчета.

    :ivar total: <text xmlns=""> Всего сметная стоимость элемента ЛСР по
        разделу или по ЛСР в базисном уровне цен, по ЛСР в текущем
        уровне цен. </text> <formula xmlns=""> Для базисного уровня цен:
        Total.PriceBase (Всего сметная стоимость элемента ЛСР по разделу
        или по ЛСР в базисном уровне цен) = Price.PriceBase(Итоговая
        сметная стоимость элемента ЛСР в базисном уровне
        цен)+Transport.PriceBase (Сметная стоимость дополнительной
        перевозки элемента ЛСР в базисном уровне цен) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций. Для текущего уровня цен:
        Total.PriceCurrent (Всего сметная стоимость элемента ЛСР по ЛСР
        в текущем уровне цен) = Price.PriceCurrent (Итоговая сметная
        стоимость элемента ЛСР в текущем уровне цен)+Transport.PriceCur
        (Сметная стоимость дополнительной перевозки элемента ЛСР в
        текущем уровне цен) Округление до 2-х знаков. Округление
        производится один раз после всех математических операций.
        </formula> <links xmlns="">Методика определения сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр. </links>
    :ivar price: <text xmlns=""> Итоговая сметная стоимость элемента ЛСР
        по разделу или по ЛСР в базисном уровне цен, по ЛСР в текущем
        уровне цен, в том числе стоимость элемента, отсутствующего в
        ФРСН (без учета стоимости дополнительной перевозки) </text>
        <formula xmlns=""> Для базисного уровня цен: Price.PriceBase
        (Итоговая сметная стоимость элемента ЛСР по разделу или по ЛСР в
        базисном уровне цен) = Сумма элементов Item.Price.PriceBase
        (Сметная стоимость элемента ЛСР по расценке в базисном уровне
        цен) Округление до 2-х знаков. Округление производится один раз
        после всех математических операций. Для текущего уровня цен:
        Price.PriceCurrent (Итоговая сметная стоимость элемента ЛСР по
        ЛСР в текущем уровне цен) = Price.PriceBase (Итоговая сметная
        стоимость элемента ЛСР в базисном уровне цен)*PriceIndex (Индекс
        изменения сметной стоимости элемента ЛСР) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций. </formula> <links xmlns="">Методические
        рекомендации по определению сметных цен на материалы, изделия,
        конструкции, оборудование, утвержденные приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 4 сентября 2019 г. № 517/пр. </links>
    :ivar external: <text xmlns=""> Итоговая сметная стоимость элемента
        ЛСР, отсутствующего в ФРСН, по разделу или по локальному
        сметному расчету (смете). Определяется справочно, для указания в
        том числе в итого по разделу и в итого по смете. </text>
        <formula xmlns=""> Для базисного уровня цен: External.PriceВase
        (Сметная стоимость элемента ЛСР, отсутствующего в ФРСН, по
        разделу или по ЛСР в базисном уровне цен)= Сумма элементов
        Item.External.PriceBase (Сметная стоимость элемента ЛСР,
        отсутствующего в ФРСН, в базисном уровне цен) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций. Для текущего уровня цен:
        External.PriceCurrent (Сметная стоимость элемента ЛСР,
        отсутствующего в ФРСН, по разделу или по ЛСР в текущем уровне
        цен)= Сумма элементов Item.External.PriceCur (Сметная стоимость
        элемента ЛСР, отсутствующего в ФРСН, в текущем уровне цен)
        Округление до 2-х знаков. Округление производится один раз после
        всех математических операций. </formula> <links
        xmlns="">Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 августа 2020 г. № 421/пр. </links>
    :ivar transport: <text xmlns="">Итоговая сметная стоимость
        дополнительной перевозки элемента ЛСР по разделу или по
        локальному сметному расчету (смете). Определяется суммированием
        значений соответствующих позиций по перевозке элемента ЛСР.
        </text> <formula xmlns=""> Для базисного уровня цен:
        Transport.PriceBase(Сметная стоимость дополнительной перевозки
        элемента ЛСР по разделу или по ЛСР в базисном уровне цен)=Сумма
        элементов Item.PriceParameters.Totals.Base.Total (Стоимость
        дополнительной перевозки по позиции в базисном уровне цен)
        имеющих тип Item/Type ФССЦпг Округление до 2-х знаков.
        Округление производится один раз после всех математических
        операций Для текущего уровня цен: Transport.PriceCurrent(Сметная
        стоимость дополнительной перевозки элемента ЛСР по разделу или
        по ЛСР в текущем уровне цен) = Сумма элементов
        Item.PriceParameters.Totals.Prise.Total (Стоимость
        дополнительной перевозки по позиции в текущем уровне цен)
        имеющих тип Item/Type ФССЦпг. Округление до 2-х знаков.
        Округление производится один раз после всех математических
        операций. </formula> <links xmlns="">Методика определения
        сметной стоимости строительства, реконструкции, капитального
        ремонта, сноса объектов капитального строительства, работ по
        сохранению объектов культурного наследия (памятников истории и
        культуры) народов Российской Федерации на территории Российской
        Федерации, утвержденная приказом Министерства строительства и
        жилищно-коммунального хозяйства Российской Федерации от 4
        августа 2020 г. № 421/пр. Методические рекомендации по
        применению федеральных единичных расценок на строительные,
        специальные строительные, ремонтно-строительные, монтаж
        оборудования и пусконаладочные работы, утвержденные приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 сентября 2019 г. № 519/пр. </links>
    """

    class Meta:
        name = "TSummaryDetails"

    total: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "Total",
            "type": "Element",
        },
    )
    price: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
        },
    )
    external: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "External",
            "type": "Element",
        },
    )
    transport: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "Transport",
            "type": "Element",
        },
    )


@dataclass
class Tmachine(Tresource):
    """
    Комплексный тип для передачи данных машин и механизмов локального сметного
    расчета.

    :ivar machinist: Машинист, управляющий машиной
    :ivar machinist_salary: <text xmlns="">Оплата труда машинистов
        (рабочих, управляющих машинами), включенная в состав затрат на
        эксплуатацию строительных машин. Рассчитывается в составе
        стоимости маш.–ч машин. </text> <links xmlns="">Методические
        рекомендации по определению сметных цен на эксплуатацию машин и
        механизмов утвержденные приказом Министерства строительства и
        жилищно-коммунального хозяйства Российской Федерации от 4
        сентября 2019 г. № 513/пр. </links>
    """

    class Meta:
        name = "TMachine"

    machinist: Optional[Tmachinist] = field(
        default=None,
        metadata={
            "name": "Machinist",
            "type": "Element",
        },
    )
    machinist_salary: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MachinistSalary",
            "type": "Element",
        },
    )


@dataclass
class TsummaryItems:
    """
    Итоговые показатели сметной стоимости локального сметного расчета по элементам
    затрат заданного вида работ или общие по всем видам, за исключением
    оборудования и прочих затрат.

    :ivar total: <text xmlns="">Итоговая сметная стоимость по разделу
        или по ЛСР в базисном уровне цен, по ЛСР в текущем уровне цен.
        Включает: стоимость элементов прямых затрат, накладные расходы,
        сметная прибыль, затраты на перевозку </text> <formula xmlns="">
        Для базисного уровня цен (при применении "индексов к элементам
        ПЗ" и "индекса к СМР"): Total.PriceBase(Итоговая сметная
        стоимость вида работ по разделу или по ЛСР в базисном уровне
        цен) = WorkersSalary.PriceBase(Итоговая оплата труда по разделу
        или по ЛСР в базисном уровне цен )+
        MachinesTotal.PriceBase(Всего стоимость эксплуатации машин и
        механизмов по разделу или по ЛСР в базисном уровне
        цен)+Materials.PriceBase(Итоговая стоимость материалов по
        разделу или по ЛСР в базисном уровне цен)+
        Overhead.PriceBase(Итоговые накладные расходы по разделу или по
        ЛСР в базисном уровне цен)+ Profit.PriceBase(Итоговая сметная
        прибыль по разделу или по ЛСР в базисном уровне
        цен)+Transport.PriceBase(Сметная стоимость перевозки грузов по
        разделу или по ЛСР в базисном уровне цен)+
        TransportAdd.PriceBase(Сметная стоимость дополнительной
        перевозки грузов по разделу или по ЛСР в базисном уровне цен)
        Округление до 2-х знаков. Округление производится один раз после
        всех математических операций. Для текущего уровня цен (при
        применении "индексов к элементам ПЗ»): Total.PriceCur(Итоговая
        сметная стоимость по ЛСР в текущем уровне цен) =
        WorkersSalary.PriceCur(Итоговая оплата труда по ЛСР в текущем
        уровне цен)+ MachinesTotal.PriceCur(Всего стоимость эксплуатации
        машин и механизмов по ЛСР в текущем уровне
        цен)+Materials.PriceCur(Итоговая стоимость материалов по ЛСР в
        текущем уровне цен)+ Overhead.PriceCur(Итоговые накладные
        расходы по ЛСР в текущем уровне цен)+ Profit.PriceCur(Итоговая
        сметная прибыль по ЛСР в текущем уровне
        цен)+Transport.PriceCur(Сметная стоимость перевозки грузов по
        ЛСР в текущем уровне цен)+ TransportAdd.PriceCur(Сметная
        стоимость дополнительной перевозки грузов по ЛСР в текущем
        уровне цен) Округление до 2-х знаков. Округление производится
        один раз после всех математических операций. Для текущего уровня
        цен (при применении "индекса к СМР»): Total.PriceCur(Итоговая
        сметная стоимость вида работ по ЛСР в текущем уровне цен) =
        PriceIndex(Индекс изменения сметной стоимости СМР или
        ПНР)*(WorkersSalary.PriceBase(Итоговая оплата труда по ЛСР в
        базисном уровне цен)+Machines.PriceBase(Итоговая стоимость
        эксплуатации машин и механизмов по ЛСР в базисном уровне
        цен)+MachinesTotal.PriceBase(Всего стоимость материалов по ЛСР в
        базисном уровне цен)+ Overhead.PriceBase(Итоговые накладные
        расходы по ЛСР в базисном уровне цен)+ Profit.PriceBase(Итоговая
        сметная прибыль по ЛСР в базисном уровне
        цен))+Transport.PriceCur(Сметная стоимость перевозки грузов по
        ЛСР в текущем уровне цен)+ TransportAdd.PriceCur(Сметная
        стоимость дополнительной перевозки грузов по ЛСР в текущем
        уровне цен) Округление до 2-х знаков. Округление производится
        один раз после всех математических операций. </formula> <links
        xmlns="">Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 04 августа 2020 г. № 421/пр. </links>
    :ivar workers_salary: <text xmlns="">Итоговая оплата труда рабочих и
        работников-исполнителей составе заданного вида работ по разделу
        или по ЛСР в базисном уровне цен, по ЛСР в текущем уровне цен.
        </text> <formula xmlns=""> Для базисного уровня цен (при
        применении "индексов к элементам ПЗ» и «индекса к СМР"):
        WorkersSalary.PriceBase (Итоговая оплата труда по разделу или по
        ЛСР в базисном уровне цен) =Сумма элементов
        Item.PriceParametersBase.WorkersSalary (Оплата труда по расценке
        в базисном уровне цен) Округление до 2-х знаков. Округление
        производится один раз после всех математических операций. Для
        текущего уровня цен (при применении "индексов к элементам ПЗ"):
        WorkersSalary.PriceCurrent (Итоговая оплата труда по ЛСР в
        текущем уровне цен) = Сумма элементов
        Item.PriceParametersPrice.WorkersSalary (Оплата труда по
        расценке в текущем уровне цен) Округление до 2-х знаков.
        Округление производится один раз после всех математических
        операций. </formula> <links xmlns="">Методика определения
        сметной стоимости строительства, реконструкции, капитального
        ремонта, сноса объектов капитального строительства, работ по
        сохранению объектов культурного наследия (памятников истории и
        культуры) народов Российской Федерации на территории Российской
        Федерации, утвержденная приказом Министерства строительства и
        жилищно-коммунального хозяйства Российской Федерации от 4
        августа 2020 г. № 421/пр. Методические рекомендации по
        определению сметных цен на затраты труда в строительстве,
        утвержденные приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 сентября 2019
        г. № 515/пр. </links>
    :ivar machinist_salary: <text xmlns="">Итоговая оплата труда
        машинистов (рабочих, занятых управлением и обслуживанием
        строительных машин и механизмов) заданного вида работ по разделу
        или по ЛСР в базисном уровне цен, по ЛСР в текущем уровне цен.
        Заработная плата машинистов включается в состав затрат на
        эксплуатацию строительных машин и механизмов и рассчитывается в
        составе стоимости машино–часа машин и механизмов по сборнику
        сметных тарифных ставок </text> <formula xmlns=""> Для базисного
        уровня цен (при применении "индексов к элементам ПЗ" и "индекса
        к СМР"): MachinistSalary.PriceBase(Итоговая оплата труда
        машинистов по разделу или по ЛСР в базисном уровне цен)= Сумма
        элементов Item.PriceParametersBase.MachinistSalary (Оплата труда
        машинистов по расценке в базисном уровне цен) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций. Для текущего уровня цен (при применении
        "индексов к элементам ПЗ"):
        MachinistSalary.PriceCurrent(Итоговая оплата труда машинистов по
        ЛСР в текущем уровне цен)= Сумма элементов
        Item.PriceParametersPrice.MachinistSalary (Оплата труда
        машинистов по расценке в текущем уровне цен) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций. </formula> <links xmlns="">Методика
        определения сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        работ по сохранению объектов культурного наследия (памятников
        истории и культуры) народов Российской Федерации на территории
        Российской Федерации, утвержденная приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 4 августа 2020 г. № 421/пр. Методические
        рекомендации по определению сметных цен на затраты труда в
        строительстве, утвержденные приказом Министерства строительства
        и жилищно-коммунального хозяйства Российской Федерации от 4
        сентября 2019 г. № 515/пр. </links>
    :ivar machinist_salary_extra: <text xmlns="">Итоговая Доплата к
        оплате труда машинистов по разделу или по ЛСР в базисном уровне
        цен, по ЛСР в текущем уровне цен. Прибавляется к итоговым
        затратам на эксплуатацию строительных машин и механизмов </text>
        <formula xmlns=""> Для базисного уровня цен (при применении
        "индексов к элементам ПЗ" и "индекса к СМР"):
        MachinistSalaryExtra.PriceBase(Итоговая Доплата к оплате труда
        машинистов по разделу или по ЛСР в базисном уровне цен)= Сумма
        элементов Item.Resources.Machine.PriceTotalBase (Доплата к
        оплате труда машинистов по расценке в базисном уровне цен)
        Округление до 2-х знаков. Округление производится один раз после
        всех математических операций. Для текущего уровня цен (при
        применении "индексов к элементам ПЗ"):
        MachinistSalaryExtra.PriceCurrent(Итоговая Доплата к оплате
        труда труда машинистов по ЛСР в текущем уровне цен)= Сумма
        элементов Item.Resources.Machine.PriceTotalCur (Доплата к оплате
        труда машинистов по расценке в текущем уровне цен) Округление до
        2-х знаков. Округление производится один раз после всех
        математических операций. </formula> <links xmlns="">Методика
        определения сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        работ по сохранению объектов культурного наследия (памятников
        истории и культуры) народов Российской Федерации на территории
        Российской Федерации, утвержденная приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 4 августа 2020 г. № 421/пр. Методические
        рекомендации по определению сметных цен на затраты труда в
        строительстве, утвержденные приказом Министерства строительства
        и жилищно-коммунального хозяйства Российской Федерации от 4
        сентября 2019 г. № 515/пр. </links>
    :ivar salary: <text xmlns=""> Фонд оплаты труда (ФОТ) по разделу или
        по локальному сметному расчету (смете) заданного вида работ -
        размер средств на оплату труда рабочих-строителей, машинистов и
        пусконаладочного персонала. Рассчитывается как сумма итоговых
        значений размера средств на оплату труда по позициям ЛСР по
        разделу или по ЛСР в базисном уровне цен, по ЛСР в текущем
        уровне цен. ФОТ является справочной дополнительной информацией в
        составе сметной стоимости. Итоговый ФОТ определяется в
        зависимости от вида индексов изменения сметной стоимости. При
        применении "индекса СМР" суммируется по позициям ЛСР в базисном
        уровне цен. При применении "индексов к элементам прямых затрат"
        суммируется по позициям ЛСР в базисном и текущем уровнях цен.
        Итоговый ФОТ по разделу определяется суммированием итоговых
        значений размера средств на оплату труда по позициям раздела.
        </text> <formula xmlns=""> Для базисного уровня цен при
        применении "индекса к СМР" и "индексов к элементам прямых
        затрат": Salary.PriceBase (ФОТ по разделу или по ЛСР в базисном
        уровне) = WorkersSalary.PriceBase (Оплата труда по разделу или
        по ЛСР в базисном уровне цен)+ MachinistSalary.PriceBase (Оплата
        труда машинистов по разделу или по ЛСР в базисном уровне цен)
        Округление до 2-х знаков. Округление производится один раз после
        всех математических операций. Для текущего уровня цен при
        применении "индексов к элементам прямых затрат":
        Salary.PriceCurrent (ФОТ по ЛСР в текущем уровне) =
        WorkersSalary.PriceCurrent (Оплата труда по ЛСР в текущем уровне
        цен)+ MachinistSalary.PriceCurrent (Оплата труда машинистов по
        ЛСР в текущем уровне цен) Округление до 2-х знаков. Округление
        производится один раз после всех математических операций.
        </formula> <links xmlns="">Методика определения сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр. </links>
    :ivar overhead: <text xmlns=""> Итоговые накладные расходы по
        разделу или по локальному сметному расчету (смете) в составе
        сметной стоимости, полученные в результате применения нормативов
        накладных расходов в процентах, привязанных по видам работ
        единичных расценок, от размера средств на оплату труда (фонда
        оплаты труда, учитываемого в составе сметных прямых затрат)
        рабочих-строителей, машинистов и пусконаладочного персонала ппо
        разделу или по ЛСР в базисном уровне цен, по ЛСР в текущем
        уровне цен. Итоговые накладные расходы определяются в
        зависимости от вида индексов изменения сметной стоимости. При
        применении "индекса СМР" суммируются по позициям ЛСР в базисном
        уровне цен для включения в состав итоговой стоимости по
        элементам строительства в базисном уровне цен. При применении
        "индексов к элементам прямых затрат" суммируются по позициям ЛСР
        в базисном и текущем уровнях цен для определения итоговой
        стоимости ЛСР в базисном и текущем уровнях цен. Итоговые
        накладные расходы по разделу определяются суммированием итоговых
        значений по позициям раздела и являются справочной информацией.
        </text> <formula xmlns=""> Для базисного уровня цен при
        применении "индекса СМР" и "индексов к элементам ПЗ":
        Overhead.PriceBase (Итоговые накладные расходы по разделу или по
        ЛСР в базисном уровне цен) = Сумма элементов
        Item.OverheadsBase.OverheadBase.Price.Base (Накладные расходы по
        позиции в базисном уровне цен) Округление до 2-х знаков.
        Округление производится один раз после всех математических
        операций. Для текущего уровня цен при применении "индексов к
        элементам ПЗ": Overhead.PriceCurrent (Итоговые накладные расходы
        по ЛСР в текущем уровне цен) = Сумма элементов
        Item.OverheadsBase.OverheadBase.Price.Price (Накладные расходы
        по позиции в текущем уровне цен) Округление до 2-х знаков.
        Округление производится один раз после всех математических
        операций </formula> <links xmlns=""> Методика по разработке и
        применению нормативов накладных расходов при определении сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 21.12.2020 № 812/пр (с учетом изменений
        от 02.09.2021 № 636/пр). </links>
    :ivar profit: <text xmlns=""> Итоговая сметная прибыль по разделу
        или по локальному сметному расчету (смете) в составе сметной
        стоимости, полученная в результате применения нормативов сметной
        прибыли в процентах, привязанных по видам работ единичных
        расценок, от размера средств на оплату труда (фонда оплаты
        труда, учитываемого в составе сметных прямых затрат) рабочих-
        строителей, машинистов и пусконаладочного персонала по разделу
        или по ЛСР в базисном уровне цен, по ЛСР в текущем уровне цен.
        Итоговая сметная прибыль определяется в зависимости от вида
        индексов изменения сметной стоимости. При применении "индекса
        СМР" суммируется по позициям ЛСР в базисном уровне цен для
        включения в состав итоговой стоимости по элементам строительства
        в базисном уровне цен. При применении "индексов к элементам
        прямых затрат" суммируется по позициям ЛСР в базисном и текущем
        уровнях цен для определения итоговой стоимости ЛСР в базисном и
        текущем уровнях цен. Итоговая сметная прибыль по разделу
        определяется суммированием итоговых значений по позициям раздела
        и является справочной информацией. </text> <formula xmlns="">
        Для базисного уровня цен при применении "индекса СМР" и
        "индексов к элементам ПЗ": Profit.PriceBase(Итоговая сметная
        прибыль по разделу или по ЛСР в базисном уровне цен)=Сумма
        элементов Item.ProfitsBase.ProfitBase.Price.Base (Сметная
        прибыль по позиции в базисном уровне цен) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций Для текущего уровня цен при применении
        "индексов к элементам ПЗ": Profit.PriceCurrent (Итоговая сметная
        прибыль по ЛСР в текущем уровне цен)= Сумма элементов
        Item.ProfitsBase.ProfitBase.Price.Price (Сметная прибыль по
        позиции в текущем уровне цен) Округление до 2-х знаков.
        Округление производится один раз после всех математических
        операций </formula> <links xmlns=""> Методика по разработке и
        применению нормативов сметной прибыли при определении сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, утвержденная приказом
        Минстроя России от 11.12.2020 №774/пр (с учетом изменений от
        22.04.2022 № 317/пр) </links>
    :ivar machines_total: <text xmlns=""> Всего сметная стоимость
        эксплуатации машин и механизмов (с учетом доплат к оплате труда
        машинистов) по разделу или по ЛСР в базисном уровне цен, по ЛСР
        в текущем уровне цен. Сметные цены на эксплуатацию машин и
        механизмов отражают общие суммарные затраты на их эксплуатацию и
        оплату труда машинистов (механизаторов). </text> <formula
        xmlns=""> Для базисного уровня цен (при применении "индексов к
        элементам ПЗ" и "индекса к СМР"): MachinesTotal.PriceBase (Всего
        сметная стоимость эксплуатации строительных машин и механизмов
        по разделу или по ЛСР в базисном уровне цен)= Machines.PriceBase
        (Итогова сметная стоимость эксплуатации строительных машин и
        механизмов по разделу или по ЛСР в базисном уровне цен без учета
        доплат к оплате труда машинистов)+
        MachinistSalaryExtra.PriceBase(Итоговая Доплата к оплате труда
        машинистов по разделу или по ЛСР в базисном уровне цен)
        Округление до 2-х знаков. Округление производится один раз после
        всех математических операций. Для текущего уровня цен (при
        применении "индексов к элементам ПЗ"): MachinesTotal.PriceCur
        (Всего сметная стоимость эксплуатации строительных машин и
        механизмов по разделу или по ЛСР в текущем уровне цен)=
        Machines.PriceCur (Итогова сметная стоимость эксплуатации
        строительных машин и механизмов по разделу или по ЛСР в текущем
        уровне цен без учета доплат к оплате труда машинистов)+
        MachinistSalaryExtra.PriceCur(Итоговая Доплата к оплате труда
        машинистов по разделу или по ЛСР в текущем уровне цен)
        Округление до 2-х знаков. Округление производится один раз после
        всех математических операций. </formula> <links
        xmlns="">Методические рекомендации по определению сметных цен на
        эксплуатацию машин и механизмов утвержденные приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 сентября 2019 г. № 513/пр. </links>
    :ivar machines: <text xmlns=""> Итоговая сметная стоимость
        эксплуатации строительных машин без учета доплат к оплате труда
        машинистов, автотранспортных средств, механизированных
        инструментов и механизмов по разделу или по ЛСР в базисном
        уровне цен, по ЛСР в текущем уровне цен. Сметные цены на
        эксплуатацию машин и механизмов отражают общие суммарные затраты
        на их эксплуатацию и оплату труда машинистов (механизаторов).
        </text> <formula xmlns=""> Для базисного уровня цен (при
        применении "индексов к элементам ПЗ" и "индекса к СМР"):
        Machines.PriceBase (Итоговая сметная стоимость эксплуатации
        строительных машин и механизмов по разделу или по ЛСР в базисном
        уровне цен)= Сумма элементов Item.PriceParametersBase.Machines
        (Стоимость эксплуатации строительных машин и механизмов по
        расценке в базисном уровне цен) Округление до 2-х знаков.
        Округление производится один раз после всех математических
        операций. Для текущего уровня цен (при применении "индексов к
        элементам ПЗ"): Machines.PriceCurrent (Итоговая сметная
        стоимость эксплуатации строительных машин и механизмов по ЛСР в
        текущем уровне цен) = Machines.PriceBase (Стоимость эксплуатации
        строительных машин и механизмов по ЛСР в базисном уровне
        цен)*PriceIndex(Индекс изменения сметной стоимости к
        эскплуатации машин ЭМ) Округление до 2-х знаков. Округление
        производится один раз после всех математических операций.
        </formula> <links xmlns="">Методические рекомендации по
        определению сметных цен на эксплуатацию машин и механизмов
        утвержденные приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 сентября 2019
        г. № 513/пр. </links>
    :ivar materials: <text xmlns=""> Итоговая сметная стоимость
        материалов, изделий и конструкции по разделу или по ЛСР в
        базисном уровне цен, по ЛСР в текущем уровне цен, в том числе
        стоимость материалов, отсутствующих в ФРСН. </text> <formula
        xmlns=""> Для базисного уровня цен (при применении "индекса к
        СМР" и "индексов к элементам ПЗ"): Materials.PriceBase (Итоговая
        сметная стоимость материалов по разделу или по ЛСР в базисном
        уровне цен) = Сумма элементов Item.PriceParametersBase.Materials
        (Cметная стоимость материалов, изделия и конструкции по расценке
        в базисном уровне цен) Округление до 2-х знаков. Округление
        производится один раз после всех математических операций. Для
        текущего уровня цен (при применении "индексов к элементам ПЗ"):
        Materials.PriceCurrent(Итоговая сметная стоимость материалов по
        ЛСР в текущем уровне цен)= Materials.PriceBase (Стоимость
        материалов по ЛСР в базисном уровне цен)* PriceIndex (Индекс
        изменения сметной стоимости материалов МР) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций. </formula> <links xmlns="">Методические
        рекомендации по определению сметных цен на материалы, изделия,
        конструкции, оборудование, утвержденные приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 4 сентября 2019 г. № 517/пр. </links>
    :ivar direct: <text xmlns="">Итоговые прямые затраты по разделу или
        по ЛСР в базисном уровне цен, по ЛСР в текущем уровне цен.
        </text> <formula xmlns=""> В базисном уровне цен (при применении
        "индексов к элементам ПЗ" и "индекса к СМР"): Direct.PriceBase
        (Итоговые прямые затраты по разделу или по локальному сметному
        расчету в базисном уровне цен) = WorkersSalary.PriceBase(Итогова
        оплата труда по разделу или по ЛСР в базисном уровне
        цен)+Machines.PriceBase(Итоговая стоимость эксплуатации машин и
        механизмов по разделу или по ЛСР в базисном уровне
        цен)+Materials.PriceBase(Итоговая стоимость материалов по
        разделу или по ЛСР в базисном уровне
        цен)+Transport.PriceBase(Сметная стоимость перевозки грузов по
        разделу или по ЛСР в базисном уровне цен)+
        TransportAdd.PriceBase(Сметная стоимость дополнительной
        перевозки грузов по разделу или по ЛСР в базисном уровне цен) В
        текущем уровне цен (при применении "индексов к элементам ПЗ"):
        Direct.PriceСurrent (Итоговые прямые затраты по локальному
        сметному расчету в текущем уровне цен) =
        WorkersSalary.PriceCur(Итоговая оплата труда по ЛСР в текущем
        уровне цен)+Machines.PriceCur(Итоговая стоимость эксплуатации
        машин и механизмов по ЛСР в текущем уровне
        цен)+Materials.PriceCur(Итоговая стоимость материалов по ЛСР в
        текущем уровне цен)+ Transport.PriceCur(Сметная стоимость
        перевозки грузов по ЛСР в текущем уровне цен)+
        TransportAdd.PriceCur(Сметная стоимость дополнительной перевозки
        грузов по ЛСР в текущем уровне цен) Округление до 2-х знаков.
        Округление производится один раз после всех математических
        операций. </formula> <links xmlns="">Методика определения
        сметной стоимости строительства, реконструкции, капитального
        ремонта, сноса объектов капитального строительства, работ по
        сохранению объектов культурного наследия (памятников истории и
        культуры) народов Российской Федерации на территории Российской
        Федерации, утвержденная приказом Министерства строительства и
        жилищно-коммунального хозяйства Российской Федерации от 4
        августа 2020 г. № 421/пр. </links>
    :ivar total_labor_costs: <text xmlns="">Итоговые затраты труда по
        локальному сметному расчету (смете) для заданного вида работ
        </text> <formula xmlns=""> TotalLaborCosts (Итоговые затраты
        труда) = LaborCosts (Итоговые затраты труда рабочих или
        пусконаладочного персонала) + MachinistLaborCosts (Итоговые
        затраты труда машинистов) Округление до 7-ми знаков. Округление
        производится один раз после всех математических операций.
        </formula> <links xmlns="">Методические рекомендации по
        определению сметных цен на затраты труда в строительстве,
        утвержденные приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 сентября 2019
        г. № 515/пр. </links>
    :ivar labor_costs: <text xmlns="">Итоговые затраты труда рабочих по
        локальному сметному расчету (смете) и работников-исполнителей
        пусконаладочных работ не занятых обслуживанием машин заданного
        вида работ </text> <formula xmlns=""> LaborCosts (Итоговые
        затраты труда рабочих или пусконаладочного персонала по ЛСР) =
        Сумма LaborCosts (Итоговые затраты труда по ЛСР) Округление до
        7-ми знаков. Округление производится один раз после всех
        математических операций. </formula> <links xmlns="">Методические
        рекомендации по определению сметных цен на затраты труда в
        строительстве, утвержденные приказом Министерства строительства
        и жилищно-коммунального хозяйства Российской Федерации от 4
        сентября 2019 г. № 515/пр. </links>
    :ivar machinist_labor_costs: <text xmlns="">Итоговые затраты труда
        машинистов (рабочих, управляющих машинами) по локальному
        сметному расчету (смете) заданного вида работ </text> <formula
        xmlns=""> MachinistLaborCosts (Итоговые затраты труда машинистов
        по ЛСР) = Сумма MachinistLaborCosts (Итоговые затраты труда
        машинистов по ЛСР) Округление до 7-ми знаков. Округление
        производится один раз после всех математических операций.
        </formula> <links xmlns="">Методические рекомендации по
        определению сметных цен на затраты труда в строительстве,
        утвержденные приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 сентября 2019
        г. № 515/пр. </links>
    :ivar transport_total: <text xmlns=""> Всего сметная стоимость
        перевозки по разделу или по локальному сметному расчету (смете).
        Определяется суммированием значений стоимости перевозки грузов
        (грунт, мусор и подобное) и дополнительной перевозки, согласно
        пункта 63 Методики №421/пр </text> <formula xmlns=""> Для
        базисного уровня цен: TransporTotal.PriceBase(Всего cметная
        стоимость перевозки по разделу или по ЛСР в базисном уровне
        цен)= Transport.PriceBase(Итоговая сметная стоимость перевозки
        грузов по разделу или по ЛСР в базисном уровне
        цен)+TransportAdd.PriceBase(Итоговая сметная стоимость
        дополнительной перевозки грузов по разделу или по ЛСР в базисном
        уровне цен) Округление до 2-х знаков. Округление производится
        один раз после всех математических операций Для текущего уровня
        цен: TransportTotal.PriceCurrent(Всего сметная стоимость
        перевозки по разделу или по ЛСР в текущем уровне цен) =
        Transport.PriceCurrent(Итоговая сметная стоимость перевозки
        грузов по разделу или по ЛСР в текущем уровне
        цен)+TransportAdd.PriceCurrent(Итоговая сметная стоимость
        дополнительной перевозки грузов по разделу или по ЛСР в текущем
        уровне цен) Округление до 2-х знаков. Округление производится
        один раз после всех математических операций. </formula> <links
        xmlns=""> Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 августа 2020 г. № 421/пр. Методические
        рекомендации по применению федеральных единичных расценок на
        строительные, специальные строительные, ремонтно-строительные,
        монтаж оборудования и пусконаладочные работы, утвержденные
        приказом Министерства строительства и жилищно-коммунального
        хозяйства Российской Федерации от 4 сентября 2019 г. № 519/пр.
        </links>
    :ivar transport_add: <text xmlns=""> Дополнительная сметная
        стоимость дополнительной перевозки грузов по разделу или по
        локальному сметному расчету (смете). </text> <formula xmlns="">
        Для базисного уровня цен: TransportAdd.PriceBase(Итоговая
        сметная стоимость дополнительной перевозки грузов по разделу или
        по ЛСР в базисном уровне цен)=Сумма элементов
        Item.PriceParameters.Totals.Base.Total (Итоговая стоимость
        дополнительной перевозки по расценке в базисном уровне цен)
        имеющих тип Item/Type ФССЦпг Округление до 2-х знаков.
        Округление производится один раз после всех математических
        операций Для текущего уровня цен:
        Transport.PriceCurrent(Итоговая сметная стоимость дополнительной
        перевозки грузов по разделу или по ЛСР в текущем уровне цен) =
        Сумма элементов Item.PriceParameters.Totals.Prise.Total
        (Итоговая стоимость дополнительной перевозки по расценке в
        текущем уровне цен) имеющих тип Item/Type ФССЦпг Округление до
        2-х знаков. Округление производится один раз после всех
        математических операций. </formula> <links xmlns=""> Методика
        определения сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        работ по сохранению объектов культурного наследия (памятников
        истории и культуры) народов Российской Федерации на территории
        Российской Федерации, утвержденная приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 4 августа 2020 г. № 421/пр. Методические
        рекомендации по применению федеральных единичных расценок на
        строительные, специальные строительные, ремонтно-строительные,
        монтаж оборудования и пусконаладочные работы, утвержденные
        приказом Министерства строительства и жилищно-коммунального
        хозяйства Российской Федерации от 4 сентября 2019 г. № 519/пр.
        </links>
    :ivar transport: <text xmlns=""> Cметная стоимость перевозки по
        разделу или по локальному сметному расчету (смете). Определяется
        суммированием значений соответствующих позиций по перевозке
        грузов (грунт, мусор и подобное), за исключением указанных в
        пункте 63 Методики №421/пр по стротельным и монтажным работам.
        </text> <formula xmlns=""> Для базисного уровня цен:
        Transport.PriceBase(Итоговая сметная стоимость перевозки грузов
        по разделу или по ЛСР в базисном уровне цен)=Сумма элементов
        Item.PriceParameters.Totals.Base.Total (Итоговая стоимость по
        расценке в базисном уровне цен) имеющих тип Item/Type ФССЦпг
        Округление до 2-х знаков. Округление производится один раз после
        всех математических операций Для текущего уровня цен:
        Transport.PriceCurrent(Итоговая сметная стоимость перевозки
        грузов по разделу или по ЛСР в текущем уровне цен) = Сумма
        элементов Item.PriceParameters.Totals.Prise.Total (Итоговая
        стоимость по расценке в текущем уровне цен) имеющих тип
        Item/Type ФССЦпг Округление до 2-х знаков. Округление
        производится один раз после всех математических операций.
        </formula> <links xmlns=""> Методика определения сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр. Методические рекомендации по применению федеральных
        единичных расценок на строительные, специальные строительные,
        ремонтно-строительные, монтаж оборудования и пусконаладочные
        работы, утвержденные приказом Министерства строительства и
        жилищно-коммунального хозяйства Российской Федерации от 4
        сентября 2019 г. № 519/пр. </links>
    :ivar price: <text xmlns="">Итоговая сметная стоимость по разделу
        или по ЛСР в базисном уровне цен, по ЛСР в текущем уровне цен.
        Включает: стоимость элементов прямых затрат, накладные расходы,
        сметная прибыль. Затраты на перевозку (грунт, мусор),
        дополнительная перевозка не учитываются при индексации СМР.
        Затраты на перевозку (грунт, мусор) не учитывается при
        индексации по элементам ПЗ, дополнительная перевозка учитывается
        при индексации по элементам ПЗ </text> <formula xmlns=""> Для
        базисного уровня цен (при применении «индекса к СМР"):
        Total.PriceBase(Итоговая сметная стоимость вида работ по разделу
        или по ЛСР в базисном уровне цен) =
        WorkersSalary.PriceBase(Итоговая оплата труда по разделу или по
        ЛСР в базисном уровне цен )+ MachinesTotal.PriceBase(Всего
        стоимость эксплуатации машин и механизмов по разделу или по ЛСР
        в базисном уровне цен)+Materials.PriceBase(Итоговая стоимость
        материалов по разделу или по ЛСР в базисном уровне цен)+
        Overhead.PriceBase(Итоговые накладные расходы по разделу или по
        ЛСР в базисном уровне цен)+ Profit.PriceBase(Итоговая сметная
        прибыль по разделу или по ЛСР в базисном уровне цен) Округление
        до 2-х знаков. Округление производится один раз после всех
        математических операций. Для базисного уровня цен (при
        применении "индексов к элементам ПЗ»): Total.PriceBase(Итоговая
        сметная стоимость вида работ по ЛСР в базисном уровне цен) =
        WorkersSalary.PriceBase(Итоговая оплата труда по ЛСР в базисном
        уровне цен )+MachinesTotal.PriceBase(Всего стоимость
        эксплуатации машин и механизмов по ЛСР в базисном уровне
        цен)+Materials.PriceBase(Итоговая стоимость материалов по ЛСР в
        базисном уровне цен)+ Overhead.PriceBase(Итоговые накладные
        расходы по ЛСР в базисном уровне цен)+ Profit.PriceBase(Итоговая
        сметная прибыль по ЛСР в базисном уровне
        цен)+TransportAdd.PriceBase(Сметная стоимость дополнительной
        перевозки грузов по ЛСР в базисном уровне цен) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций. Для текущего уровня цен (при применении
        "индекса к СМР»): Total.PriceCur(Итоговая сметная стоимость вида
        работ по ЛСР в текущем уровне цен) = PriceIndex(Индекс изменения
        сметной стоимости СМР или ПНР)*(WorkersSalary.PriceBase(Итоговая
        оплата труда по ЛСР в базисном уровне
        цен)+MachinesTotal.PriceBase(Всего стоимость эксплуатации машин
        и механизмов по ЛСР в базисном уровне
        цен)+Materials.PriceBase(Итоговая стоимость материалов по ЛСР в
        базисном уровне цен)+ Overhead.PriceBase(Итоговые накладные
        расходы по ЛСР в базисном уровне цен)+ Profit.PriceBase(Итоговая
        сметная прибыль по ЛСР в базисном уровне цен)) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций. Для текущего уровня цен (при применении
        "индексов к элементам ПЗ»): Total.PriceCur(Итоговая сметная
        стоимость по ЛСР в текущем уровне цен) =
        WorkersSalary.PriceCur(Итоговая оплата труда по ЛСР в текущем
        уровне цен)+MachinesTotal.PriceCur(Всего стоимость эксплуатации
        машин и механизмов по ЛСР в текущем уровне
        цен)+Materials.PriceCur(Итоговая стоимость материалов по ЛСР в
        текущем уровне цен)+ Overhead.PriceCur(Итоговые накладные
        расходы по ЛСР в текущем уровне цен)+ Profit.PriceCur(Итоговая
        сметная прибыль по ЛСР в текущем уровне
        цен)+TransportAdd.PriceCur(Сметная стоимость дополнительной
        перевозки грузов по ЛСР в текущем уровне цен) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций. </formula> <links xmlns="">Методика
        определения сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        работ по сохранению объектов культурного наследия (памятников
        истории и культуры) народов Российской Федерации на территории
        Российской Федерации, утвержденная приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 04 августа 2020 г. № 421/пр. </links>
    """

    class Meta:
        name = "TSummaryItems"

    total: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "Total",
            "type": "Element",
            "required": True,
        },
    )
    workers_salary: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "WorkersSalary",
            "type": "Element",
        },
    )
    machinist_salary: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "MachinistSalary",
            "type": "Element",
        },
    )
    machinist_salary_extra: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "MachinistSalaryExtra",
            "type": "Element",
        },
    )
    salary: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "Salary",
            "type": "Element",
        },
    )
    overhead: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "Overhead",
            "type": "Element",
        },
    )
    profit: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "Profit",
            "type": "Element",
        },
    )
    machines_total: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "MachinesTotal",
            "type": "Element",
        },
    )
    machines: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "Machines",
            "type": "Element",
        },
    )
    materials: Optional[TsummaryDetails] = field(
        default=None,
        metadata={
            "name": "Materials",
            "type": "Element",
        },
    )
    direct: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "Direct",
            "type": "Element",
        },
    )
    total_labor_costs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TotalLaborCosts",
            "type": "Element",
        },
    )
    labor_costs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LaborCosts",
            "type": "Element",
        },
    )
    machinist_labor_costs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MachinistLaborCosts",
            "type": "Element",
        },
    )
    transport_total: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "TransportTotal",
            "type": "Element",
        },
    )
    transport_add: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "TransportAdd",
            "type": "Element",
        },
    )
    transport: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "Transport",
            "type": "Element",
        },
    )
    price: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Titem:
    """
    Комплексный тип позиции локального сметного расчета.

    :ivar summary_type: Графа объектной сметы
    :ivar work_type: Вид работ позиции в соответствии с технологической
        структурой капитальных вложений: стоимость строительных
        (ремонтно-строительных) работ; стоимость работ по монтажу
        оборудования (монтажных работ); затраты на приобретение
        (изготовление) оборудования, мебели и инвентаря; прочие затраты;
        перевозка.
    :ivar is_return_mat: <text xmlns="">Признак возвратных сумм.</text>
        <links xmlns="">Методика определения сметной стоимости
        строительства, реконструкции, капитального ремонта, сноса
        объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр. </links>
    :ivar overheads: Накладные расходы позиции в локальном сметном
        расчете (базисный и текущий уровень цен)
    :ivar profits: Сметная прибыль позиции в локальном сметном расчете
        (базисный и текущий уровень цен)
    :ivar cost: Единичная расценка локального сметного расчета
    :ivar resources: Ресурсы вне единичной расценки (неучтенные), нормы.
        Предназначены для учета ресурсов по проекту согласно
        технического задания (проекта). Данные ресурсы содержат точный
        код (обоснование), наименование с полным указанием
        характеристик, единицу измерения, количество, сметную стоимость
        за единицу измерения и итоговую сметную стоимость
    :ivar material: <text xmlns="">Материальный ресурс в соответствии с
        Классификатором строительных ресурсов или сметными ценами на
        материалы, изделия, конструкции и оборудование, применяемые в
        строительстве, сведения о которых включены в федеральный реестр
        сметных нормативов или материальный ресурс, сметная стоимость
        которого определена с учетом положений пунктов 13–18 Методики №
        421/пр. </text> <links xmlns="">Методические рекомендации по
        определению сметных цен на материалы, изделия, конструкции,
        оборудование и цен услуг на перевозку грузов для строительства,
        утвержденные приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 сентября 2019
        г. № 517/пр. </links>
    :ivar machine: <text xmlns="">Ресурс (машины и механизмы) в
        соответствии с Классификатором строительных ресурсов,
        сформированным приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации. </text> <links
        xmlns="">Методические рекомендации по определению сметных цен на
        материалы, изделия, конструкции, оборудование и цен услуг на
        перевозку грузов для строительства, утвержденные приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 сентября 2019 г. № 517/пр. </links>
    :ivar equipment: <text xmlns="">Оборудование в соответствии с
        Классификатором строительных ресурсов или сметными ценами на
        материалы, изделия, конструкции и оборудование, применяемые в
        строительстве, сведения о которых включены в федеральный реестр
        сметных нормативов или оборудование, сметная стоимость которого
        определена с учетом положений пунктов 13–18 Методики № 421/пр.
        </text> <links xmlns="">Методические рекомендации по определению
        сметных цен на материалы, изделия, конструкции, оборудование и
        цен услуг на перевозку грузов для строительства, утвержденные
        приказом Министерства строительства и жилищно-коммунального
        хозяйства Российской Федерации от 4 сентября 2019 г. № 517/пр.
        </links>
    :ivar transport: <text xmlns="">Затраты на перевозку грузов в
        соответствии со сметными ценами на перевозки грузов для
        строительства, сведения о которых включены в федеральный реестр
        сметных нормативов или сметная стоимость которых определена с
        учетом положений пунктов 13–18 Методики № 421/пр. </text> <links
        xmlns="">Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 августа 2020 г. № 421/пр </links>
    :ivar other: <text xmlns="">Прочие затраты - затраты, учитываемые в
        соответствии с пунктом 184 МДС 421/пр: "Стоимость работ по
        созданию произведений изобразительного искусства монументального
        характера. Учитывается в сметной стоимости соответствующего
        объекта капитального строительства. Относится к прочим затратам
        (графа 7 ССР СС). Пересчет в текущий уровень цен в позиции
        сметы. Округление до 2-х знаков. Округление производится один
        раз после всех математических операций. </text> <links
        xmlns="">Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 августа 2020 г. № 421/пр. </links>
    :ivar amendments: Сумма поправочных надбавок к стоимости  согласно
        пунктов общих положений к применению единичных расценок,
        учитывающих дополнительные условия работ (в рублях). Округление
        до 2 знаков.
    :ivar load_percent: <text xmlns="">Доля пусконаладочных работ "под
        нагрузкой" в % в структуре полного комплекса ПНР, учтенной в
        сборниках ГЭСНп-2001 и ФЕРп-2001 на ПНР </text> <links
        xmlns="">Приложение № 8 Методика определения сметной стоимости
        строительства (реконструкции, капитального ремонта, сноса
        объектов капитального строительства, работ по сохранению
        объектов культурного наследия) на территории Российской
        Федерации (Приказ № 344/пр от 26.06.2020) </links>
    :ivar idle_percent: <text xmlns="">Доля пусконаладочных работ
        "вхолостую" в % в структуре полного комплекса ПНР, учтенной в
        сборниках ГЭСНп-2001 и ФЕРп-2001 на ПНР </text> <links
        xmlns="">Приложение № 8 Методика определения сметной стоимости
        строительства (реконструкции, капитального ремонта, сноса
        объектов капитального строительства, работ по сохранению
        объектов культурного наследия) на территории Российской
        Федерации (Приказ № 344/пр от 26.06.2020) </links>
    :ivar salary: <text xmlns="">Фонд оплаты труда рабочих-строителей и
        машинистов (ФОТ). Для определения накладных расходов и размера
        сметной прибыли. Определяется как сумма итоговых значений оплаты
        труда рабочих и машинистов по позиции ЛСР </text> <formula
        xmlns=""> Итоговый Базовый: Item.Salary.Base (ФОТ в базовом
        уровне цен по позиции ЛСР) = Item.Cost.Totals.Base.WorkersSalary
        (Итоговая оплата труда рабочих в базовом уровне по расценке) +
        Item.Cost.Totals.Base.MachinistSalary (Итоговая оплата труда
        машинистов в базовом уровне по расценке) +
        Item.Resources.Machine.Machinist.PriceTotalBase (Итоговая оплата
        труда машинистов в базовом уровне по машине вне расценки)+
        Item.Machine.MachinistSalary.Base(Итоговая оплата труда
        машинистов в базовом уровне по машине) Округление до 2-х знаков.
        Округление производится один раз после всех математических
        операций. Итоговый Текущий: Item.Salary.Current (ФОТ в текущем
        уровне цен по позиции ЛСР) = Item.Cost.Totals.
        Current.WorkersSalary (Итоговая оплата труда рабочих в текущем
        уровне по расценке) + Item.Cost.Totals.Current.MachinistSalary
        (Итоговая оплата труда машинистов в текущем уровне по расценке)
        + Item.Resources.Machine.Machinist.PriceTotalCur (Итоговая
        оплата труда машинистов в текущем уровне по машине вне
        расценки)+ Item.Machine.MachinistSalary.Current (Итоговая оплата
        труда машинистов в текущем уровне по машине) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций. </formula> <links xmlns="">Методика
        определения сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        работ по сохранению объектов культурного наследия (памятников
        истории и культуры) народов Российской Федерации на территории
        Российской Федерации, утвержденная приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 4 августа 2020 г. № 421/пр. </links>
    :ivar totals: <text xmlns="">Всего по позиции - Итоговые (суммарные)
        показатели позиции в локальном сметном расчете включающие итоги
        по единичной расценке, накладные расходы, сметную прибыль,
        итоговые стоимости ресурсов вне единичной расценки или итоговые
        стоимости ресурсов, отсутствующих в ФРСН (материал,
        оборудование), транспортные расходы (перевозка грунта или
        мусора), прочие затраты </text> <formula xmlns=""> Для позиции
        (расценки) в базисном уровне: Totals.Base (Итоговые (суммарные)
        показатели позиции в локальном сметном расчете в базисном уровне
        цен) = OverheadsBase (Накладные расходы позиции в локальном
        сметном расчете (базисный уровень цен)) + ProfitsBase (Сметная
        прибыль позиции в локальном сметном расчете (базисный уровень
        цен)) + Cost.Totals (Итоговые (суммарные) показатели единичной
        расценки (базисный уровень цен)) +
        Resources.Material.PriceTotalBase (Стоимость материала вне
        единичной расценки (базисный уровень цен))+
        Resources.Machine.PriceTotalBase (Стоимость машины или механизма
        вне единичной расценки (базисный уровень цен)) +
        Resources.Equipment.PriceTotalBase (Стоимость оборудования вне
        единичной расценки (базисный уровень цен))+ Amendments (Сумма
        поправочных надбавок в руб.) Округление до 2-х знаков.
        Округление производится один раз после всех математических
        операций. Для материалов, учтенных отдельными позициями в
        текущем уровне цен: Totals.Cur (Итоговые (суммарные) показатели
        позиции в локальном сметном расчете в текущем уровне цен) =
        Transport.PriceTotalCur (Стоимость материалов, учтенных
        отдельной позицией (текущий уровень цен))+ Amendments (Сумма
        поправочных надбавок в руб.) Для оборудования, учтенных
        отдельными позициями в текущем уровне цен: Totals.Cur (Итоговые
        (суммарные) показатели позиции в локальном сметном расчете в
        текущем уровне цен) = Equipment.PriceTotalCur (Стоимость
        оборудования, учтенного отдельной позицией (текущий уровень
        цен))+ Amendments (Сумма поправочных надбавок в руб.) Для
        эсксплуатации машин, учтенных отдельными позициями в текущем
        уровне цен: Totals.Cur (Итоговые (суммарные) показатели позиции
        в локальном сметном расчете в текущем уровне цен) =
        Machine.PriceTotalCur (Стоимость эксплуатации машин, учтенных
        отдельной позицией (текущий уровень цен))+ Amendments (Сумма
        поправочных надбавок в руб.) Для перевозки, учтеной отдельными
        позициями в текущем уровне цен: Totals.Cur (Итоговые (суммарные)
        показатели позиции в локальном сметном расчете в текущем уровне
        цен) = Equipment.PriceTotalCur (Стоимость перевозки, учтенной
        отдельной позицией (текущий уровень цен))+ Amendments (Сумма
        поправочных надбавок в руб.) Для прочих затрат, учтенных
        отдельными позициями в текущем уровне цен: Totals.Cur (Итоговые
        (суммарные) показатели позиции в локальном сметном расчете в
        текущем уровне цен) = Other.PriceTotalCur (Стоимость прочих
        затрат, учтенных отдельными позициями (текущий уровень цен))+
        Amendments (Сумма поправочных надбавок в руб.) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операци </formula> <links xmlns="">Методика
        определения сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        работ по сохранению объектов культурного наследия (памятников
        истории и культуры) народов Российской Федерации на территории
        Российской Федерации, утвержденная приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 4 августа 2020 г. № 421/пр. Методические
        рекомендации по определению сметных цен на затраты труда в
        строительстве, утвержденные приказом Министерства строительства
        и жилищно-коммунального хозяйства Российской Федерации от 4
        сентября 2019 г. № 515/пр. </links>
    :ivar bimdata: Ссылки на элементы BIM модели
    """

    class Meta:
        name = "TItem"

    summary_type: Optional[TitemSummaryType] = field(
        default=None,
        metadata={
            "name": "SummaryType",
            "type": "Element",
            "required": True,
        },
    )
    work_type: Optional[TitemWorkType] = field(
        default=None,
        metadata={
            "name": "WorkType",
            "type": "Element",
            "required": True,
        },
    )
    is_return_mat: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsReturnMat",
            "type": "Element",
        },
    )
    overheads: Optional[Toverhead] = field(
        default=None,
        metadata={
            "name": "Overheads",
            "type": "Element",
        },
    )
    profits: Optional[Tprofit] = field(
        default=None,
        metadata={
            "name": "Profits",
            "type": "Element",
        },
    )
    cost: Optional["Titem.Cost"] = field(
        default=None,
        metadata={
            "name": "Cost",
            "type": "Element",
        },
    )
    resources: Optional["Titem.Resources"] = field(
        default=None,
        metadata={
            "name": "Resources",
            "type": "Element",
        },
    )
    material: Optional[Tresource] = field(
        default=None,
        metadata={
            "name": "Material",
            "type": "Element",
        },
    )
    machine: Optional[Tmachine] = field(
        default=None,
        metadata={
            "name": "Machine",
            "type": "Element",
        },
    )
    equipment: Optional[Tresource] = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Element",
        },
    )
    transport: Optional[Ttransportation] = field(
        default=None,
        metadata={
            "name": "Transport",
            "type": "Element",
        },
    )
    other: Optional[Tresource] = field(
        default=None,
        metadata={
            "name": "Other",
            "type": "Element",
        },
    )
    amendments: Optional[float] = field(
        default=None,
        metadata={
            "name": "Amendments",
            "type": "Element",
        },
    )
    load_percent: Optional[float] = field(
        default=None,
        metadata={
            "name": "LoadPercent",
            "type": "Element",
        },
    )
    idle_percent: Optional[float] = field(
        default=None,
        metadata={
            "name": "IdlePercent",
            "type": "Element",
        },
    )
    salary: Optional["Titem.Salary"] = field(
        default=None,
        metadata={
            "name": "Salary",
            "type": "Element",
        },
    )
    totals: Optional["Titem.Totals"] = field(
        default=None,
        metadata={
            "name": "Totals",
            "type": "Element",
            "required": True,
        },
    )
    bimdata: Optional["Titem.Bimdata"] = field(
        default=None,
        metadata={
            "name": "BIMData",
            "type": "Element",
        },
    )

    @dataclass
    class Salary:
        """
        :ivar base: Итого в базовом уровне
        :ivar current: Итого в текущем уровне
        """

        base: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "Base",
                "type": "Element",
            },
        )
        current: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "Current",
                "type": "Element",
            },
        )

    @dataclass
    class Totals:
        """
        :ivar base: Итог по позиции, в базовом уровне
        :ivar current: Итог по позиции, в текущем уровне
        """

        base: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "Base",
                "type": "Element",
            },
        )
        current: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "Current",
                "type": "Element",
            },
        )

    @dataclass
    class Bimdata:
        """
        :ivar element: Ссылка на элемент BIM модели
        """

        element: list[Tbimdata] = field(
            default_factory=list,
            metadata={
                "name": "Element",
                "type": "Element",
            },
        )

    @dataclass
    class Cost:
        """
        :ivar num: <text xmlns="">Порядковый номер единичной расценки в
            локальном сметном расчете. Производится сквозная нумерация
            позиций сметного расчета, к которым относятся единичные
            расценки. </text> <links xmlns="">Методика определения
            сметной стоимости строительства, реконструкции, капитального
            ремонта, сноса объектов капитального строительства, работ по
            сохранению объектов культурного наследия (памятников истории
            и культуры) народов Российской Федерации на территории
            Российской Федерации, утвержденная приказом Министерства
            строительства и жилищно-коммунального хозяйства Российской
            Федерации от 4 августа 2020 г. № 421/пр. </links>
        :ivar prefix: <text xmlns="">Префикс шифра единичной расценки:
            строительные работы, монтаж оборудования, капитальный ремонт
            оборудования, ремонтно- строительные работы, цены на
            материалы, изделия, конструкции и оборудования, расценки на
            эксплуатацию строительных машин и автотранспортных средств,
            цены на перевозку грузов для строительства </text> <links
            xmlns="">Методика определения сметной стоимости
            строительства, реконструкции, капитального ремонта, сноса
            объектов капитального строительства, работ по сохранению
            объектов культурного наследия (памятников истории и
            культуры) народов Российской Федерации на территории
            Российской Федерации, утвержденная приказом Министерства
            строительства и жилищно-коммунального хозяйства Российской
            Федерации от 4 августа 2020 г. № 421/пр. Методические
            рекомендации по определению сметных цен на материалы,
            изделия, конструкции, оборудование, утвержденные приказом
            Министерства строительства и жилищно-коммунального хозяйства
            Российской Федерации от 4 сентября 2019 г. № 517/пр.
            </links>
        :ivar code: <text xmlns="">Шифр единичной расценки в локальном
            сметном расчете.</text> <links xmlns="">Методика определения
            сметной стоимости строительства, реконструкции, капитального
            ремонта, сноса объектов капитального строительства, работ по
            сохранению объектов культурного наследия (памятников истории
            и культуры) народов Российской Федерации на территории
            Российской Федерации, утвержденная приказом Министерства
            строительства и жилищно-коммунального хозяйства Российской
            Федерации от 4 августа 2020 г. № 421/пр. </links>
        :ivar name: Наименование единичной расценки в локальном сметном
            расчете. Указывается полностью, без сокращений в
            соответствии с данными, включенными в ФРСН или в
            соответствии с проектной и иной технической документацией
        :ivar comment: Примечание к элементу в локальном сметном расчете
        :ivar quantity_formula: Формула, использовавшаяся для расчета
            объема работ. Информационное поле.
        :ivar quantity: Объем работ - количество в соответствии с
            проектной и (или) иной технической документацией и с учетом
            единицы измерения расценки (без применения коэффициентов к
            количеству)
        :ivar quantity_total: <text xmlns="">Результирующий объем работ
            с учетом поправочных коэффициентов</text> <formula
            xmlns="">QuantityTotal(Результирующий объем работ с учетом
            поправочных коэффициентов)=Quantity(Объем
            работ)*Coefficient(Итоговый поправочный коэффициент к объему
            работ) Округление производится один раз после всех
            математических операций. Округление до 7 знаков. </formula>
            <links xmlns="">Методика определения сметной стоимости
            строительства, реконструкции, капитального ремонта, сноса
            объектов капитального строительства, работ по сохранению
            объектов культурного наследия (памятников истории и
            культуры) народов Российской Федерации на территории
            Российской Федерации, утвержденная приказом Министерства
            строительства и жилищно-коммунального хозяйства Российской
            Федерации от 4 августа 2020 г. № 421/пр. </links>
        :ivar unit: Единица измерения единичной расценки в локальном
            сметном расчете
        :ivar per_unit: Показатели за единицу измерения единичной
            расценки в локальном сметном расчете
        :ivar totals: Итоговые (суммарные) показатели единичной расценки
            в локальном сметном расчете включающие оплату труда рабочих,
            стоимость эксплуатации машин и механизмов, стоимость
            материальных ресурсов
        :ivar coefficients: Поправочные коэффициенты (учитывающие
            усложняющие факторы и (или) условия производства работ),
            применяемые к показателям позиции в локальном сметном
            расчете к количеству или к стоимости. Округление
            производится до 7 знаков после запятой по итогу
            перемножения.
        :ivar index: <text xmlns="">Индексы изменения сметной стоимости
            к элементам затрат локального сметного расчета Округление до
            2-х знаков. Округление производится один раз после всех
            математических операций. </text>
        :ivar resources_internal: <text xmlns="">Совокупность
            строительных ресурсов (затрат труда рабочих-строителей и
            пусконаладочного персонала, затраты на эксплуатацию
            строительных машин и механизмов, затраты на материальные
            ресурсы, изделия и конструкции и т.п., затраты на
            оборудование, мебель, инвентарь), учтенная и установленная
            на принятый измеритель строительных, монтажных или других
            работ с учетом объема выполняемых работ и условий
            производства работ (справочно) </text> <links xmlns="">
            Методика определения сметной стоимости строительства,
            реконструкции, капитального ремонта, сноса объектов
            капитального строительства, работ по сохранению объектов
            культурного наследия (памятников истории и культуры) народов
            Российской Федерации на территории Российской Федерации,
            утвержденная приказом Министерства строительства и жилищно-
            коммунального хозяйства Российской Федерации от 4 августа
            2020 г. № 421/пр. </links>
        :ivar resources: Ресурсы по проекту (неучтенные в стоимости
            единичной расценки), приведенные в совокупности с единичной
            расценкой и отмеченные как ресурсы по проекту. Имеют
            неточный код (обоснование) в виде привязки к группе КСР
            (ССЦ), общее наименование, единицу измерения и количество
            (не у всех ресурсов). Сметная стоимость за единицу измерения
            отсутствует
        """

        num: Optional[int] = field(
            default=None,
            metadata={
                "name": "Num",
                "type": "Element",
                "required": True,
            },
        )
        prefix: Optional[str] = field(
            default=None,
            metadata={
                "name": "Prefix",
                "type": "Element",
                "required": True,
            },
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Element",
                "required": True,
            },
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Element",
                "required": True,
            },
        )
        comment: Optional[str] = field(
            default=None,
            metadata={
                "name": "Comment",
                "type": "Element",
            },
        )
        quantity_formula: Optional[str] = field(
            default=None,
            metadata={
                "name": "QuantityFormula",
                "type": "Element",
            },
        )
        quantity: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "Quantity",
                "type": "Element",
                "required": True,
            },
        )
        quantity_total: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "QuantityTotal",
                "type": "Element",
                "required": True,
            },
        )
        unit: Optional[str] = field(
            default=None,
            metadata={
                "name": "Unit",
                "type": "Element",
                "required": True,
            },
        )
        per_unit: Optional[TitemParameters] = field(
            default=None,
            metadata={
                "name": "PerUnit",
                "type": "Element",
                "required": True,
            },
        )
        totals: Optional[TitemParameters] = field(
            default=None,
            metadata={
                "name": "Totals",
                "type": "Element",
                "required": True,
            },
        )
        coefficients: Optional["Titem.Cost.Coefficients"] = field(
            default=None,
            metadata={
                "name": "Coefficients",
                "type": "Element",
            },
        )
        index: Optional["Titem.Cost.Index"] = field(
            default=None,
            metadata={
                "name": "Index",
                "type": "Element",
            },
        )
        resources_internal: Optional["Titem.Cost.ResourcesInternal"] = field(
            default=None,
            metadata={
                "name": "ResourcesInternal",
                "type": "Element",
            },
        )
        resources: Optional["Titem.Cost.Resources"] = field(
            default=None,
            metadata={
                "name": "Resources",
                "type": "Element",
            },
        )

        @dataclass
        class Coefficients:
            """
            :ivar final: <text xmlns="">Итоговые значения поправочных
                коэффициентов, применяемых к показателям позиции в
                локальном сметном расчете. Округление до 7-ми знаков.
                Округление производится один раз после всех
                математических операций. </text>
            :ivar coefficient: Поправочный коэффициент, применяемый к
                показателю позиции в локальном сметном расчете
            """

            final: Optional[TcostCoefficients] = field(
                default=None,
                metadata={
                    "name": "Final",
                    "type": "Element",
                    "required": True,
                },
            )
            coefficient: list["Titem.Cost.Coefficients.Coefficient"] = field(
                default_factory=list,
                metadata={
                    "name": "Coefficient",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass
            class Coefficient(TcostCoefficients):
                """
                :ivar name: Наименование коэффициента. Указывается
                    наименование, величина, а также составляющие
                    единичных расценок, к которым коэффициент
                    применяется.
                :ivar reason: Обоснование коэффициента (шифр
                    коэффициента (при наличии) или ссылка на положения
                    сметных нормативов и (или) пункты разделов сборников
                    единичных расценок)
                """

                name: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Name",
                        "type": "Element",
                        "required": True,
                    },
                )
                reason: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Reason",
                        "type": "Element",
                    },
                )

        @dataclass
        class Index:
            """
            Комплексный тип для передачи значений индексов к позиции локального сметного
            расчета или общих индексов локального сметного расчета.

            :ivar name: Наименование индекса изменения сметной стоимости
            :ivar reason: Обоснование индекса изменения сметной
                стоимости
            :ivar num: Порядковый номер индекса изменения сметной
                стоимости
            :ivar values: Значения индекса изменения сметной стоимости
            """

            name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Name",
                    "type": "Element",
                    "required": True,
                },
            )
            reason: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Reason",
                    "type": "Element",
                },
            )
            num: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Num",
                    "type": "Element",
                    "required": True,
                },
            )
            values: Optional["Titem.Cost.Index.Values"] = field(
                default=None,
                metadata={
                    "name": "Values",
                    "type": "Element",
                    "required": True,
                },
            )

            @dataclass
            class Values:
                value: list[TcostIndexValue] = field(
                    default_factory=list,
                    metadata={
                        "name": "Value",
                        "type": "Element",
                        "min_occurs": 1,
                    },
                )

        @dataclass
        class ResourcesInternal:
            """
            :ivar worker: <text xmlns="">Оплата труда рабочих,
                непосредственно занятых в процессе создания материальных
                ценностей при выполнении строительных работ и
                работников-исполнителей пусконаладочных работ
                (справочно) </text> <links xmlns=""> Методические
                рекомендации по определению сметных цен на затраты труда
                в строительстве, утвержденные приказом Министерства
                строительства и жилищно-коммунального хозяйства
                Российской Федерации от 4 сентября 2019 г. № 515/пр.
                Методика определения сметной стоимости строительства,
                реконструкции, капитального ремонта, сноса объектов
                капитального строительства, работ по сохранению объектов
                культурного наследия (памятников истории и культуры)
                народов Российской Федерации на территории Российской
                Федерации, утвержденная приказом Министерства
                строительства и жилищно-коммунального хозяйства
                Российской Федерации от 4 августа 2020 г. № 421/пр.
                </links>
            :ivar machine: <text xmlns="">Затраты на эксплуатацию
                строительных машин, автотранспортных средств,
                механизированных инструментов и механизмов (справочно)
                </text> <links xmlns=""> Методические рекомендации по
                определению сметных цен на эксплуатацию машин и
                механизмов, утвержденные приказом Министерства
                строительства и жилищно-коммунального хозяйства
                Российской Федерации от 4 сентября 2019 г. № 513/пр.
                Методика определения сметной стоимости строительства,
                реконструкции, капитального ремонта, сноса объектов
                капитального строительства, работ по сохранению объектов
                культурного наследия (памятников истории и культуры)
                народов Российской Федерации на территории Российской
                Федерации, утвержденная приказом Министерства
                строительства и жилищно-коммунального хозяйства
                Российской Федерации от 4 августа 2020 г. № 421/пр.
                </links>
            :ivar material: <text xmlns="">Затраты на материальные
                ресурсы, изделия и конструкции (справочно) </text>
                <links xmlns=""> Методические рекомендации по
                определению сметных цен на материалы, изделия,
                конструкции, оборудование, утвержденные приказом
                Министерства строительства и жилищно-коммунального
                хозяйства Российской Федерации от 4 сентября 2019 г. №
                517/пр. Методика определения сметной стоимости
                строительства, реконструкции, капитального ремонта,
                сноса объектов капитального строительства, работ по
                сохранению объектов культурного наследия (памятников
                истории и культуры) народов Российской Федерации на
                территории Российской Федерации, утвержденная приказом
                Министерства строительства и жилищно-коммунального
                хозяйства Российской Федерации от 4 августа 2020 г. №
                421/пр. </links>
            :ivar equipment: <text xmlns="">Затраты на оборудование,
                мебель, инвентарь (справочно) </text> <links xmlns="">
                Методические рекомендации по определению сметных цен на
                материалы, изделия, конструкции, оборудование,
                утвержденные приказом Министерства строительства и
                жилищно-коммунального хозяйства Российской Федерации от
                4 сентября 2019 г. № 517/пр. Методика определения
                сметной стоимости строительства, реконструкции,
                капитального ремонта, сноса объектов капитального
                строительства, работ по сохранению объектов культурного
                наследия (памятников истории и культуры) народов
                Российской Федерации на территории Российской Федерации,
                утвержденная приказом Министерства строительства и
                жилищно-коммунального хозяйства Российской Федерации от
                4 августа 2020 г. № 421/пр. </links>
            """

            worker: list[Tresource] = field(
                default_factory=list,
                metadata={
                    "name": "Worker",
                    "type": "Element",
                },
            )
            machine: list[Tmachine] = field(
                default_factory=list,
                metadata={
                    "name": "Machine",
                    "type": "Element",
                },
            )
            material: list[Tresource] = field(
                default_factory=list,
                metadata={
                    "name": "Material",
                    "type": "Element",
                },
            )
            equipment: list[Tresource] = field(
                default_factory=list,
                metadata={
                    "name": "Equipment",
                    "type": "Element",
                },
            )

        @dataclass
        class Resources:
            """
            :ivar material: <text xmlns="">Сметные цен на материалы,
                изделия и конструкции по локальному сметному расчету
                (смете) предназначены для определения сметных затрат на
                материальные ресурсы при составлении сметной
                документации на строительство, реконструкцию,
                капитальный ремонт зданий и сооружений. </text> <links
                xmlns="">Методические рекомендации по определению
                сметных цен на материалы, изделия, конструкции,
                оборудование, утвержденные приказом Министерства
                строительства и жилищно-коммунального хозяйства
                Российской Федерации от 4 сентября 2019 г. № 517/пр.
                </links>
            :ivar equipment: <text xmlns="">Сметные цены на
                оборудование, мебель, инвентарь по локальному сметному
                расчету (смете) предназначены для определения сметных
                затрат на монтаж оборудования при составлении сметной
                документации на строительство, реконструкцию,
                капитальный ремонт зданий и сооружений. </text> <links
                xmlns="">Методические рекомендации по определению
                сметных цен на материалы, изделия, конструкции,
                оборудование, утвержденные приказом Министерства
                строительства и жилищно-коммунального хозяйства
                Российской Федерации от 4 сентября 2019 г. № 517/пр.
                </links>
            """

            material: list[Tresource] = field(
                default_factory=list,
                metadata={
                    "name": "Material",
                    "type": "Element",
                },
            )
            equipment: list[Tresource] = field(
                default_factory=list,
                metadata={
                    "name": "Equipment",
                    "type": "Element",
                },
            )

    @dataclass
    class Resources:
        """
        :ivar material: <text xmlns="">Сметные цен на материалы, изделия
            и конструкции по локальному сметному расчету (смете)
            предназначены для определения сметных затрат на материальные
            ресурсы при составлении сметной документации на
            строительство, реконструкцию, капитальный ремонт зданий и
            сооружений. </text> <links xmlns="">Методические
            рекомендации по определению сметных цен на материалы,
            изделия, конструкции, оборудование, утвержденные приказом
            Министерства строительства и жилищно-коммунального хозяйства
            Российской Федерации от 4 сентября 2019 г. № 517/пр.
            </links>
        :ivar machine: <text xmlns="">Ресурс (машины и механизмы) в
            соответствии с Классификатором строительных ресурсов,
            сформированным приказом Министерства строительства и
            жилищно-коммунального хозяйства Российской Федерации или
            Доплата труда машинистов (дополнительно к стоимости ЭМ)
            </text> <links xmlns="">Методические рекомендации по
            определению сметных цен на материалы, изделия, конструкции,
            оборудование и цен услуг на перевозку грузов для
            строительства, утвержденные приказом Министерства
            строительства и жилищно-коммунального хозяйства Российской
            Федерации от 4 сентября 2019 г. № 517/пр. </links>
        :ivar equipment: <text xmlns="">Сметные цен на оборудование,
            мебель, инвентарь по локальному сметному расчету (смете)
            предназначены для определения сметных затрат на монтаж
            оборудования при составлении сметной документации на
            строительство, реконструкцию, капитальный ремонт зданий и
            сооружений. </text> <links xmlns="">Методические
            рекомендации по определению сметных цен на материалы,
            изделия, конструкции, оборудование, утвержденные приказом
            Министерства строительства и жилищно-коммунального хозяйства
            Российской Федерации от 4 сентября 2019 г. № 517/пр.
            </links>
        :ivar transport: <text xmlns="">Затраты на перевозку грузов
            автомобильным или иным видом транспорта </text> <links
            xmlns="">Методика определения сметной стоимости
            строительства, реконструкции, капитального ремонта, сноса
            объектов капитального строительства, работ по сохранению
            объектов культурного наследия (памятников истории и
            культуры) народов Российской Федерации на территории
            Российской Федерации, утвержденная приказом Министерства
            строительства и жилищно-коммунального хозяйства Российской
            Федерации от 4 августа 2020 г. № 421/пр </links>
        """

        material: list[Tresource] = field(
            default_factory=list,
            metadata={
                "name": "Material",
                "type": "Element",
            },
        )
        machine: list[Tmachine] = field(
            default_factory=list,
            metadata={
                "name": "Machine",
                "type": "Element",
            },
        )
        equipment: list[Tresource] = field(
            default_factory=list,
            metadata={
                "name": "Equipment",
                "type": "Element",
            },
        )
        transport: list[Ttransportation] = field(
            default_factory=list,
            metadata={
                "name": "Transport",
                "type": "Element",
            },
        )


@dataclass
class Tsummary:
    """
    Итоговые показатели сметной стоимости локального сметного расчета общие и по
    видам основных работ (элементы строительства)

    :ivar building: <text xmlns="">ВСЕГО строительные работы - общие
        итоги по разделу или по ЛСР в базисном уровне цен, по ЛСР в
        текущем уровне цен по строительным (ремонтно-строительным)
        работам с раскладкой по элементам затрат в базисном уровне и в
        текущем уровне цен </text> <formula xmlns=""> Для базисного
        уровня - итоги по разделу или по ЛСР в базисном уровне цен с
        раскладкой по элементам затрат. Округление до 2-х знаков.
        Округление производится один раз после всех математических
        операций Для текущего уровня при применении индексов по
        элементам ПЗ: итоги по ЛСР в текущем уровне цен с раскладкой по
        элементам затрат. Текущая стоимость перевозки при применении
        индексов СМР: итоги по разделу или по ЛСР. Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций. </formula> <links xmlns="">Методика
        определения сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        работ по сохранению объектов культурного наследия (памятников
        истории и культуры) народов Российской Федерации на территории
        Российской Федерации, утвержденная приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 4 августа 2020 г. № 421/пр. </links>
    :ivar mounting: <text xmlns="">ВСЕГО монтажные работы - общие итоги
        по разделу или по ЛСР в базисном уровне цен, по ЛСР в текущем
        уровне цен по монтажным работам с раскладкой по элементам затрат
        в базисном уровне и в текущем уровне цен </text> <formula
        xmlns=""> Для базисного уровня - итоги по разделу или по ЛСР в
        базисном уровне цен с раскладкой по элементам затрат. Округление
        до 2-х знаков. Округление производится один раз после всех
        математических операций Для текущего уровня при применении
        индексов по элементам ПЗ: итоги по ЛСР в текущем уровне цен с
        раскладкой по элементам затрат. Текущая стоимость перевозки при
        применении индексов СМР: итоги по разделу или по ЛСР. Округление
        до 2-х знаков. Округление производится один раз после всех
        математических операций. </formula> <links xmlns="">Методика
        определения сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        работ по сохранению объектов культурного наследия (памятников
        истории и культуры) народов Российской Федерации на территории
        Российской Федерации, утвержденная приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 4 августа 2020 г. № 421/пр. </links>
    :ivar restoration: <text xmlns="">ВСЕГО ремонтно-реставрационные
        работы - общие итоги по разделу или по ЛСР в базисном уровне цен
        и в текущем уровне цен </text> <formula xmlns=""> Для базисного
        уровня при применении индексов по элементам ПЗ в позициях ЛС: -
        итоги по разделу или по ЛСР в базисном уровне цен с раскладкой
        по элементам затрат: ПЗ, ОТ, ЭМ, ОТм, МР, ФОТ (справочно), НР,
        СП. Для базисного уровня при применении индексов СМР: 1. Всего в
        базисном уровне цен 1984 года 2. Всего в базисном уровне цен
        2001 года 3. Раскладка по элементам затрат в базисном уровне
        1984 года: ПЗ, ОТ, ЭМ, ОТм, МР, ФОТ (справочно), НР, СП.
        Округление до 2-х знаков. Округление производится один раз после
        всех математических операций Для текущего уровня при применении
        индексов по элементам ПЗ в позициях ЛС: - итоги по ЛСР в текущем
        уровне цен с раскладкой по элементам затрат: ПЗ, ОТ, ЭМ, ОТм,
        МР, ФОТ (справочно), НР, СП. Для текущего уровня при применении
        индексов СМР в итогах сметы: 1. Всего в уровне цен 2001 -
        ремонтно-реставрационные работы в базисном уровне цен 1984 года
        с пересчетом в уровень цен сметно-нормативной базы 2001 года 2.
        Всего в текущем уровне цен - ремонтно-реставрационные работы в
        уровне цен сметно-нормативной базы 2001 года с пересчетом в
        текущий уровень цен Округление до 2-х знаков. Округление
        производится один раз после всех математических операций.
        </formula> <links xmlns="">Методика определения сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр. </links>
    :ivar equipment: <text xmlns="">ВСЕГО оборудование - общие итоги по
        разделу или по ЛСР в базисном уровне цен, по ЛСР в текущем
        уровне цен по оборудованию с указанием стоимости дополнительной
        перевозки. В текущем и базисном уровнях цен </text> <formula
        xmlns=""> Для базисного уровня - итоги по разделу или по ЛСР в
        базисном уровне цен: стоимость оборудования и дополнительной
        перевозки. Округление до 2-х знаков. Округление производится
        один раз после всех математических операций Для текущего уровня
        - итоги по ЛСР в текущем уровне цен стоимость: оборудования и
        дополнительной перевозки. Округление до 2-х знаков. Округление
        производится один раз после всех математических операций.
        </formula> <links xmlns="">Методика определения сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр. </links>
    :ivar other_works: <text xmlns="">Прочие работы (ПНР) - общие итоги
        по разделу или по ЛСР в базисном уровне цен, по ЛСР в базисном и
        текущем уровнях цен с раскладкой по элементам затрат. Под
        прочими работами понимаются затраты, учитываемые в соответствии
        с пунктами 122-128 МДС 421/пр - сметные затраты на
        пусконаладочные работы </text> <formula xmlns=""> Для базисного
        уровня - суммирование позиций ПНР в базисном уровне цен с
        раскладкой по элементам затрат. Округление до 2-х знаков.
        Округление производится один раз после всех математических
        операций Для текущего уровня при применении индексов по
        элементам ПЗ: суммирование значений позиций ПНР в текущем уровне
        цен. Для текущего уровня при применении индекса СМР:
        суммирование значений позиций ПНР в базисном уровне цен и
        умножение на единый индекс:
        OtherWorks.Total.PriceCurrent=OtherWorks.Total.PriceBase*OtherWorks.Total.PriceIndex
        Округление до 2-х знаков. Округление производится один раз после
        всех математических операций. </formula> <links
        xmlns="">Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 августа 2020 г. № 421/пр. </links>
    :ivar other: <text xmlns="">Прочие затраты - общие итоги по разделу
        или ЛСР в базисном и текущем уровнях цен. Прочие затраты,
        учитываемые в соответствии с пунктом 184 МДС 421/пр: "Стоимость
        работ по созданию произведений изобразительного искусства
        монументального характера. Учитывается в сметной стоимости
        соответствующего объекта капитального строительства. Относится к
        прочим затратам (графа 7 ССР СС). Пересчет в текущий уровень цен
        в позиции сметы. </text> <formula xmlns=""> Для базисного
        уровня: Other.PriceBase (Всего по прочим затратам по разделу или
        по ЛСР в базисном уровне цен)=Сумма элементов
        Item.Other.PriceTotalBase(Cтоимость прочих затрат в базисном
        уровне цен) Округление до 2-х знаков. Округление производится
        один раз после всех математических операций Для текущего уровня:
        Other.PriceCur (Всего по прочим затратам по разделу или по ЛСР
        текущем уровне цен)=Сумма элементов
        Item.Other.PriceTotalCur(Cтоимость прочих затрат в текущем
        уровне цен) Округление до 2-х знаков. Округление производится
        один раз после всех математических операций </formula> <links
        xmlns="">Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 августа 2020 г. № 421/пр. </links>
    :ivar other_total: <text xmlns="">ВСЕГО прочие затраты - общие итоги
        по ЛСР в базисном и текущем уровнях цен по прочим работам и
        затратам. Сумма итоговых прочих затрат и итоговых прочих работ
        по ЛСР. </text> <formula xmlns=""> Для базисного уровня:
        OtherTotal.PriceBase (Всего по прочим затратам по ЛСР в базисном
        уровне цен)=OtherWorks.Total.PriceBase(Всего стоимость прочих
        работ ПНР по ЛСР в базисном уровне цен)+Other.PriceBase(Всего
        стоимость прочих затрат по ЛСР в базисном уровне цен) Округление
        до 2-х знаков. Округление производится один раз после всех
        математических операций Для текущего уровня: OtherTotal.PriceCur
        (Всего по прочим затратам по ЛСР в текущем уровне
        цен)=OtherWorks.Total.PriceCur(Всего стоимость прочих работ ПНР
        по ЛСР в текущем уровне цен)+Other.PriceCur(Всего стоимость
        прочих затрат по ЛСР в текущем уровне цен) Округление до 2-х
        знаков. Округление производится один раз после всех
        математических операций </formula> <links xmlns="">Методика
        определения сметной стоимости строительства, реконструкции,
        капитального ремонта, сноса объектов капитального строительства,
        работ по сохранению объектов культурного наследия (памятников
        истории и культуры) народов Российской Федерации на территории
        Российской Федерации, утвержденная приказом Министерства
        строительства и жилищно-коммунального хозяйства Российской
        Федерации от 4 августа 2020 г. № 421/пр. </links>
    :ivar commissioning: <text xmlns="">Стоимость пусконаладочных работ
        по ЛСР в текущем и базовом уровнях цен в виде разделения на
        затраты «вхолостую» и «под нагрузкой» </text> <links
        xmlns="">Методика определения сметной стоимости строительства,
        реконструкции, капитального ремонта, сноса объектов капитального
        строительства, работ по сохранению объектов культурного наследия
        (памятников истории и культуры) народов Российской Федерации на
        территории Российской Федерации, утвержденная приказом
        Министерства строительства и жилищно-коммунального хозяйства
        Российской Федерации от 4 августа 2020 г. № 421/пр. </links>
    :ivar summary: <text xmlns="">Общие итоги по разделу или по ЛСР в
        базисном уровне цен, по ЛСР в текущем уровне цен с раскладкой по
        элементам затрат в базисном уровне и в текущем уровне цен - СМР
        (Building, Mounting), ПНР(OtherWorks), стоимость перевозки в
        двух уровнях цен. </text> <formula xmlns=""> Для базисного
        уровня - итоги по разделу или по ЛСР в базисном уровне цен с
        раскладкой по элементам затрат. Округление до 2-х знаков.
        Округление производится один раз после всех математических
        операций. Для текущего уровня при применении индексов по
        элементам ПЗ: итоги по ЛСР в текущем уровне цен с раскладкой по
        элементам затрат. Округление до 2-х знаков. Округление
        производится один раз после всех математических операций. Для
        текущего уровня при применении индексов СМР: итоги по ЛСР в
        текущем уровне цен без раскладки по элементам затрат. Текущая
        стоимость перевозки и дополнительной перевозки. Округление до
        2-х знаков. Округление производится один раз после всех
        математических операций. При индексации по элементам ПЗ
        отображаются значения индексов на материалы, эксплуатацию машин.
        Индексы на оплату труда, перевозку, дополнительную перевозку не
        отображаются. При индексации СМР отображаются значения индексов
        на СМР. Индексы на перевозку и дополнительную перевозку не
        отображаются. </formula> <links xmlns="">Методика определения
        сметной стоимости строительства, реконструкции, капитального
        ремонта, сноса объектов капитального строительства, работ по
        сохранению объектов культурного наследия (памятников истории и
        культуры) народов Российской Федерации на территории Российской
        Федерации, утвержденная приказом Министерства строительства и
        жилищно-коммунального хозяйства Российской Федерации от 4
        августа 2020 г. № 421/пр. </links>
    :ivar total: <text xmlns="">Всего по разделу или по ЛСР в базисном
        уровне цен, по ЛСР в текущем уровне цен. В том числе указывается
        стоимость материалов и оборудования, отсутствующих в ФРСН.
        </text> <formula xmlns=""> Для базисного уровня: Total.PriceBase
        (Всего по разделу или по ЛСР в базисном уровне
        цен)=Building.Total.PriceBase (Всего сметная стоимость по
        строительным (ремонтно-строительным) работам по разделу или ЛСР
        в базисном уровне цен) + Mounting.Total.PriceBase (Всего сметная
        стоимость по монтажным работам по разделу или ЛСР в базисном
        уровне цен) + Equipment.Total.PriceBase (Всего сметная стоимость
        оборудования по разделу или ЛСР в базисном уровне цен)+
        OtherTotal.PriceBase(Всего стоимость прочих затрат по разделу
        или ЛСР в базисном уровне цен)+
        (Restoration.Restoration2001.PriceBase(Всего стоимость
        "Реставрация" по разделу или ЛСР в базисном уровне цен 2001 -
        при "Индексе СМР") или
        Restoration.RestorationElement.Total.PriceBase(Всего стоимость
        "Реставрация" по разделу или ЛСР в базисном уровне цен - при
        "Индексе по элементам ПЗ")) Округление до 2-х знаков. Округление
        производится один раз после всех математических операций Для
        текущего уровня: Total.PriceCur (Всего по ЛСР в текущем уровне
        цен)=Building.Total.PriceCur (Всего сметная стоимость по
        строительным (ремонтно-строительным) работам по ЛСР в текущем
        уровне цен) + Mounting.Total.PriceCur (Всего сметная стоимость
        по монтажным работам по ЛСР в текущем уровне цен) +
        Equipment.Total.PriceCur (Всего сметная стоимость оборудования
        по ЛСР в текущем уровне цен)+ OtherTotal.PriceCur (Всего
        стоимость прочих затрат по ЛСР в текущем уровне цен)+
        (Restoration.Restoration2001.PriceCur(Всего стоимость
        "Реставрация" по разделу или ЛСР в текущем уровне цен)- при
        "Индексе СМР") или
        Restoration.RestorationElement.Total.PriceCur(Всего стоимость
        "Реставрация" по разделу или ЛСР в текущем уровне цен - при
        "Индексе по элементам ПЗ")) Округление до 2-х знаков. Округление
        производится один раз после всех математических операций
        </formula> <links xmlns="">Методика определения сметной
        стоимости строительства, реконструкции, капитального ремонта,
        сноса объектов капитального строительства, работ по сохранению
        объектов культурного наследия (памятников истории и культуры)
        народов Российской Федерации на территории Российской Федерации,
        утвержденная приказом Министерства строительства и жилищно-
        коммунального хозяйства Российской Федерации от 4 августа 2020
        г. № 421/пр. </links>
    """

    class Meta:
        name = "TSummary"

    building: Optional[TsummaryItems] = field(
        default=None,
        metadata={
            "name": "Building",
            "type": "Element",
        },
    )
    mounting: Optional[TsummaryItems] = field(
        default=None,
        metadata={
            "name": "Mounting",
            "type": "Element",
        },
    )
    restoration: Optional["Tsummary.Restoration"] = field(
        default=None,
        metadata={
            "name": "Restoration",
            "type": "Element",
        },
    )
    equipment: Optional[TsummaryDetails] = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Element",
        },
    )
    other_works: Optional[TsummaryItems] = field(
        default=None,
        metadata={
            "name": "OtherWorks",
            "type": "Element",
        },
    )
    other: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "Other",
            "type": "Element",
        },
    )
    other_total: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "OtherTotal",
            "type": "Element",
        },
    )
    commissioning: Optional["Tsummary.Commissioning"] = field(
        default=None,
        metadata={
            "name": "Commissioning",
            "type": "Element",
        },
    )
    summary: Optional[TsummaryItems] = field(
        default=None,
        metadata={
            "name": "Summary",
            "type": "Element",
            "required": True,
        },
    )
    total: Optional[TpriceElement] = field(
        default=None,
        metadata={
            "name": "Total",
            "type": "Element",
        },
    )

    @dataclass
    class Restoration:
        """
        :ivar restoration_element: <text xmlns="">Ремонтно-
            реставрационные работы в базисном с раскладкой по элементам
            затрат (ПЗ, ОТ, ЭМ, ОТм, МР, ФОТ (справочно), НР, СП): - в
            уровне цен 1984 года при применении индексов СМР; - в
            текущем уровне цен при примении индексов по элементам
            затрат. Округление до 2-х знаков. Округление производится
            один раз после всех математических операций </text> <links
            xmlns="">Методика определения сметной стоимости
            строительства, реконструкции, капитального ремонта, сноса
            объектов капитального строительства, работ по сохранению
            объектов культурного наследия (памятников истории и
            культуры) народов Российской Федерации на территории
            Российской Федерации, утвержденная приказом Министерства
            строительства и жилищно-коммунального хозяйства Российской
            Федерации от 4 августа 2020 г. № 421/пр. </links>
        :ivar restoration1984: <text xmlns="">Ремонтно-реставрационные
            работы в базисном уровне цен 1984 года с пересчетом в
            уровень цен сметно-нормативной базы 2001 года </text> <links
            xmlns="">Методика определения сметной стоимости
            строительства, реконструкции, капитального ремонта, сноса
            объектов капитального строительства, работ по сохранению
            объектов культурного наследия (памятников истории и
            культуры) народов Российской Федерации на территории
            Российской Федерации, утвержденная приказом Министерства
            строительства и жилищно-коммунального хозяйства Российской
            Федерации от 4 августа 2020 г. № 421/пр. </links>
        :ivar restoration2001: <text xmlns="">Ремонтно-реставрационные
            работы в уровне цен сметно-нормативной базы 2001 года с
            пересчетом в текущий уровень цен </text> <links
            xmlns="">Методика определения сметной стоимости
            строительства, реконструкции, капитального ремонта, сноса
            объектов капитального строительства, работ по сохранению
            объектов культурного наследия (памятников истории и
            культуры) народов Российской Федерации на территории
            Российской Федерации, утвержденная приказом Министерства
            строительства и жилищно-коммунального хозяйства Российской
            Федерации от 4 августа 2020 г. № 421/пр. </links>
        """

        restoration_element: Optional[TsummaryItems] = field(
            default=None,
            metadata={
                "name": "RestorationElement",
                "type": "Element",
                "required": True,
            },
        )
        restoration1984: Optional[TpriceElement] = field(
            default=None,
            metadata={
                "name": "Restoration1984",
                "type": "Element",
                "required": True,
            },
        )
        restoration2001: Optional[TpriceElement] = field(
            default=None,
            metadata={
                "name": "Restoration2001",
                "type": "Element",
                "required": True,
            },
        )

    @dataclass
    class Commissioning:
        """
        :ivar under_load: <text xmlns="">Пусконаладочные работы "под
            нагрузкой")</text> <formula xmlns=""> в текущем уровне цен:
            Commissioning.UnderLoad (Стоимость ПНР «под нагрузкой» в
            текущем уровне цен) = UnderLoad.TotalCur(Стоимость ПНР «под
            нагрузкой» в текущем уровне цен) в базовом уровне цен:
            Commissioning.UnderLoad (Стоимость ПНР «под нагрузкой» в
            базовом уровне цен) = UnderLoad.TotalBase(Стоимость ПНР «под
            нагрузкой» в базовом уровне цен) </formula> <links
            xmlns="">Методика определения сметной стоимости
            строительства, реконструкции, капитального ремонта, сноса
            объектов капитального строительства, работ по сохранению
            объектов культурного наследия (памятников истории и
            культуры) народов Российской Федерации на территории
            Российской Федерации, утвержденная приказом Министерства
            строительства и жилищно-коммунального хозяйства Российской
            Федерации от 4 августа 2020 г. № 421/пр. </links>
        :ivar idle: <text xmlns="">Пусконаладочные работы
            "вхолостую"</text> <formula xmlns=""> в текущем уровне цен:
            Commissioning.Idle (Стоимость ПНР "вхолостую" в текущем
            уровне цен) = UnderLoad.TotalCur(Стоимость ПНР "вхолостую" в
            текущем уровне цен) в базовом уровне цен: Commissioning.Idle
            (Стоимость ПНР "вхолостую" в базовом уровне цен) =
            UnderLoad.TotalBase(Стоимость ПНР "вхолостую" в базовом
            уровне цен) </formula> <links xmlns="">Методика определения
            сметной стоимости строительства, реконструкции, капитального
            ремонта, сноса объектов капитального строительства, работ по
            сохранению объектов культурного наследия (памятников истории
            и культуры) народов Российской Федерации на территории
            Российской Федерации, утвержденная приказом Министерства
            строительства и жилищно-коммунального хозяйства Российской
            Федерации от 4 августа 2020 г. № 421/пр. </links>
        """

        under_load: Optional["Tsummary.Commissioning.UnderLoad"] = field(
            default=None,
            metadata={
                "name": "UnderLoad",
                "type": "Element",
            },
        )
        idle: Optional["Tsummary.Commissioning.Idle"] = field(
            default=None,
            metadata={
                "name": "Idle",
                "type": "Element",
            },
        )

        @dataclass
        class UnderLoad:
            """
            :ivar item:
            :ivar total_base: <text xmlns="">Итоговая стоимость
                пусконаладочных работ: «вхолостую» или «под нагрузкой» в
                базовом уровне цен </text> <formula xmlns="">TotalBase
                (Итоговая стоимость пусконаладочных работ: «вхолостую»
                или «под нагрузкой» в базовом уровне цен) = Сумма
                элементов (BasePrice (Стоимость пусконаладочных работ
                «вхолостую» или «под нагрузкой» в базовом уровне цен)
                Округление до 2-х знаков. Округление производится один
                раз после всех математических операций </formula> <links
                xmlns="">Приложение № 8 к Методике определения сметной
                стоимости строительства, реконструкции, капитального
                ремонта, сноса объектов капитального строительства,
                работ по сохранению объектов культурного наследия
                (памятников истории и культуры) народов Российской
                Федерации на территории Российской Федерации,
                утвержденной приказом Министерства строительства и
                жилищно-коммунального хозяйства Российской Федерации от
                4 августа 2020 г. № 421/пр </links>
            :ivar total_cur: <text xmlns="">Итоговая стоимость
                пусконаладочных работ: «вхолостую» или «под нагрузкой» в
                текущем уровне цен </text> <formula xmlns="">TotalCur
                (Итоговая стоимость пусконаладочных работ: «вхолостую»
                или «под нагрузкой» в текущем уровне цен) = Сумма
                элементов (CurrentPrice (Стоимость пусконаладочных работ
                «вхолостую» или «под нагрузкой» в текущем уровне цен)
                Округление до 2-х знаков. Округление производится один
                раз после всех математических операций </formula> <links
                xmlns="">Приложение № 8 к Методике определения сметной
                стоимости строительства, реконструкции, капитального
                ремонта, сноса объектов капитального строительства,
                работ по сохранению объектов культурного наследия
                (памятников истории и культуры) народов Российской
                Федерации на территории Российской Федерации,
                утвержденной приказом Министерства строительства и
                жилищно-коммунального хозяйства Российской Федерации от
                4 августа 2020 г. № 421/пр </links>
            """

            item: list[Tcomissioning] = field(
                default_factory=list,
                metadata={
                    "name": "Item",
                    "type": "Element",
                },
            )
            total_base: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "TotalBase",
                    "type": "Element",
                    "required": True,
                },
            )
            total_cur: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "TotalCur",
                    "type": "Element",
                    "required": True,
                },
            )

        @dataclass
        class Idle:
            """
            :ivar item:
            :ivar total_base: <text xmlns="">Итоговая стоимость
                пусконаладочных работ: «вхолостую» или «под нагрузкой» в
                базовом уровне цен </text> <formula xmlns="">TotalBase
                (Итоговая стоимость пусконаладочных работ: «вхолостую»
                или «под нагрузкой» в базовом уровне цен) = Сумма
                элементов (BasePrice (Стоимость пусконаладочных работ
                «вхолостую» или «под нагрузкой» в базовом уровне цен)
                Округление до 2-х знаков. Округление производится один
                раз после всех математических операций </formula> <links
                xmlns="">Приложение № 8 к Методике определения сметной
                стоимости строительства, реконструкции, капитального
                ремонта, сноса объектов капитального строительства,
                работ по сохранению объектов культурного наследия
                (памятников истории и культуры) народов Российской
                Федерации на территории Российской Федерации,
                утвержденной приказом Министерства строительства и
                жилищно-коммунального хозяйства Российской Федерации от
                4 августа 2020 г. № 421/пр </links>
            :ivar total_cur: <text xmlns="">Итоговая стоимость
                пусконаладочных работ: «вхолостую» или «под нагрузкой» в
                текущем уровне цен </text> <formula xmlns="">TotalCur
                (Итоговая стоимость пусконаладочных работ: «вхолостую»
                или «под нагрузкой» в текущем уровне цен) = Сумма
                элементов (CurrentPrice (Стоимость пусконаладочных работ
                «вхолостую» или «под нагрузкой» в текущем уровне цен)
                Округление до 2-х знаков. Округление производится один
                раз после всех математических операций </formula> <links
                xmlns="">Приложение № 8 к Методике определения сметной
                стоимости строительства, реконструкции, капитального
                ремонта, сноса объектов капитального строительства,
                работ по сохранению объектов культурного наследия
                (памятников истории и культуры) народов Российской
                Федерации на территории Российской Федерации,
                утвержденной приказом Министерства строительства и
                жилищно-коммунального хозяйства Российской Федерации от
                4 августа 2020 г. № 421/пр </links>
            """

            item: list[Tcomissioning] = field(
                default_factory=list,
                metadata={
                    "name": "Item",
                    "type": "Element",
                },
            )
            total_base: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "TotalBase",
                    "type": "Element",
                    "required": True,
                },
            )
            total_cur: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "TotalCur",
                    "type": "Element",
                    "required": True,
                },
            )


@dataclass
class Construction:
    """Объекты капитального строительства (реконструкции, капитального ремонта)(Стройка)
    Элемент обязан содержать аттрибуты указывающие на применяемый xsd-шаблон описания сметы: xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="LocalEstimateBaseIndexMethod-1_09.xsd". Электронные документы,
    представляемые для проведения государственной экспертизы проектной документации и (или) результатов
    инженерных изысканий и проверки достоверности определения сметной стоимости строительства,
    реконструкции, капитального ремонта, должны иметь расширение файла .gge

    :ivar meta: Информация о программном продукте, использующемся для
        составления локального сметного расчета
    :ivar num: Номер объектов капитального строительства (реконструкции,
        капитального ремонта)(Номер стройки)
    :ivar name: Наименование объектов капитального строительства
        (реконструкции, капитального ремонта)) (Наименование стройки)
    :ivar object_value: Объект капитального строительства
        (реконструкции, капитального ремонта)
    :ivar bimfiles: Список прилагаемых IFC файлов
    """

    meta: Optional[Tmeta] = field(
        default=None,
        metadata={
            "name": "Meta",
            "type": "Element",
            "required": True,
        },
    )
    num: Optional[str] = field(
        default=None,
        metadata={
            "name": "Num",
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        },
    )
    object_value: Optional["Construction.Object"] = field(
        default=None,
        metadata={
            "name": "Object",
            "type": "Element",
            "required": True,
        },
    )
    bimfiles: Optional["Construction.Bimfiles"] = field(
        default=None,
        metadata={
            "name": "BIMFiles",
            "type": "Element",
        },
    )

    @dataclass
    class Object:
        """
        :ivar num: Номер объекта капитального строительства
            (реконструкции, капитального ремонта)
        :ivar access_level:
        :ivar name: Наименование объекта капитального строительства
            (реконструкции, капитального ремонта)
        :ivar address: Адрес объекта капитального строительства
            (реконструкции, капитального ремонта)
        :ivar region: Территориальное расположение объекта строительства
            (регион, субъект РФ)
        :ivar sub_region: Наименование зоны субъекта Российской
            Федерации - подрайон, ценовая зона в составе основного
            региона (субъект РФ), в котором расположен объект
            строительства
        :ivar estimate: Локальный сметный расчет определения сметной
            стоимости строительства объекта капитального строительства
            (реконструкции, капитального ремонта)
        """

        num: Optional[str] = field(
            default=None,
            metadata={
                "name": "Num",
                "type": "Element",
                "required": True,
            },
        )
        access_level: Optional[TaccessLevel] = field(
            default=None,
            metadata={
                "name": "AccessLevel",
                "type": "Element",
            },
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Element",
                "required": True,
            },
        )
        address: Optional[str] = field(
            default=None,
            metadata={
                "name": "Address",
                "type": "Element",
            },
        )
        region: Optional[Tregion] = field(
            default=None,
            metadata={
                "name": "Region",
                "type": "Element",
                "required": True,
            },
        )
        sub_region: Optional[str] = field(
            default=None,
            metadata={
                "name": "SubRegion",
                "type": "Element",
            },
        )
        estimate: Optional["Construction.Object.Estimate"] = field(
            default=None,
            metadata={
                "name": "Estimate",
                "type": "Element",
                "required": True,
            },
        )

        @dataclass
        class Estimate:
            """
            :ivar guid: Глобальный уникальный идентификатор локального
                сметного расчета
            :ivar num: Номер локального сметного расчета. Номер
                локального сметного расчета (сметы) должен содержать три
                группы цифр: первые две группы цифр соответствуют номеру
                объектного сметного расчета (сметы), третья группа цифр
                - порядковому номеру локального сметного расчета (сметы)
                в объектном сметном расчете (смете).
            :ivar name: Наименование локального сметного расчета
            :ivar date: Дата составления локального сметного расчета
            :ivar industry: Отраслевая специфика
            :ivar quantity: Расчетный измеритель конструктивного решения
                (количество) на заданную единицу измерения по локальному
                сметному расчету объекта капитального строительства
                (реконструкции, капитального ремонта)
            :ivar price_per_unit: <text xmlns="">Показатель единичной
                стоимости на расчетный измеритель конструктивного
                решения по локальному сметному расчету объекта
                капитального строительства (реконструкции, капитального
                ремонта) в текущем уровне цен </text> <formula xmlns="">
                PricePerUnit (Показатель единичной стоимости на
                расчетный измеритель конструктивного решения по
                ЛСР)=Total.PriceCurrent (Всего сметная стоимость в
                текущем уровне цен)/Quantity (Объем работ (количество)
                по ЛСР на заданную единицу измерения конструктивного
                решения) </formula> <links xmlns="">Методика определения
                сметной стоимости строительства, реконструкции,
                капитального ремонта, сноса объектов капитального
                строительства, работ по сохранению объектов культурного
                наследия (памятников истории и культуры) народов
                Российской Федерации на территории Российской Федерации,
                утвержденная приказом Министерства строительства и
                жилищно-коммунального хозяйства Российской Федерации от
                4 августа 2020 г. № 421/пр. </links>
            :ivar quantity_unit: Расчетный измеритель конструктивного
                решения (измеритель) по локальному сметному расчету
                объекта капитального строительства (реконструкции,
                капитального ремонта)
            :ivar estimate_type: Тип определения сметной стоимости: 1.
                "Строительство" - определение сметной стоимости
                строительства за исключением работ по сохранению
                объектов культурного наследия (памятников истории и
                культуры) народов Российской Федерации на территории
                Российской Федерации 2. "Реставрация" - определение
                сметной стоимости работ по сохранению объектов
                культурного наследия (памятников истории и культуры)
                народов Российской Федерации на территории Российской
                Федерации.
            :ivar index_type: Тип применяемого индекса изменения сметной
                стоимости
            :ivar price_level_base: Базисный уровень цен локального
                сметного расчета
            :ivar price_level_cur: Текущий уровень цен локального
                сметного расчета
            :ivar reason: Основание для определения стоимости локального
                сметного расчета
            :ivar estimate_price: Итоговая сметная стоимость локального
                сметного расчета по элементам и видам работ
            :ivar legal: Описание данных, используемых для определения
                стоимости работ и затрат в локальном сметном расчете
                (сметные нормативы, индексы, и др.)
            :ivar signatures: Подписи исполнителей, представителей
                заказчика и подрядчика
            :ivar sections: Разделы локального сметного расчета
            """

            guid: Optional[str] = field(
                default=None,
                metadata={
                    "name": "GUID",
                    "type": "Element",
                    "pattern": r"\{[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}\}",
                },
            )
            num: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Num",
                    "type": "Element",
                    "required": True,
                },
            )
            name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Name",
                    "type": "Element",
                    "required": True,
                },
            )
            date: Optional[Tdate] = field(
                default=None,
                metadata={
                    "name": "Date",
                    "type": "Element",
                },
            )
            industry: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Industry",
                    "type": "Element",
                },
            )
            quantity: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "Quantity",
                    "type": "Element",
                },
            )
            price_per_unit: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "PricePerUnit",
                    "type": "Element",
                },
            )
            quantity_unit: Optional[str] = field(
                default=None,
                metadata={
                    "name": "QuantityUnit",
                    "type": "Element",
                },
            )
            estimate_type: Optional[EstimateEstimateType] = field(
                default=None,
                metadata={
                    "name": "EstimateType",
                    "type": "Element",
                    "required": True,
                },
            )
            index_type: Optional[EstimateIndexType] = field(
                default=None,
                metadata={
                    "name": "IndexType",
                    "type": "Element",
                    "required": True,
                },
            )
            price_level_base: Optional[TpriceLevel] = field(
                default=None,
                metadata={
                    "name": "PriceLevelBase",
                    "type": "Element",
                },
            )
            price_level_cur: Optional[TpriceLevel] = field(
                default=None,
                metadata={
                    "name": "PriceLevelCur",
                    "type": "Element",
                },
            )
            reason: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Reason",
                    "type": "Element",
                },
            )
            estimate_price: Optional[Tsummary] = field(
                default=None,
                metadata={
                    "name": "EstimatePrice",
                    "type": "Element",
                },
            )
            legal: Optional["Construction.Object.Estimate.Legal"] = field(
                default=None,
                metadata={
                    "name": "Legal",
                    "type": "Element",
                    "required": True,
                },
            )
            signatures: Optional[Tsignatures] = field(
                default=None,
                metadata={
                    "name": "Signatures",
                    "type": "Element",
                },
            )
            sections: Optional["Construction.Object.Estimate.Sections"] = (
                field(
                    default=None,
                    metadata={
                        "name": "Sections",
                        "type": "Element",
                        "required": True,
                    },
                )
            )

            @dataclass
            class Legal:
                """
                :ivar main: "Сметные нормативы"
                :ivar indexes: "Индексы изменения сметной стоимости"
                :ivar salary: "Оплата труда"
                :ivar overheads: "Накладные расходы"
                :ivar profits: "Сметная прибыль"
                """

                main: Optional[Tlegal] = field(
                    default=None,
                    metadata={
                        "name": "Main",
                        "type": "Element",
                        "required": True,
                    },
                )
                indexes: list[Tlegal] = field(
                    default_factory=list,
                    metadata={
                        "name": "Indexes",
                        "type": "Element",
                    },
                )
                salary: Optional[Tlegal] = field(
                    default=None,
                    metadata={
                        "name": "Salary",
                        "type": "Element",
                    },
                )
                overheads: Optional[Tlegal] = field(
                    default=None,
                    metadata={
                        "name": "Overheads",
                        "type": "Element",
                        "required": True,
                    },
                )
                profits: Optional[Tlegal] = field(
                    default=None,
                    metadata={
                        "name": "Profits",
                        "type": "Element",
                        "required": True,
                    },
                )

            @dataclass
            class Sections:
                """
                :ivar section: Раздел локального сметного расчета
                :ivar string: Строка содержащая справочную информацию в
                    свободной форме
                """

                section: list[
                    "Construction.Object.Estimate.Sections.Section"
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "Section",
                        "type": "Element",
                    },
                )
                string: list[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "String",
                        "type": "Element",
                    },
                )

                @dataclass
                class Section:
                    """
                    :ivar code: Номер раздела локального сметного
                        расчета
                    :ivar name: Наименование раздела локального сметного
                        расчета
                    :ivar items: Позиции раздела локального сметного
                        расчета
                    :ivar section_price: Итоговая сметная стоимость по
                        разделу локального сметного расчета по элементам
                        и видам работ
                    """

                    code: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "Code",
                            "type": "Element",
                            "required": True,
                        },
                    )
                    name: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "Name",
                            "type": "Element",
                            "required": True,
                        },
                    )
                    items: Optional[
                        "Construction.Object.Estimate.Sections.Section.Items"
                    ] = field(
                        default=None,
                        metadata={
                            "name": "Items",
                            "type": "Element",
                            "required": True,
                        },
                    )
                    section_price: Optional[Tsummary] = field(
                        default=None,
                        metadata={
                            "name": "SectionPrice",
                            "type": "Element",
                            "required": True,
                        },
                    )

                    @dataclass
                    class Items:
                        """
                        :ivar item: Позиция раздела локального сметного
                            расчета
                        :ivar string: Строка содержащая справочную
                            информацию в свободной форме
                        """

                        item: list[Titem] = field(
                            default_factory=list,
                            metadata={
                                "name": "Item",
                                "type": "Element",
                            },
                        )
                        string: list[str] = field(
                            default_factory=list,
                            metadata={
                                "name": "String",
                                "type": "Element",
                            },
                        )

    @dataclass
    class Bimfiles:
        """
        :ivar file_name: Имя IFC файла с путем относительно файла
            локальной сметы
        """

        file_name: list[str] = field(
            default_factory=list,
            metadata={
                "name": "FileName",
                "type": "Element",
            },
        )
