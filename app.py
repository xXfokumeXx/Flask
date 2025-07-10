from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello, World!"


@app.route("/fancy")
def hello_world_fancy():
    return """
        <html>
        <body>

        <h1>Greetings!</h1>
        <p>"Hello, World"!</p>
        
        </body>
        </html>
    """