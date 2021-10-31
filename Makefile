deploy:
	sam deploy -g
update:
	sam deploy
build:
	sam build
test:
	python -m pytest tests/unit -v -s