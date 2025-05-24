# Generated from Python3Parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Python3Parser import Python3Parser
else:
    from Python3Parser import Python3Parser

# This class defines a complete generic visitor for a parse tree produced by Python3Parser.

class Python3ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Python3Parser#file_input.
    def visitFile_input(self, ctx:Python3Parser.File_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#funcdef.
    def visitFuncdef(self, ctx:Python3Parser.FuncdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#if_stmt.
    def visitIf_stmt(self, ctx:Python3Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#parameters.
    def visitParameters(self, ctx:Python3Parser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#typedargslist.
    def visitTypedargslist(self, ctx:Python3Parser.TypedargslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#suite.
    def visitSuite(self, ctx:Python3Parser.SuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#simple_stmt.
    def visitSimple_stmt(self, ctx:Python3Parser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#small_stmt.
    def visitSmall_stmt(self, ctx:Python3Parser.Small_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#expr_stmt.
    def visitExpr_stmt(self, ctx:Python3Parser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#flow_stmt.
    def visitFlow_stmt(self, ctx:Python3Parser.Flow_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#return_stmt.
    def visitReturn_stmt(self, ctx:Python3Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#statement.
    def visitStatement(self, ctx:Python3Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#compound_stmt.
    def visitCompound_stmt(self, ctx:Python3Parser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#test.
    def visitTest(self, ctx:Python3Parser.TestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#or_test.
    def visitOr_test(self, ctx:Python3Parser.Or_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#and_test.
    def visitAnd_test(self, ctx:Python3Parser.And_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#not_test.
    def visitNot_test(self, ctx:Python3Parser.Not_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#comparison.
    def visitComparison(self, ctx:Python3Parser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#comp_op.
    def visitComp_op(self, ctx:Python3Parser.Comp_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#expr.
    def visitExpr(self, ctx:Python3Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#term.
    def visitTerm(self, ctx:Python3Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#factor.
    def visitFactor(self, ctx:Python3Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#atom.
    def visitAtom(self, ctx:Python3Parser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#list_literal.
    def visitList_literal(self, ctx:Python3Parser.List_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#dict_literal.
    def visitDict_literal(self, ctx:Python3Parser.Dict_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#dict_pairs.
    def visitDict_pairs(self, ctx:Python3Parser.Dict_pairsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#dict_pair.
    def visitDict_pair(self, ctx:Python3Parser.Dict_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#testlist.
    def visitTestlist(self, ctx:Python3Parser.TestlistContext):
        return self.visitChildren(ctx)



del Python3Parser