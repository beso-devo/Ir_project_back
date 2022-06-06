from flask import Flask, request, jsonify
import IR_Project.utils.document.parser_ci as ci_document
import IR_Project.utils.document.parser_ci as ci_query

import IR_Project.utils.document.parser_cacm as ca_cm_document

from IR_Project.API.features import features
from IR_Project.API.core import core

import IR_Project.API.variables.lists as lists

main_app = Flask(__name__)
main_app.register_blueprint(features.app)
main_app.register_blueprint(core.app)


@main_app.route('/')
def index():
    return "Welcome to our first API"


if __name__ == "__main__":
    # lists.documents_ci = ci_document.parse_ci_all()
    # lists.documents_ca_cm = ca_cm_document.parse_ca_cm_all()
    # lists.queries_ci = ci_query.parse_ci_all()
    main_app.run(debug=True, host='192.168.1.7')
