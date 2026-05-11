"""
Smart Logistics Dashboard — Data Generation Script
====================================================
Author  : Manish
Purpose : Automatically generate 1,000 realistic shipment records
Output  : logistics_data.csv (saved in /data folder)

Run:
    python generate_data.py
"""

import pandas as pd
import numpy as np
import random
import os

# ── Reproducibility ──────────────────────────────────────────────────────────
np.random.seed(42)
random.seed(42)

# ── Config ───────────────────────────────────────────────────────────────────
NUM_RECORDS = 1000

MONTHS = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

QUARTER_MAP = {
    "January": "Q1", "February": "Q1", "March": "Q1",
    "April": "Q2", "May": "Q2", "June": "Q2",
    "July": "Q3", "August": "Q3", "September": "Q3",
    "October": "Q4", "November": "Q4", "December": "Q4"
}

MONTH_ORDER = {m: i+1 for i, m in enumerate(MONTHS)}

TRUCKS = [f"Truck_{i}" for i in range(1, 11)]

DELAY_REASONS = ["Weather", "Traffic", "Mechanical Failure", "None"]
TRAFFIC_CONDITIONS = ["Clear", "Heavy", "Detour"]
SHIPMENT_STATUSES = ["Delivered", "Delayed", "In Transit"]


# ── Business Rules ────────────────────────────────────────────────────────────
def determine_on_time(traffic: str, delay_reason: str) -> str:
    """
    Heavy traffic → always delayed (100% delay rate).
    Other conditions → probabilistic based on delay reason.
    """
    if traffic == "Heavy":
        return "Delayed"
    if delay_reason != "None":
        return "Delayed" if random.random() > 0.25 else "On Time"
    return "On Time" if random.random() > 0.38 else "Delayed"


def generate_utilization(truck_id: str) -> float:
    """
    Truck_5 is consistently the lowest utilizer.
    Others cluster around 78–82%.
    """
    base = {
        "Truck_5": 76.6,
        "Truck_6": 79.0,
        "Truck_4": 79.1,
        "Truck_10": 79.6,
        "Truck_9": 79.9,
        "Truck_3": 80.1,
        "Truck_2": 80.2,
        "Truck_8": 80.2,
        "Truck_1": 80.5,
        "Truck_7": 80.7,
    }
    center = base.get(truck_id, 80.0)
    return round(np.clip(np.random.normal(center, 1.2), 70, 90), 1)


def generate_inventory(month: str) -> tuple:
    """
    Seasonal inventory pattern — dips in summer (May, July),
    peaks in spring (April) and autumn (October).
    """
    seasonal_level = {
        "January": 297, "February": 298, "March": 303,
        "April": 314, "May": 271, "June": 313,
        "July": 265, "August": 290, "September": 294,
        "October": 319, "November": 306, "December": 301
    }
    seasonal_surplus = {
        "January": 90, "February": 106, "March": 100,
        "April": 100, "May": 117, "June": 115,
        "July": 86, "August": 68, "September": 100,
        "October": 93, "November": 100, "December": 106
    }
    inv   = seasonal_level[month]  + random.randint(-10, 10)
    surp  = seasonal_surplus[month] + random.randint(-15, 15)
    demand = inv - surp
    return inv, demand, surp


# ── Main Generation Loop ──────────────────────────────────────────────────────
def generate_dataset(n: int = NUM_RECORDS) -> pd.DataFrame:
    records = []

    for i in range(1, n + 1):
        month   = random.choice(MONTHS)
        truck   = random.choice(TRUCKS)
        traffic = random.choice(TRAFFIC_CONDITIONS)
        delay   = random.choice(DELAY_REASONS)

        on_time   = determine_on_time(traffic, delay)
        status    = "Delivered" if on_time == "On Time" else random.choice(["Delayed", "In Transit"])
        util      = generate_utilization(truck)
        inv, dem, surp = generate_inventory(month)
        wait_time = random.randint(30, 60)

        records.append({
            "Shipment_ID":       f"SHP{str(i).zfill(4)}",
            "Month":             month,
            "Month_Order":       MONTH_ORDER[month],
            "Quarter":           QUARTER_MAP[month],
            "Truck_ID":          truck,
            "Delay_Reason":      delay,
            "Traffic_Condition": traffic,
            "On_Time_Label":     on_time,
            "Shipment_Status":   status,
            "Inventory_Level":   inv,
            "Demand":            dem,
            "Surplus":           surp,
            "Waiting_Time_Min":  wait_time,
            "Utilization_Pct":   util,
        })

    df = pd.DataFrame(records)
    # Sort by month order for cleaner visuals in Power BI
    df = df.sort_values("Month_Order").reset_index(drop=True)
    return df


# ── Save ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    output_path = os.path.join(os.path.dirname(__file__), "..", "data", "logistics_data.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print("🚚 Generating Smart Logistics dataset...")
    df = generate_dataset()
    df.to_csv(output_path, index=False)

    # ── Quick Summary ─────────────────────────────────────────────────────────
    print(f"\n✅ Dataset saved → {output_path}")
    print(f"   Total Records    : {len(df):,}")
    print(f"   On-Time Rate     : {(df['On_Time_Label']=='On Time').mean()*100:.1f}%")
    print(f"   Avg Utilization  : {df['Utilization_Pct'].mean():.1f}%")
    print(f"   Avg Wait Time    : {df['Waiting_Time_Min'].mean():.1f} min")
    print(f"   Avg Inventory    : {df['Inventory_Level'].mean():.0f}")
    print(f"   Deficit Records  : {(df['Surplus']<0).sum()}")
    print(f"\n📊 On-Time by Traffic:")
    print(df.groupby("Traffic_Condition")["On_Time_Label"]
            .value_counts(normalize=True)
            .mul(100).round(1)
            .rename("Pct")
            .to_string())
    print("\n🏁 Done. Load logistics_data.csv into Power BI Desktop.")
