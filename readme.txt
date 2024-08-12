#  UPC_API

## Overview
The Text Summarizer is a Django-based web application designed to upload PDF files, extract and summarize the text content, and translate the summarized text into multiple languages. The application also extracts keywords from the summaries to provide a concise overview of the text.

## Features
-  Upload PDF: Upload a PDF file to the system.
-  Extract Text: Extract text from the uploaded PDF.
-  Summarize Text: Summarize the extracted text using the LSA summarizer.
-  Translate Summary: Translate the summary into English and Marathi.
-  Extract Keywords: Generate keywords from the translated summaries.
-  Display Results: Show the summarized text and keywords in both English and Marathi.

## Requirements
- Python 3.x
- Django
- PyPDF2
- sumy
- googletrans
- yake

## Setup

### Install the required Python packages:
```
pip install django pypdf2 sumy googletrans==4.0.0-rc1 yake
```
### Set up the Django project and application:
1. Create a new Django project and application:
```
django-admin startproject TextSummarizer
cd TextSummarizer
python manage.py startapp myfile
);
```
 2. Add myfile to the INSTALLED_APPS list in TextSummarizer/settings.py.

## Create the Django model for file uploads 
### In myfile/models.py:
```
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
```
## Create the form for file uploads:
### In myfile/forms.py:
```
from django import forms
from .models import UploadedFile

class UploadsForms(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']
```
## Create the view for handling uploads and processing:
### In myfile/views.py:
```
from django.shortcuts import render
from .forms import UploadsForms
from PyPDF2 import PdfReader
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from googletrans import Translator
import yake

def upload(request):
    if request.method == "POST":
        form = UploadsForms(request.POST, request.FILES)
        pdf_file = request.FILES['file']
        if form.is_valid():
            pdf_reader = PdfReader(pdf_file)
            no_page = len(pdf_reader.pages)
            if no_page >= 15:
                extracted_text = extract_text(pdf_file)
                extracted_summary = get_summary(extracted_text)
                translated_summary_en = translate_summary_english(extracted_summary)
                english_keywords = extract_keywords(translated_summary_en)
                translated_summary_mr = translate_summary_marathi(extracted_summary)
                marathi_keywords = extract_keywords(translated_summary_mr)
                
                return render(request, 'display.html', {
                    'value1': translated_summary_en,
                    'value2': english_keywords,
                    'value3': translated_summary_mr,
                    'value4': marathi_keywords
                })
            else:
                msg = 'Uploaded file should not be less than 15 pages'
                return render(request, 'upload.html', {'msg': msg})
    else:
        form = UploadsForms()
    return render(request, "upload.html", {"form": form})

def extract_text(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def get_summary(extracted_text):
    parser = PlaintextParser.from_string(extracted_text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count=5)
    return " ".join(str(sentence) for sentence in summary)

def translate_summary_english(extracted_summary):
    translator = Translator()
    translated_text = translator.translate(extracted_summary, dest='en')
    return translated_text.text

def extract_keywords(text):
    extractor = yake.KeywordExtractor()
    keywords = extractor.extract_keywords(text)
    return [word[0] for word in keywords]

def translate_summary_marathi(extracted_summary):
    translator = Translator()
    translated_text = translator.translate(extracted_summary, dest='mr')
    return translated_text.text

```
## Create the templates for upload and display:
### upload.html:
```
<!DOCTYPE html>
<html>
<head>
    <title>Upload PDF</title>
</head>
<body>
    <h1>Upload PDF</h1>
    {% if msg %}
    <p>{{ msg }}</p>
    {% endif %}
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Upload</button>
    </form>
</body>
</html>

```
### display.html:
```
<!DOCTYPE html>
<html>
<head>
    <title>Summary and Keywords</title>
</head>
<body>
    <h1>Summary and Keywords</h1>
    <h2>English Summary</h2>
    <p>{{ value1 }}</p>
    <h2>English Keywords</h2>
    <ul>
        {% for keyword in value2 %}
        <li>{{ keyword }}</li>
        {% endfor %}
    </ul>
    <h2>Marathi Summary</h2>
    <p>{{ value3 }}</p>
    <h2>Marathi Keywords</h2>
    <ul>
        {% for keyword in value4 %}
        <li>{{ keyword }}</li>
        {% endfor %}
    </ul>
</body>
</html>

```

## Usage
1. Start the Django development server:
```
python manage.py runserver

```
2. Open a web browser and go to http://127.0.0.1:8000/upload/ to upload a PDF file.

3. After uploading, the summarized text and keywords in both English and Marathi will be displayed.
## Additional Information 
Additional Information
This project leverages the following libraries and tools:

- PyPDF2 for extracting text from PDF files.
- sumy for text summarization.
- googletrans for translating text.
- yake for keyword extraction
