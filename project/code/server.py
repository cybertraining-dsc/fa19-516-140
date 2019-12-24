from flask import jsonify
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("project.yaml")


# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "Server is working Now"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
