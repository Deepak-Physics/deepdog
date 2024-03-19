
# execute default build
default: build

# builds the python module using poetry
build:
	echo "building..."
	poetry build

# print a message displaying whether nix is being used
checknix:
	#!/usr/bin/env bash
	set -euxo pipefail
	if [[ "${DO_NIX_CUSTOM:=0}" -eq 1 ]]; then
		echo "In an interactive nix env."
	else
		echo "Using poetry as runner, no nix detected."
	fi

test:
	#!/usr/bin/env bash
	set -euxo pipefail
	
	if [[ "${DO_NIX_CUSTOM:=0}" -eq 1 ]]; then
		echo "testing, using nix..."
		flake8 deepdog tests
		mypy deepdog
		pytest
	else
		echo "testing..."
		poetry run flake8 deepdog tests
		poetry run mypy deepdog
		poetry run pytest
	fi

fmt:
	#!/usr/bin/env bash
	set -euxo pipefail
	if [[ "${DO_NIX_CUSTOM:=0}" -eq 1 ]]; then
	      black .
	else
		poetry run black .
	fi
	find . -type f -name "*.py" -exec sed -i -e 's/    /\t/g' {} \;

release:
	./scripts/release.sh

htmlcov:
	poetry run pytest --cov-report=html
