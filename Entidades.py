
def getHora(palavra):
    hora = {
        "1": 1, "1h": 1, "uma": 1, "Uma": 1,
        "2": 2, "2h": 2, "duas": 2, "Duas": 2,
        "3": 3, "3h": 3, "tres": 3, "três": 3, "Tres": 3, "Três": 3,
        "4": 4, "4h": 4, "quatro": 4, "Quatro": 4,
        "5": 5, "5h": 5, "cinco": 5, "Cinco": 5,
        "6": 6, "6h": 6, "seis": 6, "Seis": 6,
        "7": 7, "7h": 7, "sete": 7, "Sete": 7,
        "8": 8, "8h": 8, "oito": 8, "Oito": 8,
        "9": 9, "9h": 9, "nove": 9, "Nove": 9,
        "10": 10, "10h": 10, "dez": 10, "Dez": 10,
        "11": 11, "11h": 11, "onze": 11, "Onze": 11,
        "12": 12, "12h": 12, "doze": 12, "meio": 12, "Doze": 12, "Meio": 12,
        "13": 13, "13h": 13, "treze": 13, "Treze": 13,
        "14": 14, "14h": 14, "quatorze": 14, "Quatorze": 14,
        "15": 15, "15h": 15, "quinze": 15, "Quinze": 15,
        "16": 16, "16h": 16, "dezesseis": 16, "Dezesseis": 16,
        "17": 17, "17h": 17, "dezessete": 17, "Dezessete": 17,
        "18": 18, "18h": 18, "dezoito": 18, "Dezoito": 18,
        "19": 19, "19h": 19, "dezenove": 19, "Dezenove": 19,
        "20": 20, "20h": 20, "vinte": 20, "Vinte": 20,
        "21": 21, "21h": 21, "vinte e uma": 21, "Vinte e uma": 21,
        "22": 22, "22h": 22, "vinte e duas": 22, "Vinte e duas": 22,
        "23": 23, "23h": 23, "vinte e tres": 23, "vinte e três": 23, "Vinte e tres": 23, "Vinte e três": 23,
        "24": 24, "24h": 24, "vinte e quatro": 24, "Vinte e quatro": 24
    }

    return hora.get(palavra)

def getDia(palavra):
    dia = {
        "1": 1, "primeiro": 1, "Primeiro": 1,
        "2": 2, "dois": 2, "Dois": 2,
        "3": 3, "tres": 3, "três": 3, "Tres": 3, "Três": 3,
        "4": 4, "quatro": 4, "Quatro": 4,
        "5": 5, "cinco": 5, "Cinco": 5,
        "6": 6, "seis": 6, "Seis": 6,
        "7": 7, "sete": 7, "Sete": 7,
        "8": 8, "oito": 8, "Oito": 8,
        "9": 9, "nove": 9, "Nove": 9,
        "10": 10, "dez": 10, "Dez": 10,
        "11": 11, "onze": 11, "Onze": 11,
        "12": 12, "doze": 12, "Doze": 12,
        "13": 13, "treze": 13, "Treze": 13,
        "14": 14, "quatorze": 14, "Quatorze": 14,
        "15": 15, "quinze": 15, "Quinze": 15,
        "16": 16, "dezesseis": 16, "Dezesseis": 16,
        "17": 17, "dezessete": 17, "Dezessete": 17,
        "18": 18, "dezoito": 18, "Dezoito": 18,
        "19": 19, "dezenove": 19, "Dezenove": 19,
        "20": 20, "vinte": 20, "Vinte": 20,
        "21": 21, "vinte e um": 21, "Vinte e um": 21,
        "22": 22, "vinte e dois": 22, "Vinte e dois": 22,
        "23": 23, "vinte e tres": 23, "Vinte e três": 23, "vinte e tres": 23, "vinte e três": 23,
        "24": 24, "vinte e quatro": 24, "Vinte e quatro": 24,
        "25": 25, "vinte e cinco": 25, "Vinte e cinco": 25,
        "26": 26, "vinte e seis": 26, "Vinte e seis": 26,
        "27": 27, "vinte e sete": 27, "Vinte e sete": 27,
        "28": 28, "vinte e oito": 28, "Vinte e oito": 28,
        "29": 29, "vinte e nove": 29, "Vinte e nove": 29,
        "30": 30, "trinta": 30, "Trinta": 30,
        "31": 31, "trinta e um": 31, "Trinta e um": 31
    }

    return dia.get(palavra)

