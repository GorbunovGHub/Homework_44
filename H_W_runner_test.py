import unittest
import runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        object_runner = runner.Runner('Alex')
        for i in range(10):
            object_runner.walk()
        self.assertEqual(object_runner.distance, 50)

    def test_run(self):
        object_runner = runner.Runner('Sofia')
        for i in range(10):
            object_runner.run()
        self.assertEqual(object_runner.distance, 100)

    def test_challenge(self):
        object_runner_1 = runner.Runner('Paul')
        object_runner_2 = runner.Runner('Dominik')
        for i in range(10):
            object_runner_1.walk()
            object_runner_2.run()
        self.assertNotEqual(object_runner_1.distance, object_runner_2.distance)


if __name__ == "__main__":
    unittest.main()
