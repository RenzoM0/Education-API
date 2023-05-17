from flask import Flask,jsonify,request
from views import views
import config


app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    app.run(debug=True, port=5000)