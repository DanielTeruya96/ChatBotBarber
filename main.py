import Calendario
import Classificador
import Entidades
#saudacao
def saudacao(frase):
    print("Bom dia")



def verificar(frase):
  data = ""
  #mes =
  dia = ""
  hora = ""
  for palavra in frase:
      auxMes = Entidades.getMes(palavra)
      auxDia = Entidades.getDia(palavra)
      auxHora = Entidades.getHora(palavra)



def switch_intencao(intencao, frase):
    if (intencao == "saudacao"):
        saudacao(frase)
    if (intencao == "verificar"):
        verificar(frase)
    # if (intencao == "positivo"):
    #     finalizar(frase)
    # if (intencao == "negativo"):
    #     negativo(frase)
    # if (intencao == "preco"):
    #     preco(frase)


#Main
classificador = Classificador.Classificador()
intencao = "saudacao"
print("Seja bem vindo a barbearia!  ")
while(intencao != "finalizar"):
  frase = input("")
  intencao = classificador.getIntencao(frase)
  switch_intencao(intencao,frase)


