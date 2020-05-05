import unittest
import features


class TestFeatures(unittest.TestCase):

    def test_find_vulnerable_statements(self):
        filename = "../samples/SARD_sample.c"
        flaw, line_numbers, flaw_description = features.find_vulnerable_statements(filename)
        self.assertEqual([45, 78, 111], line_numbers)
        self.assertEqual(['        data = data_buf - 8;\n',
                          '        data = data_buf - 8;\n',
                          '        data = data_buf - 8;\n'], flaw)
        self.assertEqual('        /* FLAW: Set data pointer to before the allocated memory buffer */\n', flaw_description[0])


if __name__ == '__main__':
    unittest.main()