dev:
	@echo "Starting Flask dev server..."
	@FLASK_APP=server.py FLASK_ENV=developement flask run

.PHONY: dev