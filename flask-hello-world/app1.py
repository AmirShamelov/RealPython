from flask import Flask

app=Flask(__name__)

app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")

def hello_world():
    return "Hello, Amir!"

@app.route("/")
@app.route("/name/<name>")

def index(name):
    if name.lower() == "michael":
        return "Hello, {}".format(name)
    else:
        return "Not Found", 400

@app.route("/test/<search_query>")
def search(search_query):
    return search_query

if __name__ == "__main__":
    app.run()
