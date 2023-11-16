from services.kafka import kafka_consumer
from services.db_postgres import create_table


if __name__ == "__main__":
    create_table()
    kafka_consumer()