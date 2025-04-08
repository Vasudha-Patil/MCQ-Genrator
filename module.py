import pdfplumber
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# Extract text from PDF file
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text
 
# Extract text from .txt file
def extract_text_from_txt(txt_path):
    with open(txt_path, 'r') as file:
        text = file.read()
    return text

# Summarization Model
def summarize_text(text):
    model_name = "t5-small"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    
    inputs = tokenizer("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs['input_ids'], max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# MCQ Generation using T5 Model (or GPT-based model)
def generate_mcqs(text):
    model_name = "t5-small"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    
    # Constructing the prompt for MCQ generation
    prompt = f"Generate multiple-choice questions from the following text: {text}"
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    
    mcq_ids = model.generate(inputs['input_ids'], max_length=300, num_beams=4, early_stopping=True)
    mcqs = tokenizer.decode(mcq_ids[0], skip_special_tokens=True)
    
    return mcqs

# Full pipeline
def process_file(file_path, file_type='pdf'):
    if file_type == 'pdf':
        text = extract_text_from_pdf(file_path)
    elif file_type == 'txt':
        text = extract_text_from_txt(file_path)
    
    # Summarize the extracted text
    summarized_text = summarize_text(text)
    
    # Generate MCQs from the summarized text
    mcqs = generate_mcqs(summarized_text)
    
    return mcqs

# Example Usage
file_path = 'sample.pdf'  # Change this to your file path
file_type = 'pdf'  # Change this to 'txt' if it's a text file
mcqs = process_file(file_path, file_type)

print(mcqs)
