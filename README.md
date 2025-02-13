MultiLang Invoice Extractor
📄 AI-powered invoice extraction and analysis using Google Gemini AI and Streamlit

🚀 Overview
MultiLang Invoice Extractor is an AI-driven application that extracts and analyzes invoice details from uploaded images. It utilizes Google Gemini AI for intelligent text recognition and multi-language support. The app is built with Streamlit for an interactive and user-friendly experience.

✨ Features
✔️ Extracts invoice details from images (JPG, JPEG, PNG)
✔️ Multi-language support for invoices
✔️ AI-powered responses to invoice-related queries
✔️ Secure API key handling with dotenv
✔️ Simple and intuitive Streamlit UI

🛠 Tech Stack
Python 3.x
Streamlit (for UI)
Google Gemini AI (for vision and text processing)
Pillow (PIL) (for image handling)
dotenv (for environment variables)
📥 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/MultiLang-Invoice-Extractor.git
cd MultiLang-Invoice-Extractor
2️⃣ Create a Virtual Environment
bash
Copy
Edit
python -m venv myenv
source myenv/bin/activate    # For macOS/Linux
myenv\Scripts\activate       # For Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up API Key
Create a .env file in the root directory and add your Google API key:

ini
Copy
Edit
GOOGLE_API_KEY=your_api_key_here
5️⃣ Run the Application
bash
Copy
Edit
streamlit run MultiLang_Invoice_extractor.py
📸 How It Works
1️⃣ Upload an invoice image (.jpeg, .jpg, .png).
2️⃣ Enter a query related to the invoice (e.g., "What is the total amount?").
3️⃣ Click "Tell me about the Invoice" to get AI-powered insights.

🖼 Demo Screenshot
(Add a screenshot of your Streamlit app here for better visualization.)

📌 Future Enhancements
✅ Export extracted details to CSV or PDF
✅ Support for additional invoice formats
✅ Integration with OCR for better text recognition
🤝 Contributing
Contributions are welcome! Feel free to fork this repo, submit issues, or create pull requests.

📜 License
This project is licensed under the MIT License.
