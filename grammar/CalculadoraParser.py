# Generated from Calculadora.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("&\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\5\2\20\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\31\n\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\7\3!\n\3\f\3\16\3$\13\3\3\3\2\3\4")
        buf.write("\4\2\4\2\4\3\2\n\13\3\2\f\r\2)\2\17\3\2\2\2\4\30\3\2\2")
        buf.write("\2\6\7\5\4\3\2\7\b\7\6\2\2\b\20\3\2\2\2\t\n\7\t\2\2\n")
        buf.write("\13\7\3\2\2\13\f\5\4\3\2\f\r\7\6\2\2\r\20\3\2\2\2\16\20")
        buf.write("\7\6\2\2\17\6\3\2\2\2\17\t\3\2\2\2\17\16\3\2\2\2\20\3")
        buf.write("\3\2\2\2\21\22\b\3\1\2\22\31\7\7\2\2\23\31\7\b\2\2\24")
        buf.write("\25\7\4\2\2\25\26\5\4\3\2\26\27\7\5\2\2\27\31\3\2\2\2")
        buf.write("\30\21\3\2\2\2\30\23\3\2\2\2\30\24\3\2\2\2\31\"\3\2\2")
        buf.write("\2\32\33\f\7\2\2\33\34\t\2\2\2\34!\5\4\3\b\35\36\f\6\2")
        buf.write("\2\36\37\t\3\2\2\37!\5\4\3\7 \32\3\2\2\2 \35\3\2\2\2!")
        buf.write("$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\5\3\2\2\2$\"\3\2\2\2")
        buf.write("\6\17\30 \"")
        return buf.getvalue()


class CalculadoraParser ( Parser ):

    grammarFileName = "Calculadora.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NEWLINE", "INT", "DOUBLE", "ID", "MUL", "DIV", "ADD", 
                      "SUB" ]

    RULE_stat = 0
    RULE_expr = 1

    ruleNames =  [ "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    NEWLINE=4
    INT=5
    DOUBLE=6
    ID=7
    MUL=8
    DIV=9
    ADD=10
    SUB=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(CalculadoraParser.NEWLINE, 0)

        def ID(self):
            return self.getToken(CalculadoraParser.ID, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = CalculadoraParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_stat)
        try:
            self.state = 13
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalculadoraParser.T__1, CalculadoraParser.INT, CalculadoraParser.DOUBLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.expr(0)
                self.state = 5
                self.match(CalculadoraParser.NEWLINE)
                pass
            elif token in [CalculadoraParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.match(CalculadoraParser.ID)
                self.state = 8
                self.match(CalculadoraParser.T__0)
                self.state = 9
                self.expr(0)
                self.state = 10
                self.match(CalculadoraParser.NEWLINE)
                pass
            elif token in [CalculadoraParser.NEWLINE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 12
                self.match(CalculadoraParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculadoraParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExprContext,i)

        def MUL(self):
            return self.getToken(CalculadoraParser.MUL, 0)
        def DIV(self):
            return self.getToken(CalculadoraParser.DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExprContext,i)

        def ADD(self):
            return self.getToken(CalculadoraParser.ADD, 0)
        def SUB(self):
            return self.getToken(CalculadoraParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class DoubleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DOUBLE(self):
            return self.getToken(CalculadoraParser.DOUBLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDouble" ):
                return visitor.visitDouble(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CalculadoraParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculadoraParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalculadoraParser.INT]:
                localctx = CalculadoraParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 16
                self.match(CalculadoraParser.INT)
                pass
            elif token in [CalculadoraParser.DOUBLE]:
                localctx = CalculadoraParser.DoubleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(CalculadoraParser.DOUBLE)
                pass
            elif token in [CalculadoraParser.T__1]:
                localctx = CalculadoraParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(CalculadoraParser.T__1)
                self.state = 19
                self.expr(0)
                self.state = 20
                self.match(CalculadoraParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 30
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = CalculadoraParser.MulDivContext(self, CalculadoraParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 24
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 25
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CalculadoraParser.MUL or _la==CalculadoraParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 26
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = CalculadoraParser.AddSubContext(self, CalculadoraParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 28
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CalculadoraParser.ADD or _la==CalculadoraParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 29
                        self.expr(5)
                        pass

             
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




