# Gmail SMTP Email Automation 📧

A Python-based email automation system that uses Gmail's SMTP service to
send personalized emails to multiple recipients automatically.

The system reads recipient information from a CSV file containing names
and email addresses, dynamically customizes the email content for each
recipient, and sends individual emails without requiring manual
intervention.

## 🚀 Features

-   **Automated Email Sending:** Automatically sends emails to multiple
    recipients listed in a CSV file.
-   **CSV Integration:** Reads recipient names and email addresses
    directly from a CSV file.
-   **Personalized Emails:** Dynamically customizes email content using
    individual recipient details.
-   **Gmail SMTP Integration:** Uses Python's built-in `smtplib` library
    to establish an SMTP connection with Gmail.
-   **HTML Email Support:** Supports structured HTML email templates for
    professional-looking emails.
-   **Secure Credentials:** Uses environment variables and `.env` files
    to manage sensitive credentials.
-   **Reusable Code:** Designed to be easily adapted for recruitment
    notifications, event invitations, announcements, and other email
    campaigns.

## 🛠️ Tech Stack

  Technology      Purpose
  --------------- --------------------------------
  Python          Core programming language
  smtplib         Gmail SMTP communication
  email           Email message construction
  csv             Reading recipient data
  python-dotenv   Managing environment variables

## 📂 Project Structure

``` text
gmail-smtp-email-automation/
│
├── main.py              # Main automation script
├── recipients.csv       # Recipient names and email addresses
├── .env                 # Email credentials and configuration
├── .gitignore           # Files excluded from Git
└── README.md            # Project documentation
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

``` bash
git clone https://github.com/YOUR_USERNAME/gmail-smtp-email-automation.git

cd gmail-smtp-email-automation
```

### 2. Install Dependencies

``` bash
pip install -r requirements.txt
```

### 3. Configure Gmail SMTP & Generate App Password

To send emails using Gmail SMTP, you need to generate a **Google App
Password**.

Follow these steps:

1.  Open your [Google Account Security
    Settings](https://myaccount.google.com/security).
2.  Navigate to **How you sign in to Google**.
3.  Enable **2-Step Verification** if it is not already enabled.
4.  After enabling it, navigate to **App Passwords**.
5.  Enter an app name (e.g., `Python Email Automation`).
6.  Click **Create**.
7.  Google will generate a 16-character App Password.
8.  Copy this password and use it in your project's `.env` file.

**Note:** App Passwords require 2-Step Verification and may not be
available for certain Google accounts, such as accounts with Advanced
Protection or organization-managed restrictions.

#### Configure the `.env` File

Create a file named `.env` in the root directory of your project:

``` env
SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_16_character_app_password
```

Replace the placeholder values with your Gmail address and the generated
App Password.

**Important Security Notes:**

-   Use the generated App Password, NOT your regular Gmail password.
-   Never share your App Password.
-   Never upload your `.env` file to GitHub.
-   Add `.env` to your `.gitignore` file to prevent accidental exposure.

### 4. Prepare the CSV File

Create a `recipients.csv` file containing recipient information.

Example:

``` csv
Name,Email
Rahul,rahul@example.com
Priya,priya@example.com
Aman,aman@example.com
```

### 5. Run the Automation

``` bash
python main.py
```

The script reads the CSV file, generates personalized email content for
each recipient, and sends the emails using Gmail SMTP.

## ✉️ How It Works

1.  Loads Gmail credentials securely using environment variables.
2.  Reads recipient information from the CSV file.
3.  Extracts individual names and email addresses.
4.  Dynamically generates personalized email content.
5.  Establishes an SMTP connection with Gmail.
6.  Sends individual emails to the respective recipients.

## 💡 Use Cases

-   College recruitment and selection notifications.
-   Event invitations and announcements.
-   Internship and application updates.
-   Personalized communication.
-   Automated organizational emails.

## 🔒 Security & Best Practices

-   Store credentials in `.env` files.
-   Add `.env` and sensitive CSV files to `.gitignore`.
-   Never hardcode passwords in Python scripts.
-   Use Google App Passwords instead of your regular Gmail password.
-   Respect Gmail sending limits and avoid unsolicited bulk emails.

## 🔮 Future Improvements

-   Email delivery and failure logging.
-   Email attachments support.
-   Interactive HTML email templates.
-   Sending reports and delivery statistics.
-   Duplicate recipient detection.
-   Retry mechanism for failed emails.
-   Support for multiple email templates.

## 👨‍💻 Author

**Diamond Taneja**

B.Tech Student \| Python & Software Development Enthusiast

------------------------------------------------------------------------

⭐ If you find this project useful, consider giving the repository a
star!
