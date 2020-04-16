spark-submit \
 --class com.example.HelloSpark \
  --deploy-mode client \
  --executor-memory 4G \
  --total-executor-cores 6 \
  --master spark://localhost:7077 \
  ../jars/job.jar
  

