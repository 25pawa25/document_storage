# Wake up docker containers
up:
	docker-compose -f docker-compose.yml up -d

# Shut down docker containers
down:
	docker-compose -f docker-compose.yml down

# Show a status of each container
status:
	docker-compose -f docker-compose.yml ps

test:
	docker-compose -f docker-compose.yml exec -e DEBUG=True cve_extract_api sh -c "cd .. && pytest -vv -s tests/test_GRPCAsyncServer.py"

# Status alias
s: status

# Show logs of each container
logs:
	docker-compose -f docker-compose.yml logs

# Restart all containers
restart: down up

# Build and up docker containers
build:
	docker-compose -f docker-compose.yml build --force-rm

# Build and up docker containers
rebuild: down build

connect:
	 docker exec -it vpn-manager bash

grant-permissions:
	docker-compose -f docker-compose.yml exec -T -u root vpn-manager-postgres chown postgres:postgres /var/lib/postgresql/data

check-linters:
	@echo "Start checking isort..."
	docker run -it --volume=./:/src --platform=linux/amd64 --rm registry.mathun.team/matrix-hunter/dev/linters/python-lints/all-lints:latest isort --settings-file=/pyproject.toml /src
	@echo "Stop checking isort..."

	@echo "Start checking black..."
	docker run -it --volume=./src:/src --platform=linux/amd64 --rm registry.mathun.team/matrix-hunter/dev/linters/python-lints/all-lints:latest black --config=/pyproject.toml /src
	@echo "Stop checking black..."

	@echo "Start checking flake8..."
	docker run -it --volume=./src:/src --platform=linux/amd64 --rm registry.mathun.team/matrix-hunter/dev/linters/python-lints/all-lints:latest flake8 --config=/.flake8 /src
	@echo "Stop checking flake8..."

proto:
	python -m grpc_tools.protoc -I=protobuf/ --python_out=src/proto --grpc_python_out=src/proto protobuf/*.proto
	cd src/proto && sed -i '' 's/^\(import.*pb2\)/from . \1/g' *.py