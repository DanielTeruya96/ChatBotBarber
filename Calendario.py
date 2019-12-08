class Calendario:

    def __init__(self):
        self.mes = []
        for i in range(12):
            dias = []
            for j in range(31):
                horas = []
                for k in range(24):
                    if k >= 8 and k <= 18:
                        horas.append(0)
                    else:
                        horas.append(1)
                dias.append(horas)
            self.mes.append(dias)

    def formatarData(self, data):
        vet = []
        vet = data.split(":")
        ret = []
        ret.append(int(vet[0]))
        ret.append(int(vet[1]))
        ret.append(int(vet[2]))
        return ret

    def verificaData(self, data):
        data = self.formatarData(data)
        if (self.mes[data[0]-1][data[1]-1][data[2]-1] == 1):
            return False
        else:
            return True

    # Formato do data tem que ser mes:dia:hora mm:dd:hh
    def setarData(self, data):
        dataHora = self.formatarData(data)
        if (self.verificaData(data)):
            self.mes[dataHora[0]-1][dataHora[1]-1][dataHora[2]-1] = 1
            return True
        else:
            return False


    def verificaDia(self,dia):
        dia = int(dia)
        for d in self.mes[11][dia-1]:
            if d == 0:
                return True

        return False

    def disponibilidadeDia(self,mes,dia):
        for dia in self.mes[mes-1][dia-1]:
            if dia == 0:
                return True

        return False

    def montarHorasPorPeriodo(self, listaPeriodo, adia, ames):
        dia = int(adia)
        mes = int(ames)
        retorno = "Temos disponível\n"
        for periodo in listaPeriodo:
            if (periodo == 1):
                if self.mes[mes-1][dia-1][8-1] == 0:
                    retorno += "8 horas da amnhã\n"
                if(self.mes[mes-1][dia-1][9-1] == 0):
                    retorno += "9 horas da manhã\n"
                if(self.mes[mes-1][dia-1][10-1] == 0):
                    retorno += "10 horas da amnhã\n"
                if(self.mes[mes-1][dia-1][11-1] == 0):
                    retorno += "11 horas da manhã\n"

            if(periodo == 2):
                if self.mes[mes-1][dia-1][12-1] == 0:
                    retorno+="12 horas \n"
                if self.mes[mes-1][dia-1][13-1] == 0:
                    retorno+="13hora(1hora) da tarde\n"
                if self.mes[mes-1][dia-1][14-1] == 0:
                    retorno+="14hora(2hora) da tarde\n"
                if self.mes[mes-1][dia-1][15-1] == 0:
                    retorno += "15hora(3hora) da tarde\n"
                if self.mes[mes-1][dia-1][16-1] == 0:
                    retorno += "16hora(4hora) da tarde\n"

            if(periodo == 3):
                if self.mes[mes-1][dia-1][17-1] == 0:
                    retorno += "17hora(5hora) \n"
                if self.mes[mes-1][dia-1][18-1] == 0:
                    retorno += "18hora(6hora) \n"

        return retorno

    def getPeriodoForaDaLista(self, listaPeriodo, diaGlobal, mesHoje):
        lista = list()
        for i in range(3):
            if i not in listaPeriodo:
                lista.append(i)

        return self.montarHorasPorPeriodo(lista,diaGlobal,mesHoje)
    pass



