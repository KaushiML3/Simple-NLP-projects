from keras.models import load_model
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import *
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import nltk
nltk.download('stopwords')



# Load model
model_spam = load_model('artifact/model/spam_massage/spam_massage.keras')

# loading
with open('artifact/model/spam_massage/tokenizer_spam.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


def pre_text(tweet):
    ''' Convert tweet text into a sequence of words '''

    # convert to lowercase
    text = tweet.lower()
    # remove non letters
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    # tokenize
    words = text.split()
    # remove stopwords
    words = [w for w in words if w not in stopwords.words("english")]
    # apply stemming
    words = [PorterStemmer().stem(w) for w in words]
    # return list

    final_text=' '.join(words)
    return final_text



def predict_spam(text):
    try:
        '''Function to predict sentiment class of the passed text'''

        sentiment_classes = ['ham', 'spam']
        max_len=100
        final_text=pre_text(text)
        #print(pro_text)
        # Transforms text to a sequence of integers using a tokenizer object
        xt = tokenizer.texts_to_sequences([final_text])
        # Pad sequences to the same length
        xt = pad_sequences(xt, padding='post', maxlen=max_len)
        # Do the prediction using the loaded model
        yt = model_spam .predict(xt).argmax(axis=1)
        #print(yt)
        # Print the predicted sentiment
        print('The predicted sentiment is', sentiment_classes[yt[0]])
        return sentiment_classes[yt[0]]
    
    except Exception as e:
        return None