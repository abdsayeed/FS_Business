from flask import Flask
from blueprints.auth.auth import auth_bp
from blueprints.businesses.businesses import business_bp
from blueprints.reviews.reviews import reviews_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(business_bp)
app.register_blueprint(reviews_bp)

if __name__ == '__main__':
    app.run(debug=True)