// Generated from Python.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PythonParser}.
 */
public interface PythonListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PythonParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(PythonParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(PythonParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(PythonParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(PythonParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#simpleStatement}.
	 * @param ctx the parse tree
	 */
	void enterSimpleStatement(PythonParser.SimpleStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#simpleStatement}.
	 * @param ctx the parse tree
	 */
	void exitSimpleStatement(PythonParser.SimpleStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#compoundStatement}.
	 * @param ctx the parse tree
	 */
	void enterCompoundStatement(PythonParser.CompoundStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#compoundStatement}.
	 * @param ctx the parse tree
	 */
	void exitCompoundStatement(PythonParser.CompoundStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#assignmentStatement}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentStatement(PythonParser.AssignmentStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#assignmentStatement}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentStatement(PythonParser.AssignmentStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#varAssignment}.
	 * @param ctx the parse tree
	 */
	void enterVarAssignment(PythonParser.VarAssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#varAssignment}.
	 * @param ctx the parse tree
	 */
	void exitVarAssignment(PythonParser.VarAssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void enterExpressionStatement(PythonParser.ExpressionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void exitExpressionStatement(PythonParser.ExpressionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(PythonParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(PythonParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#functionDef}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDef(PythonParser.FunctionDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#functionDef}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDef(PythonParser.FunctionDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#parameterList}.
	 * @param ctx the parse tree
	 */
	void enterParameterList(PythonParser.ParameterListContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#parameterList}.
	 * @param ctx the parse tree
	 */
	void exitParameterList(PythonParser.ParameterListContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(PythonParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(PythonParser.ParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(PythonParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(PythonParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#elseIfStatement}.
	 * @param ctx the parse tree
	 */
	void enterElseIfStatement(PythonParser.ElseIfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#elseIfStatement}.
	 * @param ctx the parse tree
	 */
	void exitElseIfStatement(PythonParser.ElseIfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#elseStatement}.
	 * @param ctx the parse tree
	 */
	void enterElseStatement(PythonParser.ElseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#elseStatement}.
	 * @param ctx the parse tree
	 */
	void exitElseStatement(PythonParser.ElseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(PythonParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(PythonParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void enterForStatement(PythonParser.ForStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void exitForStatement(PythonParser.ForStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(PythonParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(PythonParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#orExpr}.
	 * @param ctx the parse tree
	 */
	void enterOrExpr(PythonParser.OrExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#orExpr}.
	 * @param ctx the parse tree
	 */
	void exitOrExpr(PythonParser.OrExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#andExpr}.
	 * @param ctx the parse tree
	 */
	void enterAndExpr(PythonParser.AndExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#andExpr}.
	 * @param ctx the parse tree
	 */
	void exitAndExpr(PythonParser.AndExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#notExpr}.
	 * @param ctx the parse tree
	 */
	void enterNotExpr(PythonParser.NotExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#notExpr}.
	 * @param ctx the parse tree
	 */
	void exitNotExpr(PythonParser.NotExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#comparison}.
	 * @param ctx the parse tree
	 */
	void enterComparison(PythonParser.ComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#comparison}.
	 * @param ctx the parse tree
	 */
	void exitComparison(PythonParser.ComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#compOp}.
	 * @param ctx the parse tree
	 */
	void enterCompOp(PythonParser.CompOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#compOp}.
	 * @param ctx the parse tree
	 */
	void exitCompOp(PythonParser.CompOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#addExpr}.
	 * @param ctx the parse tree
	 */
	void enterAddExpr(PythonParser.AddExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#addExpr}.
	 * @param ctx the parse tree
	 */
	void exitAddExpr(PythonParser.AddExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#addOp}.
	 * @param ctx the parse tree
	 */
	void enterAddOp(PythonParser.AddOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#addOp}.
	 * @param ctx the parse tree
	 */
	void exitAddOp(PythonParser.AddOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#multExpr}.
	 * @param ctx the parse tree
	 */
	void enterMultExpr(PythonParser.MultExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#multExpr}.
	 * @param ctx the parse tree
	 */
	void exitMultExpr(PythonParser.MultExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#multOp}.
	 * @param ctx the parse tree
	 */
	void enterMultOp(PythonParser.MultOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#multOp}.
	 * @param ctx the parse tree
	 */
	void exitMultOp(PythonParser.MultOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(PythonParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(PythonParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#power}.
	 * @param ctx the parse tree
	 */
	void enterPower(PythonParser.PowerContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#power}.
	 * @param ctx the parse tree
	 */
	void exitPower(PythonParser.PowerContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(PythonParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(PythonParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#list}.
	 * @param ctx the parse tree
	 */
	void enterList(PythonParser.ListContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#list}.
	 * @param ctx the parse tree
	 */
	void exitList(PythonParser.ListContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#dict}.
	 * @param ctx the parse tree
	 */
	void enterDict(PythonParser.DictContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#dict}.
	 * @param ctx the parse tree
	 */
	void exitDict(PythonParser.DictContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#keyValuePair}.
	 * @param ctx the parse tree
	 */
	void enterKeyValuePair(PythonParser.KeyValuePairContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#keyValuePair}.
	 * @param ctx the parse tree
	 */
	void exitKeyValuePair(PythonParser.KeyValuePairContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(PythonParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(PythonParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void enterArgumentList(PythonParser.ArgumentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void exitArgumentList(PythonParser.ArgumentListContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(PythonParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(PythonParser.ArgumentContext ctx);
}