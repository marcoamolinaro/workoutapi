run:
	python -m uvicorn workout_api.main:app --reload

create-migrations:
	python -m alembic revision --autogenerate -m 'init_db'

run-migrations:
	python alembic upgrade head