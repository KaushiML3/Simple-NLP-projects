
import joblib


# Load the HashingVectorizer
hv_loaded = joblib.load('artifact/model/js/hashing_vectorizer.pkl')
tfidf_loaded = joblib.load('artifact/model/js/tfidf_transformer.pkl')
model=joblib.load("artifact/model/js/xgb_model.pkl")

class_names=["not_obfuscated","obfuscated"]
def js_classification(js_text):

    try:
        test_normal = hv_loaded .transform([js_text])
        test_normal = tfidf_loaded.transform(test_normal)
        result_array = model.predict(test_normal)
        print("Result: ", class_names[result_array[0]])
        return class_names[result_array[0]]
    except Exception as e:
        return None