PKG_NAME = yhttp-ssr-boilerplate
PYTEST_FLAGS = -vv
PYDEPS_COMMON = \
	'coveralls >= 4.1.0' \
	'bddrest >= 6.3.3, < 7' \
	'pytest >= 7.4.4, < 8' \
	'pytest-fixkit >= 2.0.2' \
	'yhttp-dev >= 4.0.2' \
	'time_machine'

PYTHON_MAKELIB_VERSION_REQUIRED = 4.5
PYTHON_MAKELIB_PATH = /usr/local/lib/python-makelib

ifeq (,$(wildcard $(PYTHON_MAKELIB_PATH)))
  $(error python-makelib is not installed. see https://github.com/pylover/python-makelib)
endif

include $(PYTHON_MAKELIB_PATH)/venv-lint-test-webapi.mk

NPM = pnpm
ENV_DEPS += www-env

.PHONY: www-env
www-env:
	$(NPM) install

.PHONY: www-dist
www-dist:
	$(NPM) run build

.PHONY: www-lint
www-lint:
	$(NPM) run lint

.PHONY: www-format
www-format:
	$(NPM) run format

.PHONY: format
format: www-format

.PHONY: run-backend
run-backend:
	$(PREFIX)/bin/$(PKG_NAME) serve

.PHONY: run
run:
	$(PREFIX)/bin/$(PKG_NAME) -Odebug=True serve \
		--watch-directories 'yhttp_ssr_boilerplate/**' \
		--watch-excludedirectory 'yhttp_ssr_boilerplate/templates/*' \
		--watch-excludefile '*.md' \
		--subprocess "$(NPM) run dev"
