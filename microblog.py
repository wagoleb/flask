from app import app, db, errors
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    app.logger.info("starting flask app")
    return {"db": db, "User": User, "Post": Post, "Errors": errors}
