# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 22:57:46 2017

@author: NYLDO
"""
from grammar.CalculadoraVisitor import CalculadoraVisitor
from grammar.CalculadoraParser import CalculadoraParser


class CalculadoraVisitorImplement(CalculadoraVisitor):
    
    def visitInt(self, ctx:CalculadoraParser.IntContext):
        return int(ctx.INT().getText())
    
    def visitDouble(self, ctx:CalculadoraParser.DoubleContext):
        return float(ctx.DOUBLE().getText())
    
    def visitAddSub(self, ctx:CalculadoraParser.AddSubContext):
        esquerda = self.visit(ctx.expr(0))
        direita = self.visit(ctx.expr(1))
        
        if ctx.op.type == CalculadoraParser.ADD:
            return esquerda + direita
        return esquerda-direita
    
    def visitMulDiv(self, ctx:CalculadoraParser.MulDivContext):
        esquerda = self.visit(ctx.expr(0))
        direita = self.visit(ctx.expr(1))
        
        if ctx.op.type == CalculadoraParser.MUL:
            return esquerda * direita
        return esquerda / direita
    
    def visitParens(self, ctx:CalculadoraParser.ParensContext):
        return self.visit(ctx.expr())