from flask import Flask, request, session, redirect, url_for
from app.routes import bp

# db = SQLAlchemy()
# migrate = Migrate()

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)
    # cors = CORS(app, resources={"r/*": {"origins": "0.0.0.0"}})
    app.url_map.strict_slashes = False

    # db.init_app(app)
    # migrate.init_app(app, db)

    app.register_blueprint(bp)

    @app.before_request
    def require_login():
        """Ensure only authenticated users access the site"""
        path = request.path
        excluded_endpoints = ['login', 'test']
        # if path not in excluded_endpoints:
        #     print(path)

        if not any(endpoint in path for endpoint in excluded_endpoints) and not session.get('user_id'):
            return redirect(url_for('routes.login'))

    # @app.after_request
    # def after_request(response):
    #     """Remove cache for e-portal to prevent voting twice"""
    #     response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    #     # if 'e-portal' in request.path:
    #     #     session.pop('user_id', None)
    #     return response

    return app





