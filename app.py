from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Bienvenido al Sistema de Reservas Médicas – Clínica SaludPlus"

@app.route('/cita/<paciente>')
def cita(paciente):
    return f"Hola {paciente}, tu cita médica está en proceso de confirmación."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
