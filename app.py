from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv


def crear_app():
    app = Flask(__name__)


    def verificar_pci_critico(entrada_json):
        JsonRetorno = [
            {
                "seccion": "PI-1",
                "Plan Mantenimiento": [0, 0, 0, 3, 1, 0, 1, 0, 1, 0, 1, 2, 2, 2, 0, 1, 0, 2, 0, 0],
                "Costos": [0, 0, 0, 5, 2, 0, 2, 0, 2, 0, 2, 4, 4, 4, 0, 2, 0, 4, 0, 0],
                "PCI": [92, 87, 83, 76, 92, 95, 92, 95, 92, 95, 92, 95, 95, 95, 95, 92, 95, 92, 95, 92]
            }
        ]

        return JsonRetorno if entrada_json.get("PCI_critico") == 65 else []





    @app.route("/")
    def pagina():
        return render_template("pagina.html")


    @app.route("/api/verificar", methods=["POST"])
    def api_verificar():
        entrada_json = request.get_json()
        nuevoJson = verificar_pci_critico(entrada_json)
        return jsonify(nuevoJson)
    return app

if __name__ == "__main__":
    app = crear_app()
    app.run()