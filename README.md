# 🚛 Trade Corridor Delay Risk Prediction

### Predictive Analytics for Border Operations (Mombasa → Malaba → Kampala)

## 📌 Overview

Border delays increase logistics costs, slow down trade, and create inefficiencies across supply chains—especially for landlocked countries.

This project demonstrates how **data analytics and machine learning** can be used to predict shipment delay risk along a trade corridor.

Using a simulated dataset representing shipments moving from **Mombasa Port → Malaba Border → Kampala**, the project builds a full analytics pipeline including:

- Data validation
    
- Feature engineering
    
- Exploratory analysis
    
- Time-series trend analysis
    
- Machine learning delay prediction
    

The goal is to move from **reactive reporting → proactive risk prediction**.



# 🎯 Problem Statement

Border operations often identify congestion **after delays occur**.

The key question addressed in this project:

> Can we predict shipment delays before they happen using operational and environmental signals?

If successful, such predictions could help corridor operators allocate resources more efficiently and reduce economic losses from congestion.



# 📊 Dataset

A **synthetic but realistic dataset** simulates operational shipment data across the Northern Corridor.

Each record represents a shipment with:

- Shipment identifiers
    
- Transport timestamps
    
- Cargo characteristics
    
- Environmental conditions
    
- Delay reasons
    

### Example features

|Feature|Description|
|---|---|
|depart_time|Shipment departure timestamp|
|clearance_hours|Border clearance duration|
|goods_category|Type of cargo|
|weight_kg|Shipment weight|
|fuel_price_usd_per_litre|Fuel market signal|
|rainfall_indicator|Weather condition|
|delay_reason|Operational delay cause|



# 🧠 Feature Engineering

Key features were engineered to capture corridor behavior:

### Operational Metrics

- `clearance_hours`
    
- `travel_to_border_hours`
    
- `total_transit_hours`
    

### Time-Based Signals

- `depart_month`
    
- `depart_hour`
    
- `day_of_week`
    
- `is_weekend`
    

### Shipment Characteristics

- `is_heavy`
    
- `is_high_value`
    

### Congestion Indicators

- `rolling_delay_rate_30`
    
- `rolling_clearance_mean_30`
    

These features allow the model to capture **operational congestion patterns**.

---

# 📈 Exploratory Analysis

The analysis identified several key insights:

### Clearance Time Distribution

Most shipments clear quickly, but a **long tail of extreme delays** exists.

### Delay Drivers

Higher delay probability is associated with:

- rainfall conditions
    
- heavier shipments
    
- congestion momentum
    
- peak operating hours
    

### Time Trends

Trend analysis revealed:

- seasonal congestion variation
    
- weekly operational patterns
    
- rolling congestion signals
    

Example visualizations include:

- delay rate by cargo category
    
- rainfall impact on clearance time
    
- rolling congestion trends
    
- delay reason distributions
    



# 🤖 Machine Learning Model

Two models were evaluated:

|Model|Purpose|
|---|---|
|Logistic Regression|Baseline classifier|
|Random Forest|Nonlinear ensemble model|

Evaluation metrics:

- Accuracy
    
- Precision
    
- Recall
    
- F1 Score
    
- ROC AUC
    

### Evaluation Strategy

A **time-based train/test split** was used to simulate real deployment:

- Train on historical shipments
    
- Test on future shipments
    

This avoids temporal data leakage.



# 📊 Results

The **Random Forest model** achieved the best performance.

Key findings:

- Delay probability is strongly influenced by **historical congestion momentum**
    
- Environmental conditions (rainfall) affect clearance time
    
- Operational timing (hour/day) impacts delay likelihood
    

The model produces a **delay risk probability score** between 0 and 1.

-

# 🎯 Operational Use Case

The predicted risk score can support proactive corridor management.

Example use cases:

- Allocate additional customs officers during high-risk periods
    
- Increase scanning capacity on predicted congestion days
    
- Prioritize high-value shipments
    
- Monitor corridor congestion signals in real time
    

This transforms border management from **reactive → predictive operations**.

---

# 🛠 Tech Stack

Python  
Pandas  
NumPy  
Scikit-learn  
Matplotlib  
Seaborn

Machine Learning Techniques:

- Feature engineering
    
- Time-based model evaluation
    
- Classification modeling
    
- Feature importance analysis
    
- Probability threshold tuning
    

---

# 📂 Project Structure

trade-corridor-analytics  
│  
├── data  
│   ├── raw  
│   └── processed  
│  
├── notebooks  
│   ├── 01_data_validation.ipynb  
│   ├── 02_feature_engineering.ipynb  
│   ├── 03_eda_analysis.ipynb  
│   └── 04_modeling.ipynb  
│  
├── reports  
│   ├── figures  
│   └── models  
│  
└── README.md

---

# 🚀 Future Improvements

Potential extensions include:

- Real-time shipment tracking integration
    
- Walk-forward validation for time-series modeling
    
- Model drift detection
    
- Deployment as a delay-risk prediction API
    
- Interactive analytics dashboard
    

---

# 📌 Key Takeaways

This project demonstrates how data science can support:

- logistics optimization
    
- border operations management
    
- infrastructure analytics
    
- predictive decision-making
    

The approach can be extended to **real-world trade corridors and supply chain systems**.

---

# 👤 Author

Martin Wandera

Data Engineering | Data Science | AI Systems
