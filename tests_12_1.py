import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_runner = Runner('fedor')
        for _ in range(10):
            test_runner.walk()
            return test_runner
        self.assertEqual(test_runner.walk(), 50)
    def test_run(self):
        test_runner = Runner('werden')
        for _ in range(10):
            test_runner.run()
            return test_runner
        self.assertEqual(test_runner.run(), 100)

    def test_challenge(self):
        tes_run = Runner('qwerty')
        tes_run_1 = Runner('gogi')
        for _ in range(10):
            tes_run.walk()
            tes_run.run()
            tes_run_1.walk()
            tes_run_1.run()
            return tes_run, tes_run_1
        self.tes_run_1(tes_run, tes_run_1)