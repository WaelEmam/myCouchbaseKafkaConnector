#!/usr/bin/env bash


readonly LOG_FILE="/Users/Downloads/script.log"


#
## create log file or overrite if already present
printf "Log File Date and Time - " > $LOG_FILE
#
## append date to log file
date >> $LOG_FILE

echo "You are running $0 the results are below" >> $LOG_FILE

cd /Users/Couchbase/kafka/confluent-5.5.1/

./bin/zookeeper-server-start ./etc/kafka/zookeeper.properties
