from .rollup import app


@app.route(r'/')
@app.bodyguard(strict=True)
@app.queryguard(strict=True)
@app.template('index.mako')
def get(req):
    return {}
