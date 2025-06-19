import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

st.set_page_config(layout='wide', page_title='Melbourne Housing Dashboard')
st.markdown("<h1 style='text-align: center; color: white;'>Melbourne Housing Dashboard</h1>", unsafe_allow_html=True)

# Load data
df = pd.read_csv("melb_data_clean.csv", index_col=0)

# Sidebar navigation
page = st.sidebar.selectbox("Select Page", ["Home", "Univariate Analysis", "Bivariate Analysis", "Multivariate Analysis"])

# ---- Home Page ----
if page == "Home":
    st.title("Melbourne Housing Dataset Overview")
    st.dataframe(df)

# ---- Univariate Analysis ----
elif page == "Univariate Analysis":
    st.title("Univariate Analysis")

    st.subheader("What is the distribution of building area?")
    st.plotly_chart(px.histogram(df, x='buildingarea'))

    st.subheader("What is the distribution of prices?")
    st.plotly_chart(px.histogram(df, x='price', title='Distribution of Prices'))

    st.subheader("What is the distribution of Rooms?")
    st.plotly_chart(px.pie(data_frame=df, names='rooms', title='Distribution of Rooms'))

    st.subheader("What is the percentage of types?")
    st.plotly_chart(px.pie(data_frame=df, names='type', title='Percentage of Property Types'))

# ---- Bivariate Analysis ----
elif page == "Bivariate Analysis":
    st.title("Bivariate Analysis")

    # --- Price vs Building Area ---
    st.subheader("What is the relationship between Price and BuildingArea?")
    corr1 = df[['buildingarea', 'price']].corr()
    st.write("Correlation between Price and BuildingArea:")
    st.dataframe(corr1)
    st.plotly_chart(px.imshow(corr1, text_auto=True, title="Correlation Heatmap: Price vs BuildingArea"))
    st.plotly_chart(px.scatter(df, x='price', y='buildingarea', title='Price vs BuildingArea'))
    st.markdown("""
    **Insight:** The correlation between Price and BuildingArea is very weak (~0.09),
    indicating that building area does not significantly affect property prices in this dataset.
    The scatter plot confirms this with no clear upward or downward trend.
    """)

    # --- Rooms vs Price ---
    st.subheader("What is the relationship between number of rooms and price?")
    corr2 = df[['rooms', 'price']].corr()
    st.write("Correlation between Rooms and Price:")
    st.dataframe(corr2)
    st.plotly_chart(px.imshow(corr2, text_auto=True, title="Correlation Heatmap: Rooms vs Price"))
    st.plotly_chart(px.scatter(df, x='rooms', y='price', title='Rooms vs Price'))
    st.markdown("""
    **Insight:** There is a moderate positive correlation between number of rooms and price (~0.50),
    suggesting that properties with more rooms tend to be more expensive.
    This is supported by the upward trend in the scatter plot.
    """)

    # --- Type vs Average Price ---
    st.subheader("What is the average price for each property type?")
    avg_type_price = df.groupby('type')['price'].mean().reset_index()
    st.plotly_chart(px.bar(avg_type_price, x='type', y='price', title='Average Price per Property Type'))

    # --- Type vs Rooms ---
    st.subheader("What is the average number of rooms per property type?")
    avg_rooms = df.groupby('type')['rooms'].mean().reset_index()
    st.plotly_chart(px.bar(avg_rooms, x='type', y='rooms', title='Average Number of Rooms by Property Type'))

    # --- Region vs Land Size ---
    st.subheader("How much is the average land size by region?")
    avg_land_region = df.groupby('regionname')['landsize'].mean().reset_index()
    st.plotly_chart(px.bar(avg_land_region, x='regionname', y='landsize', 
                           title='Average Land Size by Region'))

    # --- Method Pie Chart ---
    st.subheader("How many properties sold using each sale method?")
    method_counts = df['method'].value_counts()
    st.plotly_chart(px.pie(values=method_counts.values, names=method_counts.index, 
                           title='Distribution of Sale Methods'))

    # --- Suburb vs Price ---
    st.subheader("Does the suburb affect the selling price?")
    avg_price_by_suburb = df.groupby('suburb')['price'].mean().sort_values(ascending=False).head(10).reset_index()
    st.plotly_chart(px.bar(avg_price_by_suburb, x='suburb', y='price', 
                           title='Average Price in Top 10 Suburbs'))

# ---- Multivariate Analysis ----
elif page == "Multivariate Analysis":
    st.title("Multivariate Analysis")

    st.subheader("How does Price vary by Rooms and Type?")
    price_by_rooms_type = df.groupby(['rooms', 'type'])['price'].mean().reset_index()
    st.plotly_chart(px.bar(data_frame=price_by_rooms_type, x='rooms', y='price', 
                           title='Price Variation by Rooms and Type',
                           text_auto=True, color='type', barmode='group'))
