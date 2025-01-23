from MaliciousQRCodeDetection.logging.logger import logger
from MaliciousQRCodeDetection.exception import MaliciousQRException
from tld import get_tld
from urllib.parse import urlparse
import re
import pandas as pd
import numpy as np
from MaliciousQRCodeDetection.entity.config_entity import FeatureEngineeringConfig
import os
from sklearn.model_selection import train_test_split
import pickle
from sklearn.preprocessing import StandardScaler
from joblib import dump
import sys


class FeatureEngineering:
    def __init__(self,config: FeatureEngineeringConfig):
        self.config = config


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
    
    def process_urls(self,df):

        feature = ['@','?','-','=','.','#','%','+','$','!','*',',','//']

        df['url_len'] = df['url'].apply(lambda i: self.url_len(i))
        df['httpSecure'] = df['url'].apply(lambda i: self.httpSecure(i))
        df['no_of_digits'] = df['url'].apply(lambda i: self.no_of_digits(i))
        df['letter_count'] = df['url'].apply(lambda i: self.letter_count(i))
        df['Shortining_Service'] = df['url'].apply(lambda i: self.Shortining_Service(i))
        df['having_ip_address'] = df['url'].apply(lambda i: self.having_ip_address(i))
        df['path_length'] = df['url'].apply(lambda i: len(urlparse(i).path))
        df['fd_length'] = df['url'].apply(lambda i: self.fd_length(i))
        df['count-www'] = df['url'].apply(lambda i: i.count('www'))
        df['count-dir'] = df['url'].apply(lambda i: self.no_of_dir(i))

        for a in feature:
            df[a] = df['url'].apply(lambda i: i.count(a))

        return df

    # get csv and read in dataframe format
    def train_test_split(self):

        csvPath = self.config.csv_file
        logger.info('csv file downloaded successfully for feature engineering')

        df = pd.read_csv(csvPath)
        logger.info('csv to DataFrame done..')

        df = self.process_urls(df)
        logger.info('all features extracted successfully..')

        df = df.drop(columns=['url','label'])
        logger.info('unnecessay columns dropped successfully..')

        train,test = train_test_split(df,test_size=0.2,random_state=42)
        logger.info('Train Test split successfully..')

        # Separate features and target
        X_train = train.drop(columns=['result'])
        y_train = train['result']
        X_test = test.drop(columns=['result'])
        y_test = test['result']
        logger.info('X_train,y_train,X_test,y_test splitted sucessfully..')

        # scale the features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        logger.info('Data scaled sucessfully..')

        #combine scaled features with target column for saving
        train = pd.DataFrame(X_train_scaled,columns=X_train.columns)
        train['result'] = y_train.reset_index(drop=True)

        test = pd.DataFrame(X_test_scaled,columns=X_test.columns)
        test['result'] = y_test.reset_index(drop=True)
        logger.info('New scaled train and test df made sucessfully..')

        train.to_csv(self.config.train_data, index=False)
        test.to_csv(self.config.test_data,index=False)
        logger.info('New scaled train and test df saved sucessfully..')

        dump(scaler,self.config.scaler_file)
        logger.info('scaler.joblib saved sucessfully..')
    