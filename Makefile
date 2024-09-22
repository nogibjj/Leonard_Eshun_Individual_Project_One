install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	# pylint --disable=R,C --ignore-patterns=test_.*?py *.py
	ruff check *.py mylib/*.py test_*.py *.ipynb

test:
	python -m pytest -vv --nbval -cov=mylib -cov=main test_*.py *.ipynb

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

generate_and_push:
	# Create the markdown file
	python script.py

	# Add, commit, and push the generated files to GitHub
	git config --local user.email "action@github.com"; \
	git config --local user.name "GitHub Action"; \
	git add .; \
	git commit -m "Add generated plots and markdown"; \
	git push; \


all: install format lint test container-lint refactor generate_and_push