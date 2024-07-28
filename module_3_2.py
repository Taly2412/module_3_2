def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if "@" not in (recipient and sender) or not (recipient.endswith(".com") or recipient.endswith(".ru")
                                                 or recipient.endswith(".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")

    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 's.tasha@inbox.ru', sender='urban.info@gmail.com')
