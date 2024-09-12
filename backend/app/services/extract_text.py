import os
import fitz  # PyMuPDF
import requests
from bs4 import BeautifulSoup
from docx import Document

HOME_DIR = os.getenv('HOME')
DATA_PATH = os.path.join(HOME_DIR,'data')

def download_file_from_url(url, save_path):
    '''Downloads PDF file from URL'''

    response = requests.get(url)
    if response.status_code == 200:
        with open(DATA_PATH + '\\' + save_path, 'wb') as file:
            file.write(response.content)
        return save_path
    else:
        raise ValueError(f"Failed to download file from {url}, status code: {response.status_code}")
    
    
def extract_text_from_pdf(pdf_path):
    '''Parses text from a PDF file.'''

    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def extract_text_from_txt(txt_path):
    '''Parses text from a .txt file.'''

    with open(txt_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def get_text_from_url(url):
    '''Parses text from URL'''

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract text from specific HTML elements
    paragraphs = soup.find_all('p')
    text = '\n'.join([para.get_text() for para in paragraphs])
    return text


def extract_text_from_word(docx_path):
    '''Parses text from Word document.'''

    doc = Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text


def extract_text(source):
    '''This function identifies source format and extracts the text from that source.'''

    # Check if url
    if source.startswith('http://') or source.startswith('https://'):
        # Check if pdf
        if source.lower().endswith('.pdf'):
            file_name = source.split('/')[-1]
            dowloaded_file = download_file_from_url(source,file_name) # Douwnload first
            return extract_text_from_pdf(DATA_PATH+'\\'+dowloaded_file) # Parse second
        else: # If webpage
            return get_text_from_url(source)
    # If it is an uploaded file
    else: 
        # Get the extension and parse depending of format
        file_extension = os.path.splitext(source)[1].lower() 
        if file_extension == '.pdf':
            return extract_text_from_pdf(source)
        elif file_extension == '.docx':
            return extract_text_from_word(source)
        elif file_extension == '.doc':
            pass
        elif file_extension == '.txt':
            return extract_text_from_txt(source)
        else:
            raise ValueError(f'Not supported file format: {file_extension}')

        