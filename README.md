# 🏠 Melbourne Housing Dashboard

This project presents an interactive data analysis dashboard built using **Streamlit** and **Plotly**, focused on exploring and analyzing the Melbourne Housing dataset.

---

## 📊 Project Description

The goal of this project is to understand the factors affecting housing prices in Melbourne, Australia, through:

- **Univariate Analysis** – distribution of individual features  
- **Bivariate Analysis** – relationships between price and other variables  
- **Multivariate Analysis** – interaction between multiple variables

---

## 🧾 Dataset

The dataset used is the cleaned version of [Melbourne Housing Snapshot](https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot), containing various features like:

- `price`, `buildingarea`, `rooms`, `type`, `suburb`, `regionname`, etc.

The file used: `melb_data_clean.csv`

---
## 🧹 Data Exploration & Cleaning

- Checked data types (e.g., `date` column was stored as object)
- Summary statistics for numerical and categorical features
- Identified and handled missing values
- Converted all column names to lowercase
- Converted `date` to datetime
- Extracted `year`, `month`, `day` from `date`
- Created new column: `price per square meter`
- Removed outliers in the `price` column using the **IQR method**

---
## 📊 Data Analysis

### 🔹 Univariate Analysis:
- Distribution of:
  - `price`
  - `buildingarea`
  - `rooms`
- Pie charts for:
  - `type`
  - `rooms`

### 🔹 Bivariate Analysis:
- Correlation & scatter plots:
  - `price` vs `buildingarea`  
  - `price` vs `rooms`
- Average price by property type and region

### 🔹 Multivariate Analysis:
- Combined effect of `rooms` and `type` on `price`

---

## 💡 Insights Examples

- 🟡 `price` has a **very weak** correlation with `buildingarea` (~0.09)
- 🟢 `price` shows a **moderate positive** correlation with `rooms` (~0.50)
- 🏘️ Some suburbs and regions consistently have higher average prices

---

## 🧪 Data Preprocessing

- Split data into input features (`X`) and target (`price`)
- Split data into train/test sets
- Handled missing values:
  - `car`, `yearbuilt` → using **SimpleImputer** with `median` strategy
  - `councilarea` → using **SimpleImputer** with `most_frequent` strategy
  - `buildingarea` → using **KNNImputer**
- Encoded categorical columns:
  - **Ordinal** encoding for `type`
  - **One-Hot Encoding** for `method`
  - **Binary Encoding** for `regionname`, `councilarea`, `sellerg`
- Scaled numerical features and handled remaining outliers using **RobustScaler**


