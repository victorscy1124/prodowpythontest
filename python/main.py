# -*- coding: utf-8 -*-
from bottle import Bottle, run
from controller.foo import foo_app

Routes = Bottle()

Routes.mount("/foo", foo_app)

@Routes.error(404)
def error404(error):
    return 'sorry, 404'

@Routes.error(500)
def error500(error):
    return 'sorry, 500'

if __name__ == '__main__':
    run(Routes, host='0.0.0.0', port=8080, reloader=True, debug=True)