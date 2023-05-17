import requests
from bs4 import BeautifulSoup
import os

file_path=os.listdir('./')
for file in file_path:
    if 'jpg' in file:
        os.remove(file)