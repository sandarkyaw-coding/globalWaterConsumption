import streamlit as st
import fun_water_quiz
import home
import prediction
import saving_guide  # if you create a separate guide file

st.set_page_config(page_title="Global Water Intelligence App", layout="wide")

# ------------------------
# Top navigation without sidebar
# ------------------------
st.markdown("""
    <style>
        /* This targets the sidebar container */
        [data-testid="stSidebar"] {
            background-color: #001219; /* Deep Ocean Black-Blue */
            background-image: linear-gradient(180deg, #001219 0%, #002b5c 100%);
        }

        /* This changes the text color inside the sidebar to match */
        [data-testid="stSidebar"] .st-emotion-cache-17l2puu, 
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] span {
            color: #a0c4ff !important;
            font-weight: bold;
        }

        /* This changes the color of the radio button options */
        [data-testid="stSidebar"] .stRadio div {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Your existing menu code
menu = st.sidebar.radio(
    "Global Water Prediction",
    ["Home", "Prediction Dashboard", "Water Saving Guide", "Quiz Time"]
)

if menu == "Home":
    home.show()
elif menu == "Prediction Dashboard":
    prediction.show()
elif menu == "Water Saving Guide":
    saving_guide.show()
elif menu == "Quiz Time":
    fun_water_quiz.show()
