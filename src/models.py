class Medico:
    def __init__(self, id=None, login="", senha="", nome=""):
        self.id = id
        self.login = login
        self.senha = senha
        self.nome = nome

    def __repr__(self):
        return f"<Medico {self.login}>"


class Paciente:
    def __init__(self, id=None, prontuario="", identificacao=""):
        self.id = id
        self.prontuario = prontuario
        self.identificacao = identificacao

    def __repr__(self):
        return f"<Paciente {self.prontuario} - {self.identificacao}>"


class Exame:
    def __init__(self, id=None, data="", descricao="", dados_csv="", id_paciente=None, id_medico=None):
        self.id = id
        self.data = data
        self.descricao = descricao
        self.dados_csv = dados_csv
        self.id_paciente = id_paciente
        self.id_medico = id_medico

    def __repr__(self):
        return f"<Exame {self.data} - Paciente {self.id_paciente} - Médico {self.id_medico}>"
