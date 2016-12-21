import pytest
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
        scope = {}
        Conditional(Number(1), [Number(1)]).evaluate(scope)

    def test_empty_conditional(self):
        scope = {}
        Conditional(Number(1), [], []).evaluate(scope)
        Conditional(Number(0), None).evaluate(scope)
        Conditional(Number(0), [], [Number(1)]).evaluate(scope)
        Conditional(Number(1), None, [Number(1)]).evaluate(scope)
        Conditional(Number(0), [Number(1)], None).evaluate(scope)


class TestFunction:

    def test_simple_function(self):
        assert get_v(Function((), [Number(1)])) == 1

    def test_empty_function(self):
        scope = {}
        Function((), []).evaluate(scope)


class TestFunctionDefinition:

    def test_function_definition(self):
        scope = {}
        func = Function((), [Number(1)])
        FunctionDefinition('func', func).evaluate(scope)
        assert scope['func'] is func


class TestFunctionCall:

    def test_function_call_simple(self):
        scope = {}
        scope["nothing"] = Function((), [Number(1)])
        assert get_v(FunctionCall(
            FunctionDefinition(
                'nothing', scope['nothing']), [])) == 1

    def test_function_call(self):
        scope = {}
        scope["multiply_two_numbers"] = Function(
            ('first_number', 'second_number'), [
                BinaryOperation(
                    Reference('first_number'), '*',
                    Reference('second_number'))])
        scope['first'] = Number(3)
        scope['second'] = Number(4)
        scope
        t = FunctionCall(
            FunctionDefinition(
                'multiply_two_numbers', scope['multiply_two_numbers']), [
                Reference("first"), Reference("second")]).evaluate(scope)
        assert get_v(t) == 12


class TestBinaryOperation:

    def test_logic_binary_operation(self):
        assert get_v(BinaryOperation(Number(0), '||', Number(1))) != 0
        assert get_v(BinaryOperation(Number(0), '&&', Number(1))) == 0

    def test_comparison_binary_operation(self):
        assert get_v(BinaryOperation(Number(4), '>', Number(5))) == 0
        assert get_v(BinaryOperation(Number(4), '<', Number(5))) != 0
        assert get_v(BinaryOperation(Number(5), '==', Number(5))) != 0
        assert get_v(BinaryOperation(Number(4), '!=', Number(5))) != 0
        assert get_v(BinaryOperation(Number(0), '<=', Number(1))) != 0
        assert get_v(BinaryOperation(Number(4), '>=', Number(5))) == 0

    def test_arifmetic_binary_operation(self):
        assert get_v(BinaryOperation(Number(10), '/', Number(5))) == 2
        assert get_v(BinaryOperation(Number(4), '+', Number(5))) == 9
        assert get_v(BinaryOperation(Number(4), '*', Number(5))) == 20
        assert get_v(BinaryOperation(Number(6), '-', Number(5))) == 1


class TestReference:

    def test_reference_simple(self):
        scope = {}
        scope['example'] = 123
        assert Reference('example').evaluate(scope) == 123

    def test_reference(self):
        scope = {}
        t = Function((), [Number(1)])
        scope['example'] = t
        assert Reference('example').evaluate(scope) is t

    def test_reference_and_conditional(self):
        scope = {}
        scope["true"] = Number(1)
        res = Conditional(
            Reference("true"), [
                Number(1)], [Number(0)]).evaluate(scope)
        assert get_v(res) == 1


class TestUnaryOperation:

    def test_minus_unary_operation(self):
        assert get_v(UnaryOperation('-', Number(4))) == -4

    def test_not_unary_operation(self):
        assert get_v(UnaryOperation('!', Number(0))) != 0


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


class TestPrint:

    def test_print_simple(self):
        scope = {}
        ex = Number(1)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        Print(ex).evaluate(scope)
        res = int(sys.stdout.getvalue())
        sys.stdout = old_stdout
        assert res == 1

    def test_print_with_evaluate(self):
        scope = {}
        ex = BinaryOperation(Number(10), '/', Number(5))
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        Print(ex).evaluate(scope)
        res = int(sys.stdout.getvalue())
        sys.stdout = old_stdout
        assert res == 2


class TestRead:

    def test_read_simple(self):
        scope = {}
        old_stdin = sys.stdin
        sys.stdin = io.StringIO('6')
        t = Read('a').evaluate(scope)
        sys.stdin = old_stdin
        assert get_v(t) == 6


if __name__ == "__main__":
    pytest.main()
