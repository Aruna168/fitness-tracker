import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Set up page configuration
st.set_page_config(page_title="Futuristic Fitness Tracker", layout="wide", page_icon="💪")

# Sample data for visualizations (in real app, replace with your data source)
sample_data = pd.DataFrame({
    "date": pd.date_range(start="2023-10-01", periods=30, freq="D"),
    "steps": [1000 + i*50 for i in range(30)],
    "calories": [2000 - i*30 for i in range(30)],
    "heart_rate": [60 + (i % 5) * 10 for i in range(30)]
})

# Header and styling
st.markdown(
    """
    <style>
    .main-title { font-size:50px; font-weight:bold; color:#00FFCA; text-align:center; }
    .section-header { font-size:28px; color:#FF6D00; margin-top:40px; }
    .data-box { background-color: #1F1F1F; padding: 20px; border-radius: 10px; }
    .data-box h3 { color: #00FFCA; font-size:24px; }
    </style>
    """, unsafe_allow_html=True
)
st.markdown('<h1 class="main-title">Futuristic Fitness Tracker</h1>', unsafe_allow_html=True)

# Sidebar for User Login or Data Filters
with st.sidebar:
    st.header("User Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    st.button("Login")

# Dashboard Layout
# Section 1: Activity Tracking (Line Chart)
st.markdown('<div class="section-header">Activity Tracking</div>', unsafe_allow_html=True)
st.markdown('<div class="data-box">', unsafe_allow_html=True)
st.write("Track your steps and calories burned over time.")

# Plot Steps and Calories Over Time
fig_activity = px.line(sample_data, x="date", y=["steps", "calories"], 
                       labels={"date": "Date", "value": "Count", "variable": "Activity"},
                       title="Daily Steps and Calories Burned")
fig_activity.update_layout(title_font_size=20, template="plotly_dark", legend_title_text="Metrics")
st.plotly_chart(fig_activity, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Section 2: Heart Rate Monitoring
st.markdown('<div class="section-header">Heart Rate Monitoring</div>', unsafe_allow_html=True)
st.markdown('<div class="data-box">', unsafe_allow_html=True)
st.write("Monitor your heart rate trends.")

# Plot Heart Rate Over Time
fig_heart_rate = px.line(sample_data, x="date", y="heart_rate", 
                         labels={"date": "Date", "heart_rate": "Heart Rate (bpm)"},
                         title="Daily Heart Rate")
fig_heart_rate.update_layout(title_font_size=20, template="plotly_dark")
st.plotly_chart(fig_heart_rate, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Section 3: Fitness Summary
st.markdown('<div class="section-header">Weekly Fitness Summary</div>', unsafe_allow_html=True)
st.markdown('<div class="data-box">', unsafe_allow_html=True)
st.write("Overview of weekly fitness metrics.")

# Display Key Stats
avg_steps = sample_data["steps"].mean()
avg_calories = sample_data["calories"].mean()
avg_heart_rate = sample_data["heart_rate"].mean()

st.metric(label="Average Steps (Week)", value=f"{avg_steps:.0f}")
st.metric(label="Average Calories Burned (Week)", value=f"{avg_calories:.0f}")
st.metric(label="Average Heart Rate (Week)", value=f"{avg_heart_rate:.0f} bpm")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <footer style='text-align: center; padding: 20px; color: #00FFCA;'>
    © 2024 Futuristic Fitness Tracker | Designed with 💪 by You
    </footer>
    """, unsafe_allow_html=True
)
