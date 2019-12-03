
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression


class Classificador:

    def __init__(self):
        self.vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, strip_accents='unicode')
        corpus = ['Bom dia',
                  'Boa tarde',
                  'Olá',
                  'Como vai',
                  'Eae',
                  'Hey',
                  'Opa',
                  'Blz',
                  'Beleza',
                  'Hello',
                  'Boa noite',
                  'Oi',
                  'Salve',
                  'Boa noite',
                  'Firmesa',
                  'E aí chefia',
                  'Tem horário às 17h?',
                  'Está livre às 17h?',
                  'Quero marcar um horário para às 17h.',
                  'Gostaria de marcar um horário para às 17h',
                  'Tem disponibilidade para 17h?',
                  'Quero Marcar as 17h',
                  'Quero as 17h',
                  'Quero fazer a barba',
                  'gostaria de fazer a barba',
                  'Atende no sábado?',
                  'Atende às 17h?',
                  'Vocês abrem final de semana?',
                  'Quinta tem horário?',
                  'Então quero marcar as 18h',
                  'Ainda tem horário hoje?',
                  'vou às 14h',
                  'to indo às 17h',
                  'segunda às 6h',
                  'Quero marcar entre 15h até as 18h',
                  'Quero agendar um horário',
                  'Quero marcar um horário',
                  'Tem outro horário?',
                  'Quero marcar outro horário',
                  'Me vê um horário',
                  'Tem mais tarde?',
                  'Tem mais cedo?',
                  'Beleza',
                  'Pode ser',
                  'Confirmado.',
                  'ok',
                  'Até lá',
                  'Só isso.',
                  'Obrigado',
                  'Tá okay.',
                  'Sim.',
                  'desde já agradeço.',
                  'Obrigado por tudo.',
                  'Obrigado pela atenção.',
                  'Abraço.',
                  'Beijo.',
                  'Aguardo retorno.',
                  'Nessa hora não dá.',
                  'Não quero.',
                  'Muito caro.',
                  'Não tenho interesse.',
                  'não posso.',
                  'Quanto custa fazer a barba?',
                  'Quanto é?',
                  'serve cerveja?',
                  'preço',
                  'qual o preço do corte?',
                  'o corte de cabelo é quanto?',
                  'Quanto é o corte?',
                  'Tem desconto?',
                  'Tem promoção?',
                  'Corta de criança?',
                  'Tem corte infantil?',
                  'Levando a família tem desconto?',
                  'Quanto fica?',
                  'Qual é o mais barato?',
                  'Passa cartão?',
                  'Passa no débito?',
                  'Parcela?',
                  'Aceita VR?',
                  'Faz mais barato?',
                  'É caro?',
                  'Lista de preço.',
                  'Cortam na máquina?',
                  'Tinge cabelo?',
                  'Faz cavanhaque?']
        x = self.vectorizer.fit_transform(corpus)

        y = np.array(
            ['saudacao', 'saudacao', 'saudacao', 'saudacao', 'saudacao', 'saudacao', 'saudacao', 'saudacao', 'saudacao',
             'saudacao', 'saudacao', 'saudacao', 'saudacao', 'saudacao', 'saudacao', 'saudacao',
             'verificar', 'verificar', 'verificar', 'verificar', 'verificar', 'verificar', 'verificar', 'verificar',
             'verificar', 'verificar', 'verificar', 'verificar', 'verificar', 'verificar', 'verificar', 'verificar',
             'verificar', 'verificar', 'verificar', 'verificar', 'verificar', 'verificar', 'verificar', 'verificar',
             'verificar', 'verificar',
             'confirmar', 'confirmar', 'confirmar', 'confirmar', 'confirmar', 'confirmar', 'confirmar', 'confirmar',
             'confirmar', 'confirmar', 'confirmar', 'confirmar', 'confirmar', 'confirmar', 'confirmar',
             'negar', 'negar', 'negar', 'negar', 'negar',
             'preco', 'preco', 'preco', 'preco', 'preco', 'preco', 'preco', 'preco', 'preco', 'preco', 'preco', 'preco',
             'preco', 'preco', 'preco', 'preco', 'preco', 'preco', 'preco', 'preco', 'preco', 'preco', 'preco',
             'preco'])

        # classificando com decision tree
        self.model = DecisionTreeClassifier(random_state=0)
        self.model.fit(x, y)

    def getIntencao(self,frase):
        inst = self.vectorizer.transform([frase])
        return self.model.predict(inst)

