# A company webstie with Go

To build, first edit company information in `gen-site.py`, then run

``` bash
make build
```

To run/test the target build

``` bash
cd target/be 
./main
```

To run in dev mode:

``` bash
cd be 
make dev
```

To run in docker mode:

``` bash
docker run -d -p 8080:3122 -v camellia:/opt/camellia camellia
docker run -p 8080:3122 \
-v $(pwd)/be/feedback.db:/opt/camellia/be/feedback.db \
-v $(pwd)/be/news.db:/opt/camellia/be/news.db \
-v $(pwd)/be/product.db:/opt/camellia/be/product.db \
-v $(pwd)/be/solution.db:/opt/camellia/be/solution.db \
-v $(pwd)/be/news/:/opt/camellia/be/news/ \
-v $(pwd)/be/templates/:/opt/camellia/be/templates/ \
camellia
```
