import os
import sys

backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(backend_path)
from app.services.extract_text import extract_text

HOME_DIR = os.getenv('HOME')
DATA_PATH = os.path.join(HOME_DIR,'data')

# Different sources
url = 'https://en.wikipedia.org/wiki/Main_Page'
url_pdf = 'https://www.bombmanual.com/print/KeepTalkingAndNobodyExplodes-BombDefusalManual-v1.pdf'
elements = os.listdir(DATA_PATH)
source_pdf = DATA_PATH + '/' + elements[0]

source_files = {'url':url,
              'url_pdf':url_pdf,
              'source_pdf':source_pdf}
source_text = {'url':None,
              'url_pdf':None,
              'source_pdf':None}

for source in source_files:
    try:
        text = extract_text(source_files[source])
        source_text[source] = len(text)
    except:
        print(f'There was a problem processing: {source}.\n')



print(f'The length of each source is: {source_text}.')







