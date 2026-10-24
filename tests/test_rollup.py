from types import SimpleNamespace

from yhttp_ssr_boilerplate.rollup import app as application


ready = next(
    callback
    for callback in application.events['ready']
    if callback.__module__ == 'yhttp_ssr_boilerplate.rollup'
)


def test_ready_registers_production_directories():
    registered = []
    app = SimpleNamespace(
        settings=SimpleNamespace(
            env='production',
            assets=SimpleNamespace(
                serve=True,
                url='/assets',
                directory='/srv/assets',
            ),
            media=SimpleNamespace(
                serve=True,
                url='/media',
                directory='/srv/media',
            ),
            public=SimpleNamespace(
                serve=True,
                url='/',
                directory='/srv/public',
            ),
        ),
        staticdirectory=lambda *args, **kwargs: registered.append(
            (args, kwargs),
        ),
    )

    ready(app)

    assert [item[0][0] for item in registered] == [
        '/assets',
        '/media',
        '/',
    ]


def test_ready_skips_disabled_directories():
    registered = []
    app = SimpleNamespace(
        settings=SimpleNamespace(
            env='production',
            assets=SimpleNamespace(serve=False, url='/assets'),
            media=SimpleNamespace(serve=False, url='/media'),
            public=SimpleNamespace(serve=False, url='/'),
        ),
        staticdirectory=lambda *args, **kwargs: registered.append(args),
    )

    ready(app)

    assert registered == []
