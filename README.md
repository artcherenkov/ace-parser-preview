```bash

xsltproc xml/sort-attributes.xsl xml/schema.xsd > xml/schema-beautified.xsd
```

### Данные для расчета DTO EstimateSummary

##### Для справки

###### Основные элементы оплаты труда и заработной платы
- **WorkersSalary**.PriceBase = `Σ(Item.PriceParametersBase.WorkersSalary)`
- WorkersSalary.PriceCurrent = `Σ(Item.PriceParametersPrice.WorkersSalary)`
- **MachinistSalary**.PriceBase = `Σ(Item.PriceParametersBase.MachinistSalary)`
- MachinistSalary.PriceCurrent = `Σ(Item.PriceParametersPrice.MachinistSalary)`
- **_Salary_** = `WorkersSalary + MachinistSalary`

###### Машины и механизмы
- **MachinistSalaryExtra**.PriceBase = `Σ(Item.Resources.Machine.PriceTotalBase)`
- MachinistSalaryExtra.PriceCurrent = `Σ(Item.Resources.Machine.PriceTotalCur)`
- **Machines**.PriceBase = `Σ(Item.PriceParametersBase.Machines)`
- Machines.PriceCurrent = `Machines.PriceBase * PriceIndex`
- **_MachinesTotal_** = `Machines + MachinistSalaryExtra`

###### Материалы
- **_Materials_**.PriceBase = `Σ(Item.PriceParametersBase.Materials)`
- Materials.PriceCurrent = `Materials.PriceBase * PriceIndex`

###### Накладные расходы и прибыль
- **_Overhead_**.PriceBase = `Σ(Item.OverheadsBase.OverheadBase.Price.Base)`
- Overhead.PriceCurrent = `Σ(Item.OverheadsBase.OverheadBase.Price.Price)`
- **_Profit_**.PriceBase = `Σ(Item.ProfitsBase.ProfitBase.Price.Base)`
- Profit.PriceCurrent = `Σ(Item.ProfitsBase.ProfitBase.Price.Price)`

###### Перевозка
- **Transport**.PriceBase = `Σ(Item.PriceParameters.Totals.Base.Total)` [для типа ФССЦпг]
- Transport.PriceCurrent = `Σ(Item.PriceParameters.Totals.Price.Total)` [для типа ФССЦпг]
- **TransportAdd**.PriceBase = `Σ(Item.PriceParameters.Totals.Base.Total)` [для доп. перевозки]
- TransportAdd.PriceCurrent = `Σ(Item.PriceParameters.Totals.Price.Total)` [для доп. перевозки]
- **_TransportTotal_** = `Transport + TransportAdd`

###### Затраты труда
- LaborCosts = `Σ(Затраты труда рабочих по позициям)`
- MachinistLaborCosts = `Σ(Затраты труда машинистов по позициям)`
- **_TotalLaborCosts_** = `LaborCosts + MachinistLaborCosts`

#### Итоговые показатели
##### Прямые затраты
- **Direct** = `WorkersSalary + Machines + Materials + Transport + TransportAdd`

##### Общая стоимость (для индексов к элементам ПЗ)
- **Total** = `WorkersSalary + MachinesTotal + Materials + Overhead + Profit + TransportAdd`

##### Итоговая сметная стоимость
- **Price** = `WorkersSalary + MachinesTotal + Materials + Overhead + Profit + TransportAdd`
