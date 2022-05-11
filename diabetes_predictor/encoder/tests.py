from django.test import TestCase
import os

class EncoderTests(TestCase):
    def test_readfile(self):
        file = open("../diabetes.csv","r") 
        self.assertEqual(file.readable() , True)
