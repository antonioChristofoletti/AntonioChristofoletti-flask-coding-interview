from flask_openapi3 import OpenAPI

from api.users.routes import users_app
from database import db


def register_routes(app):
    pass


def create_app():
    app = OpenAPI(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://test:test@localhost:5432/flask_interview"
    db.init_app(app)
    app.register_api(users_app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
