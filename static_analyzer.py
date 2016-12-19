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
        return self.visit(
            a.left_part) and self.visit(
            a.right_part)

    def visit_unary_operation(self, a):
        return self.visit(a.expr)

    def visit_conditional(self, a):
        left = False
        right = False
        if a.if_true:
            right = all([self.visit(x) for x in a.if_true])
        if a.if_false:
            left = all([self.visit(x) for x in a.if_false])
        return left and right

    def visit_function(self, a):
        tmp = True
        tmp = tmp and all([self.visit(x) for x in a.body])
        tmp = tmp and all([self.visit(x) for x in a.args])
        return tmp

    def visit_function_definition(self, a):
        return self.visit(a.function)

    def visit_function_call(self, a):
        tmp = True
        tmp = tmp and all([self.visit(x), a.args])
        return tmp and self.visit(a.expr)


class NoReturnValueCheckVisitor:

    def visit(self, a):
        return a.accept(self)

    def visit_binary_operation(self, a):
        return self.visit(a.left_part) and self.visit(a.right_part)

    def visit_conditional(self, a):
        left = False
        right = False
        if a.if_true:
            right = all([self.visit(x) for x in a.if_false])
        if a.if_false:
            left = all([self.visit(x) for x in a.if_true])
        return left and right

    def visit_function(self, a):
        if not a.body:
            return False
        else:
            return [self.visit(x) for x in a.body][-1]

    def visit_function_definition(self, a):
        if not self.visit(a.function):
            print(a.name)
        return True

    def visit_function_call(self, a):
        return self.visit(a.expr) and all([self.visit(x) for x in a.args])

    def visit_number(self, a):
        return True

    def visit_read(self, a):
        return self.visit(a.expr)

    def visit_print(self, a):
        return self.visit(a.expr)

    def visit_reference(self, a):
        return True

    def visit_unary_operation(self, a):
        return self.visit(a.expr)
