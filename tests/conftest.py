import functools

import bddrest
import pytest

import yhttp_ssr_boilerplate


pytest_plugins = ['yhttp.dev.fixtures']


@pytest.fixture
def app(freshdb, tmp_path):
    yhttp_ssr_boilerplate.app.settings |= f'''
db:
  url: {freshdb}
mako:
  modules: {tmp_path / 'mako'}
media:
  directory: {tmp_path / 'media'}
'''
    yhttp_ssr_boilerplate.app.ready()
    yhttp_ssr_boilerplate.app.db.create_objects()
    yield yhttp_ssr_boilerplate.app
    yhttp_ssr_boilerplate.app.shutdown()


@pytest.fixture
def httpreq(app):
    return functools.partial(bddrest.Given, app)
