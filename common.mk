# Common Make variables and targets

RUN_CSV=DATA=data/staff.csv flask --app
RUN_LAB=DATA=data/lab.db flask --app
RUN_MIGRATE=python bin/migrate.py
RUN_TEMP=DATA=temp.db flask --app

## ---: ---

## commands: show available commands (*)
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} \
	| sed -e 's/## //g' \
	| column -t -s ':'

## clean: clean up
clean:
	@find . -type f -name '*~' -exec rm {} \;
	@find . -type d -name __pycache__ | xargs rm -r
	@find . -type d -name .pytest_cache | xargs rm -r
	@find . -type d -name .ruff_cache | xargs rm -r
