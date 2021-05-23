from flask import Flask, render_template, make_response
from flask.views import MethodView

import logging
import apitest.conf as conf

logger = logging.getLogger(__name__)


app = Flask(f"apitest.core")


class Info(MethodView):
    """
    Handler class for the main information (root) endpoint.
    """

    @classmethod
    def get(cls):
        template_args = {
            "info": conf.Info,
        }
        response = make_response(render_template('info.html', **template_args), 200)
        return response


logger.info("Bringing up apitest !")

app.add_url_rule('/health', view_func=Info.as_view("healthinfo"))

logger.info("All request handlers initialized.")
