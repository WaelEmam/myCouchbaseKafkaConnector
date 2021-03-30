import json
from datetime import datetime
from confluent_kafka import Producer

from json import dumps


def run_producer():
    p = Producer({"bootstrap.servers": "localhost:9092"})

    json_dict_doc = {"type": "kafka_record"}

    try:
        for val in range(1, 22):
            now = str(datetime.now())
            msg = f"This is message number {val} from kafka created at {now}"

            print(msg)

            p.produce("rj_topic", key="hello" + str(val), value=msg)
            p.flush(30)

    except KeyboardInterrupt:
        pass

    p.flush(30)


run_producer()
