from werkzeug.wsgi import SharedDataMiddleware
from sr.comp.http import app as api_app

app = SharedDataMiddleware(api_app, {
    '/screens': 'srcomp-screens'
})

api_app.config['COMPSTATE'] = 'dummy-comp'
api_app.config['COMPSTATE_LOCAL'] = True

