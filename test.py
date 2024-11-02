import unittest
from main import AiChatBot
class TestAiChatBot(unittest.TestCase):
    def setUp(self):
        self.bot = AiChatBot()

    def test_addition(self):
        result = self.bot.calculate("1", 10, 5)
        self.assertEqual(result, 15)

    def test_division_by_zero(self):
        result = self.bot.calculate("4", 10, 0)
        self.assertEqual(result, "Error: Division by zero is not allowed.")

if __name__ == "__main__":
    unittest.main()