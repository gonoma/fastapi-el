# How to use alembic

Essential Alembic:
* Run an upgrade --> `alembic upgrade head`
* Run a downgrade --> `alembic downgrade -1`
* Create revision --> `alembic revision --autogenerate -m "revision comment"`
* Check revisions history --> `alembic history`
* Check current branch --> `alembic current`

Dry run command --> `alembic -x dry-run upgrade head`