# app.py

import streamlit as st
import requests
import re
from crew import run_crew

st.set_page_config(page_title="YouTube Video Blog Generator", page_icon="🎥")

st.title("🎥 YouTube Video Blog Generator")

api_key = st.sidebar.text_input("OpenAI API Key", type="password")
topic = st.text_input("Enter Topic")
channel_input = st.text_input("Enter YouTube Channel URL / Handle")

# -----------------------------
# Convert Channel → UC ID
# -----------------------------

def extract_channel_id(input_value):
    try:
        # CASE 1: Already UC ID
        if input_value.startswith("UC"):
            return input_value

        # CASE 2: Full channel URL
        if "channel/" in input_value:
            return input_value.split("channel/")[-1].replace("/", "")

        # CASE 3: Handle (@username)
        if "@" in input_value:
            url = input_value if input_value.startswith("http") else f"https://youtube.com/channel/@{input_value}"
            html = requests.get(url).text

            match = re.search(r'"channelId":"(UC[\w-]+)"', html)
            if match:
                return match.group(1)

        # CASE 4: Plain username
        url = f"https://youtube.com/@{input_value}"
        html = requests.get(url).text

        match = re.search(r'"channelId":"(UC[\w-]+)"', html)
        if match:
            return match.group(1)

    except Exception as e:
        print("Conversion error:", e)

    return None


# -----------------------------
# Button Action
# -----------------------------

if st.button("Generate Blog"):

    if not api_key or not topic or not channel_input:
        st.error("Please fill all fields")
        st.stop()

    with st.spinner("Processing channel..."):

        channel_id = extract_channel_id(channel_input)

        if not channel_id:
            st.error("❌ Could not extract channel ID. Please check URL.")
            st.stop()

    st.success(f"✅ Channel ID detected: {channel_id}")
    print("https://youtube.com/channel/"+channel_id)

    with st.spinner("Running AI agents..."):
        
        result = run_crew(
            topic=topic,
            channel="https://youtube.com/channel/"+channel_id,
            api_key=api_key
        )

    st.write("## ✍️ Generated Blog")
    st.markdown(result)