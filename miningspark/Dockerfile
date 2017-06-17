FROM openjdk:8

MAINTAINER Kaniu Ndungu

#RUN java -version

#RUN git version

RUN uname -a

WORKDIR /maven

RUN apt-get -y update && apt-get -y install maven

WORKDIR /

RUN git clone -b develop https://github.com/kaniutest/streammining.git

WORKDIR streammining

RUN mvn clean install

RUN echo $PATH
ENV $PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Define default command.
ENTRYPOINT ["java", "-cp", "/streammining/target/spark-kafka-streamer.jar", "io.kaniu.spark.MainAllJobRunner","SENTIMENT_PROC","tweet-topic"]
