from EvalExp import evaluar_expresion, shuntingyard, Operar
import os

def main():

    # 🤖 Prompt: Por que no funciona el declarar la ruta como '../expresiones.txt'? Me suelta error en el que no encuentra el archivo deseado.
    ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'expresiones.txt'))

    with open(ruta, 'r') as archivo:
        for expresion in archivo:
            expresion = expresion.strip()
            print(f"InFix: {expresion}")
            postfix = shuntingyard(expresion)
            if evaluar_expresion(expresion):
                print(f"PostFix: {postfix}")
                print(f"Resultado: {Operar(postfix)}")
            print("-" * 40)

if __name__ == "__main__":
    main()
