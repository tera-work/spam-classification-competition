import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.metrics import f1_score

def train_model(train_df):
    X = train_df["text_clean"]
    y = train_df["label"]

    vectorizer = CountVectorizer()
    X_vec = vectorizer.fit_transform(X).toarray()

    kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = []

    for train_idx, valid_idx in kf.split(X_vec, y):
        model = MultinomialNB()
        model.fit(X_vec[train_idx], y.iloc[train_idx])
        pred = model.predict(X_vec[valid_idx])
        scores.append(f1_score(y.iloc[valid_idx], pred))

    return model, vectorizer, np.mean(scores)
