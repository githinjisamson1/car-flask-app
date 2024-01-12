# imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instantiate SQLAlchemy
db = SQLAlchemy()

# create_app function to initialize and configure the Flask application


def create_app():
    # Instantiate the Flask application
    app = Flask(__name__)

    # Configure the database URI for SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    # Initialize the SQLAlchemy extension with the Flask app
    db.init_app(app)

    # Import and register the blueprint from the 'routes' module
    from .routes import bp
    app.register_blueprint(bp)

    # Create the database tables within the application context
    with app.app_context():
        db.create_all()

    # Return the configured Flask application
    return app
