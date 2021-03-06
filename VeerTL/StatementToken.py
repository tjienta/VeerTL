# Template Language for code generation.
# Copyright (C) 2018  Tjienta Vara
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys

from . import Token
from . import StatementNode

class StatementToken (Token.Token):
    def __init__(self, source):
        statement = (source + 2).getLine()
        self.lines = [str(statement)]
        super().__init__(source[:statement.stop])

    def __str__(self):
        leading_spaces = len(self.lines[0]) - len(self.lines[0].lstrip())
        return "\n".join(x[leading_spaces:] for x in self.lines) + "\n"

    def __repr__(self):
        return "<statement %s>" % repr(str(self))

    def getNode(self, context):
        return StatementNode.StatementNode(context, self.source, str(self))

    def merge(self, other):
        if isinstance(other, StatementToken):
            self.lines.append(other.lines[0])
            return True
        else:
            return False
