#https://makefiletutorial.com/

.PHONY: info
info:
	echo "\nList of Makefile commands:\n" && echo "  readme" && echo "  run"  && echo "  setup" && echo "  packages"  && echo "  github"   && echo "  push" 
info-info:
	echo "\noutput the list of commands for this Makefile\n"

.PHONY: readme
readme:
	echo "commit Readme file"
	git commit -am 'readme'
	echo "publish it on github on Master branch"
	git push -u origin master
info-readme:
	echo "\nCommit the Readme file and push this repository on Github\n"

.PHONY: runserver
runserver:
	echo "run python3 server"
	poetry run python -m http.server
info-runserver:
	echo "\nRun a python server\n"
	
.PHONY: remove
remove:
	echo "removing the ODESI container"
	docker stop odesi.docker.test
	docker container rm odesi.docker.test
info-remove:
	echo "\nremoving the ODESI container\n"

.PHONY: up
up:
	echo "start the ODESI Docker container"
	bash start.sh
info-up:
	echo "\nStart the ODESI Docker container\n"

.PHONY: logs
logs:
	echo "Show logs of the ODESI Docker container"
	docker logs odesi.docker.test
info-logs:
	echo "\nShow logs of the ODESI Docker container\n"

.PHONY: setup
setup:
	pip install poetry
	poetry install -v
	poetry run python sp_ask_service_availability_alert.py
info-setup:
	echo "\nRun this python app\n"

.PHONY: pytest
pytest:
	poetry run pytest -v
info-pytest:
	echo "\nRunning Tests\n"


.PHONY: run
run:
	poetry run python sp_ask_service_availability_alert.py
info-run:
	echo "\nRun this python app\n"

.PHONY: packages
packages:
	poetry install -v
info-packages:
	echo "\nInstall packages\n"

.PHONY: github
github:
	echo "--On Mac Open this github repository url--"
	open https://github.com/guinslym/sp_odesi_report_top_10_downloads
info-github:
	echo "\nOpen this github repository url \n"

.PHONY: push
push:
	git push -u origin master
info-push:
	echo "\nGit Pushed to master branch repository\n"

.PHONY: dumpfile
dumpfile:
	echo "--Dumping all table from ODESI--"
	mysqldump -uroot -p sp_odesi_practice --single-transaction --no-create-info --no-create-db  > /root/sp_odesi/odesi_all.sql
	echo "--Dumping only this table OdesiDailyAccess for 2019 and up --"
	mysqldump -uroot -p sp_odesi_practice --single-transaction --no-create-info --no-create-db  --where "OdesiDailyAccess.date_id > 3213 " OdesiDailyAccess > /root/sp_odesi/odesi.sql
	echo "--\n\n\nYou will need to replace OdesiDailyAccess on odesi_all.sql with the one in odesi.sql --"
	echo "--\n\n\n61 dd on odesi_all.sql for OdesiDailyAccess --"
info-dumpfile:
	echo "\nDumping all table from ODESI\n"

.PHONY: dumpschema
dumpschema:
	echo "--Dumping schema of all table from ODESI--"
	mysqldump -uroot -p sp_odesi_practice --no-data  > /root/sp_odesi/odesi_schema.sql
info-dumpschema:
	echo "\nDumping schema of all table from ODESI\n"

.PHONY: dump-schema-and-data
dump-schema-and-data:
	echo "--Dumping schema of all table from ODESI--"
	mysqldump -uroot -p sp_odesi_practice --no-data  > /root/sp_odesi/odesi_schema.sql
	echo "--\n\nDumping all table from ODESI--"
	mysqldump -uroot -p sp_odesi_practice --single-transaction --no-create-info --no-create-db  > /root/sp_odesi/odesi_all.sql
	echo "--Dumping only this table OdesiDailyAccess for 2019 and up --"
	mysqldump -uroot -p sp_odesi_practice --single-transaction --no-create-info --no-create-db  --where "OdesiDailyAccess.date_id > 3213 " OdesiDailyAccess > /root/sp_odesi/odesi.sql
	echo "--\n\n\nYou will need to replace OdesiDailyAccess on odesi_all.sql with the one in odesi.sql --"
	echo "--\n\n\n61 dd on odesi_all.sql for OdesiDailyAccess --"
	echo "--\n\n\nload-data-and-schema --"
info-dump-schema-and-data:
	echo "\nDumping schema of all table from ODESI\n"

.PHONY: loadschema
loadschema:
	echo "--Loading schema of all table from ODESI--"
	mysql -u root -p sp_odesi < odesi_schema.sql
info-loadschema:
	echo "\nLoading schema of all table from ODESI\n"

.PHONY: loaddata
loaddata:
	echo "--Loading schema of all table from ODESI--"
	mysql -u root -p sp_odesi < odesi_all.sql
info-loaddata:
	echo "\nLoading schema of all table from ODESI\n"

.PHONY: load-data-and-schema
load-data-and-schema:
	echo "--Loading schema data for all table from ODESI--"
	cat odesi.sql >> odesi_all.sql
	mysql -u root -p sp_odesi < odesi_schema.sql
	mysql -u root -p sp_odesi < odesi_all.sql
info-load-data-and-schema:
	echo "\nLoading schema data for all table from ODESI\n"

.PHONY: docker-remove-container
docker-remove-container:
	echo "\ndocker rm -vf $(docker ps -a -q)"
	docker rm -vf $(docker ps -a -q)
info-docker-remove-container:
	echo "\nRemove all containers\n"

.PHONY: docker-remove-images
docker-remove-images:
	echo "\ndocker rmi -f $(docker images -a -q)\n"
	docker rmi -f $(docker images -a -q)
info-docker-remove-images:
	echo "\nRemove all images\n"


.PHONY: coverage
coverage:
	echo "\ncoverage \n"
	pytest --cov=. tests/
info-coverage:
	echo "\ncoverage\n"