import unittest
from unittest.mock import patch
from task import Circle, Rectangle, Triangle


class TestAssignment(unittest.TestCase):

    def test_case1(self):
        circle = Circle(5)

        with patch("builtins.print") as mock_print:
            print("Area: {:.2f}".format(circle.area()))

        mock_print.assert_called_once_with("Area: 78.54")

    def test_case2(self):
        circle = Circle(2.5)

        with patch("builtins.print") as mock_print:
            print("Area: {:.2f}".format(circle.area()))

        mock_print.assert_called_once_with("Area: 19.63")

    def test_case3(self):
        rectangle = Rectangle(10, 5)

        with patch("builtins.print") as mock_print:
            print("Area: {:.2f}".format(rectangle.area()))

        mock_print.assert_called_once_with("Area: 50.00")

    def test_case4(self):
        rectangle = Rectangle(7.5, 4)

        with patch("builtins.print") as mock_print:
            print("Area: {:.2f}".format(rectangle.area()))

        mock_print.assert_called_once_with("Area: 30.00")

    def test_case5(self):
        triangle = Triangle(8, 6)

        with patch("builtins.print") as mock_print:
            print("Area: {:.2f}".format(triangle.area()))

        mock_print.assert_called_once_with("Area: 24.00")

    def test_case6(self):
        triangle = Triangle(10, 12)

        with patch("builtins.print") as mock_print:
            print("Area: {:.2f}".format(triangle.area()))

        mock_print.assert_called_once_with("Area: 60.00")

if __name__ == "__main__":
    unittest.main()
