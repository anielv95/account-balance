import pandas as pd
import uuid
import datetime
import random
import numpy as np

account = str(uuid.uuid4())
email = "anielvillegas@gmail.com"
# initial_date = datetime.datetime.strptime("2024-02-17","%Y-%m-%d")

random.seed(42)

# number of records in csv file
entries = round(100 * random.random())

# number of months considered
months = round(10 * random.random()) + 2

percentages = np.array([random.random() for i in range(months)])

percentages = percentages / percentages.sum()

first_month = round((13 - months - 1) * random.random()) + 1
dates = []
transaction = []

for i in range(months):
    # entries_by_month.append(round(percentages[i]*entries))
    ith_month = first_month + i
    for j in range(round(percentages[i] * entries)):
        day = round(27 * random.random()) + 1
        dates.append(
            datetime.datetime.strptime(f"2023-{str(ith_month)}-{str(day)}", "%Y-%m-%d")
        )
        x = 100 * random.random()
        transaction.append(-x + 2 * x * round(random.random()))

df = pd.DataFrame(data={"Date": dates, "Transaction": transaction})
df["Id"] = df.index
df = df[["Id", "Date", "Transaction"]].copy()
df.to_csv("data/" + account + "_" + email + ".csv", index=False)
