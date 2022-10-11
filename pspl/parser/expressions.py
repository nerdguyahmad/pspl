# MIT License

# Copyright (c) 2022 I. Ahmad

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

from typing import TYPE_CHECKING, Any
from pspl.parser import generator
from pspl import ast
from pspl.parser.errors import IdentifierNotDefined

if TYPE_CHECKING:
    from pspl.state import RuntimeState

__all__ = ()

gen = generator.get()

@gen.production('expr : LT_STRING')
@gen.production('expr : LT_INTEGER')
@gen.production('expr : IDENT')
def prod_expr(state: RuntimeState, tokens: Any):
    tok = tokens[0].gettokentype()
    val = tokens[0].getstr()

    if tok == 'LT_STRING':
        return ast.String(val)
    if tok == 'LT_INTEGER':
        return ast.Integer(val)
    if tok == 'IDENT':
        try:
            return state.get_def(val)
        except KeyError:
            raise IdentifierNotDefined(tokens[0].getsourcepos(), val)

    assert False
