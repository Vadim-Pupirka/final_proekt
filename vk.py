import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from vk_api import VkUpload
from random import randint


def main():
    vk_session = vk_api.VkApi(
        token='68dadaae5ed0862c2d5cf7b427f05d65acf6e71c2727f06080ad367b73a56fe8a76734b7943ab24237137')
    longpoll = VkBotLongPoll(vk_session, 203543139)
    a = 0
    spisok = 0
    image = 'dead.png'
    upload = VkUpload(vk_session)
    slovar_sovet = {1: 'Имей позитивный настрой', 2: 'Найди дело по душе', 3: 'Упростите свою жизнь',
                    4: 'Занимайтесь спортом', 5: 'Посмотрите мотивирующие фильмы', 6: 'Правильно питайтесь',
                    7: 'Занимайтесь саморазвитием', 8: 'Будьте ближе к природе', 9: 'Выдайте себе индульгенцию',
                    10: 'Перестаньте быть как все '}
    spisok_drusei = ['странные', 'плохие', 'фиговые', 'уроды', 'дебилы']
    spisok_sebya = ['урод', 'уродина', 'не понимают', 'хочу умереть', 'не умею', 'дразнят']
    spisok_d = 0
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if a == 0:
                vk = vk_session.get_api()
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Здраствуйте вас приветствует психологический бот."
                                         "Выберете тему для разговора, "
                                         "друзья,семья,любовь,личность,булинг. Секретная функция:доработка и совет",
                                 random_id=random.randint(0, 2 ** 64))
                a = a + 1
        if event.obj.message['text'] == 'dead inside' and a == 1:
            attachments = []
            upload_image = upload.photo_messages(photos=image)[0]
            attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="",
                             random_id=random.randint(0, 2 ** 64), attachment=','.join(attachments))
            a = 0
        if event.obj.message['text'] == 'совет' and a == 1:
            sovet = slovar_sovet[randint(1, 10)]
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=sovet + " .Чтоб получить другой совет повторите действия.",
                             random_id=random.randint(0, 2 ** 64))
            a = 0
        if event.obj.message['text'] == 'булинг' and a == 1:
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Булинг одна из акутальных проблем любого школьника или взрослого. Булинг это"
                                     "травля другого человека, то чего не должно быть в жизни человека."
                                     "Ты должен сделать комплексную работу над ситуацией, "
                                     "должен признать проблему, поменять своё восприятие действительности, "
                                     "по возможности исправить реальные недостатки (если они присутствуют)"
                                     " и только после этого начать влиять на окружение. На этой ситуации мы закончим"
                                     "наш разговор, приятного время провождени.",
                             random_id=random.randint(0, 2 ** 64))
            a = 0
        if event.obj.message['text'] == 'доработка' and a == 1:
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Вас приветсвует функция доработка выберете какую функцию вы хотите доработать:"
                                     " личность или друзья",
                             random_id=random.randint(0, 2 ** 64))
            a = a + 1
        if event.obj.message['text'] == 'личность' and a == 2:
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Для доработки вводите слова через ';' с маленькой буквы без пробелов("
                                     "как миниум 2 слова).",
                             random_id=random.randint(0, 2 ** 64))
            a = a + 1
        if event.obj.message['text'] == 'друзья' and a == 2:
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Для доработки вводите слова через ';' с маленькой буквы без пробелов(как миниум"
                                     " 2 слова).",
                             random_id=random.randint(0, 2 ** 64))
            a = a + 2
        if a == 3 and ';' in event.obj.message['text']:
            perem1 = event.obj.message['text'].split(';')
            spisok_sebya = spisok_sebya + perem1
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Доработка для личности выполнина",
                             random_id=random.randint(0, 2 ** 64))
            a = 0
        if a == 4 and ';' in event.obj.message['text']:
            perem2 = event.obj.message['text'].split(';')
            spisok_drusei = spisok_drusei + perem2
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Доработка для друзей выполнина",
                             random_id=random.randint(0, 2 ** 64))
            a = 0
        if event.obj.message['text'] == 'друзья' and a == 1:
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Друзья самое важно что должно быть у человека, они "
                                     "могут помочь в трудных ситуациях.Опишите свою проблему"
                                     " страйтесь использовать как можно больше прилагательных.",
                             random_id=random.randint(0, 2 ** 64))
            a = a + 1
            spisok_d = 1
        for item in spisok_drusei:
            if item in event.obj.message['text'] and spisok_d == 1 and a == 2:
                vk = vk_session.get_api()
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="У друзей бывают и плюсы, и минусы, попытайтесь их"
                                         " проанализировать, как они относяться к вам, плохо или хорошо"
                                         " подумайте а друзья они вообще или нет. На этой ситуации мы закончим"
                                         "наш разговор, приятного время провождени.",
                                 random_id=random.randint(0, 2 ** 64))
                spisok_d = 0
                a = 0
        if event.obj.message['text'] == 'личность' and a == 1:
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Любовь к себе самое главное что должно быть в человеке, без "
                                     "любви к себе не возможно понять другого человека, быть с ним на одной волне, "
                                     "ведь главное в жизни не нажить себе врага внутри себя. Опишите свою проблему"
                                     " страйтесь использовать как можно больше прилагательных.",
                             random_id=random.randint(0, 2 ** 64))
            a = a + 1
            spisok = 1
        for item in spisok_sebya:
            if item in event.obj.message['text'] and spisok == 1 and a == 2:
                vk = vk_session.get_api()
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Попытайтесь разобраться в себе, сделайте мозговой штурм "
                                         "как можно исправить ваше положение, развейтесь попытайтесь "
                                         "меньше думать о негативных мыслях, помните что всегда лучше "
                                         "попытаться что то сделать чем жить в бездействии.На этой ситуации мы закончим"
                                         "наш разговор, приятного время провождени.",
                                 random_id=random.randint(0, 2 ** 64))
                spisok = 0
                a = 0
        if event.obj.message['text'] == 'семья' and a == 1:
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Семья это лучшее что есть у человека, очаг который"
                                     " укроет от всех невзгод и вырастит тебя, попробуйте описать свою проблему"
                                     " используйте как можно больше прилагательных",
                             random_id=random.randint(0, 2 ** 64))
            a = a + 1
        if ('плохая' in event.obj.message['text'] or 'не понимает' in event.obj.message['text'] or \
            'скучная' in event.obj.message['text'] or 'злая' in event.obj.message['text'] \
            or 'надоедливая' in event.obj.message['text']) and a == 2:
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="У каждой проблемы есть свой корень, попытайтесь проанализировать свою проблему"
                                     ", понять из чего она исходит, поговрите со своей семьей почти всегда можно найти"
                                     " выход из проблемы, просто попытайтесь если выхода совсему нету то надо"
                                     " предпринимать уже что то серьезное. На этой ситуации мы закончим"
                                     "наш разговор, приятного время провождения",
                             random_id=random.randint(0, 2 ** 64))
            a = 0
        if event.obj.message['text'] == 'любовь' and a == 1:
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Любовь - что может быть в том слове? "
                                     "Лишь буквы в слове , только и всего. "
                                     "А вдумайтесь немного , сколько там родного, "
                                     "И сколько нежности для сердца твоего! "
                                     "Рождается дитя и сразу - же любимо, "
                                     "Растет , и матери не чают в нем души ."
                                     "За руки водят, с ним неразделимы "
                                     "Родителям любовь даруют малыши. "
                                     "Проходит время , замуж вышла иль женился, "
                                     "Своих детей родили , в школу повели… "
                                     "С любовью в сердце мать за детей гордится, "
                                     "И внуков любит , дети счастье родили… "
                                     "Жить не любя...",
                             random_id=random.randint(0, 2 ** 64))
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Какая проблема в любви вас гложет, парень, девушка, друг?",
                             random_id=random.randint(0, 2 ** 64))
            a = a + 1
        if event.obj.message['text'] == 'парень' or event.obj.message['text'] == 'девушка' and a == 2:
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Попытайтесь разобраться в вашей проблеме, поговорите со своим партнером, "
                                     "иногда что то пытаться сохранить намного сложнее чем отпустить, "
                                     "но если вы по настояшему любите друг друга то вы сможете найти решение "
                                     "и попытаться не допускать больше таких ситуаций, на этой ситуации мы закончим"
                                     "наш разговор, приятного время провождения",
                             random_id=random.randint(0, 2 ** 64))
            a = 0
        if event.obj.message['text'] == 'друг' and a == 2:
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Посидите, раслабтесь, обдумайте свои чувства, посо"
                                     "ветуйтесь со своими близкими друзьями, может"
                                     "быть ваш друг станет вам чем то большим чем просто друг, а "
                                     "на этой ситуации мы закончим"
                                     "наш разговор, приятного время провождения",
                             random_id=random.randint(0, 2 ** 64))
            a = 0


if __name__ == '__main__':
    main()
