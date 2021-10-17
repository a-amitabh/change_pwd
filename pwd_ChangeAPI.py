from flask import Flask, jsonify
import changePassword

app = Flask(__name__)

@app.route("/chg_pwd/<string:curr_pwd>/<string:new_pwd>", methods=['GET'])
def chg_pwd(curr_pwd, new_pwd):
    print(type(changePassword.changePassword(curr_pwd, new_pwd)))
    return str(changePassword.changePassword(curr_pwd, new_pwd))

if __name__ == "__main__":
    app.run(debug=True)