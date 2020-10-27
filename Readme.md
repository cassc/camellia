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

To run in docker mode after building:

``` bash
cd target ; docker-compose up -d
```
