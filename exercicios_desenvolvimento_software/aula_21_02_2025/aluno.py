class Aluno:
    def __init__(self,codigo,nome,idade,serie,periodo,nota_1,nota_2):
        self._codigo = codigo
        self.nome = nome
        self.idade = idade
        self.serie = serie
        self.periodo = periodo
        self.nota_1 = nota_1
        self.nota_2 =  nota_2

    def __str__(self):
        return(f"Nome: {self.nome} / idade: {self.idade} / Série:{self.serie} / Período: {self.periodo}")
    def calcular_media(self):
        media= (self.nota_1 + self.nota_2) / 2
        print(f"a média do aluno foi de: {media}")

if __name__ == "__main__":

    aluno1=Aluno(12453,"João Silva",18,"8","Manhã",6,10)
    print(aluno1)
    aluno1.calcular_media()
