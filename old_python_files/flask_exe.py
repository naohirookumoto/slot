from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
# @manager.command
# @login_required
def index():
    return 


