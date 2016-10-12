class Scope:

    def __init__(self, parent=None):
        self.d = {}
        self.parent = parent

    def __getitem__(self, name):
        if (name in self.d.keys()):
            return self.d[name]
        else:
            return self.parent[name]

    def __setitem__(self, name, value):
        self.d[name] = value


class Number:

    def __init__(self, value):
        self.value = int(value)

    def evaluate(self, scope):
        return self


class Function:

    def __init__(self, args, body):
        self.args = args
        self.body = body

    def evaluate(self, scope):
        function_answ = list(map(lambda x: x.evaluate(scope), self.body))
        return function_answ[-1]


class FunctionDefinition:

    def __init__(self, name, function):
        self.name = name
        self.function = function

    def evaluate(self, scope):
        scope[self.name] = self.function
        return self.function


class Conditional:

    def __init__(self, condtion, if_true, if_false=None):
        self.condtion = condtion
        self.if_true = if_true
        self.if_false = if_false

    def evaluate(self, scope):
        logic_exp = self.condtion.evaluate(scope)
        if logic_exp.value:
            rt = list(map(lambda x: x.evaluate(scope), self.if_true))
        else:
            if self.if_false:
                rt = list(map(lambda x: x.evaluate(scope), self.if_false))
            else:
                rt = Number(0)
        return rt


class Print:

    def __init__(self, expr):
        self.expr = expr

    def evaluate(self, scope):
        print(self.expr.evaluate(scope).value)


class Read:

    def __init__(self, name):
        self.name = name

    def evaluate(self, scope):
        value = input()
        scope[self.name] = Number(value)


class FunctionCall:

    def __init__(self, fun_expr, args=None):
        self.args = args
        self.expr = fun_expr

    def evaluate(self, scope):
        child_scope = Scope(scope)
        list_args = list(map(lambda x: x.evaluate(child_scope), self.args))
        for x, y in zip(self.expr.evaluate(scope).args, list_args):
            child_scope[x] = y
        return self.expr.evaluate(scope).evaluate(child_scope)


class Reference:

    def __init__(self, name):
        self.name = name

    def evaluate(self, scope):
        return scope[self.name]


class BinaryOperation:

    def __init__(self, lhs, op, rhs):
        self.left_part = lhs
        self.right_part = rhs
        self.op = op

    def evaluate(self, scope):
        left_num = self.left_part.evaluate(scope)
        right_num = self.right_part.evaluate(scope)
        if self.op == "+":
            return Number(left_num.value + right_num.value)
        elif self.op == "-":
            return Number(left_num.value - right_num.value)
        elif self.op == "*":
            return Number(left_num.value * right_num.value)
        elif self.op == "/":
            return Number(left_num.value / right_num.value)
        elif self.op == "%":
            return Number(left_num.value % right_num.value)
        elif self.op == "==":
            return Number(left_num.value == right_num.value)
        elif self.op == "!=":
            return Number(left_num.value != right_num.value)
        elif self.op == "<":
            return Number(left_num.value < right_num.value)
        elif self.op == ">":
            return Number(left_num.value > right_num.value)
        elif self.op == "<=":
            return Number(left_num.value <= right_num.value)
        elif op == ">=":
            return Number(left_num.value >= right_num.value)
        elif op == "&&":
            return Number(left_num.value and right_num.value)
        elif op == "||":
            return Number(left_num.value or right_num.value)
        else:
            raise NotImplementedError


class UnaryOperation:

    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

    def evaluate(self, scope):
        expr_num = self.expr.evaluate(scope)
        if self.op == "-":
            return Number(expr_num.value * (-1))
        elif self.op == "!":
            return Number(not expr_num.value)
        else:
            raise NotImplementedError


def example():
    parent = Scope()
    parent["foo"] = Function(('hello', 'world'),
                             [Print(BinaryOperation(Reference('hello'),
                                                    '+',
                                                    Reference('world')))])
    parent["bar"] = Number(10)
    scope = Scope(parent)
    assert 10 == scope["bar"].value
    scope["bar"] = Number(20)
    assert scope["bar"].value == 20
    print('It should print 2: ', end=' ')
    FunctionCall(FunctionDefinition('foo', parent['foo']),
                 [Number(5), UnaryOperation('-', Number(3))]).evaluate(scope)


def my_tests():
    scope = Scope()
    scope["multiply_two_numbers"] = Function(
        ('first_number', 'second_number'), [
            Print(
                BinaryOperation(
                    Reference('first_number'), '*', Reference('second_number')))])
    print("Function for multiplication of two numbers")
    print("Write first number")
    Read("first").evaluate(scope)
    print("Write second number")
    Read("second").evaluate(scope)
    FunctionCall(
        FunctionDefinition(
            'multiply_two_numbers', scope['multiply_two_numbers']), [
            Reference("first"), Reference("second")]).evaluate(scope)
    print("Comparison two numbers")
    print("Write first number")
    Read("first").evaluate(scope)
    print("Write second number")
    Read("second").evaluate(scope)
    print("If first number > second number print(1) else print(0)")
    Conditional(
        BinaryOperation(
            Reference("first"), ">", Reference("second")), [
            Print(
                Number(1))], [
                    Print(
                        Number(0))]).evaluate(scope)
    print("Change sign")
    print("Write number")
    Read("number").evaluate(scope)
    Print(UnaryOperation('-', Reference("number"))).evaluate(scope)


if __name__ == '__main__':
    example()
    my_tests()
