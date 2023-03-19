class MailDto:
    def __init__(self, from_email: str, to_emails: list, subject: str, content: str):
        self.from_email = from_email
        self.to_emails = to_emails
        self.subject = subject
        self.content = content
