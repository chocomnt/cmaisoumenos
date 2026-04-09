// Generated from /home/kauan/Documentos/Projetos/cmaismenos/SimpleC.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link SimpleCParser}.
 */
public interface SimpleCListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link SimpleCParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(SimpleCParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleCParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(SimpleCParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleCParser#declaracao}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracao(SimpleCParser.DeclaracaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleCParser#declaracao}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracao(SimpleCParser.DeclaracaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleCParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterExpressao(SimpleCParser.ExpressaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleCParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitExpressao(SimpleCParser.ExpressaoContext ctx);
}