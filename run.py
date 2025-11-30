from src.load_data import load_train, load_test
from src.preprocess import preprocess_text
from src.train import train_model
from src.inference import inference

train_df = load_train("train_master.csv", "train2")
test_df = load_test("test2")

train_df = preprocess_text(train_df)
test_df = preprocess_text(test_df)

model, vec, score = train_model(train_df)
print("Validation F1:", score)

inference(model, vec, test_df, "submission.csv")
