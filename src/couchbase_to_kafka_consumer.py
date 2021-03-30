from confluent_kafka import Consumer, KafkaError

from couchbase.cluster import Cluster
from couchbase.cluster import ClusterOptions
from couchbase.cluster import PasswordAuthenticator


def couchbase_connect():
    endpoint = "couchbase://localhost"
    username = "admin"
    password = "password"
    bucket_name = "kafka"

    try:
        cluster = Cluster.connect(
            endpoint, ClusterOptions(PasswordAuthenticator(username, password))
        )
        bucket = cluster.bucket(bucket_name)
        collection = bucket.default_collection()

    # catch *all* exceptions:
    except Exception as e:
        print(e)

    return collection


def run_consumer():
    settings = {
        "bootstrap.servers": "localhost:9092",
        "group.id": "mygroup",
        "client.id": "client-1",
        "enable.auto.commit": True,
        "session.timeout.ms": 6000,
        "default.topic.config": {"auto.offset.reset": "smallest"},
    }
    c = Consumer(settings)
    c.subscribe(["rj_topic"])

    try:

        while True:
            msg = c.poll(0.1)
            if msg is None:
                continue
            elif not msg.error():
                print(str(msg.value()).lstrip("b'").rstrip("'"))

            elif msg.error().code() == KafkaError._PARTITION_EOF:
                print(
                    "End of partition reached {0}/{1}".format(
                        msg.topic(), msg.partition()
                    )
                )
            else:
                print("Error occured: {0}".format(msg.error().str()))

    except KeyboardInterrupt:
        pass

    finally:
        c.close()


run_consumer()
