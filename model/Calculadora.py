# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 22:25:10 2017

@author: NYLDO
"""
import antlr4
from grammar.CalculadoraParser import CalculadoraParser
from grammar.CalculadoraLexer import CalculadoraLexer
from model.CalculadoraImplement import CalculadoraVisitorImplement

class Calculadora:
    __expressao = None
    
    def calcular(self,expressao):
        self.__expressao = expressao
        input_stream = antlr4.InputStream(expressao)
        lexer = CalculadoraLexer(input_stream)
        tokens = antlr4.CommonTokenStream(lexer)
        parser = CalculadoraParser(tokens)
        tree = parser.expr()
        
        visitor = CalculadoraVisitorImplement()
        resultado = visitor.visit(tree)

        return resultado