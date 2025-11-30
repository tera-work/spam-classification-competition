import pandas as pd

def inference(model, vectorizer, test_df, save_path="submission.csv"):
    test_vec = vectorizer.transform(test_df["text_clean"]).toarray()
    preds = model.predict(test_vec)
    submit = pd.DataFrame({"id": test_df.index, "label": preds})
    submit.to_csv(save_path, index=False)
    print(f"Saved: {save_path}")
