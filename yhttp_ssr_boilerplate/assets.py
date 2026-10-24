import functools
import json
import os


def urlresolver(app):
    @functools.cache
    def resolve(url):
        settings = app.settings.assets
        root = settings.url
        if app.settings.env == 'development':
            return f'{root}/{url}'

        with open(settings.manifest, encoding='utf-8') as manifest_file:
            manifest = json.load(manifest_file)

        mapping = manifest.get(url)
        if not mapping:
            return url

        filename = os.path.basename(mapping['file'])
        return f'{root}/{filename}'

    return resolve
