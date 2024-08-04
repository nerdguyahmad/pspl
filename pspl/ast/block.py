# MIT License

# Copyright (c) 2022-2024 I. Ahmad

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

from typing import TYPE_CHECKING
from pspl.ast.node import Node

if TYPE_CHECKING:
    from pspl.ast.statement import Statement
    from pspl.state import State

__all__ = (
    'Block',
)


class Block(Node):
    """Represents a code block with a list of statements."""

    def __init__(self, statements: list[Statement], state: State) -> None:
        self.statements: list[Statement] = []

        for statement in statements:
            if isinstance(statement, Block):
                statements.extend(statement.statements)
            elif isinstance(statement, Statement):
                statements.append(statement)

        super().__init__(state=state, source_pos=statements[0].source_pos)

    def eval(self) -> None:
        for statement in self.statements:
            statement.eval()
