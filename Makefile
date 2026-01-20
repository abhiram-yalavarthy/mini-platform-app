.PHONY: test run docker-build

test:
	pytest -q

run:
	uvicorn api.src.main:app --host 0.0.0.0 --port 8080 --reload

docker-build:
	docker build -t mini-platform-api:local .
