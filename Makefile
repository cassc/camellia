clean:
	rm -rf output
	rm -rf target 
build: clean
	python3 gen-site.py -c
	docker build -t camellia .
deploy:
	docker push camellia
