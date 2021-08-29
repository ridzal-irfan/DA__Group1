import unittest
import PythonScript

class TestProgram(unittest.TestCase):
    def test_Header(self):

        t = {'User-Agent' : 'Mobile'}
        self.assertEqual(PythonScript.headers2, t)
        self.assertEqual(PythonScript.r.status_code, 200)

if __name__ == '__main__':
    unittest.main()