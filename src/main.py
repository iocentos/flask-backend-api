from flask import Flask


# Create main application object
app = Flask(__name__)



# Routes registration
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/users")
def users():
    return "Hello users!"


# End of routes registration



# Main app code
if __name__ == "__main__":
    app.run()
