from tokenizer import Token, Tokenizer
from preprocessing import PrePro
from nodeclasses import BinOp, UnOp, IntVal, StrVal, VarDec, NoOp
from nodeclasses import Identifier, Assignment, Block, Println, If, For, FuncDec, FuncCall, FuncReturn

class Parser:
    tokenizer = Tokenizer("", 0, Token("", None))
    def parseFactor():
        if Parser.tokenizer.next.type == "INT":
            resultado = IntVal(Parser.tokenizer.next.value, None)
            Parser.tokenizer.selectNext()
            return resultado
        if Parser.tokenizer.next.type == "STRING":
            resultado = StrVal(Parser.tokenizer.next.value, None)
            Parser.tokenizer.selectNext()
            return resultado
        elif Parser.tokenizer.next.type == "IDENTIFIER":
            valor_ident = Parser.tokenizer.next.value
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "OPENPAR":
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "CLOSEPAR":
                    resultado = FuncCall(valor_ident, None)
                    Parser.tokenizer.selectNext()
                    return resultado
                else:
                    resultado = FuncCall(valor_ident, [Parser.parseBoolExpression()])
                    if Parser.tokenizer.next.type == "COMA":
                        while Parser.tokenizer.next.type == "COMA":
                            Parser.tokenizer.selectNext()
                            new_child = Parser.parseBoolExpression()
                            resultado.children.append(new_child)
                    if Parser.tokenizer.next.type == "CLOSEPAR":
                        Parser.tokenizer.selectNext()
                        return resultado
                    raise Exception("Nao fechou parenteses da funcao com args")
            resultado = Identifier(valor_ident, None)
            return resultado
        elif Parser.tokenizer.next.type == "PLUS":
            Parser.tokenizer.selectNext()
            resultado = UnOp("PLUS", [Parser.parseFactor()])
            return resultado
        elif Parser.tokenizer.next.type == "MINUS":
            Parser.tokenizer.selectNext()
            resultado = UnOp("MINUS", [Parser.parseFactor()])
            return resultado
        elif Parser.tokenizer.next.type == "NOT":
            Parser.tokenizer.selectNext()
            resultado = UnOp("NOT", [Parser.parseFactor()])
            return resultado
        elif Parser.tokenizer.next.type == "OPENPAR":
            Parser.tokenizer.selectNext()
            resultado = Parser.parseBoolExpression()
            if Parser.tokenizer.next.type == "CLOSEPAR":
                Parser.tokenizer.selectNext()
                return resultado
            raise Exception("Nao fechou parenteses 1")
        elif Parser.tokenizer.next.type == "SCAN":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "OPENPAR":
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "CLOSEPAR":
                    Parser.tokenizer.selectNext()
                    resultado = IntVal(int(input()), None)
                    return resultado
                raise Exception("Nao fechou parenteses no scan")
            raise Exception("Nao abriu parenteses no scan")
        else:
           raise Exception("Nao foi factor") 

    def parseTerm():
        resultado = Parser.parseFactor() 
        while Parser.tokenizer.next.type == "MULT" or Parser.tokenizer.next.type == "DIV":
            if Parser.tokenizer.next.type == "MULT":
                Parser.tokenizer.selectNext()
                resultado  = BinOp("MULT",[resultado, Parser.parseFactor()])
            if Parser.tokenizer.next.type == "DIV":
                Parser.tokenizer.selectNext()
                resultado  = BinOp("DIV",[resultado, Parser.parseFactor()])
        return resultado

    def parseExpression():
        resultado = Parser.parseTerm() 
        dict = {
            "PLUS" : "PLUS",
            "MINUS" : "MINUS",
            "DOT" : "DOT",
            }
        while Parser.tokenizer.next.type in dict:
            if Parser.tokenizer.next.type == "PLUS":
                Parser.tokenizer.selectNext()
                resultado = BinOp("PLUS",[resultado, Parser.parseTerm()])
            if Parser.tokenizer.next.type == "MINUS":
                Parser.tokenizer.selectNext()
                resultado = BinOp("MINUS",[resultado, Parser.parseTerm()])
            if Parser.tokenizer.next.type == "DOT":
                Parser.tokenizer.selectNext()
                resultado = BinOp("DOT",[resultado, Parser.parseTerm()])
        return resultado

    def parseRelationalExpression():
        resultado = Parser.parseExpression()
        condicao = Parser.tokenizer.next.type 
        while condicao == "EQUALTO" or condicao == "GREATERTHAN" or condicao == "LOWERTHAN":
            if Parser.tokenizer.next.type == "EQUALTO":
                Parser.tokenizer.selectNext()
                resultado = BinOp("EQUALTO",[resultado, Parser.parseExpression()])
            if Parser.tokenizer.next.type == "GREATERTHAN":
                Parser.tokenizer.selectNext()
                resultado = BinOp("GREATERTHAN",[resultado, Parser.parseExpression()])
            if Parser.tokenizer.next.type == "LOWERTHAN":
                Parser.tokenizer.selectNext()
                resultado = BinOp("LOWERTHAN",[resultado, Parser.parseExpression()])
            condicao = Parser.tokenizer.next.type
        return resultado

    def parseBoolTerm():
        resultado = Parser.parseRelationalExpression() 
        while Parser.tokenizer.next.type == "AND":
            Parser.tokenizer.selectNext()
            resultado = BinOp("AND",[resultado, Parser.parseRelationalExpression()])
        return resultado

    def parseBoolExpression():
        resultado = Parser.parseBoolTerm() 
        while Parser.tokenizer.next.type == "OR":
            Parser.tokenizer.selectNext()
            resultado = BinOp("OR",[resultado, Parser.parseBoolTerm()])
        return resultado

    def parseStatement():
        resultado = NoOp(None, [])
        if Parser.tokenizer.next.type == "ENTER":
            Parser.tokenizer.selectNext()
            return resultado
        

        elif Parser.tokenizer.next.type == "IDENTIFIER":
            valor_ident = Parser.tokenizer.next.value
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "EQUAL":
                Parser.tokenizer.selectNext()
                resultado = Assignment("EQUAL", [Identifier(valor_ident, None), Parser.parseBoolExpression()])
                if Parser.tokenizer.next.type == "ENTER":
                    Parser.tokenizer.selectNext()
                    return resultado
                raise Exception("Nao deu Enter depois do assignment")
            elif Parser.tokenizer.next.type == "OPENPAR":
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "CLOSEPAR":
                    resultado = FuncCall(valor_ident, None)
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "ENTER":
                        Parser.tokenizer.selectNext()
                        return resultado
                    raise Exception("Nao deu Enter depois do assignment da funcao")
                else:
                    resultado = FuncCall(valor_ident, [Parser.parseBoolExpression()])
                    if Parser.tokenizer.next.type == "COMA":
                        while Parser.tokenizer.next.type == "COMA":
                            Parser.tokenizer.selectNext()
                            resultado.children.append(Parser.parseBoolExpression())
                    if Parser.tokenizer.next.type == "CLOSEPAR":
                        Parser.tokenizer.selectNext()
                        if Parser.tokenizer.next.type == "ENTER":
                            Parser.tokenizer.selectNext()
                            return resultado
                        raise Exception("Nao deu Enter depois do assignment da funcao com args")
                    raise Exception("Nao fechou parenteses da funcao com args")
                    
            raise Exception("Nao botou igual ou sinal")

        elif Parser.tokenizer.next.type == "PRINT":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "OPENPAR":
                Parser.tokenizer.selectNext()
                resultado = Println("PRINT", [Parser.parseBoolExpression()])
                if Parser.tokenizer.next.type == "CLOSEPAR":
                    Parser.tokenizer.selectNext()
                    return resultado
                raise Exception("Nao fechou parenteses 2")
            raise Exception("Nao abriu parenteses")

        elif Parser.tokenizer.next.type == "IF":
            Parser.tokenizer.selectNext()
            condition = Parser.parseBoolExpression()
            if Parser.tokenizer.next.type == "DDOT":
                Parser.tokenizer.selectNext()
                block = Parser.parseBlock()
                Parser.tokenizer.selectNext()
                resultado = If("IF", [condition, block])
                if Parser.tokenizer.next.type == "ELSE":
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "DDOT":
                        Parser.tokenizer.selectNext()
                        newBlock = Parser.parseBlock()
                        resultado.children.append(newBlock)
                if Parser.tokenizer.next.type == "ENTER":
                    Parser.tokenizer.selectNext()
                    return resultado
                raise Exception("faltou Enter depois do if")
            raise Exception("faltou dois pontos depois da condicao do if")

        elif Parser.tokenizer.next.type == "FOR":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "IDENTIFIER":
                valor_ident_for = Parser.tokenizer.next.value
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "EQUAL":
                    Parser.tokenizer.selectNext()
                    init = Assignment("EQUAL", [Identifier(valor_ident_for, None), Parser.parseBoolExpression()])
                    if Parser.tokenizer.next.type == "SEMICOLON":
                        Parser.tokenizer.selectNext()
                        condition_for = Parser.parseBoolExpression()
                        if Parser.tokenizer.next.type == "SEMICOLON":
                            Parser.tokenizer.selectNext()
                            if Parser.tokenizer.next.type == "IDENTIFIER":
                                increment_ident_for = Parser.tokenizer.next.value
                                Parser.tokenizer.selectNext()
                                if Parser.tokenizer.next.type == "EQUAL":
                                    Parser.tokenizer.selectNext()
                                    increment = Assignment("EQUAL", [Identifier(increment_ident_for, None), Parser.parseBoolExpression()])
                                    Parser.tokenizer.selectNext()
                                    block_for = Parser.parseBlock()
                                    resultado = For("FOR", [init, condition_for, increment, block_for])
                                    if Parser.tokenizer.next.type == "ENTER":
                                        Parser.tokenizer.selectNext()
                                        return resultado
                                    raise Exception("faltou Enter depois do for")
                                raise Exception("Faltou atribuir valor incremento do for")
                            raise Exception("Faltou incremento do for")
                        raise Exception("Faltou ponto e virgula depois do condition do for")
                    raise Exception("Faltou ponto e virgula depois do init do for")
                raise Exception("Nao atribuiu valor no init do for")
            raise Exception("Sem init do for")

        elif Parser.tokenizer.next.type == "INTTYPE" or Parser.tokenizer.next.type == "STRINGTYPE":
            valor_type_var = Parser.tokenizer.next.value
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "IDENTIFIER":
                valor_ident_var = Parser.tokenizer.next.value
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "EQUAL":
                    Parser.tokenizer.selectNext()
                    resultado = VarDec("VARIABLE", [valor_ident_var, valor_type_var, Parser.parseBoolExpression()])
                else:
                    resultado = VarDec("VARIABLE", [valor_ident_var, valor_type_var, None])

                if Parser.tokenizer.next.type == "ENTER":
                    Parser.tokenizer.selectNext()
                    return resultado
        elif Parser.tokenizer.next.type == "RETURN":
            Parser.tokenizer.selectNext()
            resultado = FuncReturn("RETURN", [Parser.parseBoolExpression()])
            if Parser.tokenizer.next.type == "ENTER":
                Parser.tokenizer.selectNext()
                return resultado
        elif Parser.tokenizer.next.type == "FUNCTION":
            resultado = Parser.parseDeclaration()
            return resultado

        raise Exception("Nao usou uma funcionalidade") 


    def parseBlock():
        if Parser.tokenizer.next.type == "ENTER":
            Parser.tokenizer.selectNext()
            resultado = Block(None, [])
            while Parser.tokenizer.next.type != "END":
                resultado.children.append(Parser.parseStatement())
            if Parser.tokenizer.next.type == "END":
                Parser.tokenizer.selectNext()
                return resultado
            raise Exception("Nao fechou chaves")
        raise Exception("Nao deu enter")

    def parseDeclaration():
        resultado = NoOp(None, [])
        if Parser.tokenizer.next.type == "FUNCTION":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "INTTYPE" or Parser.tokenizer.next.type == "STRINGTYPE" or Parser.tokenizer.next.type == "VOIDTYPE":
                function_type = Parser.tokenizer.next.value
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "IDENTIFIER":
                    function_iden = Parser.tokenizer.next.value
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "OPENPAR":
                        Parser.tokenizer.selectNext()
                        if Parser.tokenizer.next.type == "CLOSEPAR":
                            Parser.tokenizer.selectNext()
                            if Parser.tokenizer.next.type == "DDOT":
                                Parser.tokenizer.selectNext()
                                block = Parser.parseBlock()
                                funcDec = VarDec("FUNCTION_VARIABLE", [function_iden, function_type, None])
                                resultado = FuncDec("FUNCTION", [funcDec, block])
                                if Parser.tokenizer.next.type == "ENTER":
                                    Parser.tokenizer.selectNext()
                                    return resultado
                                raise Exception("Faltou Enter Funcao")
                            raise Exception("Faltou DDOT")
                        elif Parser.tokenizer.next.type == "INTTYPE" or Parser.tokenizer.next.type == "STRINGTYPE":
                            var_type = Parser.tokenizer.next.value
                            Parser.tokenizer.selectNext()
                            if Parser.tokenizer.next.type == "IDENTIFIER":
                                var_iden = Parser.tokenizer.next.value
                                var_dec = VarDec("VARIABLE", [var_iden, var_type, None])
                                var_dec_list = [var_dec]
                                Parser.tokenizer.selectNext()
                                if Parser.tokenizer.next.type == "COMA":
                                    while Parser.tokenizer.next.type == "COMA":
                                        Parser.tokenizer.selectNext()
                                        if Parser.tokenizer.next.type == "INTTYPE" or Parser.tokenizer.next.type == "STRINGTYPE":
                                            var_type = Parser.tokenizer.next.value
                                            Parser.tokenizer.selectNext()
                                            if Parser.tokenizer.next.type == "IDENTIFIER":
                                                var_iden = Parser.tokenizer.next.value
                                                var_dec = VarDec("VARIABLE", [var_iden, var_type, None])
                                                var_dec_list.append(var_dec)
                                                Parser.tokenizer.selectNext()
                                            else:
                                                raise Exception("Faltou tipo do argumento da funcao 2")
                                        else:
                                            raise Exception("Faltou identifier do argumento da funcao")        
                                if Parser.tokenizer.next.type == "CLOSEPAR":
                                    Parser.tokenizer.selectNext()
                                    if Parser.tokenizer.next.type == "DDOT":
                                        Parser.tokenizer.selectNext()
                                        block = Parser.parseBlock()
                                        funcDec = VarDec("FUNCTION_VARIABLE", [function_iden, function_type, None])
                                        resultado = FuncDec("FUNCTION", [funcDec])
                                        for variable in var_dec_list:
                                            resultado.children.append(variable)
                                        resultado.children.append(block)
                                        if Parser.tokenizer.next.type == "ENTER":
                                            Parser.tokenizer.selectNext()
                                            return resultado
                                        raise Exception("Faltou Enter Funcao")
                                    raise Exception("Faltou dois pontos")
                                raise Exception("Faltou fechar parenteses na funcao")
                            raise Exception("Faltou nome do argumento da funcao")
                        raise Exception("Erro nos argumentos da declaracao da funcao")
                    raise Exception("Faltou abrir parenteses da funcao")
                raise Exception("Nao nomeou a funcao")
            raise Exception("Nao tipou a funcao na sua declaracao")
        raise Exception("Nao usou def ao declarar funcao")

    def parseProgram():
        resultado = Block(None, [])
        while Parser.tokenizer.next.type != "EOF":
            resultado.children.append(Parser.parseStatement())
        return resultado


    def run(arquivo):
        ProCode = PrePro(arquivo, 0)
        texto = ProCode.filter()
        Parser.tokenizer.source = texto
        Parser.tokenizer.selectNext()
        resultado = Parser.parseProgram()
        if Parser.tokenizer.next.type != "EOF":
            raise Exception("Deveria ser o fim da string")
        return resultado