from termcolor import cprint
import smtplib


class Email_Sender:
    def __init__(self) -> None:
        self.app_password = "your app password"
        self.app_email = "your email"
        pass

    def send_mail(self, email, password, message):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)
            cprint("[+] Sending Email......", "green")
            server.sendmail(email, email, message)
            cprint("[+] Message Sent.......", "green")
            server.quit()
        except Exception as ex:
            cprint(f"[+]Error Send Mail:{str(ex)}", "red")
