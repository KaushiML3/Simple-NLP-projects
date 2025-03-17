
import re
import pickle


with open('artifact/model/language/Language_detection_model_v1.pkl', 'rb') as file:
    model_language = pickle.load(file)

with open('artifact/model/language/Language_encoder.pkl', 'rb') as file:
    encode_language = pickle.load(file)


# function to clean text
def clean_txt(text):
    text=str(text)
    text=text.lower()
    text=re.sub(r'[^\w\s]',' ',text)
    text=re.sub(r'[_0-9]',' ',text)
    text=re.sub(r'\s\s+',' ',text)
    return text

def predict_language(text):
    try:
        pred =model_language.predict([clean_txt(text)])
        ans = encode_language.inverse_transform(pred)
        return ans[0]
    except Exception as e:
        return None