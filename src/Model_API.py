from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from src.preprocessing import pre_processing
from src.Scrapping import Seller_Comment
import pandas as pd


def predict_ML(url):
    seller_comment = Seller_Comment(url)
    com = pre_processing(seller_comment)
    com = ' '.join(map(str, com))

    dataset_train = "dataset/MyDF.csv"
    df = pd.read_csv(dataset_train)

    tfidf_vect_ngram = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', ngram_range=(2,3), max_features=5000)
    tfidf_vect_ngram.fit(df['text'].fillna(''))
    model = joblib.load('src/Navie_ngram.sav')
    tfidf_t = tfidf_vect_ngram.transform([com])

    prediction = model.predict(tfidf_t)
    results = ' '.join([str(elem) for elem in prediction])
    return results
