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
        if (self.mes[data[0]][data[1]][data[2]] == 1):
            return False
        else:
            return True

    # Formato do data tem que ser mes:dia:hora mm:dd:hh
    def setarData(self, data):
        dataHora = self.formatarData(data)
        if (self.verificaData(data)):
            self.mes[dataHora[0]][dataHora[1]][dataHora[2]] = 1
            return True
        else:
            return False

