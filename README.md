# 🚚 Smart Logistics Dashboard — Power BI Project

> An end-to-end logistics intelligence dashboard built with **Power BI Desktop**.  
> Dataset generated using **Python (pandas + numpy)** — 1,000 shipments × 26 columns.

---

## 📊 Dashboard Pages

| Page | Description |
|------|-------------|
| **Overview** | Total shipments, on-time rate, utilization, waiting time KPIs |
| **Delivery** | Delay reasons, traffic impact, shipment status, revenue at risk |
| **Truck Utilization** | Per-truck utilization %, delays per truck, monthly trend |
| **Inventory** | Surplus/deficit analysis, monthly inventory vs demand |
| **Wait Time** | Avg wait by truck and traffic condition, monthly trend |

---

## 🔑 Key Metrics (from real dataset)

| Metric | Value |
|--------|-------|
| Total Shipments | 1,000 |
| On-Time Rate | 43.4% |
| Delayed Shipments | 566 (56.6%) |
| Avg Truck Utilization | 79.6% |
| Avg Waiting Time | 35 min |
| Revenue at Risk | ₹1,70,000 |
| Predicted On-Time % | 74.6% |
| Stock Sufficient Rate | 73.9% |
| Worst Inventory Shortage | -185 units |

---

## 📁 Project Structure

```
smart-logistics-dashboard/
│
├── 📂 data/
│   ├── SmartLogistics_Clean.csv    # Real dataset (1,000 rows × 26 columns)
│   └── data_dictionary.md          # All 26 column descriptions
│
├── 📂 docs/
│   ├── project_story.md            # How Python + Power BI built this project
│   └── dax_measures.md             # All DAX formulas used
│
├── 📂 screenshots/
│   ├── overview.png
│   ├── delivery.png
│   ├── truck_utilization.png
│   ├── inventory.png
│   └── wait_time.png
│
├── 📂 src/
│   └── generate_data.py            # Python script that generated the dataset
│
└── README.md
```

---

## 📸 Screenshots

### Overview
![Overview](screenshots/overview.png)

### Delivery Performance
![Delivery](screenshots/delivery.png)

### Truck Utilization
![Truck Util](screenshots/truck_utilization.png)

### Inventory
![Inventory](screenshots/inventory.png)

### Wait Time
![Wait Time](screenshots/wait_time.png)

---

## 💡 Key Insights

| # | Insight |
|---|---------|
| 1 | Only **43.4% shipments on time** — industry benchmark is 85%+ |
| 2 | **Heavy traffic = 100% delay rate** across all 327 heavy-traffic shipments |
| 3 | Weather is the top delay cause (**267 cases**), followed by Traffic (236) and Mechanical Failure (234) |
| 4 | **Truck_10** has the most delays (68) — route/driver investigation needed |
| 5 | **Q1** has the worst inventory deficit rate (28.5%) |
| 6 | Truck_1 and Truck_3 have the highest average wait time (**37 min**) |
| 7 | **₹1.7 Lakh revenue at risk** from current delay rate |
| 8 | ML model predicts **74.6% on-time rate** — 31% improvement potential |

---

## 🛠️ Tech Stack

| Tool | Use |
|------|-----|
| 🐍 Python (pandas, numpy) | Dataset generation & automation |
| 📊 Power BI Desktop | Dashboard & visualizations |
| 📐 DAX | 20+ custom KPI measures |
| 🔄 Power Query (M) | Data cleaning & transformation |
| 🗺️ Power BI Map Visual | Geospatial delivery mapping |

---

## 🚀 How to Run

**Reproduce the dataset:**
```bash
cd src
pip install pandas numpy
python generate_data.py
# Output: ../data/SmartLogistics_Clean.csv
```

**Open the dashboard:**
1. Open `src/SmartLogisticsDashboard.pbix` in Power BI Desktop
2. Update data source to point to `data/SmartLogistics_Clean.csv`
3. Refresh and explore all 5 pages

---

## 📖 Read the Full Story

See [`docs/project_story.md`](docs/project_story.md) for the complete journey —  
how Python automated the data, and how Power BI turned it into a story.

---

*Made by Manish · Connect on [LinkedIn](https://linkedin.com) · [GitHub](https://github.com)*
