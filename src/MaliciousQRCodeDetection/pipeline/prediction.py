import joblib
import pandas as pd
import numpy as np
import os
from tld import get_tld
from urllib.parse import urlparse
import re
from tensorflow.keras.models import load_model
from pathlib import Path
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


class PredictionPipeline:
    def __init__(self):
        self.model = load_model(Path("artifacts\model_training\model.keras"))
        self.scaler = joblib.load(Path(r"artifacts\feature_engineering\scaler.joblib"))
    
    def extract_url_domain(self,url):
        try:
            res = get_tld(url, as_object=True, fail_silently=False, fix_protocol= True)
            pri_domain = res.parsed_url.netloc
        except:
            pri_domain = None

        return pri_domain
    
    def url_len(self,url):
        length = str(len(url))
        return length
    

    def httpSecure(self,url):
        https = urlparse(url).scheme
        match = str(https)

        if match == 'https':
            return 0
        else:
            return 1
        
    def no_of_digits(self,url):
        digits = 0
        for i in url:
            if i.isnumeric():
                digits+=1

        return digits
    
    def letter_count(self,url):
        letter = 0
        for i in url:
            if i.isalpha():
                letter+=1

        return letter
    
    def Shortining_Service(self,url):
        match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                          'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                          'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                          'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                          'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                          'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                          'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                          'tr\.im|link\.zip\.net',
                          url)
        if match:
            return 1
        else:
            return 0
        
    def having_ip_address(self,url):
        match = re.search(
            '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
            '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
            '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
            '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4 with port
            '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
            '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}|'
            '([0-9]+(?:\.[0-9]+){3}:[0-9]+)|'
            '((?:(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d|\d)(?:\/\d{1,2})?)', url)  # Ipv6
        if match:
            return 1
        else:
            return 0
        
    #first directory length    
    def fd_length(self,url):
        urlpath = urlparse(url).path
        try:
            return len(urlpath.split('/')[1])
        except:
            return 0
        
    def no_of_dir(self,url):
        urldir = urlparse(url).path
        return urldir.count('/')

    def process_urls_test_raw(self,urls):

        data = {}
        feature = ['@','?','-','=','.','#','%','+','$','!','*',',','//']
    
        data = {
            'url_len': urls.apply(lambda i: self.url_len(i)),
            'httpSecure': urls.apply(lambda i: self.httpSecure(i)),
            'no_of_digits':urls.apply(lambda i: self.no_of_digits(i)),
            'letter_count':urls.apply(lambda i: self.letter_count(i)),
            'Shortining_Service':urls.apply(lambda i: self.Shortining_Service(i)),
            'having_ip_address':urls.apply(lambda i: self.having_ip_address(i)),
            'path_length': urls.apply(lambda i: len(urlparse(i).path)),
            'fd_length': urls.apply(lambda i: self.fd_length(i)),
            'count-www': urls.apply(lambda i: i.count('www')),
            'count-dir': urls.apply(lambda i: self.no_of_dir(i))       
        }
    
        for a in feature:
            data[a] = urls.apply(lambda i: i.count(a))
    
        return pd.DataFrame(data)

    def get_url(self,qrcode):
        decoded_data = decode(Image.open(qrcode))
        qr_url = decoded_data[0].data.decode("utf-8")
        return qr_url
    
    def predict_url(self,qr_url):

        urls = pd.Series(qr_url)

        features_df = self.process_urls_test_raw(urls)

        features_scaled = self.scaler.transform(features_df)

        predictions = self.model.predict(features_scaled)

        return predictions[0]


if __name__ == "__main__":
    # Example usage
    pipeline = PredictionPipeline()
    qr_code_path = r"research\tbc_qr_code.png"
    try:
        qr_url = pipeline.get_url(qr_code_path)
        prediction = pipeline.predict_url(qr_url)
        print(f"URL: {qr_url}")
        print(f"Prediction: {'Safe' if prediction < 0.5 else 'Not Safe'}")
    except Exception as e:
        print(f"Error: {e}")