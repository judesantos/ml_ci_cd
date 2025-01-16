"""

"""

from flask import Flask, request, redirect
from flask_talisman import Talisman

from routes import main, auth
from settings import settings


def create_app(db, jwt, limiter, oauth, csrf):
    """
    Create and configure the Flask application.

    This function sets up the Flask application with necessary configurations,
    initializes extensions, and registers blueprints.

    Returns:
        Flask: The configured Flask application instance.
    """

    app = Flask(__name__)

    # Secure headers
    csp = {
        'default-src': ["'self'"],
        'img-src': ["'self'", "data:"],
        'style-src': ["'self'", "'unsafe-inline'"],
        'script-src': ["'self'", "'unsafe-inline'"],
        #    'img-src': ["'self'", "https://trusted.cdn.com"]
    }
    Talisman(app, content_security_policy=csp)

    # Configure app

    track_notifications = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    google_discovery_url = settings.GOOGLE_DISCOVERY_URL

    app.config['SECRET_KEY'] = settings.SECRET_KEY
    app.config['JWT_SECRET_KEY'] = settings.JWT_SECRET_KEY
    # Set to True in production (requires HTTPS)
    app.config['JWT_COOKIE_SECURE'] = settings.JWT_COOKIE_SECURE
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']  # Store JWT in cookies
    # Default: 'access_token'
    app.config['JWT_ACCESS_COOKIE_NAME'] = 'access_token'
    app.config['JWT_COOKIE_CSRF_PROTECT'] = True
    app.config['JWT_COOKIE_SAMESITE'] = 'None'  # For cross-site cookies

    app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = track_notifications

    app.config['GOOGLE_CLIENT_ID'] = settings.GOOGLE_CLIENT_ID
    app.config['GOOGLE_CLIENT_SECRET'] = settings.GOOGLE_CLIENT_SECRET
    app.config['GOOGLE_DISCOVERY_URL'] = google_discovery_url
    app.config['MAX_CONTENT_LENGTH'] = settings.MAX_CONTENT_LENGTH

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    limiter.init_app(app)
    csrf.init_app(app)
    oauth.init_app(app)

    # Register blueprints
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)

    with app.app_context():
        db.create_all()

    @app.before_request
    def redirect_to_https():
        if not request.is_secure and app.env != "development":
            return redirect(request.url.replace("http://", "https://"))

    # @app.after_request
    # def add_cache_control_headers(response):
    #    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    #    response.headers['Pragma'] = 'no-cache'
    #    response.headers['Expires'] = '-1'
    #    return response

    @app.after_request
    def disable_source_map(response):
        if response.content_type.startswith("text/javascript"):
            response.headers['SourceMap'] = ''
        return response

    return app
