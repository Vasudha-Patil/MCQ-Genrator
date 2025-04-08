📚 MCQ Generator 🤖
A web application that automatically generates multiple-choice questions (MCQs) from uploaded documents using Google's Gemini AI model. Perfect for educators, trainers, and content creators! ✨

🎯 Features
📤 Upload documents in PDF, DOCX, or TXT format

🔢 Specify number of questions and difficulty level

🧠 Generates a variety of MCQs including:

🔘 Simple multiple-choice

↔️ Match-the-pair

🔲 Fill-in-the-blank

💾 Download generated questions as TXT or PDF

🎥 Visual animation showing question generation process

🚀 Fast and efficient AI-powered generation

⚙️ Technologies Used
🐍 Python

🌐 Flask (web framework)

🤖 Google Gemini AI (for MCQ generation)

📄 pdfplumber (PDF text extraction)

📑 python-docx (DOCX text extraction)

📊 FPDF (PDF generation)

🎨 HTML/CSS/JavaScript (frontend)

🛠️ Installation
Clone the repository:

bash
Copy
git clone https://github.com/Vasudha-Patil/MCQ-Generator.git
cd auto-question-generator
Create and activate a virtual environment:

bash
Copy
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
Copy
pip install -r requirements.txt
Set up your Google API key:

Create a .env file in the project root

Add your API key:

🚀 Usage
Run the Flask application:

bash
Copy
python app.py
Open your browser and navigate to:

Upload a document 📂, specify the number of questions 🔢 and difficulty level ⚡, then click "Generate" 🚀

View and download the generated questions 💾

📂 Project Structure
Copy
auto-question-generator/
├── app.py                # Main Flask application
├── module.py             # Supporting functions
├── templates/
│   ├── index.html        # Main upload page
│   ├── results.html      # Results display page
│   └── home.html         # Demo animation page
├── uploads/              # Folder for uploaded files
├── results/              # Folder for generated question files
├── requirements.txt      # Python dependencies
└── README.md             # This file
📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Google for the Gemini AI model 🤖

Flask and all other open source libraries used 💖

The education community 🍎 for inspiring this tool

All contributors and testers 👥

💡 Pro Tip: For best results, use well-structured documents with clear concepts. The AI works best when the source material is organized and detailed!
