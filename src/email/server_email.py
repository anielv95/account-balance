import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import find_dotenv,load_dotenv

_ = load_dotenv(find_dotenv())

def send_email(data):

    not_months_keys = {"account","email","total","debit","credit"}
    months = set(data.keys())-not_months_keys
    months_msg = ""
    for month_ in months:
        months_msg = months_msg+f"Number of transactions in {month_}: {data[month_]}<br>"

    to  = data["email"]
    
    username = str(os.environ["USER"])  
    password = str(os.environ["PASS"])  

    message = MIMEMultipart("alternative")
    message["Subject"] = data["account"]
    message["From"] = username
    message["To"] = to

    text = f"""\
    Hi,
    
    Here's a resume for your account balance

    Total balance is {data["total"]}
    Average debit amount: {data["debit"]}
    Average credit amount: {data["credit"]}
    {months_msg}"""

    html = f"""\
    <html>
    <body>
        <p>Hi,<br>
        <br>
        Here's a resume for your account balance<br>
        <br>
        Total balance is {data["total"]}<br>
        Average debit amount: {data["debit"]}<br>
        Average credit amount: {data["credit"]}<br>
        {months_msg}
        </p>
    </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)
    
    server = smtplib.SMTP(os.environ["SMTP"],os.environ["SMTP_PORT"])
    server.login(username,password)
    server.sendmail(username, to,message.as_string())
    server.quit()    

    return {"Status":"Email was sent"}