from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_airport_info(icao):
    conn = sqlite3.connect("airports.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, municipality FROM airport WHERE ident = ?", (icao,))
    result = cursor.fetchone()
    conn.close()
    return result


@app.route("/airport/<string:icao>")
def airport(icao):
    data = get_airport_info(icao)

    if data:
        name, city = data
        return jsonify({
            "ICAO": icao,
            "Name": name,
            "Location": city
        })
    else:
        return jsonify({"error": "Airport not found"}), 404


if __name__ == "_main_":
    app.run(use_reloader=False)
