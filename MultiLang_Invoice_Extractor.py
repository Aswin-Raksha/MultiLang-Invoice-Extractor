from dotenv import load_dotenv

load_dotenv() # load all the environment variables from .env

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# Function to load Gemeini Pro Vision
def get_gemini_response(input , image , prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input , image[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [{
            "mime_type" : uploaded_file.type,
            "data":bytes_data
        }]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded!")

# Initialize Streamlit App

st.set_page_config(page_title = "MultiLanguage Invoice Extractor")

st.header("MultiLang Invoice Extractor")
input = st.text_input("Input Prompt : ",key = "input")
uploaded_file = st.file_uploader("Choose an image of the Invoice",type = ["jpeg","jpg","png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image , caption="uploaded Image." , use_column_width = True)

submit = st.button("Tell me about the Invoice.")

input_prompt = """
    You are an Expert in understanding Invoices.
    I will be uploading an Invoice as an image and
    you will have to answer any questions based on the uploaded Invoice image.
"""

# If Submit button is clicked
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is ")
    st.write(response)
