import unittest
import main


class TestStudent(unittest.TestCase):

    def test_walk(self):
        '''Первый тест: у одного объекта должен запускать метод walk 10 раз,
        после чего должен возвращаться результат сравнения полученных данных.
        В  случае провального теста должно выводится сообщение:
        Дистанции не равны [дистанция человека(объекта)] != 500'''

        student = main.Student('Student')

        for _ in range(10):
            student.walk()

        expected_dist = 50
        actual_dist = student.distance

        self.assertEqual(expected_dist, actual_dist,
                         msg=f'Distance of {student} is not correct '
                             f'Expected: {expected_dist} '
                             f'Actual: {actual_dist}')

    def test_run(self):
        '''у одного объекта должен запускать метод run 10 раз,
        после чего должен возвращаться результат сравнения полученных данных.
        В  случае провального теста должно выводится сообщение:
        Дистанции не равны [дистанция человека(объекта)] != 1000'''

        student = main.Student('Student')

        for _ in range(10):
            student.run()

        expected_dist = 100
        actual_dist = student.distance

        self.assertEqual(expected_dist, actual_dist,
                         msg=f'Distance of {student} is not correct '
                             f'Expected: {expected_dist} '
                             f'Actual: {actual_dist}')

        for _ in range(10):
            student.run()

    def test_competition(self):
        ''' 2 объекта "соревнуются", один "бежит", другой "идёт"
        (тот самый студент, кто не посещает вебинары).
        После чего должен возвращаться результат сравнения полученных данных.
        В  случае провального теста должно выводится сообщение:
        [бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек].'''

        student_1 = main.Student('First Student')
        student_2 = main.Student('Second Student')

        for _ in range(10):
            student_1.run()
            student_2.walk()

        self.assertGreater(student_1.distance, student_2.distance,
                           msg=f'Running {student_1} '
                               f'must cover more distance '
                               f'than a walking {student_2} ')


# if __name__ == '__name__':
#     unittest.main()
