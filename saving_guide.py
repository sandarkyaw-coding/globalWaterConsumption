import streamlit as st

def ocean_background():
    st.markdown("""
    <style>
    .stApp {
        background-color: #001219;
        color: #e9d8a6;
        background-size: 400% 400%;
        animation: gradientMove 15s ease infinite;
    }
    @keyframes gradientMove {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .fact-card {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #a0c4ff;
        margin-bottom: 20px;
        backdrop-filter: blur(5px);
    }
    
    h1, h2, h3 {
        color: #a0c4ff !important;
    }
                
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
    ocean_background()
    
    st.title("Every Drop Counts")
    st.write("Explore why water matters and how you can be a part of the solution.")

    # --- Section 1: Why it Matters ---
    st.markdown('<h2 class="title">Why Saving Water Matters</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="fact-card">
        Water conservation is our strongest defense against the rising threat of global scarcity.By adopting efficient habits today—like smart irrigation and waste reduction—we ensure that clean water remains a guaranteed right for the next generation rather than a rare luxury. Proactive stewardship stabilizes our ecosystems and prevents the social instability that follows resource depletion.
        Saving water is also a direct win for the climate. Ultimately, mindful water management is a vital tool in building a resilient, sustainable planet.
        </div>
        """, unsafe_allow_html=True)
    with col2:
        # Earth/Nature GIF
        st.image("world-water-day.jpg")

    st.divider()

    # --- Section 2: Home Tips ---
    
    st.markdown('<h2 class="title">Practical Tips for Home</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["Bathroom", "Kitchen", "General"])
    
    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2Zicm9ueXZueXJidXo1ZXB6Z3Z5Z3Z5Z3Z5Z3Z5Z3Z5Z3Z5JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKVUn7iM8FMEU24/giphy.gif", caption="Short showers save gallons!")
        with c2:
            st.markdown("""
            * **Take shorter showers** (2–3 min)
            * **Turn off the tap** while brushing teeth
            * **Fix leaky faucets** immediately
            """)

    with tab2:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            * **Bowl Wash:** Wash veggies in a bowl instead of running water.
            * **Full Loads:** Only run the dishwasher when it's completely full.
            """)
        with c2:
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSfyH15Lsf10dn-wcMlujYJXHuEOP9evTbiA&s")

    with tab3:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKzRDlt2EXZOslMtCFHFf-Q9QImiGs9ReZAA&s", width=300)
        st.write("Use a bucket to wash vehicles instead of a hose!")

    st.divider()

    # --- Section 3: Office & School ---
    st.markdown('<h2 class="title">Offices and Schools</h2>', unsafe_allow_html=True)
    
    col_a, col_b = st.columns([1, 2])
    with col_a:
        st.image("https://www.utilities-me.com/2021/07/Abu_dhabi_school_water_cons.jpg")
    with col_b:
        st.markdown("""
        - **Install** water-efficient faucets.
        - **Educate** others! Spread the word about conservation.
        - **Report Leaks** as soon as you see them in restrooms.
        """)

    st.divider()

    # --- Section 4: Community ---
    st.markdown('<h2 class="title">Community & Environment</h2>', unsafe_allow_html=True)
    
    st.image("https://selfhelpafrica.org/ie/wp-content/uploads/sites/4/2024/04/Di-WASH-1-877x585.jpeg", use_container_width=True)
    st.markdown("""
    <div style="text-align: center; background: rgba(0,0,0,0.3); padding: 20px; border-radius: 10px;">
    <h3>Be a Local Hero</h3>
    <p>Plant drought-resistant gardens, collect rainwater, and join local programs!</p>
    </div>
    """, unsafe_allow_html=True)

    st.info("Pro Tip: Watering your plants in the early morning or late evening prevents water loss through evaporation.")

if __name__ == "__main__":
    show()