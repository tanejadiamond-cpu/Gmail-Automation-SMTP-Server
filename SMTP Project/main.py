import os
import csv
import smtplib  #Built-in

from dotenv import load_dotenv
from email.message import EmailMessage

# Load environment variables
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
TEST_LINK = os.getenv("TEST_LINK")


def create_email(name, receiver_email):

    msg = EmailMessage()

    msg["Subject"] = "ACM Recruitment | Quiz Round"
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email

    # WRITE YOUR EMAIL MESSAGE HERE
    body = f"""
Hi {name},

You are shortlisted for the ACM Quiz Round.

Here is the link for the test:

{TEST_LINK}

Best of luck!

Regards,
ACM Thapar Student Chapter
"""

    msg.set_content(body)

    return msg


def send_emails():

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

        server.login(SENDER_EMAIL, APP_PASSWORD)

        with open("students.csv", "r", encoding="utf-8-sig") as file:

            reader = csv.DictReader(file)

            for row in reader:

                name = row["Name"].strip()
                email = row["Email"].strip()

                msg = create_email(name, email)

                server.send_message(msg)

                print(f"Email sent to {name} ({email})")


if __name__ == "__main__":
    send_emails()
