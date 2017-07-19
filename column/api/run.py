import logging

import flask
import flask_restful

from column import cfg
from column.api.controller import run_controller

app = flask.Flask(__name__)
api = flask_restful.Api(app)

api.add_resource(run_controller.Run, '/runs/<id>')
api.add_resource(run_controller.RunList, '/runs')


if __name__ == '__main__':
    log_file = cfg.get('DEFAULT', 'log_file')
    log_level = cfg.get('DEFAULT', 'log_level')
    logging.basicConfig(filename=log_file,
                        format='%(asctime)s %(levelname)s '
                               '%(name)s %(message)s',
                        level=log_level)

    server = cfg.get('API', 'server')
    port = cfg.get('API', 'port')

    app.run(host=server, port=port)
