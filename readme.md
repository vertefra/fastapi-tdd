## TDD with FastAPI and docker

- Spin up all the containers:

`docker-compose up -d --build`

option -d "detatched".

- Check containers status

`docker-compose ps`

### Tests

- run tests

`docker-compose exec web python -m pytest`

- run specific test

`docker-compose exec web python -m pytest -k <test_name>`

- disable pytest warnings

`docker-compose exec web python -m pytest -p no:warnings`
