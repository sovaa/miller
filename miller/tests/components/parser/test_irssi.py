__author__ = 'Oscar Eriksson <oscar.eriks@gmail.com>'

from miller.components.parser.irssi import Irssi
import unittest


class IrssiTests(unittest.TestCase):
    def setUp(self):
        self.user = "Metral"
        self.time = "00:26:01"
        self.msg = "Mikoto, kolla klockan. :>"
        self.line = self.time + "<@" + self.user + "> " + self.msg

    def test_parse_line_correct_user(self):
        parsed_line = Irssi().parse_line(self.line)
        self.failUnlessEqual(parsed_line.user, self.user)

    def test_parse_line_correct_time(self):
        parsed_line = Irssi().parse_line(self.line)
        self.failUnlessEqual(parsed_line.time, self.time)

    def test_parse_line_correct_msg(self):
        parsed_line = Irssi().parse_line(self.line)
        self.failUnlessEqual(parsed_line.msg, self.msg)


def main():
    unittest.main()

if __name__ == '__main__':
    main()