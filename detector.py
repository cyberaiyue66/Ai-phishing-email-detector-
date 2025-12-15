import pickle

def load_model():
    with open("model.pkl", "rb") as f:
        vectorizer, model = pickle.load(f)
    return vectorizer, model

def detect_email(text):
    vectorizer, model = load_model()
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]

    if prediction == "phishing":
        return "PHISHING DETECTED"
    else:
        return "Legit email"

if __name__ == "__main__":
    email = input("Введите текст письма:\n")
    print(detect_email(email))