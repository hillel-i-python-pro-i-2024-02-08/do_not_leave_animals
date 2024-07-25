# Get user id for macOS and Linux
ifeq ($(shell uname),Darwin)
	UID := $(shell id -u)
else
	UID := $(shell id --user)
endif

.PHONY: echo-i-uid
# Echo user id
echo-i-uid:
	@echo ${UID}


# [docker]-[BEGIN]
.PHONY: d-homework-i-run
# Just run
d-homework-i-run:
	@export UID=${UID} &&\
	COMPOSE_PROFILES=full_dev \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose up \
			--build


.PHONY: d-homework-i-local-dev
# Run services for local development
d-homework-i-local-dev:
	@export UID=${UID} &&\
	COMPOSE_PROFILES=local_dev \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose up \
			--build


.PHONY: make d-homework-i-purge
# Purge all data related with services
make d-homework-i-purge:
	@export UID=${UID} &&\
	COMPOSE_PROFILES=full_dev \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down --volumes --remove-orphans --rmi local --timeout 0
# [docker]-[END]


.PHONY: init-dev
# Init environment for development
init-dev:
	@make poetry-install && \
	make pre-commit-install


# [migrations]-[BEGIN]
.PHONY: migrations
# Make migrations
migrations:
	@python manage.py makemigrations

.PHONY: migrate
# Migrate
migrate:
	@python manage.py migrate


.PHONY: make-migrations
make-migrations:
	@python manage.py makemigrations &&\
	python manage.py migrate
# [migrations]-[END]


# [pre-commit]-[BEGIN]
.PHONY: pre-commit-install
# Install pre-commit.
pre-commit-install:
	@pre-commit install


.PHONY: hooks
# Run tools for all files.
hooks:
	@pre-commit run --all-files


.PHONY: pre-commit-autoupdate
# Update "rev" version of all pre-commit hooks.
pre-commit-autoupdate:
	@pre-commit autoupdate
# [pre-commit]-[END]


# [poetry]-[BEGIN]
.PHONY: poetry-up-latest
# Update all packages to the latest version allowed by the current constraints.
poetry-up-latest:
	@poetry up --latest


.PHONY: poetry-up-pinned-latest-no-install
# Update all packages to the latest version allowed by the current constraints.
poetry-up-pinned-latest-no-install:
	@poetry up --pinned --latest --no-install


.PHONY: poetry-lock
# Lock the current dependencies.
poetry-lock:
	@poetry lock


.PHONY: poetry-install
# Install the current dependencies.
poetry-install:
	@poetry install --no-root --sync


.PHONY: poetry-self-show-plugins
# Show plugins for poetry.
poetry-self-show-plugins:
	@poetry self show --plugins


.PHONY: poetry-export-requirements
# Export the current dependencies to requirements.txt.
poetry-export-requirements:
	@poetry export --format requirements.txt --output requirements.txt --without-hashes
# [poetry]-[END]


# [extra_python]-[BEGIN]
.PHONY: install-pipx
# Install pipx.
# Note: Reloading shell is needed after this action.
install-pipx:
	@python3.12 -m ensurepip &&\
	python3.12 -m pip install --upgrade pip &&\
	python3.12 -m pip install --user pipx &&\
	python3.12 -m pipx ensurepath


.PHONY: install-poetry
# Install poetry.
# Note: Reloading shell is needed after this action.
install-poetry:
	@pipx install poetry &&\
	pipx upgrade poetry &&\
	poetry self add poetry-plugin-export ;\
	poetry self add poetry-plugin-up


.PHONY: install-pre-commit
# Install pre-commit.
install-pre-commit:
	@pipx install pre-commit &&\
	pipx upgrade pre-commit


# [extra_python]-[END]
