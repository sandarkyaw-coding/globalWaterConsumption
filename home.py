import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def style_page():
    st.markdown("""
    <style>
    .stApp {
        background-color: #001219;
        color: #e9d8a6;
    }
    .main-title {
        font-size: 50px;
        font-weight: 800;
        text-align: center;
        color: #94d2bd;
        text-shadow: 2px 2px #005f73;
    }
    .crisis-text {
        font-size: 18px;
        line-height: 1.6;
        background: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #ae2012;
    }
    h2 { color: #a0c4ff !important; }
                
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
    # --- SECTION 1: THE DATA (PIE CHART) ---
    st.header("Where is the World's Water?")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("##")
        st.markdown("""
        The Earth is known as the 'Blue Planet,' but most of that blue is unreachable. 
        <br><br>
        97% of our water is contained in the oceans—too salty for humans, animals, or crops. 
        Of the remaining 3% that is fresh, the vast majority is locked away in polar ice caps 
        and deep underground aquifers.
        """, unsafe_allow_html=True)

    with col2:
        # 1. Setup the data
        labels = ['Oceans', 'Ice', '']
        sizes = [97, 2, 1]
        colors = ['#005f73', '#0a9396', '#ee9b00'] # Your ocean theme colors

        # 2. Create the figure (Same size as before)
        fig1, ax1 = plt.subplots(figsize=(5, 5))
        fig1.patch.set_facecolor('none')  # Transparent background
        
        # 3. Plot the Pie Chart
        # We removed the 'centre_circle' to make it a solid pie chart
        ax1.pie(sizes, 
                labels=labels, 
                autopct='%1.0f%%', 
                startangle=90, 
                colors=colors, 
                textprops={'color':"w", 'weight':'bold', 'fontsize': 12}, 
                pctdistance=0.75,
                explode=(0.05, 0, 0)) # Slightly separates the 'Oceans' slice for a modern look

        # 4. Display in Streamlit
        st.pyplot(fig1)

    st.divider()

    # --- SECTION 2: THE HUMAN CRISIS (IMAGE & TEXT) ---
    st.header("The Human Reality")
    
    col3, col4 = st.columns([1, 1])
    
    with col3:
        # Representing the global struggle for clean water
        st.image("https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", 
                 caption="Millions travel miles daily just for a single bucket of water.")
        
    with col4:
        st.markdown("""
        <div class="crisis-text">
        <strong>Water is a Human Right, yet:</strong><br>
        Over 2 billion people currently live in countries experiencing high water stress. 
        For many, 'water scarcity' isn't a future prediction—it is a daily battle for survival. 
        <br><br>
        Lack of clean water leads to disease, prevents children from attending school, 
        and traps communities in cycles of poverty. When the wells run dry, the fabric 
        of society begins to tear.
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # --- SECTION 3: THE FUTURE (BAR CHART) ---
    st.header("The 2050 Population and global water crisis")
    
    # Bar Chart Data
    years = ['Current', '2030 (Est)', '2050 (Est)']
    people_at_risk = [2.1, 3.2, 5.0] # Billions of people

    fig2, ax2 = plt.subplots(figsize=(8, 4))
    fig2.patch.set_facecolor('none')
    ax2.set_facecolor('none')
    
    bars = ax2.bar(years, people_at_risk, color=['#94d2bd', '#e9d8a6', '#ae2012'])
    ax2.set_ylabel('Billions of People', color='white')
    ax2.tick_params(axis='x', colors='white')
    ax2.tick_params(axis='y', colors='white')
    ax2.spines['bottom'].set_color('white')
    ax2.spines['left'].set_color('white')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    # Add values on top of bars
    for bar in bars:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f"{yval}B", 
                 ha='center', color='white', fontweight='bold')

    st.pyplot(fig2)

    st.markdown("""
    ### Why the surge?
    - **Population Growth:** More people means more demand for food, which uses 70% of global freshwater.
    - **Climate Instability:** Glaciers are melting too fast, and rainfall patterns are becoming unpredictable.
    - **Pollution:** Industrial waste is turning our remaining clean water into toxic zones.
    """)

    st.error("ACTION REQUIRED: Without sustainable management, 1 in 2 people will face water stress by 2050.")

if __name__ == "__main__":
    show()