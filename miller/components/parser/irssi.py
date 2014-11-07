__author__ = 'Oscar Eriksson <oscar.eriks@gmail.com>'

from miller.components.parser.parser import Parser
from miller.components.concepts.line import Line


class Irssi(Parser):
    def parse_line(self, line):
        return Line("Metral", "00:26:01", "Mikoto, kolla klockan. :>")