import streamlit as st
import pandas as pd
import joblib

# Load model & data
df = joblib.load("df_medicine.joblib")
similarity = joblib.load("similarity_matrix.joblib")

# Recommendation function
def recommend_medicines(user_input):
    user_input = user_input.lower()
    matched = df[df['Drug_Name'].str.contains(user_input, case=False)]

    if matched.empty:
        return None, []

    medicine_index = matched.index[0]
    selected_name = df.loc[medicine_index, 'Drug_Name']
    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = [df.iloc[i[0]]['Drug_Name'] for i in medicines_list]
    return selected_name, recommendations

# Streamlit UI
st.title("💊 Medicine Recommendation System (Offline Model)")
st.markdown("Enter a drug name to find similar medications based on their text profile.")

user_input = st.text_input("🔍 Enter medicine name", placeholder="e.g., Oxypamol, Paracetamol")

if user_input:
    selected, recs = recommend_medicines(user_input)

    if selected:
        st.success(f"✅ Found: **{selected}**")
        st.markdown("### 🧾 Top 5 Similar Drugs:")
        for med in recs:
            st.markdown(f"- {med}")
    else:
        st.error("❌ No matching drug found.")