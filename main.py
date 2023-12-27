import flask

def crar_app():
    app = flask.Flask(__name__)


    @app.route('/')
    def index():
        return flask.render_template('index.html')
    
    return app


if __name__ == '__main__':
    app = crar_app()
    app.run()