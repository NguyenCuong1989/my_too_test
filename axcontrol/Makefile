# AXCONTROL Local CI Makefile

.PHONY: test ci lint clean install-hooks

test:
	AXCONTROL_SIM=1 python3 -m unittest discover -s tests -v

ci: test
	@echo "All no-drift invariants passed."

lint:
	python3 -m flake8 core/ tests/ --count --select=E9,F63,F7,F82 --show-source --statistics --exclude=core/canon/,core/The/state_projector.py,core/Menh/stop_reasons.py
	python3 -m black --check core/ tests/ --exclude "(core/canon/|core/The/state_projector.py|core/Menh/stop_reasons.py)"

clean:
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete

install-hooks:
	python3 -m pip install --user --break-system-packages pre-commit flake8 black
	python3 -m pre_commit install
