def get_email(file_name):
    splitted = file_name.split("_")
    account = splitted[0]
    splitted = "_".join(splitted[1:])
    splitted = splitted.split(".csv")
    email = ".csv".join(splitted[:-1])
    return account, email
