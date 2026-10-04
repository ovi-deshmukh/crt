import unittest
from unittest.mock import patch
from task import UPI, CreditCard, Cash


class TestAssignment(unittest.TestCase):

    def test_case1(self):
        payment = UPI()

        with patch("builtins.print") as mock_print:
            payment.pay(500)

        mock_print.assert_called_once_with(
            "Payment of", 500, "successful using UPI"
        )

    def test_case2(self):
        payment = UPI()

        with patch("builtins.print") as mock_print:
            payment.pay(1500)

        mock_print.assert_called_once_with(
            "Payment of", 1500, "successful using UPI"
        )

    def test_case3(self):
        payment = CreditCard()

        with patch("builtins.print") as mock_print:
            payment.pay(2500)

        mock_print.assert_called_once_with(
            "Payment of", 2500, "successful using Credit Card"
        )

    def test_case4(self):
        payment = CreditCard()

        with patch("builtins.print") as mock_print:
            payment.pay(5000)

        mock_print.assert_called_once_with(
            "Payment of", 5000, "successful using Credit Card"
        )

    def test_case5(self):
        payment = Cash()

        with patch("builtins.print") as mock_print:
            payment.pay(1000)

        mock_print.assert_called_once_with(
            "Payment of", 1000, "successful using Cash"
        )

    def test_case6(self):
        payment = Cash()

        with patch("builtins.print") as mock_print:
            payment.pay(750)

        mock_print.assert_called_once_with(
            "Payment of", 750, "successful using Cash"
        )


if __name__ == "__main__":
    unittest.main()