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

from typing import Any
from pspl.ast.base import Node
from pspl.ast.literals import Boolean
from pspl import utils

__all__ = (
    'ArithmeticExpression',
    'Add',
    'Subtract',
    'Div',
    'Mul',
    'BooleanExpression',
    'Eq',
    'NEq',
    'Gt',
    'GtEq',
    'Lt',
    'LtEq',
)


class ArithmeticExpression(Node):
    """Base class for arithmetic operators."""
    def __init__(self, left: Any, right: Any) -> None:
        self.left = left
        self.right = right


class Add(ArithmeticExpression):
    """Represents an addition expression."""
    def eval(self) -> int:
        return utils.maybe_eval(self.left) + utils.maybe_eval(self.right)


class Subtract(ArithmeticExpression):
    """Represents a subtraction expression."""
    def eval(self) -> int:
        return utils.maybe_eval(self.left) - utils.maybe_eval(self.right)


class Div(ArithmeticExpression):
    """Represents a division expression."""
    def eval(self) -> int:
        return utils.maybe_eval(self.left) / utils.maybe_eval(self.right)


class Mul(ArithmeticExpression):
    """Represents a multiplication expression."""
    def eval(self) -> int:
        return utils.maybe_eval(self.left) * utils.maybe_eval(self.right)


class BooleanExpression(Node):
    """Base class for various boolean expressions."""
    def __init__(self, left: Any, right: Any) -> None:
        self.left = left
        self.right = right

    def eval(self) -> Boolean:
        ...

    def __pspl_output__(self) -> str:
        return self.eval().__pspl_output__()


class Eq(BooleanExpression):
    """Represents an equality boolean expression."""
    def eval(self) -> Boolean:
        return Boolean(utils.maybe_eval(self.left) == utils.maybe_eval(self.right))


class NEq(BooleanExpression):
    """Represents an inequality boolean expression."""
    def eval(self) -> Boolean:
        return Boolean(utils.maybe_eval(self.left) != utils.maybe_eval(self.right))


class Gt(BooleanExpression):
    """Represents a greater than boolean expression."""
    def eval(self) -> Boolean:
        return Boolean(utils.maybe_eval(self.left) > utils.maybe_eval(self.right))


class GtEq(BooleanExpression):
    """Represents a greater than or equality boolean expression."""
    def eval(self) -> Boolean:
        return Boolean(utils.maybe_eval(self.left) >= utils.maybe_eval(self.right))


class Lt(BooleanExpression):
    """Represents a less than boolean expression."""
    def eval(self) -> Boolean:
        return Boolean(utils.maybe_eval(self.left) < utils.maybe_eval(self.right))


class LtEq(BooleanExpression):
    """Represents an less than or equality boolean expression."""
    def eval(self) -> Boolean:
        return Boolean(utils.maybe_eval(self.left) <= utils.maybe_eval(self.right))
