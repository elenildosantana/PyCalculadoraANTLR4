# Generated from Calculadora.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("A\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\6\5!\n\5\r\5\16\5\"\3\6\6\6&\n\6\r\6")
        buf.write("\16\6\'\3\7\6\7+\n\7\r\7\16\7,\3\7\3\7\6\7\61\n\7\r\7")
        buf.write("\16\7\62\3\b\6\b\66\n\b\r\b\16\b\67\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\2\2\r\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\3\2\5\4\2\f\f\17\17\3\2\62;\4\2C\\")
        buf.write("c|\2E\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3\31\3\2\2\2\5\33")
        buf.write("\3\2\2\2\7\35\3\2\2\2\t \3\2\2\2\13%\3\2\2\2\r*\3\2\2")
        buf.write("\2\17\65\3\2\2\2\219\3\2\2\2\23;\3\2\2\2\25=\3\2\2\2\27")
        buf.write("?\3\2\2\2\31\32\7?\2\2\32\4\3\2\2\2\33\34\7*\2\2\34\6")
        buf.write("\3\2\2\2\35\36\7+\2\2\36\b\3\2\2\2\37!\t\2\2\2 \37\3\2")
        buf.write("\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\n\3\2\2\2$&\t\3")
        buf.write("\2\2%$\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(\f\3\2")
        buf.write("\2\2)+\t\3\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2")
        buf.write("-.\3\2\2\2.\60\7\60\2\2/\61\t\3\2\2\60/\3\2\2\2\61\62")
        buf.write("\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\16\3\2\2\2\64")
        buf.write("\66\t\4\2\2\65\64\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2")
        buf.write("\678\3\2\2\28\20\3\2\2\29:\7,\2\2:\22\3\2\2\2;<\7\61\2")
        buf.write("\2<\24\3\2\2\2=>\7-\2\2>\26\3\2\2\2?@\7/\2\2@\30\3\2\2")
        buf.write("\2\b\2\"\',\62\67\2")
        return buf.getvalue()


class CalculadoraLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    NEWLINE = 4
    INT = 5
    DOUBLE = 6
    ID = 7
    MUL = 8
    DIV = 9
    ADD = 10
    SUB = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "INT", "DOUBLE", "ID", "MUL", "DIV", "ADD", "SUB" ]

    ruleNames = [ "T__0", "T__1", "T__2", "NEWLINE", "INT", "DOUBLE", "ID", 
                  "MUL", "DIV", "ADD", "SUB" ]

    grammarFileName = "Calculadora.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


