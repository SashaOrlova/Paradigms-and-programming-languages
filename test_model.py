import os
import sys
import io
from model import *


def get_v(n):
    scope = {}
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    Print(n).evaluate(scope)
    res = int(sys.stdout.getvalue())
    sys.stdout = old_stdout
    return res


class TestConditional:

    def test_simple_conditional(self):
        assert get_v(Conditional(
            BinaryOperation(
                Number(3), ">", Number(2)), [
                    Number(1)], [
                        Number(0)])) == 1

    def test_simple_empty_conditional(self):
        assert get_v(Conditional(Number(1), [Number(1)])) == 1

    def test_empty_conditional(self):
        scope = {}
        assert get_v(Conditional(Number(1), [], [])) == 0
        assert get_v(Conditional(Number(0), None)) == 0
        assert get_v(Conditional(Number(0), [], [Number(1)])) == 1
        assert get_v(Conditional(Number(1), None, [Number(1)])) == 0
        assert get_v(Conditional(Number(0), [Number(1)], None)) == 0


class TestFunction:

    def test_simple_function(self):
        assert get_v(Function((), [Number(1)])) == 1

    def test_empty_function(self):
        assert get_v(Function((), [])) == 0


class TestFunctionDefinition:

    def test_function_definition(self):
        scope = {}
        func = Function((), [Number(1)])
        FunctionDefinition('func', func).evaluate(scope)
        assert scope['func'] is func


class TestFunctionCall:

    def test_function_call(self):
        scope = {}
        scope["nothing"] = Function((), [Number(1)])
        assert get_v(FunctionCall(
            FunctionDefinition(
                'nothing', scope['nothing']), [])) == 1


class TestBinaryOperation:

    def test_simple_binary_operation(self):
        assert get_v(BinaryOperation(Number(4), '+', Number(5))) == 9
        assert get_v(BinaryOperation(Number(0), '||', Number(1))) == 1
        assert get_v(BinaryOperation(Number(4), '*', Number(5))) == 20
        assert get_v(BinaryOperation(Number(4), '>', Number(5))) == 0


class TestReference:

    def test_reference(self):
        scope = {}
        scope['example'] = 123
        assert Reference('example').evaluate(scope) == 123


class TestUnaryOperation:

    def test_simple_unary_operation(self):
        assert get_v(UnaryOperation('-', Number(4))) == -4
        assert get_v(UnaryOperation('!', Number(0))) == 1


class TestScope:

    def test_simple_scope(self):
        scope = Scope()
        example = 1
        scope["example"] = example
        assert scope['example'] is example

    def test_parent_scope(self):
        parent = Scope()
        foo = Number(2)
        parent['foo'] = foo
        scope = Scope(parent)
        assert scope['foo'] is foo

if __name__ == "__main__":
    pytest.main()
