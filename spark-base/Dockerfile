FROM openjdk:15-alpine

ENV SPARK_VERSION 2.4.5
ENV HADOOP_VERSION 2.7
ENV SCALA_VERSION 2.13.1
ENV SBT_VERSION 1.2.1

ENV SCALA_URL "http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz"
ENV SBT_URL "https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz"
ENV SPARK_URL "http://apache.mirrors.ionfish.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz"

# http://blog.stuart.axelbrooke.com/python-3-on-spark-return-of-the-pythonhashseed
ENV PYTHONHASHSEED 0
ENV PYTHONIOENCODING UTF-8

## Python/Scala
ENV SPARK_HADOOP "spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION"
ENV SPARK_HOME "/usr/local/$SPARK_HADOOP"

## Python and Scala
RUN apk add --no-cache build-base curl bash python3-dev tar gzip \
    && python3 -m ensurepip --upgrade \
    && rm -r /usr/lib/python*/ensurepip \
    && pip3 install --upgrade pip setuptools \
    && if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi \
    && if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi \
    && curl -fsL $SCALA_URL | tar xfz - -C /usr/local \
    && ln -s /usr/local/scala-$SCALA_VERSION/bin/* /usr/local/bin/

## SBT
RUN curl -fsL $SBT_URL | tar xfz - -C /usr/local  \
    && $(mv /usr/local/sbt-launcher-packaging-$SBT_VERSION /usr/local/sbt || true) \
    && ln -s /usr/local/sbt/bin/* /usr/local/bin/

## Spark
RUN mkdir $SPARK_HOME \
    && curl -fsL $SPARK_URL | tar xfz - --strip-components=1 -C $SPARK_HOME \
    && ln -s $SPARK_HOME/bin/* /usr/local/bin/ \
    && ln -s $SPARK_HADOOP/sbin/* /usr/local/bin/
