class Pessoa:
    def __init__(self, character):
        self.id_person = character.get("id_pessoa")
        self.name = character.get("nome")
        self.first_name = self._only_first_name()
        self.rg = character.get("rg")
        self.cpf = character.get("cpf")
        self.birthday_date = character.get("data_nascimento")
        self.admission_date = character.get("data_admissao")
        self.function = character.get("funcao")

    def _only_first_name(self):
        return self.name.split(" ")[0]

    def format_admission_date(self):
        return self.admission_date.strftime("%d/%m/%Y")

    def __str__(self) -> str:
        return f"{self.name}/{self.rg}/{self.cpf}/{self.birthday_date}/{self.admission_date}/{self.function}"
