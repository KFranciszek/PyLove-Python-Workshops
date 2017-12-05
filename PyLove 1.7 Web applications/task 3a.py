# Napisz program, który: po wejściu na adres
# /user/<username>/set-password ustawi hasło użytkownika username (na podstawie podanego JSON-a).

from flask import Flask, request


app = Flask(__name__)
@app.route("/user/<username>/set-password", methods=["POST"])
def set(username):
    if request.method == "POST":
        data = {username: "12345"}
        data = request.get_json()
        password = "12345"
        password = data[username]
        return "Saved password"
app.run(debug=True)