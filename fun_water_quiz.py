import streamlit as st
import random

def ocean_background():
    st.markdown("""
    <style>
    /* Main Background */
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
                
    .title {
        color: #a0c4ff !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Added for readability */
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
                
    .popup {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(0, 18, 25, 0.95); /* Deep dark background */
        color: white;
        padding: 10px;
        border-radius: 25px;
        z-index: 9999;
        width: 90%;
        max-width: 500px;
        text-align: center;
        
        /* THE SHADOW SECTION */
        /* Primary shadow for depth + Blue glow for the water theme */
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), 
                    0 0 20px rgba(160, 196, 255, 0.3);
        
        /* Border to help it stand out on dark backgrounds */
        border: 1px solid rgba(160, 196, 255, 0.2);
        backdrop-filter: blur(15px); /* Blurs the background behind the popup */
    }

    /* Add a subtle animation when it appears */
    @keyframes popIn {
        from { opacity: 0; transform: translate(-50%, -45%) scale(0.95); }
        to { opacity: 1; transform: translate(-50%, -50%) scale(1); }
    }
    .popup {
        animation: popIn 0.4s ease-out;
    }
                
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
    if 'setup' not in st.session_state:
        st.set_page_config(page_title="Water Fun Quiz", layout="centered")
        st.session_state.setup = True

    ocean_background()
    st.markdown('<h2 class="title">Water Personality Quiz Time</h2>', unsafe_allow_html=True)
    st.markdown("Answer 3 simple questions and discover your water personality!")
    st.divider()

    # Initialize session state
    if "show_result" not in st.session_state:
        st.session_state.show_result = False

    # 1. Questions (First item checked using index=0)
    if not st.session_state.show_result:
        st.radio("How much water do you drink per day?", ["1–2 liters", "3–4 liters", "More than 4 liters"], key="q1", index=0)
        st.radio("How long is your shower?", ["8–15 minutes", "15-25 minutes", "30min or more"], key="q2", index=0)
        st.radio("How do you wash dishes or clothes?", ["Let water run the whole time", "Turn off sometimes", "Only full loads & water-efficient"], key="q3", index=0)

        if st.button("Reveal My Result"):
            st.session_state.show_result = True
            st.rerun()

    # 2. Popup Result
    if st.session_state.show_result:
        score = 0
        score += 3 if st.session_state.q1 == "1–2 liters" else 2 if st.session_state.q1 == "3–4 liters" else 1
        score += 2 if st.session_state.q2 == "8–15 minutes" else 1 if st.session_state.q2 == "15-25 minutes" else 0
        score += 2 if st.session_state.q3 == "Only full loads & water-efficient" else 1 if st.session_state.q3 == "Turn off sometimes" else 0

        if score <= 3:
            title, text = "The Earth Is Crying!", "The rivers are shrinking.Fish are packing their bags. Plants are nervous.The planet is sweating.You might be using a little too much water!"
            gifs = [
                "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3dwN3dvaTlldHNhNHlmbnFiYWpjYWtodHhuenFzOXZvN2tmdmV5ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Jtdisph0vW0skJi8Ri/giphy.gif",
                "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmFodzZ0eXAwdmxxY3ZjOG8wZnA1aDJwajNyMzNxdjlheXdlbHdneCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/10tIjpzIu8fe0/giphy.gif",
                "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDNwcnhnN3Q2OGtmaTA0dnVnZjF6d3lzdWY1ZjZtbTA1aTV1OHlxNyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/iIFS20pNoCg1EEVodC/giphy.gif"
            ]
        elif 4 <= score <= 5:
            title, text = "Not Bad...", "You're trying, but we can improve. Shorten showers.Turn off water while brushing. Use full loads. Small changes = BIG impact!"
            # List of okay GIFs
            gifs = [
                "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3hqYW5kOWZsdXRzZ3gzaHgyZmNoOHdwbTlqbjdtYWRoNm51NnR2ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/tIeCLkB8geYtW/giphy.gif",
                "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ZTl2cno5NWtyaWh1OHV2eTc2dTV0bWJnMXJ1azh4anJtd3c5ZGV6cCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Pa6h6P5dhin43OlwQ6/giphy.gif",
                "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWVmeDJ1OWpyZG8xZmIxd21mc3hoM2lxc25paGc0a3VneTV1ZTFybyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/buPHaNvgiNdCGPnrbG/giphy.gif"
            ]
        else:
            title, text = "YOU ARE A WATER HERO!", "Efficient showers. Smart washing. Responsible habits. Hidden Superhero of our world!"
            # List of hero GIFs
            gifs = [
                "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZG4yNmtxOHAyc2c0aHJlaGd3dHQ5a291dTR4ZmlyMjZxcHJqYTFycCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/A7Gpt39kH5sAg/giphy.gif",
                "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3aWVpNGduaHQwaWFqd3VvN25taXcyN28yaW9keTJ2YnViMnlkZjNhbSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/l4FGwtw3PWPAt6ZxK/giphy.gif",
                "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGY4ZzRnd3B6YjRnd3B6YjRnd3B6YjRnd3B6YjRnd3B6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7aCTfyhYawdOXcFW/giphy.gif",
                "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmlrNHE5NmU4N24zamxuOThubXNjMDlqenB1dTR1cmpzMXgwMW41ZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/0aIY8ZCncOtgh35ftC/giphy.gif"
            ]
        text = text.replace(".", ".<br>")

        selected_gif = random.choice(gifs)
       
        # RENDER POPUP WITH BUTTON INSIDE
        # The onclick="window.location.reload()" resets the quiz state properly
        st.markdown(f"""
        <div class="popup" id="myPopup">
            <h2>{title}</h2>
            <img src="{selected_gif}" width="200" /><br>
            <p>{text}</p>
            <a href="./" target="_self" style="text-decoration: none;">
        <div style="
            margin-top: 1.5rem;
            padding: 0.6rem 1.5rem;
            display: inline-block;
            background-color: #a0c4ff;
            color: #002b5c;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
        ">
            Okay, I got it!
        </div>
    </a>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    show()