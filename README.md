# myCouchbaseKafkaConnector

This is a sample project to demonstrate loading messgages from a Kafka topic into Couchbase.
And getting data from Couchbase to a topic so it can be consumed by Kafka.


## Instructions
* Run 01bash_start_zookeeper.sh - edited to match your Zookeeper installation.
* Run 02bash_start_kafka.sh - edited to match your Confluent Kafka installation.

### Insert messages into Couchbase
  * Run kafka_producer to create Kafka messages.
  * Run kafka_consumer to capture messages and load them into Couchbase.

### Get data from Couchbase and load to Kafka topic
  * Run couchbase_to_kafka_get_data to get json from Couchbase.
  * Run couchbase_to_kafka_consumer to put data on a Kafka topic.
