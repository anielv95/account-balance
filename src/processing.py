import pandas as pd
from io import StringIO


def calculate_values(account_, email_, df_):
    df_ = pd.read_json(StringIO(df_), orient="records")
    results = {}
    results["account"] = account_
    results["email"] = email_

    df_["Date"] = pd.to_datetime(df_["Date"], format="%Y-%m-%d")
    df_["month"] = df_["Date"].apply(lambda x: x.strftime("%B"))

    monthly_transactions = df_.groupby("month", as_index=False)[["Transaction"]].count()

    results["total"] = round(float(df_["Transaction"].sum()),2)
    results["debit"] = round(float(df_[df_["Transaction"] < 0]["Transaction"].mean()),2)
    results["credit"] = round(float(df_[df_["Transaction"] > 0]["Transaction"].mean()),2)
    for month_ in monthly_transactions["month"].values:
        results[month_] = int(
            monthly_transactions[monthly_transactions["month"] == month_][
                "Transaction"
            ].values[0]
        )

    return results
