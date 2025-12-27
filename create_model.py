import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7],
    "attendance": [40, 50, 60, 70, 80, 90, 95],
    "internal_marks": [30, 40, 45, 55, 65, 75, 85],
    "result": [0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["study_hours", "attendance", "internal_marks"]]
y = df["result"]

model = LogisticRegression()
model.fit(X, y)

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("model.pkl created successfully")
