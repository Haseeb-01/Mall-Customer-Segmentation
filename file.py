import streamlit as st
import pickle
import numpy as np

# Load pre-trained K-Means model
kmeans = pickle.load(open("k_means.pkl", 'rb')) 

# Cluster Descriptions
cluster_descriptions = {
    0: "🟠 **Cluster 0:** Customers with **medium income** and **medium spend**.",
    1: "🔵 **Cluster 1:** Customers with **high income** and **high spend**. 💳",
    2: "🟢 **Cluster 2:** Customers with **low income** but **high spend**. 🛍️",
    3: "🔴 **Cluster 3:** Customers with **high income** but **low spend**. 💰",
    4: "⚫ **Cluster 4:** Customers with **low income** and **low spend**."
}

# Streamlit App UI Enhancements
st.set_page_config(page_title="Customer Segmentation", page_icon="🛒", layout="wide")

# Main Title
st.markdown("<h1 style='text-align: center; color: #FF5733;'>Mall Customer Segmentation 🏬</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #333;'>Predict the customer segment based on spending behavior.</p>", unsafe_allow_html=True)

# Sidebar for User Input
st.sidebar.header("🔢 Enter Customer Details")
annual_income = st.sidebar.slider("💰 Annual Income ($)", 0, 200, 50)
spending_score = st.sidebar.slider("📊 Spending Score", 0, 100, 50)

# Predict Cluster
if st.sidebar.button("🔮 Predict Cluster"):
    user_data = np.array([[annual_income, spending_score]])
    predicted_cluster = kmeans.predict(user_data)[0]

    # Display result in a nice format
    st.markdown(f"<h2 style='color: #FF5733;'>🎯 Prediction Result</h2>", unsafe_allow_html=True)
    st.success(f"The customer belongs to **Cluster {predicted_cluster}**")
    st.markdown(cluster_descriptions.get(predicted_cluster, "No description available."))

    # Add a styled horizontal line
    st.markdown("<hr style='border: 1px solid #FF5733;'>", unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; font-size: 14px;'>🚀 Built BY M.HASEEB ❤️ using Streamlit</p>", unsafe_allow_html=True)
