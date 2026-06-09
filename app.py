import streamlit as st
import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Page Configuration
st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌦",
    layout="wide"
)

# Title
st.markdown(
    """
    <h1 style='text-align:center; color:#00BFFF;'>
    🌦 Real-Time Weather Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)
st.info("🌦️ Real-Time Weather Monitoring Dashboard")

# City Input
city = st.text_input("Enter City", value="Lucknow")

if city:

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Weather Metrics
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "🌡 Temperature",
                f"{data['main']['temp']} °C"
            )

        with col2:
            st.metric(
                "💧 Humidity",
                f"{data['main']['humidity']} %"
            )

        with col3:
            st.metric(
                "⚡ Pressure",
                f"{data['main']['pressure']} hPa"
            )

        st.success(
            f"📍 {data['name']}, {data['sys']['country']}"
        )

        st.write(
            f"🌤 Weather: {data['weather'][0]['description'].title()}"
        )

        # Graph Data
        graph_data = pd.DataFrame({
            "Weather Metrics": ["Temperature", "Humidity",  "Pressure" ],
            "Values": [
                data["main"]["temp"],
                data["main"]["humidity"],
                data["main"]["pressure"]
            ]
        })

        st.subheader("📊 Weather Analytics")

        st.line_chart(
            graph_data.set_index("Weather Metrics")
        )

    else:
        st.error("City not found or API issue")