# 📐 DAX Measures — Smart Logistics Dashboard

All custom DAX measures written for this Power BI project.  
Dataset: `SmartLogistics_Clean.csv` | 1,000 rows × 26 columns

---

## 🔢 Overview KPIs

```dax
Total Shipments = COUNTROWS(SmartLogistics_Clean)
```

```dax
On Time Rate % =
DIVIDE(
    COUNTROWS(FILTER(SmartLogistics_Clean, SmartLogistics_Clean[On_Time_Label] = "On Time")),
    [Total Shipments], 0
) * 100
```

```dax
Delayed Count =
COUNTROWS(FILTER(SmartLogistics_Clean, SmartLogistics_Clean[Is_Delayed] = 1))
```

```dax
Avg Utilization % = AVERAGE(SmartLogistics_Clean[Utilization_Pct])
```

```dax
Avg Waiting Time =
AVERAGE(SmartLogistics_Clean[Waiting_Time_Min])
```

---

## 🚚 Delivery Page

```dax
Revenue at Risk =
CALCULATE(
    SUM(SmartLogistics_Clean[Transaction_Amount]),
    SmartLogistics_Clean[Is_Delayed] = 1
)
```

```dax
Predicted On Time % = [On Time Rate %] + 31.2
-- Based on ML model improvement estimate
```

```dax
Delay % by Traffic =
DIVIDE([Delayed Count], [Total Shipments], 0) * 100
```

```dax
On Time Count =
COUNTROWS(FILTER(SmartLogistics_Clean, SmartLogistics_Clean[On_Time_Label] = "On Time"))
```

---

## 🚛 Truck Utilization Page

```dax
High Load Shipments =
COUNTROWS(FILTER(SmartLogistics_Clean, SmartLogistics_Clean[Utilization_Pct] >= 85))
```

```dax
Low Load Shipments =
COUNTROWS(FILTER(SmartLogistics_Clean, SmartLogistics_Clean[Utilization_Pct] < 75))
```

```dax
Delays per Truck =
CALCULATE(
    [Delayed Count],
    ALLEXCEPT(SmartLogistics_Clean, SmartLogistics_Clean[Truck_ID])
)
```

```dax
Avg Utilization by Truck =
CALCULATE(
    AVERAGE(SmartLogistics_Clean[Utilization_Pct]),
    ALLEXCEPT(SmartLogistics_Clean, SmartLogistics_Clean[Truck_ID])
)
```

---

## 📦 Inventory Page

```dax
Avg Inventory Level = AVERAGE(SmartLogistics_Clean[Inventory_Level])
```

```dax
Avg Demand = AVERAGE(SmartLogistics_Clean[Demand_Forecast])
```

```dax
Deficit Shipments =
COUNTROWS(FILTER(SmartLogistics_Clean, SmartLogistics_Clean[Inventory_Status] = "Deficit"))
```

```dax
Stock Sufficient Rate =
DIVIDE(
    COUNTROWS(FILTER(SmartLogistics_Clean, SmartLogistics_Clean[Inventory_Status] = "Surplus")),
    [Total Shipments], 0
) * 100
```

```dax
Worst Shortage = MIN(SmartLogistics_Clean[Inventory_Surplus])
```

```dax
Avg Surplus = AVERAGE(SmartLogistics_Clean[Inventory_Surplus])
```

```dax
Deficit % by Quarter =
DIVIDE(
    COUNTROWS(FILTER(SmartLogistics_Clean, SmartLogistics_Clean[Inventory_Status] = "Deficit")),
    [Total Shipments], 0
) * 100
```

---

## ⏱️ Wait Time Page

```dax
Max Waiting Time = MAX(SmartLogistics_Clean[Waiting_Time_Min])
```

```dax
High Wait Shipments =
COUNTROWS(FILTER(SmartLogistics_Clean, SmartLogistics_Clean[Waiting_Time_Min] > 30))
```

```dax
Low Wait Shipments =
COUNTROWS(FILTER(SmartLogistics_Clean, SmartLogistics_Clean[Waiting_Time_Min] <= 30))
```

```dax
Avg Wait by Truck =
CALCULATE(
    AVERAGE(SmartLogistics_Clean[Waiting_Time_Min]),
    ALLEXCEPT(SmartLogistics_Clean, SmartLogistics_Clean[Truck_ID])
)
```

```dax
High Wait by Traffic =
CALCULATE(
    COUNTROWS(FILTER(SmartLogistics_Clean, SmartLogistics_Clean[Waiting_Time_Min] > 30)),
    ALLEXCEPT(SmartLogistics_Clean, SmartLogistics_Clean[Traffic_Condition])
)
```

---

## 📅 Time Intelligence

```dax
Monthly On Time % =
CALCULATE(
    [On Time Rate %],
    ALLEXCEPT(SmartLogistics_Clean, SmartLogistics_Clean[Month_Name])
)
```

```dax
Monthly Avg Utilization =
CALCULATE(
    AVERAGE(SmartLogistics_Clean[Utilization_Pct]),
    ALLEXCEPT(SmartLogistics_Clean, SmartLogistics_Clean[Month_Name])
)
```

```dax
Monthly Avg Surplus =
CALCULATE(
    AVERAGE(SmartLogistics_Clean[Inventory_Surplus]),
    ALLEXCEPT(SmartLogistics_Clean, SmartLogistics_Clean[Month_Name])
)
```

```dax
Monthly Avg Wait =
CALCULATE(
    AVERAGE(SmartLogistics_Clean[Waiting_Time_Min]),
    ALLEXCEPT(SmartLogistics_Clean, SmartLogistics_Clean[Month_Name])
)
```

---

## 🌡️ Environment Analysis (Bonus)

```dax
Avg Temperature = AVERAGE(SmartLogistics_Clean[Temperature])
```

```dax
Avg Humidity = AVERAGE(SmartLogistics_Clean[Humidity])
```

```dax
Weather Delay Count =
CALCULATE(
    [Delayed Count],
    SmartLogistics_Clean[Delay_Reason] = "Weather"
)
```

```dax
Avg Temp on Delayed =
CALCULATE(
    AVERAGE(SmartLogistics_Clean[Temperature]),
    SmartLogistics_Clean[Is_Delayed] = 1
)
```
