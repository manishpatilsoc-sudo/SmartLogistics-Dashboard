# 📖 Data Dictionary — SmartLogistics_Clean.csv

Full column reference for the actual dataset used in this Power BI project.  
**1,000 rows × 26 columns**

---

## 📅 Date & Time Columns

| Column | Data Type | Description | Example |
|--------|-----------|-------------|---------|
| `Datetime` | DateTime | Full timestamp of the shipment | 2024-03-20 00:11:14 |
| `Date` | Date | Date only | 2024-03-20 |
| `Month_Name` | Text | Month + Year label | Mar 2024 |
| `Month_Num` | Text | Year-Month for sorting | 2024-03 |
| `Quarter` | Text | Quarter of the year | Q1 |
| `Day_Of_Week` | Text | Day name | Wednesday |
| `Hour` | Number | Hour of shipment (0–23) | 0 |

---

## 🚚 Truck & Route Columns

| Column | Data Type | Description | Example |
|--------|-----------|-------------|---------|
| `Truck_ID` | Text | Truck name | Truck_7 |
| `Truck_Number` | Number | Numeric truck ID | 7 |
| `Latitude` | Decimal | Delivery location latitude | -65.7383 |
| `Longitude` | Decimal | Delivery location longitude | 11.2497 |

---

## 📦 Shipment & Delay Columns

| Column | Data Type | Description | Example |
|--------|-----------|-------------|---------|
| `Shipment_Status` | Text | Current status | Delivered / Delayed / In Transit |
| `On_Time_Label` | Text | On-time classification | On Time / Delayed |
| `Is_Delayed` | Number | Binary delay flag (1 = delayed) | 1 |
| `Delay_Reason` | Text | Cause of delay (blank if on time) | Weather / Traffic / Mechanical Failure |
| `Traffic_Condition` | Text | Road condition at time of delivery | Clear / Heavy / Detour |

---

## 🌡️ Environment Columns

| Column | Data Type | Description | Example |
|--------|-----------|-------------|---------|
| `Temperature` | Decimal | Temperature (°C) at delivery point | 27.0 |
| `Humidity` | Decimal | Humidity % at delivery point | 67.8 |

---

## ⏱️ Wait Time & Utilization

| Column | Data Type | Description | Example |
|--------|-----------|-------------|---------|
| `Waiting_Time_Min` | Number | Truck wait time at dock (minutes) | 38 |
| `Utilization_Pct` | Decimal | Truck load utilization % | 60.1 |

---

## 📦 Inventory Columns

| Column | Data Type | Description | Example |
|--------|-----------|-------------|---------|
| `Inventory_Level` | Number | Stock available at the time | 390 |
| `Demand_Forecast` | Number | Forecasted demand for the period | 285 |
| `Inventory_Surplus` | Number | Inventory − Demand (negative = deficit) | 105 |
| `Inventory_Status` | Text | Stock status | Surplus / Deficit |

---

## 💰 Business Columns

| Column | Data Type | Description | Example |
|--------|-----------|-------------|---------|
| `Transaction_Amount` | Number | Revenue value of the shipment (₹) | 320 |
| `Purchase_Frequency` | Number | How often this customer orders | 4 |

---

## 📌 Key Notes

- `Delay_Reason` is **blank/NaN for on-time shipments** (263 nulls = on-time shipments with no delay cause)
- `Heavy` traffic has a **100% delay rate** — every single heavy-traffic shipment was delayed
- `Inventory_Surplus` can be negative — that means demand exceeded stock (deficit)
- `Latitude` / `Longitude` can be used for a **Power BI Map visual** to show delivery locations
- `Temperature` and `Humidity` can be correlated against `Weather` delays
- `Hour` and `Day_Of_Week` enable **time-of-day / weekday delay pattern analysis**
- `Transaction_Amount` is the basis for calculating **Revenue at Risk**

---

## 🔗 Suggested Power BI Star Schema

| Dimension Table | Columns to Extract |
|----------------|-------------------|
| `Dim_Date` | Datetime, Date, Month_Name, Month_Num, Quarter, Day_Of_Week, Hour |
| `Dim_Truck` | Truck_ID, Truck_Number |
| `Dim_Traffic` | Traffic_Condition |
| `Dim_Location` | Latitude, Longitude |
| `Fact_Shipments` | Everything else |
