# Generated from Calculadora.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete generic visitor for a parse tree produced by CalculadoraParser.

class CalculadoraVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculadoraParser#stat.
    def visitStat(self, ctx:CalculadoraParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#parens.
    def visitParens(self, ctx:CalculadoraParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#MulDiv.
    def visitMulDiv(self, ctx:CalculadoraParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#AddSub.
    def visitAddSub(self, ctx:CalculadoraParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#double.
    def visitDouble(self, ctx:CalculadoraParser.DoubleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#int.
    def visitInt(self, ctx:CalculadoraParser.IntContext):
        return self.visitChildren(ctx)



del CalculadoraParser