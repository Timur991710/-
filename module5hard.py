class User:
    '''''
    Класс пользователь никнейм и пароль и возраст
    '''''

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    '''''
    Класс видео содержит title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки 
    (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))     
    '''''

    def __init__(self, title: str, duration: int, adult_mode: bool = False, time_now = 0):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return  self.title == other.title

    def __contains__(self, item):
        return item in self.title

class UrTube:
    '''''
    Класс users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)     
    '''''

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None


    def log_in(self, login: str, password: str):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user




    def register(self, nickname: str, password: str, age: int):
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f"Такой пользователь {nickname}, зарегистрирован, войдите или зарегистрируйтесь под другим именем")
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user


    def regilog_out(self):
        self.current_user = None


    def add(self, *args):
        for movie in args:
            if movie not in self.videos:
                self.videos.append(movie)

    def get_videos(self, text: str):
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie


    def watch_video(self, movie):
        if not  self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for i in self.videos:
            if i.title == movie:
                if i.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return
                for j in range(i.duration):
                    print(j, end = " ")
                    i.time_now += 1
                    i.time_now = 0
                print("Конец видео")



if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
    ur.add(v1, v2)

# Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

# Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')