import glob
import pandas as pd

def load_train(train_csv_path, text_folder):
    train = pd.read_csv(train_csv_path, index_col=0)
    texts = []

    for file in sorted(glob.glob(text_folder + "/*.txt")):
        with open(file) as f:
            texts.append(f.read())

    train["text"] = texts
    return train

def load_test(test_folder):
    texts = []
    for file in sorted(glob.glob(test_folder + "/*.txt")):
        with open(file) as f:
            texts.append(f.read())

    return pd.DataFrame({"text": texts})
