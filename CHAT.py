import streamlit as st
import requests
import pandas
import numpy




st.title("Real-time Updates")

start_button = st.button("Start Process")
output_area = st.empty()

if start_button:
    try:
        # Start the process
        response = requests.post(
            "http://localhost:8000/chattopic/", stream=True, timeout=300)
        if response.status_code == 200:
            st.write("Process started...")

            # Poll for updates
            updates = []
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    updates.append(decoded_line)
                    
                    
                    output_area.text_area(
                        "Intermediate Output", value="\n".join(updates), height=400)
        else:
            st.write("Failed to start process")
    except requests.exceptions.RequestException as e:
        st.write(f"Error: {e}")
