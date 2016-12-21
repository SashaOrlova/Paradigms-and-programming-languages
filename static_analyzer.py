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
        left = True
        right = True
        if a.if_true:
            right = all([self.visit(x) for x in a.if_true])
        if a.if_false:
            left = all([self.visit(x) for x in a.if_false])
        return left and right and self.visit(a.condtion)

    def visit_function(self, a):
        tmp = True
        if a.body:
            tmp = all([self.visit(x) for x in a.body])
        return tmp

    def visit_function_definition(self, a):
        return self.visit(a.function)

    def visit_function_call(self, a):
        tmp = True
        if a.args:
            tmp = tmp and all([self.visit(x) for x in a.args])
        return tmp and self.visit(a.expr)


class NoReturnValueCheckVisitor:

    def visit(self, a):
        return a.accept(self)

    def visit_binary_operation(self, a):
        left = self.visit(a.left_part)
        right = self.visit(a.right_part)
        return left and right

    def visit_conditional(self, a):
        left = False
        right = False
        cond = self.visit(a.condtion)
        if a.if_true:
            right = [self.visit(x) for x in a.if_true][-1]
        if a.if_false:
            left = [self.visit(x) for x in a.if_false][-1]
        return left and right and cond

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
        tmp = True
        if a.args:
            tmp = all([self.visit(x) for x in a.args])
        return self.visit(a.expr) and tmp

    def visit_number(self, a):
        return True

    def visit_read(self, a):
        return True

    def visit_print(self, a):
        return self.visit(a.expr)

    def visit_reference(self, a):
        return True

    def visit_unary_operation(self, a):
        return self.visit(a.expr)
