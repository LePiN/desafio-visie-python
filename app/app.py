from .util.connection import Mysql_Connector
from .util.models import Pessoa
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        person = Pessoa(request.form.to_dict())
        Mysql_Connector().modify(
            f"INSERT INTO pessoas(nome, rg, cpf, data_nascimento, data_admissao)"
            f"VALUES('{person.name}', '{person.rg}', '{person.cpf}', '{person.birthday_date}', "
            f"'{person.admission_date}')"
        )

    result = Mysql_Connector().search("SELECT * FROM pessoas")
    return render_template(
        "base.html", person_data=[Pessoa(registro) for registro in result]
    )


@app.route("/delete", methods=["POST"])
def delete():
    if request.method == "POST":
        id_pessoa = request.form.get("id_person")
        Mysql_Connector().modify(f"DELETE FROM pessoas WHERE id_pessoa='{id_pessoa}'")
    result = Mysql_Connector().search("SELECT * FROM pessoas")
    return render_template(
        "base.html", person_data=[Pessoa(registro) for registro in result]
    )


if __name__ == "__main__":
    app.run(debug=True)
