import streamlit as st
import pandas as pd
import joblib

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
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Added for readability */
        margin-bottom: 10px;    }    
    /* Bubbles Styling */
    .bubble {
            position: fixed;
            bottom: -50px;
            
            /* 1. Shiny Highlight: Creates a bright spot at the top-left */
            background: radial-gradient(circle at 30% 30%, 
                        rgba(255, 255, 255, 0.9) 0%, 
                        rgba(255, 255, 255, 0.2) 70%);
            
            border-radius: 50%;
            
            /* 2. Shine & Glow: Adds an outer glow and an inner rim light */
            box-shadow: 0 0 12px rgba(255, 255, 255, 0.4), 
                        inset -5px -5px 10px rgba(255, 255, 255, 0.2);
            
            /* 3. Border: Adds a crisp "soap bubble" edge */
            border: 0.5px solid rgba(255, 255, 255, 0.4);
            
            opacity: 0.7; /* Increased slightly to see the shine better */
            animation: rise 10s infinite ease-in;
            z-index: 1;
            pointer-events: none;
        }

    /* Blue Light Particles (Twinkling) */
    .light {
        position: fixed;
        width: 4px;
        height: 4px;
        background-color: #a0c4ff;
        border-radius: 50%;
        box-shadow: 0 0 10px #a0c4ff, 0 0 20px #a0c4ff;
        animation: twinkle 5s infinite ease-in-out;
        z-index: 1;
        pointer-events: none;
    }      
    
    @keyframes rise {
        0% { 
            transform: translateY(0) translateX(0) scale(1); 
            opacity: 0; 
        }
        10% { opacity: 0.7; }
        50% { 
            transform: translateY(-50vh) translateX(15px) scale(1.1); 
        }
        100% { 
            transform: translateY(-110vh) translateX(-15px) scale(1.2); 
            opacity: 0; 
        }
    }

    @keyframes twinkle {
        0%, 100% { opacity: 0.2; transform: scale(1); }
        50% { opacity: 0.8; transform: scale(1.2); }
    }

    /* Positioning multiple elements */
    .b1 { left: 10%; width: 20px; height: 20px; animation-duration: 8s; }
    .b2 { left: 30%; width: 10px; height: 10px; animation-duration: 12s; animation-delay: 2s; }
    .b3 { left: 50%; width: 25px; height: 25px; animation-duration: 10s; animation-delay: 4s; }
    .b4 { left: 70%; width: 15px; height: 15px; animation-duration: 14s; }
    .b5 { left: 90%; width: 18px; height: 18px; animation-duration: 9s; animation-delay: 1s; }

    .l1 { top: 20%; left: 15%; animation-delay: 0s; }
    .l2 { top: 40%; left: 80%; animation-delay: 1s; }
    .l3 { top: 70%; left: 25%; animation-delay: 2s; }
    .l4 { top: 10%; left: 60%; animation-delay: 3s; }
                
    </style>
    
    <div class="bubble b1"></div>
    <div class="bubble b2"></div>
    <div class="bubble b3"></div>
    <div class="bubble b4"></div>
    <div class="bubble b5"></div>

    <div class="light l1"></div>
    <div class="light l2"></div>
    <div class="light l3"></div>
    <div class="light l4"></div>
    """, unsafe_allow_html=True)

                
def show():
    style_page()
    st.markdown('<h2 class="title">Water Scarcity & Consumption Predictor</h2>', unsafe_allow_html=True)
   
    df = pd.read_csv("global_water_consumption_2000_2025.csv")

    # ------------------------
    # Input controls (columns instead of sidebar)
    # ------------------------
    col1, col2 = st.columns(2)

    with col1:
        country = st.selectbox("Select Country", df["Country"].unique())

    with col2:
        year = st.slider("Select Year for Prediction", 2000, 2100)

    # ------------------------
    # Filter data for the selected country
    # ------------------------
    country_data = df[df["Country"] == country].sort_values("Year")

    # ------------------------
    # Load pre-trained models
    # ------------------------
    clf = joblib.load("water_scarcity_classifier.pkl")
    reg = joblib.load("water_consumption_regressor.pkl")
    le = joblib.load("label_encoder.pkl")

    # ------------------------
    # Calculate historical growth rate
    # ------------------------
    growth_series = country_data["Total Water Consumption (Billion m3)"].pct_change()
    avg_growth = growth_series.mean()
    if pd.isna(avg_growth) or abs(avg_growth) > 0.2:
        avg_growth = 0.01  # fallback default if unreasonable

    # ------------------------
    # PREDICTION SECTION (Show first)
    # ------------------------
    if year <= 2025:
        selected_data = country_data[country_data["Year"] == year]

        if not selected_data.empty:
            # Classification
            X_clf = selected_data.drop(["Country", "Water Scarcity Level"], axis=1)
            X_clf = X_clf[clf.feature_names_in_]
            scarcity_pred = clf.predict(X_clf)
            scarcity_label = le.inverse_transform(scarcity_pred)

            # Regression
            X_reg = selected_data.drop(["Country", "Water Scarcity Level",
                                       "Total Water Consumption (Billion m3)"], axis=1)
            X_reg = X_reg[reg.feature_names_in_]
            consumption_pred = reg.predict(X_reg)

           # Custom light blue prediction box
            st.markdown(f"""
            <div style="
                background-color: #d0f0fd;  /* Light blue */
                padding: 15px;
                border-radius: 10px;
                border: 2px solid #81d4fa;
                color: #03396c;
            ">
            <h4>Predictions for {year}</h4>
            <p>Water Scarcity Level: <b>{scarcity_label[0]}</b></p>
            <p>Total Water Consumption: <b>{round(consumption_pred[0], 2)} Billion m³</b></p>
            </div>
            """, unsafe_allow_html=True)

    else:
        last_2025 = country_data[country_data["Year"] == 2025]
        if not last_2025.empty:
            last_value = last_2025["Total Water Consumption (Billion m3)"].values[0]
            years_ahead = year - 2025
            future_value = last_value * ((1 + avg_growth) ** years_ahead)

            last_year_data = last_2025.copy()
            last_year_data["Total Water Consumption (Billion m3)"] = future_value

            # Classification
            X_clf_future = last_year_data.drop(["Country", "Water Scarcity Level"], axis=1)
            X_clf_future = X_clf_future[clf.feature_names_in_]
            scarcity_pred = clf.predict(X_clf_future)
            scarcity_label = le.inverse_transform(scarcity_pred)

            # Custom dark blue future prediction box
            st.markdown(f"""
            <div style="
                background-color: #a0c4ff;  /* Light-to-medium blue */
                padding: 15px;
                border-radius: 10px;
                border: 2px solid #3f51b5;  /* Darker blue border */
                color: #001f54;              /* Dark blue text */
            ">
            <h4>Future Predictions for {year}</h4>
            <p>Average Growth Rate: <b>{round(avg_growth * 100, 2)}%</b></p>
            <p>Projected Scarcity Level: <b>{scarcity_label[0]}</b></p>
            <p>Projected Total Water Consumption: <b>{round(future_value, 2)} Billion m³</b></p>
            </div>
            """, unsafe_allow_html=True)


    # Show dataset preview (always visible)
    # ------------------------
    st.markdown(f'<h2 class="custom-sub">Dataset Preview for {country} (2000–2025)</h2>', unsafe_allow_html=True)
    # Apply light blue gradient to numeric columns
    styled_df = country_data.style.background_gradient(
        cmap="Blues", subset=country_data.select_dtypes(include=['float', 'int']).columns
    )

    st.dataframe(styled_df, height=400)


    # ------------------------
    # LINE CHART (Historical + Future)
    # ------------------------
    st.markdown('<h2 class="title">Water Consumption Trend</h2>', unsafe_allow_html=True)
   
    # Use historical data first
    trend_df = country_data[["Year", "Total Water Consumption (Billion m3)"]].copy()

    # Add future predictions if year > 2025
    if year > 2025:
        future_years = list(range(2026, year + 1))
        last_value = trend_df["Total Water Consumption (Billion m3)"].iloc[-1]

        future_consumption = [last_value * ((1 + avg_growth) ** (y - 2025)) for y in future_years]

        future_df = pd.DataFrame({
            "Year": future_years,
            "Total Water Consumption (Billion m3)": future_consumption
        })

        trend_df = pd.concat([trend_df, future_df], ignore_index=True)

    trend_df = trend_df.set_index("Year")
    st.line_chart(trend_df)
