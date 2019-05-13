NODE_SASS=./node_modules/.bin/node-sass

compile:
	$(NODE_SASS) ./createcsv/static/createcsv/govuk-frontend/all.scss ./createcsv/static/createcsv/style.css