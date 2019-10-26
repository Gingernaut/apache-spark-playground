### Spark Playground

This is an easy-to-run standalone spark cluster attached to a Jupyter notebook instance. Just run `./build-spark.sh` to build the images, then run `docker-compose up` and navigate to `localhost:8080`(Spark UI) and `localhost:8888` (Jupyter Notebook). You may need to configure the worker resources in `docker-compose.yml` to less than your machine.
