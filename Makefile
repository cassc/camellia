clean:
	rm -rf output
	rm -rf target 
build: clean
	python3 gen-site.py -c
deploy:
	docker push camellia
