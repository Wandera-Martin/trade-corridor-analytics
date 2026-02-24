# 🚛 Northern Corridor Trade Analytics

### Data Science Project | Corridor Efficiency & Delay Intelligence


## 📌 Project Overview

This project analyzes operational shipment data from the **Mombasa → Malaba → Kampala trade corridor**, one of East Africa’s most critical logistics routes.

Trade corridors are essential economic arteries. Delays at ports and borders increase transport costs, inflate consumer prices, reduce export competitiveness, and weaken regional trade efficiency.

This project applies **data science and analytics techniques** to understand:

* Border clearance behavior
* Delay patterns
* Operational bottlenecks
* Economic impact of inefficiencies
* Predictive delay risk

The goal is to transform corridor movement data into actionable intelligence.


## 🎯 Problem Statement

Border delays and transit inefficiencies increase the cost of trade for landlocked countries like Uganda.

However, corridor performance is often:

* Poorly monitored
* Reactively managed
* Not data-driven
* Lacking predictive insights

This project answers:

> How can shipment-level data be used to measure, explain, and predict corridor performance?


## 🧠 Core Analysis Questions

The analysis is structured around four categories:

### 1️⃣ Descriptive (What is happening?)

* What is the average border clearance time?
* What is the overall delay rate?
* Which goods categories experience the highest delays?
* What are monthly shipment volume trends?


### 2️⃣ Diagnostic (Why is it happening?)

* Does rainfall increase clearance times?
* Are certain days of the week more delay-prone?
* Is there a relationship between shipment volume and delay frequency?
* What are the most common delay reasons?


### 3️⃣ Predictive (What will happen?)

* Can we predict whether a shipment will be delayed?
* Can we forecast high-delay days?
* Which factors most influence delay probability?


### 4️⃣ Prescriptive (What should be done?)

* What operational improvements would reduce delays most?
* What is the estimated economic savings if clearance time decreases by 2 hours?
* Which goods categories should be prioritized for intervention?


## 📊 Dataset Description

### Type: Synthetic Operational Shipment Dataset

### Corridor: Mombasa → Malaba → Kampala

### Size: 1,000 shipments

Because real shipment-level border data is not publicly accessible due to security and commercial sensitivity, a **realistic synthetic dataset** was generated.

This approach is common in professional portfolios when:

* Real-world operational data is proprietary
* Access is restricted
* Privacy concerns apply

The dataset simulates realistic logistics behavior including skewed clearance distributions, operational delays, and weather influence.


### Dataset Fields

| Column                   | Description                                |
| ------------------------ | ------------------------------------------ |
| shipment_id              | Unique shipment identifier                 |
| truck_id                 | Truck identifier                           |
| origin_port              | Port of departure (Mombasa)                |
| border                   | Border crossing point (Malaba)             |
| destination              | Final destination (Kampala)                |
| depart_time              | Departure timestamp                        |
| border_arrival_time      | Arrival at border                          |
| border_exit_time         | Clearance completion time                  |
| arrival_time             | Final arrival time                         |
| goods_category           | Type of goods transported                  |
| weight_kg                | Shipment weight                            |
| declared_value_usd       | Cargo declared value                       |
| fuel_price_usd_per_litre | Fuel price at time of shipment             |
| rainfall_indicator       | Weather condition (0 = no rain, 1 = rain)  |
| delay_reason             | Operational cause of delay (if applicable) |


## 🔍 Derived Features

During feature engineering, additional metrics were created:

* `clearance_hours`
* `total_transit_hours`
* `is_delayed` (clearance > 12 hours)
* `month`
* `day_of_week`
* `delay_cost_usd` (simulated economic impact)


## 🏗 Analytical Approach

The project follows a structured data science workflow:

1. Data Understanding & Validation
2. Feature Engineering
3. Exploratory Data Analysis (EDA)
4. Statistical Relationship Analysis
5. Delay Cost Simulation
6. Optional Predictive Modeling
7. Business Insight & Recommendation Layer


## 📈 Key Metrics

* Average Border Clearance Time
* Delay Rate (%)
* Monthly Shipment Volume
* Delay Rate by Goods Category
* Clearance Time Distribution
* Estimated Economic Cost of Delays


## 💰 Economic Impact Simulation

To demonstrate policy relevance, a cost-of-delay model was introduced:

Assumption:
Each additional clearance hour costs $150 per truck.

This enables estimation of:

* Total corridor delay cost
* Potential savings from efficiency improvements
* Cost-benefit scenarios


## 🛠 Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib / Seaborn
* Plotly
* Scikit-learn (optional predictive modeling)
* Jupyter Notebook

## 📁 Project Structure

```
trade-corridor-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_eda_analysis.ipynb
│   └── 04_modeling.ipynb
│
├── src/
│
├── reports/
│   ├── figures/
│   └── executive_summary.md
│
├── requirements.txt
└── README.md
```

## 🚀 Why This Project Matters

Trade corridors directly affect:

* National inflation
* Fuel prices
* Export competitiveness
* Regional integration
* Government revenue

By transforming operational shipment data into analytics insights, this project demonstrates how data science can:

* Improve logistics performance
* Support economic policy decisions
* Enable predictive corridor monitoring
* Quantify inefficiency costs

## 📌 Future Extensions

* Real GPS tracking integration
* Time-series delay forecasting
* Anomaly detection for corruption risk
* Corridor performance scoring system
* Interactive dashboard deployment (Streamlit / Power BI)


## 👤 Author

Martin Wandera
-----
Data Science & Trade Analytics
