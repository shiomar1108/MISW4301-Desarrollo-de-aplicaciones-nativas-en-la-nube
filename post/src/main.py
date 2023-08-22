from models import create_app
from models.model import db, Post
from models.model import PostSchema
from models.config import set_config
from blueprints.api import api_blueprint
from flask_cors import CORS
import uuid
from datetime import datetime

app = create_app()
set_config(app)
app_context = app.app_context()
app_context.push()
app.register_blueprint(api_blueprint)
cors = CORS(app)
db.init_app(app)
db.create_all()




if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")
