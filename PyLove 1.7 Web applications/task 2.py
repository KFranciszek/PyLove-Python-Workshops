# Napisz program, który po wejściu na adres /current-status metodą POST ustawi aktualny status na podstawie
# przekazanego w zapytaniu JSON-a (np. {"status": "starting"}),
# a po wejściu na ten sam adres metodą GET zwróci aktualny status.


from flask import Flask, request


app = Flask(__name__)
status = "Data"
@app.route("/current-status", methods=["GET", "POST"])
def save():
    global status
    if request.method == "GET":
        return status
    else:
        data = request.get_json()
        status = data["status"]
        return "Saved status: {}".format(status)

app.run(debug=True)