run:
	@PYTHONPATH=$PYTHONPATH$:$(pwd) -m uvicorn workout_api.main:app --reload

create-migrations:
	@PYTHONPATH=$PYTHONPATH$:$(pwd) -m alembic revision --autogenerate -m $(d)

run-migrations:
	@PYTHONPATH=$PYTHONPATH$:$(pwd) alembic upgrade head