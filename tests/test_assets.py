import json
from types import SimpleNamespace

from yhttp_ssr_boilerplate.assets import urlresolver


def test_asset_url_in_development():
    app = SimpleNamespace(
        settings=SimpleNamespace(
            env='development',
            assets=SimpleNamespace(url='http://localhost:5173'),
        ),
    )

    assert urlresolver(app)('www/master.js') == \
        'http://localhost:5173/www/master.js'


def test_asset_url_from_production_manifest(tmp_path):
    manifest = tmp_path / 'manifest.json'
    manifest.write_text(
        json.dumps({'www/master.js': {'file': 'assets/master-abc.js'}}),
        encoding='utf-8',
    )
    app = SimpleNamespace(
        settings=SimpleNamespace(
            env='production',
            assets=SimpleNamespace(url='/assets', manifest=manifest),
        ),
    )

    resolver = urlresolver(app)
    assert resolver('www/master.js') == '/assets/master-abc.js'
    assert resolver('www/other.js') == 'www/other.js'
