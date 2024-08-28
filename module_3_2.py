def send_email(message, recipient, sender = 'university.help@gmail.com' ):
    is_recipient = 1
    is_sender = 1
    x = '@'
    a = '.com'
    b = '.ru'
    c = '.net'
    if x in recipient:
        if a in recipient:
            is_recipient = 1
        elif b in recipient:
            is_recipient = 1
        elif c in recipient:
            is_recipient = 1
        else:
            is_recipient = -1
    else:
        is_recipient = -1

    if x in sender:
        if a in sender:
            is_sender = 1
        elif b in sender:
            is_sender = 1
        elif c in sender:
            is_sender = 1
        else:
            is_sender = -1
    else:
        is_sender = -1

    if is_recipient < 0 or is_sender < 0:
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес ', recipient)
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif is_recipient > 0 and sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient,'.')
    elif is_sender > 0:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient,'.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')