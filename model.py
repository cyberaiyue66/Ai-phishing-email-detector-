import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import pickle


def train_model():
    # 1. Загрузка данных
    data = pd.read_csv("data/emails.csv")

    # 2. Разделение на train / test
    X_train, X_test, y_train, y_test = train_test_split(
        data["text"],
        data["label"],
        test_size=0.2,
        random_state=42
    )

    # 3. TF-IDF векторизация
    vectorizer = TfidfVectorizer(
    stop_words="english",
    min_df=1,   # Слово учитывается даже если встречается один раз
    max_df=1.0  # Игнорируем ограничение сверху
)
    

    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # 4. Обучение модели
    model = MultinomialNB()
    model.fit(X_train_vec, y_train)

    # 5. Оценка качества
    y_pred = model.predict(X_test_vec)

    print("Accuracy:", model.score(X_test_vec, y_test))
    print("\nClassification report:")
    print(classification_report(y_test, y_pred))

    # 6. Сохранение модели и векторизатора
    with open("model.pkl", "wb") as f:
        pickle.dump((vectorizer, model), f)


if __name__ == "__main__":
    train_model()