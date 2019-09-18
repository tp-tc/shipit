# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import jinja2


def init_app(app):
    app.jinja_loader = jinja2.loaders.FileSystemLoader(app.config["APP_TEMPLATES_FOLDER"])


def app_heartbeat():
    pass
