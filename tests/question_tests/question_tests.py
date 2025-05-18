#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_b.question_b import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_question_b_config(self):
        self.assertEqual((2, 4, 10), get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT"))
    def test_question_c_config(self):
        self.assertEqual((2, 4, 10), get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT"))


