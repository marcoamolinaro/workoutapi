run:
	@python -m uvicorn workout_api.main:app --reload

create-migrations:
	@python -m alembic revision --autogenerate -m $(d)

run-migrations:
	@PYTHONPATH=$PYTHONPATH$:$(pwd) alembic upgrade head