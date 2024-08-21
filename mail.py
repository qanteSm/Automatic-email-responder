import imaplib
import email
from email.mime.text import MIMEText
import smtplib
import time

EMAIL_ADDRESS = "iletisim@alibuyuk.net" # mail adresi
EMAIL_PASSWORD = "" # şifre

IMAP_SERVER = "server"
IMAP_PORT = 993  # port

SMTP_SERVER = "server"
SMTP_PORT = 465 # port

NOTIFF_MAIL = "muhammetalibyk@gmail.com" # mail geldiğinde notiff gönderilecek mail adresi

NON_REPLY_KEYWORDS = ["noreply", "no-reply", "donotreply", "do-not-reply", "automated", "auto-generated"]

with open("mail.html", "r") as f:
    EMAIL_TEMPLATE = f.read()

def yeni_epostaları_kontrol_et():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        mail.select("inbox")
        status, data = mail.search(None, 'UNSEEN')
        email_ids = data[0].split()
        return email_ids
    except Exception as e:
        print(f"Yeni epostalar kontrol edilirken hata oluştu: {e}")
        return []

def insan_epostası_mı(email_message):
    from_address = email_message["From"]
    subject = email_message["Subject"]
    body = email_message.get_payload(decode=True)
    if body is not None:
        try:
            body = body.decode("utf-8", errors="ignore")
        except AttributeError:
            body = ""
    else:
        body = ""

    for keyword in NON_REPLY_KEYWORDS:
        if keyword in from_address.lower() or keyword in subject.lower() or keyword in body.lower():
            return False
    return True

def cevap_epostası_gönder(email_message):
    try:
        sender_name = email.utils.parseaddr(email_message["From"])[0]
        reply_message = EMAIL_TEMPLATE.replace("[Gönderen Adı]", sender_name)

        msg = MIMEText(reply_message, 'html')
        msg["Subject"] = f"Re: {email_message['Subject']}"
        msg["To"] = email_message["From"]
        msg["From"] = EMAIL_ADDRESS

        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Cevap epostası başarıyla gönderildi!")
    except Exception as e:
        print(f"Cevap epostası gönderilirken hata oluştu: {e}")

def bildirim_epostası_gönder(email_message):
    try:
        sender = email_message["From"]
        subject = email_message["Subject"]
        date = email_message["Date"]
        body = email_message.get_payload(decode=True)
        if body is not None:
            try:
                body = body.decode("utf-8", errors="ignore")
            except AttributeError:
                body = "" 

        notification_message = f"""
        Konu: Yeni Eposta Aldınız

        Yeni bir eposta aldınız:

        Kimden: {sender}
        Konu: {subject}
        Tarih: {date}
        İçerik: {body}
        """

        msg = MIMEText(notification_message)
        msg["Subject"] = "Yeni Eposta Aldınız"
        msg["To"] = NOTIFF_MAIL # mail geldiği belirtilcek mail
        msg["From"] = EMAIL_ADDRESS

        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Bildirim epostası başarıyla gönderildi!")
    except Exception as e:
        print(f"Bildirim epostası gönderilirken hata oluştu: {e}")

if __name__ == "__main__":
    while True:
        yeni_email_idler = yeni_epostaları_kontrol_et()

        if yeni_email_idler:
            print(f"{len(yeni_email_idler)} yeni eposta bulundu.")
            with imaplib.IMAP4_SSL(IMAP_SERVER) as mail:
                mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                mail.select("inbox")
                for email_id in yeni_email_idler:
                    status, data = mail.fetch(email_id, "(RFC822)")
                    email_message = email.message_from_bytes(data[0][1])

                    if insan_epostası_mı(email_message):
                        cevap_epostası_gönder(email_message)

                    bildirim_epostası_gönder(email_message)
        else:
            print("Yeni eposta bulunamadı.")

        time.sleep(30)