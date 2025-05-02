import sys
from os.path import dirname, join, abspath
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sys.path.insert(0, abspath(join(dirname(__file__), "..")))


class messageCore:
    def __init__(self, fromTitle, fromEmail, toEmail, subject, body):
        self.fromTitle = fromTitle
        self.fromEmail = fromEmail
        self.toEmail = toEmail
        self.subject = subject
        self.body = body

    def messageBody(self):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = self.subject
        msg["From"] = f"{self.fromTitle} <{self.fromEmail}>"
        msg["To"] = self.toEmail

        # Optional: create plain text version by stripping tags
        plain_body = (
            self.body.replace("<br>", "\n")
            .replace("<br/>", "\n")
            .replace("<strong>", "")
            .replace("</strong>", "")
        )

        # Attach both plain and HTML (some email clients prefer plain text)
        msg.attach(MIMEText(plain_body, "plain"))
        msg.attach(MIMEText(self.body, "html"))

        return msg.as_string()
