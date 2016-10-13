class Scope:

    def __init__(self, parent=None):
        self.d = {}
        self.parent = parent

    def __getitem__(self, name):
        if name in self.d:
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

    def __init__(self, args, body=None):
        self.args = args
        self.body = body

    def evaluate(self, scope):
        function_answ = list(map(lambda x: x.evaluate(scope), self.body))
        if function_answ:
            return function_answ[-1]
        else:
            return Number(0)


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
            if self.if_true:
                return list(map(lambda x: x.evaluate(scope), self.if_true))[-1]
            else:
                return Number(0)
        else:
            if self.if_false:
                return list(map(lambda x: x.evaluate(scope),
                                self.if_false))[-1]
            else:
                return Number(0)


class Print:

    def __init__(self, expr):
        self.expr = expr

    def evaluate(self, scope):
        num = self.expr.evaluate(scope)
        print(num.value)
        return num


class Read:

    def __init__(self, name):
        self.name = name

    def evaluate(self, scope):
        value = input()
        scope[self.name] = Number(value)
        return Number(value)


class FunctionCall:

    def __init__(self, fun_expr, args=None):
        self.args = args
        self.expr = fun_expr

    def evaluate(self, scope):
        child_scope = Scope(scope)
        list_args = list(map(lambda x: x.evaluate(child_scope), self.args))
        function = self.expr.evaluate(scope)
        for new_name, value in zip(function.args, list_args):
            child_scope[new_name] = value
        return function.evaluate(child_scope)


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
            return Number(left_num.value // right_num.value)
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
        elif self.op == ">=":
            return Number(left_num.value >= right_num.value)
        elif self.op == "&&":
            return Number(left_num.value and right_num.value)
        elif self.op == "||":
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
            return Number(-expr_num.value)
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
                    Reference('first_number'), '*',
                    Reference('second_number')))])
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
    Print(BinaryOperation(
        Number(0), '||',
        Number(1))).evaluate(scope)
    scope["nothing"] = Function((), [])
    FunctionCall(
        FunctionDefinition(
            'nothing', scope['nothing']), []).evaluate(scope)
    print("Write number")
    print("It will write your number, your number * 2 and your number div 2")
    scope["a"] = Read("something").evaluate(scope)
    scope["b"] = Print(Reference('a')).evaluate(scope)
    Print((BinaryOperation(
        Reference('b'), '+',
        Reference('a'))).evaluate(scope)).evaluate(scope)
    Print((BinaryOperation(
        Reference('a'), '/',
        Number(2))).evaluate(scope)).evaluate(scope)
    print("Print 1 if your number is 201. Else doing nothing")
    Conditional(
        BinaryOperation(
            Reference("a"), "==", Number(201)), [
            Print(
                Number(1))]).evaluate(scope)
    assert Print(Number(2)).evaluate(scope).value == 2
    print("Write 5")
    assert Read("five").evaluate(scope).value == 5
    assert Conditional(Number(1), [Number(1)]).evaluate(scope).value == 1
    scope["plus one"] = Function(("number"), [BinaryOperation(
        Reference("number"), '+',
        Number(1))])
    scope["return number"] = Function((), [Number(5)])
    a = FunctionCall(
        FunctionDefinition(
            'plus one', scope['plus one']), [FunctionCall(
                FunctionDefinition('return number', scope['return number']),
                    [])]).evaluate(scope)
    assert a.value == 6

if __name__ == '__main__':
    example()
    my_tests()
