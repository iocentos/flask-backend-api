from flask import Flask, request


# Create main application object
app = Flask(__name__)



# Routes registration
@app.route("/hello-world")
def hello():
    return "Hello World!"


@app.route("/user/<user_id>", methods=['GET'])
def user(user_id):
    return "Hello user {}".format(user_id)


# End of routes registration



# Main app code
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
