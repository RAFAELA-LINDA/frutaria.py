from cad_fruta import Fruta 
frutinhas = Fruta()

acessopemitido = False
usuario = "adm"
senha = "adm"

qusuario = input("Digite seu usuario: ")
qsenha = input("Digite sua senha: ") 

if (senha == qsenha and usuario == qusuario):
    acessopermitido = True
else: 
    print("Acesso negado")

while acessopermitido:
    print("menu \n")
    print("1 - cadastro")
    print("10 - sair")
    menu = input("qual opção: ")
    if menu == "1":
        frutinhas.cadastro_fruta()
    elif menu == "10":
        acessopermitido = False
    else:
        print("opção invalida")





