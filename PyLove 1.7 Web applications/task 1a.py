# Napisz program, który po wejściu na adres:
# /add/<liczba1>/<liczba2> odpowie sumą podanych liczb. Przykład: wejście na /add/3/5 powinno zwrócić "8".


from flask import Flask


app = Flask(__name__)

@app.route("/add/<int:liczba1>/<int:liczba2>")
def function(liczba1, liczba2):
    return str(liczba1+liczba2)

app.run(debug=True)