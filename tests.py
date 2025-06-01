import unittest
from pinsite import age, faculties, Groups, names,secondnames,lastnames

class TestSite(unittest.TestCase):

    def test_string(self):
        self.assertEqual(age("1"), 1)
        self.assertEqual(age("-2"), "That's wrong")
        self.assertEqual(age(" "), "That's wrong")
        self.assertEqual(age("#"), "That's wrong")
        self.assertEqual(age("121"), "That's wrong")
        self.assertEqual(age("mathematic"), "That's wrong")
        self.assertEqual(age(1.2), "That's wrong")

    def test_faculties(self):
        self.assertEqual(faculties("ФГО"), "ФГО")
        self.assertEqual(faculties("ВГО"), "That's wrong")

    def test_groups(self):
        self.assertEqual(Groups("ПИН-241"), "ПИН-241")
        self.assertEqual(Groups("ПИН-243"), "That's wrong")


    def test_names(self):
        self.assertEqual(names("Никита"), "Никита")
        self.assertEqual(names(1.2), "That's wrong")
        self.assertEqual(names(" "), "That's wrong")

    def test_secondname(self):
        self.assertEqual(secondnames("Кибкало"), "Кибкало")
        self.assertEqual(secondnames(1.2), "That's wrong")
        self.assertEqual(secondnames(" "), "That's wrong")

    def test_lastnames(self):
        self.assertEqual(lastnames("Александрович"), "Александрович")
        self.assertEqual(lastnames(1.2), "That's wrong")
        self.assertEqual(lastnames(" "), "That's wrong")