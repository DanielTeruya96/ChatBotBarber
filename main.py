import Calendario
import Classificador
import Entidades
from datetime import date

data_atual = date.today()
datas = str(data_atual).split("-")


hoje = data_atual
diaHoje = datas[2]
mesHoje = datas[1]
diaGlobal = ""
horaGlobal = ""
semana = data_atual.weekday()


def verificar(frase):

    dia = definirDia()

    horario = definirHorario(dia)

    frase = input("Voce gostaria de confirmar no dia "+str(dia)+" as "+str(horario)+"horas?")
    intencao = classificador.getIntencao(frase)

    if intencao == "confirmar":
        data = str(mesHoje)+":"+str(dia)+":"+str(horario)
        if(agenda.setarData(data)):
            print("confirmamos sua reserva te espero no dia "+str(dia)+" as "+str(horario)+"horas")
        else:
            print("ops, algo deu de errado, vamos marcar horario novamente?")

    else:
        return




def switch_intencao(intencao, frase):
    if (intencao == "saudacao"):
        saudacao(frase)
    if (intencao == "verificar"):
        verificar(frase)





def saudacao(frase):
    print("Bom dia")


def definirDia():
    intencao = "negar"
    contador = 0
    perguntaPadrao = " para qual dia gostaria marcar?"
    pergunta = perguntaPadrao;
    while intencao == "negar" and contador < 10:
        frase = input(pergunta)
        dia = ""
        if frase is None or len(frase) == 0:
            continue
        if(Entidades.contemDiaSemana(frase)):
            dif = Entidades.getDiferencaSemana(frase,semana)
            dia = int(diaHoje)+dif
        else:
            dia = Entidades.descobreDia(frase)


        if dia is None:
            pergunta = "Não intendi direito, para qual dia voce gostaria de marcar?"
            continue

        if agenda.disponibilidadeDia(int(mesHoje),int(dia)) is not True:
            pergunta = "Esse dia esta cheio, por favor poderia escolher outro dia?"
            continue

        frase = input("para o dia "+str(dia)+" temos horario gostaria de marcar para esse dia?")
        intencao = classificador.getIntencao(frase)
        if(intencao == "negar"):
            pergunta = "Qual o outro dia que gostaria de marcar então?"
            contador = contador+1

    return dia


def definirHorario(dia):
    perguntaPadrao = "Em que horario gostaria de marcar?"
    pergunta = perguntaPadrao
    intencao = "negar"
    while intencao == "negar":
        frase = input(pergunta)
        if Entidades.possuiPeriodo(frase):
            listaPeriodo = Entidades.getListaPeriodo(frase)
            pergunta = agenda.montarHorasPorPeriodo(listaPeriodo,dia,mesHoje)
            continue
        else:
            pergunta = "Não temos horario nesse período "
            listaPeriodo = Entidades.getListaPeriodo(frase)
            pergunta = agenda.getPeriodoForaDaLista(listaPeriodo,dia,mesHoje)


        if Entidades.temHora(frase):
            horas = Entidades.getHoras(frase)
            if len(horas) == 1:

                if agenda.verificaData(str(mesHoje)+":"+str(dia)+":"+str(horas[0])):
                    frase = input("voce gostaria de marcar as " + str(horas[0]) + " horas?")
                    intencao = classificador.getIntencao(frase)
                    if intencao == "confirmar":
                        return horas[0]
                else:
                    pergunta = "Não temos disponibilidade para esse horario"
                    continue


            else:
                pergunta = "em que horario voce gostaria de marcar? "
                for hora in horas:
                    pergunta+= str(hora)+"h "

        else:
            pergunta = "Não intendi direito, por favor me diga um horario que gostaria de marcar"
            continue









#Main
classificador = Classificador.Classificador()
agenda = Calendario.Calendario()
intencao = "saudacao"
print("Seja bem vindo a barbearia!  ")
while(intencao != "confirmar"):
  frase = input("")
  intencao = classificador.getIntencao(frase)
  switch_intencao(intencao,frase)