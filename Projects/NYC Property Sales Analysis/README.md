# 🏙️ NYC Property Sales Analysis

This project explores property sales data in New York City to uncover insights into real estate trends, pricing patterns, neighborhood dynamics, and property characteristics. Using Exploratory Data Analysis (EDA), we clean and visualize the data to better understand the factors influencing property values across the five boroughs of NYC.

---

## 📁 Dataset

- **Source**: [NYC Open Data](https://www.kaggle.com/datasets/new-york-city/nyc-property-sales)
- **File Used**: `nyc-rolling-sales.csv`
- **Size**: ~85,000 property transactions
- **Features**:
  - BOROUGH, NEIGHBORHOOD
  - BUILDING CLASS CATEGORY
  - GROSS SQUARE FEET, LAND SQUARE FEET
  - YEAR BUILT, SALE DATE, SALE PRICE

---

## 🎯 Project Goals

- Clean and preprocess raw property sales data
- Perform exploratory data analysis (EDA)
- Visualize trends in sale prices and sales volume
- Discover how location, square footage, and building class affect price
- Identify most and least expensive neighborhoods
- Lay the foundation for further predictive modeling and geospatial analysis

---

## ✅ Key Steps & Techniques

### 1. 🧹 Data Cleaning
- Removed rows with missing or zero `SALE PRICE`
- Converted `SALE PRICE`, `SALE DATE`, and square footage columns to proper formats
- Removed outliers and non-informative entries (e.g., $0 sales)

### 2. 📊 Exploratory Data Analysis (EDA)
- **Sale Price Distribution**: Visualized spread of property prices and removed extreme outliers
- **Monthly Trends**: Analyzed median sale price and sales volume over time
- **Borough Comparison**: Compared number of sales and average prices across boroughs
- **Size vs Price**: Investigated how `GROSS SQUARE FEET` impacts property value
- **Top Neighborhoods**: Identified most expensive areas in NYC

---

## 🧠 Insights & Findings

- **Manhattan** consistently has the highest average sale prices.
- **Brooklyn** and **Queens** show strong activity in mid-range property sales.
- Larger properties generally sell for more, but the correlation varies by location.
- Certain neighborhoods stand out with unusually high prices (e.g., Tribeca, SoHo).

---

## 📌 Future Work

- 🔮 **Predictive Modeling**: Use regression or machine learning to predict property prices
- 🗺️ **Geospatial Mapping**: Use Folium or Plotly to map property locations and prices
- 📈 **Dashboarding**: Build an interactive Streamlit or Tableau dashboard
- 🏠 **Feature Engineering**: Use building class, age, and zip code for deeper analysis

---

## 🧰 Tools & Technologies

- Python (Pandas, Matplotlib, Seaborn)
- Jupyter Notebook
- Data Visualization & EDA techniques
- (Optional in future: Scikit-learn, Folium, Streamlit)

---

## 👨‍💼 Who Can Use This?

This project is ideal for:
- **Aspiring Data Analysts/Scientists** to showcase skills in EDA
- **Real Estate Professionals** for market understanding
- **Urban Planners** to study property distribution
- **Investors** looking for data-driven insights

---

## 📂 Project Structure

📁 NYC_Property_Sales_Analysis/
├── nyc-rolling-sales.csv
├── NYC_Property_EDA.ipynb
├── README.md
└── (Optional) /images/