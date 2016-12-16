from model import *


class PureCheckVisitor:

    def visit(self, a):
        return a.accept(self)

    def visit_number(self, a):
        return True

    def visit_read(self, a):
        return False

    def visit_print(self, a):
        return False

    def visit_reference(self, a):
        return True

    def visit_binary_operation(self, a):
        return PureCheckVisitor().visit(
            a.left_part) and PureCheckVisitor().visit(
            a.right_part)

    def visit_unary_operation(self, a):
        return PureCheckVisitor().visit(a.expr)

    def visit_conditional(self, a):
        tmp = True
        tmp = tmp and all(
            list(map(lambda x: PureCheckVisitor().visit(x), a.if_true)))
        tmp = tmp and all(
            list(map(lambda x: PureCheckVisitor().visit(x), a.if_false)))
        tmp = tmp and PureCheckVisitor().visit(a.condtion)
        return tmp

    def visit_function(self, a):
        tmp = True
        tmp = tmp and all(
            list(map(lambda x: PureCheckVisitor().visit(x), a.body)))
        tmp = tmp and all(
            list(map(lambda x: PureCheckVisitor().visit(x), a.args)))
        return tmp

    def visit_function_definition(self, a):
        return PureCheckVisitor().visit(a.function)

    def visit_function_call(self, a):
        tmp = True
        tmp = tmp and all(
            list(map(lambda x: PureCheckVisitor().visit(x), a.args)))
        return tmp and PureCheckVisitor().visit(a.expr)


class NoReturnValueCheckVisitor:

    def visit(self, a):
        return a.accept(self)

    def visit_binary_operation(self, a):
        NoReturnValueCheckVisitor().visit(a.left_part)
        NoReturnValueCheckVisitor().visit(a.right_part)

    def visit_conditional(self, a):
        if (not a.if_true):
            all(list(map(lambda x: NoReturnValueCheckVisitor().visit(x),
                         a.if_false)))
            return False
        if (not a.if_false):
            all(list(map(lambda x: NoReturnValueCheckVisitor().visit(x),
                         a.if_true)))
            return False
        else:
            return (all(
                list(map(
                    lambda x: NoReturnValueCheckVisitor().visit(x),
                    a.if_true)))
                    and all(list(map(
                        lambda x: NoReturnValueCheckVisitor().visit(x),
                        a.if_false))))

    def visit_function(self, a):
        if (not a.body):
            return False
        else:
            return list(
                map(lambda x: NoReturnValueCheckVisitor().visit(x),
                    a.body))[-1]

    def visit_function_definition(self, a):
        if (not NoReturnValueCheckVisitor().visit(a.function)):
            print(a.name)
        return True

    def visit_function_call(self, a):
        return NoReturnValueCheckVisitor().visit(a.expr)

    def visit_number(self, a):
        return True

    def visit_read(self, a):
        return True

    def visit_print(self, a):
        return True

    def visit_reference(self, a):
        return True

    def visit_unary_operation(self, a):
        return NoReturnValueCheckVisitor().visit(a.expr)
