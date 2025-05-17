// Generated from Python.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link PythonParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface PythonVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link PythonParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(PythonParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(PythonParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#simpleStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSimpleStatement(PythonParser.SimpleStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#compoundStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCompoundStatement(PythonParser.CompoundStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#assignmentStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignmentStatement(PythonParser.AssignmentStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#varAssignment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarAssignment(PythonParser.VarAssignmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#expressionStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressionStatement(PythonParser.ExpressionStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#returnStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturnStatement(PythonParser.ReturnStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#functionDef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionDef(PythonParser.FunctionDefContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#parameterList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameterList(PythonParser.ParameterListContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#parameter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameter(PythonParser.ParameterContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#ifStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfStatement(PythonParser.IfStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#elseIfStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitElseIfStatement(PythonParser.ElseIfStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#elseStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitElseStatement(PythonParser.ElseStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#whileStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileStatement(PythonParser.WhileStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#forStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForStatement(PythonParser.ForStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(PythonParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#orExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOrExpr(PythonParser.OrExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#andExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAndExpr(PythonParser.AndExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#notExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNotExpr(PythonParser.NotExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#comparison}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComparison(PythonParser.ComparisonContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#compOp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCompOp(PythonParser.CompOpContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#addExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAddExpr(PythonParser.AddExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#addOp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAddOp(PythonParser.AddOpContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#multExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultExpr(PythonParser.MultExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#multOp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultOp(PythonParser.MultOpContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#factor}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFactor(PythonParser.FactorContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#power}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPower(PythonParser.PowerContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtom(PythonParser.AtomContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitList(PythonParser.ListContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#dict}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDict(PythonParser.DictContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#keyValuePair}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitKeyValuePair(PythonParser.KeyValuePairContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#functionCall}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionCall(PythonParser.FunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#argumentList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgumentList(PythonParser.ArgumentListContext ctx);
	/**
	 * Visit a parse tree produced by {@link PythonParser#argument}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgument(PythonParser.ArgumentContext ctx);
}