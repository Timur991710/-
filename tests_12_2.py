import unittest



class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers




class TestTournament(unittest.TestCase):
        all_results = None

        @classmethod
        def setUpClass(cls):
            cls.all_results = {}


        def setUp(self):

            self.bedun_1 = Runner('Усэйн', 10)
            self.bedun_2 = Runner('Андрей', 9)
            self.bedun_3 = Runner('Ник', 3)

        def test_tournament_1(self):
            test_z = Tournament(90, self.bedun_1, self.bedun_3)
            result = test_z.start()
            TestTournament.all_results[1] = result
            self.assertTrue(result[2] == self.bedun_3.name)

        def test_tournament_2(self):
            test_z = Tournament(90, self.bedun_2, self.bedun_3)
            result = test_z.start()
            TestTournament.all_results[2] = result
            self.assertTrue(result[2] == self.bedun_3.name)

        def test_tournament_3(self):
            test_z = Tournament(90, self.bedun_1, self.bedun_2, self.bedun_3)
            result = test_z.start()
            TestTournament.all_results[3] = result
            self.assertTrue(result[1] == self.bedun_1.name)


        @classmethod
        def tearDownClass(cls):
            for rezult in cls.all_results.values():
                print(rezult)
