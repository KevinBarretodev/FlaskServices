from flask import Flask


app = Flask(__name__)

# Este primer servicio es de introduccion, solo nos devuelve el saludo
@app.route("/helloworld", methods=['GET'])
def index():

    return "Hello world"



if __name__ == "__main__":
    app.run()