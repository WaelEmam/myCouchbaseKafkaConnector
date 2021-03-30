
import snowflake.connector
from couchbase.cluster import Cluster
from couchbase.cluster import ClusterOptions
from couchbase.cluster import PasswordAuthenticator

from confluent_kafka import Producer


def couchbase_connect_local():
    endpoint = "couchbase://localhost"
    username = "admin"
    password = "password"
    bucket_name = "snowflake"

    try:
        cluster = Cluster.connect(
            endpoint, ClusterOptions(PasswordAuthenticator(username, password))
        )
        bucket = cluster.bucket(bucket_name)
        collection = bucket.default_collection()

    # catch *all* exceptions:
    except Exception as e:
        print(e)

    return cluster


def get_couchbase_data(query):
    endpoint = "couchbase://localhost"
    username = "<username>"
    password = "<password>"
    bucket_name = "kafka"

    try:
        cluster = couchbase_connect_local()
        bucket = cluster.bucket(bucket_name)
        collection = bucket.default_collection()

        results = cluster.analytics_query(query)

        dict_messages = {}

        for value in results:
            id = value["kafka"]["record_id"]
            msg = value["kafka"]["message"]

            dict_messages[id] = msg

        run_producer(dict_messages)

    # catch *all* exceptions:
    except Exception as e:
        print(e)

    return results


def run_producer(dict_messages):
    p = Producer({"bootstrap.servers": "localhost:9092"})

    msg_number = 1
    try:
        for item in dict_messages.values():
            print(item)

            p.produce("rj_topic", key="hello" + str(msg_number), value=item)
            p.flush(30)

    except KeyboardInterrupt:
        pass

    p.flush(30)


def run_migration():

    query = r"SELECT * FROM kafka;"
    get_couchbase_data(query)


run_migration()
