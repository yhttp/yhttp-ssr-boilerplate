# YHTTP SSR Boilerplate

A minimal server-side-rendered application built with YHTTP, Mako, and its
database, media, and authentication extensions.

## Development

Use `make venv` to create a python virtual environment.

Create the Python environment and install project dependencies with `make env`.
Start the YHTTP server and Vite together with `make run`. Build frontend assets
with `make www-dist`, and run the Python coverage suite with `make cover`.

The application composition root is `yhttp_ssr_boilerplate/rollup.py`. Add
routes in `pages.py` (or a feature module imported from `routes.py`) and render
Mako templates from `yhttp_ssr_boilerplate/templates/`.
