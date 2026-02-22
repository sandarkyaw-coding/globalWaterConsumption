import streamlit as st
import pandas as pd
import joblib
import numpy as np

def style_page():
    st.markdown("""
    <style>
    .stApp {
        background-color: #001219;
        color: #e9d8a6;
    }
    h2 {
        font-weight: 800;
        color: #a0c4ff !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        margin-bottom: 10px;
    }
    .bubble {
        position: fixed;
        bottom: -50px;
        background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.9) 0%, rgba(255, 255, 255, 0.2) 70%);
        border-radius: 50%;
        box-shadow: 0 0 12px rgba(255, 255, 255, 0.4), inset -5px -5px 10px rgba(255, 255, 255, 0.2);
        opacity: 0.7;
        animation: rise 10s infinite ease-in;
        z-index: 1;
        pointer-events: none;
    }
    @keyframes rise {
        0% { transform: translateY(0) translateX(0) scale(1); opacity: 0; }
        10% { opacity: 0.7; }
        50% { transform: translateY(-50vh) translateX(15px) scale(1.1); }
        100% { transform: translateY(-110vh) translateX(-15px) scale(1.2); opacity: 0; }
    }
    .b1 { left: 10%; width: 20px; height: 20px; animation-duration: 8s; }
    .b2 { left: 30%; width: 10px; height: 10px; animation-duration: 12s; }
    .b3 { left: 50%; width: 25px; height: 25px; animation-duration: 10s; }
    </style>
    <div class="bubble b1"></div>
    <div class="bubble b2"></div>
    <div class="bubble b3"></div>
    """, unsafe_allow_html=True)

def show():
    style_page()
    st.markdown('<h2>Water Scarcity & Consumption Predictor</h2>', unsafe_allow_html=True)
    
    # --- Load Data & Models ---
    try:
        df = pd.read_csv("global_water_consumption_2000_2025.csv")
        clf = joblib.load("water_scarcity_classifier.pkl")
        reg = joblib.load("water_consumption_regressor.pkl")
        le = joblib.load("label_encoder.pkl")
        metrics = joblib.load("model_metrics.pkl")
        clf_acc = metrics.get('clf_accuracy', 0.9910)
        reg_acc = metrics.get('reg_accuracy', 0.9538)
    except Exception as e:
        st.error(f"File Error: {e}")
        return

    # --- UI Inputs ---
    col1, col2 = st.columns(2)
    with col1:
        country = st.selectbox("Select Country", df["Country"].unique())
    with col2:
        year = st.slider("Select Year", 2000, 2100, 2030)

    # --- Logic Processing ---
    country_data = df[df["Country"] == country].sort_values("Year")
    base_2025 = country_data[country_data["Year"] == 2025]
    
    actual_scar_html = ""
    actual_cons_html = ""
    is_future = year > 2025

    if not is_future:
        row = country_data[country_data["Year"] == year]
        if not row.empty:
            input_df = row.copy()
            a_cons = row["Total Water Consumption (Billion m3)"].values[0]
            
            # --- FIX FOR VALUEERROR ---
            raw_scar = row["Water Scarcity Level"].values[0]
            # If it's already a string (e.g., 'High'), use it. If it's a number, decode it.
            if isinstance(raw_scar, (int, np.integer, float)):
                a_scar = le.inverse_transform([int(raw_scar)])[0]
            else:
                a_scar = str(raw_scar)
            
            actual_scar_html = f'<div style="color:#d62828; font-size:18px;">Actual: {a_scar}</div>'
            actual_cons_html = f'<div style="color:#d62828; font-size:18px;">Actual: {round(a_cons, 2)} B m³</div>'
            display_title = f"Historical Comparison: {year}"
        else:
            input_df = base_2025.copy()
            display_title = "Using 2025 Baseline"
    else:
        years_ahead = year - 2025
        input_df = base_2025.copy()
        input_df["Year"] = year
        evolve_cols = ["Per Capita Water Use (L/Day)", "Agricultural Water Use (%)", "Industrial Water Use (%)", "Household Water Use (%)", "Rainfall Impact (mm)", "Groundwater Depletion Rate (%)"]
        for col in evolve_cols:
            slope = (country_data[col].iloc[-1] - country_data[col].iloc[0]) / 25
            input_df[col] += (slope * years_ahead)
            if "%" in col: input_df[col] = np.clip(input_df[col], 0, 100)
        display_title = f"AI Future Projection: {year}"

    # --- Predictions ---
    # Ensure we only pass numeric columns to the models
    cons_pred = reg.predict(input_df[reg.feature_names_in_])[0]
    
    # Temporarily add prediction for the classifier
    temp_df = input_df[clf.feature_names_in_].copy()
    scar_pred_num = clf.predict(temp_df)[0]
    scar_pred = le.inverse_transform([int(scar_pred_num)])[0]

    # --- UI BOX ---
    ui_box = f"""<div style="background-color: #d0f0fd; padding: 20px; border-radius: 15px; border: 2px solid #81d4fa; color: #03396c; margin: 20px 0; font-family: sans-serif; position: relative; z-index: 10;">
<h3 style="margin: 0 0 15px 0; color: #03396c; border-bottom: 1px solid #81d4fa; padding-bottom: 5px;">{display_title}</h3>
<div style="display: flex; justify-content: space-between;">
<div style="width: 48%;">
<div style="font-size: 20px; opacity: 0.8;">Scarcity Prediction</div>
<div style="font-size: 24px; font-weight: bold; color: #001219;">{scar_pred}</div>
{actual_scar_html}
<div style="margin-top: 20px; font-size: 20px; color: #0077b6; font-weight: bold;">Accuracy: {clf_acc*100:.2f}%</div>
</div>
<div style="width: 48%; text-align: right;">
<div style="font-size: 20px; opacity: 0.8;">Consumption Prediction</div>
<div style="font-size: 24px; font-weight: bold; color: #001219;">{round(cons_pred, 2)} B m³</div>
{actual_cons_html}
<div style="margin-top: 20px; font-size: 20px; color: #0077b6; font-weight: bold;">Reliability (R²): {reg_acc*100:.2f}%</div>
</div>
</div>
</div>"""

    st.markdown(ui_box, unsafe_allow_html=True)

    # --- Visuals ---
    st.markdown("### Historical Trends")
    chart_data = country_data[["Year", "Total Water Consumption (Billion m3)"]].copy()
    if is_future:
        future_point = pd.DataFrame({"Year": [year], "Total Water Consumption (Billion m3)": [cons_pred]})
        chart_data = pd.concat([chart_data, future_point], ignore_index=True)
    
    st.line_chart(chart_data.set_index("Year"))
    st.dataframe(country_data.style.background_gradient(cmap="Blues"), height=250)

if __name__ == "__main__":
    show()