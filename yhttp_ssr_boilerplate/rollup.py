import os

from yhttp.core import Application
from yhttp.ext import auth, dbmanager, mako, media, sqlalchemy as saext

from . import assets
from .common.models import BaseModel
from .manifest import __appname__, __version__


env = os.environ.get('YHTTP_ENV', 'development')
pkgdir = os.path.dirname(__file__)
prjdir = os.path.abspath(os.path.join(pkgdir, '..'))
vardir = os.path.join(prjdir, '.var')
os.makedirs(vardir, exist_ok=True)

app = Application(__version__, __appname__)
media.install(app)
dbmanager.install(app)
saext.install(app, basemodel=BaseModel)
mako.install(app, data={
    'settings': app.settings,
    'asseturl': assets.urlresolver(app),
})
auth.install(app)

app.settings |= f'''
debug: true
env: {env}
publicurl: http://127.0.0.1:8080

assets:
  serve: true
  manifest: {vardir}/static/.vite/manifest.json
  directory: {vardir}/static/assets
  url: /assets

public:
  serve: true
  directory: {prjdir}/public
  url: /

media:
  serve: true
  directory: {vardir}/media
  url: /media

db:
  url: postgresql://:@/{app.name}
  migration:
    directory: {pkgdir}/dbmigration

mako:
  modules: {vardir}/mako
  lookup:
    - {pkgdir}/templates
'''


@app.when
def ready(app):
    if app.settings.env == 'development':
        app.settings.assets.serve = False
        app.settings.assets.url = 'http://localhost:5173'
    elif app.settings.assets.serve:
        app.staticdirectory(
            app.settings.assets.url,
            app.settings.assets.directory,
            autoindex=False,
            exists='remove',
        )

    if app.settings.media.serve:
        app.staticdirectory(
            app.settings.media.url,
            app.settings.media.directory,
            autoindex=False,
            exists='remove',
        )

    if app.settings.public.serve:
        app.staticdirectory(
            app.settings.public.url,
            app.settings.public.directory,
            exists='remove',
        )


from . import routes  # noqa: E402,F401
