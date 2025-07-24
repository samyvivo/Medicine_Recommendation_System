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

st.title("💊 Medicine Recommendation System (Offline Model)")
st.markdown("Enter a drug name to find similar medications based on their text profile.")

# Drug list for dropdown
drug_list = df['Drug_Name'].sort_values().unique()

# Input widgets
typed_input = st.text_input("🔍 Type medicine name (optional)", placeholder="e.g., Oxypamol, Paracetamol")
selected_input = st.selectbox("Or select medicine from list 🔽", options=[""] + list(drug_list))

# Choose which input to use
user_input = typed_input.strip() or selected_input.strip()

if user_input:
    selected, recs = recommend_medicines(user_input)
    if selected:
        st.success(f"✅ Found: **{selected}**")
        st.markdown("### 🧾 Top 5 Similar Drugs:")
        for med in recs:
            st.markdown(f"- {med}")
    else:
        st.error("❌ No matching drug found.")
else:
    st.info("Please type a drug name or select one from the list.")



st.markdown("---")  # horizontal line to separate footer

footer = """
<div style="text-align: center; font-size: 0.8em; color: gray;">
Designed by <strong>Saman Zeitounian</strong> |
<a href="https://www.linkedin.com/in/saman-zeitounian-56a0a5164" target="_blank">LinkedIn</a> |
<a href="https://github.com/samyvivo" target="_blank">GitHub</a>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)