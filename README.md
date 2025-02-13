
# MultiLanguage Invoice Extractor

📄 AI-powered invoice extraction and analysis using Google Gemini AI and Streamlit.




## 🚀 Overview

MultiLang Invoice Extractor is an AI-driven application that extracts and analyzes invoice details from uploaded images. It utilizes Google Gemini AI for intelligent text recognition and multi-language support. The app is built with Streamlit for an interactive and user-friendly experience.


## ✨ Features
✔️ Extracts invoice details from images (JPG,JPEG, PNG).  
✔️ Multi-language support for invoices.  
✔️ AI-powered responses to invoice-related queries.  
✔️ Secure API key handling with dotenv.  
✔️ Simple and intuitive Streamlit UI.


## Tech Stack



## Installation

1️⃣ Clone the Repository

```bash
git clone https://github.com/Aswin-Raksha/MultiLang-Invoice-Extractor.git
cd MultiLang-Invoice-Extractor
```
2️⃣ Create a Virtual Environment
```bash
python -m venv myenv
source myenv/bin/activate    # For macOS/Linux
myenv\Scripts\activate       # For Windows
```
3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Set Up API Key

Create a .env file in the root directory and add your Google API key:
```bash
GOOGLE_API_KEY=your_api_key_here
```
5️⃣ Run the Application
```bash
streamlit run MultiLang_Invoice_extractor.py
```
