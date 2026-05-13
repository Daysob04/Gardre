from flask import Flask, redirect
import os

app = Flask(__name__)

# Alias principal
@app.route('/unidos-por-el-futbol')
def pdf():
    return redirect(
        "https://drive.google.com/file/d/11CyguACvI0XXEZCYx_S2mvuJDof6-UoU/view?usp=sharing",
        code=302
    )

# Página inicio
@app.route('/')
def home():
    return "Servidor funcionando correctamente"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)