def getMes(palavra):
    mes = {
        "janeiro": 1, "Janeiro": 1, "jan": 1, "Jan": 1,
        "fevereiro": 2, "Fevereiro": 2, "fev": 2, "Fev": 2,
        "marco": 3, "Março": 3, "marco": 3, "Março": 3, "mar": 3, "Mar": 3,
        "abril": 4, "Abril": 4, "abr": 4, "Abr": 4,
        "maio": 5, "Maio": 5, "mai": 5, "Mai": 5,
        "junho": 6, "Junho": 6, "jun": 6, "Jun": 6,
        "julho": 7, "Julho": 7, "jul": 7, "Jul": 7,
        "agosto": 8, "Agosto": 8, "ago": 8, "Ago": 8,
        "setembro": 9, "Setembro": 9, "set": 9, "Set": 9,
        "outubro": 10, "Outubro": 10, "out": 10, "Out": 10,
        "novembro": 11, "Novembro": 11, "nov": 11, "Nov": 11,
        "dezembro": 12, "Dezembro": 12, "dez": 12, "Dez": 12
    }

    return mes.get(palavra)


def getSemana(palavra):
    semana = {
        "domingo": 1, "Domingo": 1, "dom": 1, "Dom": 1,
        "segunda": 2, "Segunda": 2, "seg": 2, "Seg": 2,
        "terça": 3, "terca": 3, "Terça": 3, "Terca": 3, "ter": 3, "Ter": 3,
        "quarta": 4, "Quarta": 4, "qua": 4, "Qua": 4,
        "quinta": 5, "Quinta": 5, "qui": 5, "Qui": 5,
        "sexta": 6, "Sexta": 6, "sex": 6, "Sex": 6,
        "sábado": 7, "sabado": 7, "Sábado": 7, "Sabado": 7, "sab": 7, "Sab": 7
    }
    if(semana.get(palavra) is None):
        return None
    return semana.get(palavra)-2

def getPeriodo(palavra):
    periodo = {
        "manha": 1, "Manha": 1, "manhã": 1, "Manhã": 1,
        "tarde": 2, "Tarde": 2,
        "noite": 3, "Noite": 3
    }
    return periodo.get(palavra)

def descobreDia(frase):
    palavras = frase.split(" ")
    for palavra in palavras:
        numero = getDia(palavra)
        if numero is not None:
            return numero

    return None


def possuiPeriodo(frase):
    palavras = frase.split(" ")
    for palavra in palavras:
        periodo = getPeriodo(palavra)
        if periodo is not None:
            return True

    return False


def getListaPeriodo(frase):
    palavras = frase.split(" ")
    listaPeriodos = list()
    for palavra in palavras:
        periodo = getPeriodo(palavra)
        if periodo is not None:
            listaPeriodos.append(periodo)


    return listaPeriodos


def temHora(frase):
    palavras = frase.split(" ")
    for palavra in palavras:
        if getHora(palavra) is not None:
            return True

    return False


    return None

#retorna uma lista de horas
def getHoras(frase):

    lista = list()
    for palavra in frase.split(" "):
        hora = getHora(palavra)
        if hora is not None:
            lista.append(hora)


    return lista


def contemDiaSemana(frase):
    for palavra in frase.split(" "):
        if getSemana(palavra) is not None:
            return True

    return False



def getDiferencaSemana(frase,hoje):
    semana = 0
    for palavra in frase.split(" "):
        if getSemana(palavra) is not None:
            semana = getSemana(palavra)
    if semana < hoje:
        semana = semana+7


    return semana-hoje