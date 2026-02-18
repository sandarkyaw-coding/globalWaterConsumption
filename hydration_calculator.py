import streamlit as st
import plotly.graph_objects as go

def show():
    # 1. Custom CSS & Animations (The "Vibe" Layer)
    st.markdown("""
        <style>
        /* Overall App Background */
        .stApp {
            background-color: #001219;
            color: #e9d8a6;
        }
        
        /* Headers & Text */
        h1, h2, h3 { color: #a0c4ff !important; }
        .stMarkdown p { color: #e9d8a6; }

        /* The Result "Pop-up" Card */
        .result-card {
            background-color: #0a9396;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            border: 2px solid #94d2bd;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
            margin: 20px 0px;
        }
        .result-number {
            font-size: 48px;
            font-weight: bold;
            color: #ffffff;
            margin: 10px 0px;
        }

        /* Bubble & Light Animations */
        .bubble {
            position: fixed; bottom: -50px;
            background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.1));
            border-radius: 50%;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
            animation: rise 10s infinite ease-in;
            z-index: 0; pointer-events: none;
        }
        .light {
            position: fixed; width: 4px; height: 4px;
            background-color: #a0c4ff; border-radius: 50%;
            box-shadow: 0 0 10px #a0c4ff;
            animation: twinkle 5s infinite ease-in-out;
            z-index: 0; pointer-events: none;
        }
        @keyframes rise {
            0% { transform: translateY(0) scale(1); opacity: 0; }
            10% { opacity: 0.5; }
            100% { transform: translateY(-110vh) scale(1.2); opacity: 0; }
        }
        @keyframes twinkle {
            0%, 100% { opacity: 0.2; } 50% { opacity: 0.8; }
        }
        
        /* Positioning Bubbles */
        .b1 { left: 10%; width: 20px; height: 20px; animation-duration: 8s; }
        .b2 { left: 35%; width: 12px; height: 12px; animation-duration: 12s; }
        .b3 { left: 60%; width: 25px; height: 25px; animation-duration: 10s; }
        .b4 { left: 85%; width: 15px; height: 15px; animation-duration: 7s; }
        </style>
        
        <div class="bubble b1"></div><div class="bubble b2"></div>
        <div class="bubble b3"></div><div class="bubble b4"></div>
        <div class="light" style="top:20%; left:15%;"></div>
        <div class="light" style="top:50%; left:80%;"></div>
    """, unsafe_allow_html=True)

    # 2. Main UI Content
    st.title("Personal Hydration Calculator")
    st.markdown("---")

    col1, col2 = st.columns(2)
    
    with col1:
        weight = st.number_input("Enter Weight (lbs):", min_value=1.0, value=150.0)
        st.markdown("### Outdoor Temp")
        temp = st.select_slider(
            "How hot is it?",
            options=["Cool", "Mild", "Warm", "Hot", "Extreme Heat"],
            value="Mild"
        )
                    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True) # Alignment
        exercise_minutes = st.slider("Exercise (mins):", 0, 180, 30)

    # 3. Logic & Results
    if weight > 0:
        # Calculate base and adjustments
        base_oz = weight * 0.5
        heat_mult = {"Cool": 1.0, "Mild": 1.0, "Warm": 1.1, "Hot": 1.2, "Extreme Heat": 1.3}
        
        total_oz = (base_oz * heat_mult[temp]) + ((exercise_minutes / 30) * 12)
        total_liters = total_oz * 0.0295735
        bottles = total_liters / 0.5

        # Results Pop-up Card
        st.markdown(f"""
            <div class="result-card">
                <p style="color: white; font-size: 18px; letter-spacing: 2px;">YOUR DAILY GOAL</p>
                <div class="result-number">{total_liters:.2f} Liters</div>
                <p style="color: #e9d8a6;">≈ {round(bottles)} bottles (500ml) or {round(total_oz)} oz</p>
            </div>
        """, unsafe_allow_html=True)

        # 4. Gauge Chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=round(total_liters, 2),
            number={'font': {'color': "#a0c4ff"}},
            title={'text': "Daily Intake Scale", 'font': {'color': "#e9d8a6"}},
            gauge={
                'axis': {'range': [0, 6], 'tickcolor': "#e9d8a6"},
                'bar': {'color': "#a0c4ff"},
                'bgcolor': "rgba(255,255,255,0.05)",
                'steps': [
                    {'range': [0, 2], 'color': '#ae2012'},
                    {'range': [2, 4], 'color': '#ee9b00'},
                    {'range': [4, 6], 'color': '#0a9396'}]
            }
        ))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=350)
        st.plotly_chart(fig, use_container_width=True)

        st.info("Pro-Tip: Carry a reusable bottle to make hitting this goal easier!  Sip consistently! Drinking a whole liter at once isn't as effective as steady hydration.")

if __name__ == "__main__":
    show()