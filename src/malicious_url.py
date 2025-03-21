from tld import get_tld
from googlesearch import search
from urllib.parse import urlparse
import numpy as np
import re
import joblib
import os

model = joblib.load("artifact/model/malicious_url/URL_detection_random_forest_model.pkl")

#Use of IP or not in domain
def having_ip_address(url: str) -> int:
  match = re.search(
      '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
      '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
      '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
      '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # Ipv6
  if match:
      # print match.group()
      return 1
  else:
      # print 'No matching pattern found'
      return 0

def google_index(url):
    site = search(url, 5)
    return 1 if site else 0


def abnormal_url(url):
  hostname = urlparse(url).hostname
  hostname = str(hostname)
  match = re.search(hostname, url)
  if match:
      # print match.group()
      return 1
  else:
      # print 'No matching pattern found'
      return 0

def suspicious_words(url):
  match = re.search('PayPal|login|signin|bank|account|update|free|lucky|service|bonus|ebayisapi|webscr',
                    url)
  if match:
      return 1
  else:
      return 0

def digit_count(url):
    digits = 0
    for i in url:
        if i.isnumeric():
            digits = digits + 1
    return digits

def letter_count(url):
    letters = 0
    for i in url:
        if i.isalpha():
            letters = letters + 1
    return letters

#First Directory Length
def fd_length(url):
    urlpath= urlparse(url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0

def tld_length(tld):
    try:
        return len(tld)
    except:
        return -1

def shortening_service(url):
    match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                      'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                      'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                      'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                      'db\.tt|qr\.ae|adataset\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                      'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                      'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                      'tr\.im|link\.zip\.net',url)
    if match:
        return 1
    else:
        return 0

def url_length(url):
    return len(str(url))

def hostname_length(url):
    return len(urlparse(url).netloc)

def count_www(url):
    url.count('www')
    return url.count('www')

def count_https(url):
    return url.count('https')

def count_http(url):
    return url.count('http')

def count_dot(url):
    count_dot = url.count('.')
    return count_dot

def count_per(url):
    return url.count('%')

def count_ques(url):
    return url.count('?')

def count_hyphen(url):
    return url.count('-')

def count_equal(url):
    return url.count('=')

def count_atrate(url):
    return url.count('@')

def no_of_dir(url):
    urldir = urlparse(url).path
    return urldir.count('/')

def no_of_embed(url):
    urldir = urlparse(url).path
    return urldir.count('//')


def get_url(url):

  status = []

  status.append(having_ip_address(url))
  status.append(abnormal_url(url))
  status.append(count_dot(url))
  status.append(count_www(url))
  status.append(count_atrate(url))
  status.append(no_of_dir(url))
  status.append(no_of_embed(url))

  status.append(shortening_service(url))
  status.append(count_https(url))
  status.append(count_http(url))

  status.append(count_per(url))
  status.append(count_ques(url))
  status.append(count_hyphen(url))
  status.append(count_equal(url))

  status.append(url_length(url))
  status.append(hostname_length(url))
  status.append(suspicious_words(url))
  status.append(digit_count(url))
  status.append(letter_count(url))
  status.append(fd_length(url))
  tld = get_tld(url,fail_silently=True)

  status.append(tld_length(tld))

  return status


def ULR_Detections(test_url):
    try:

        features_test = get_url(test_url)
        #print(features_test)
        features_test = np.array(features_test).reshape((1, -1))
        #print(features_test)

        pred = model.predict(features_test)
        if int(pred[0]) == 0:
            res="Bening"
            return res

        elif int(pred[0]) == 1:
            res="Defacement"
            return res

        elif int(pred[0]) == 2:
            res="Phising"
            return res

        elif int(pred[0]) == 3:
            res="Malware"
            return res
    except Exception as e:
        return None
