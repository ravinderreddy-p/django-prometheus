from prometheus_api_client import PrometheusConnect
# import psycopg2
import json

# Connect to Prometheus
prom = PrometheusConnect(url="http://localhost:9090", disable_ssl=True)

# Query the desired metrics and filter the data using PromQL
memory_data = prom.custom_query(query='process_resident_memory_bytes{'
                                      'instance="docker.for.mac.localhost:8000", '
                                      'job="monitoring"}')

cpu_data = prom.custom_query(query='avg by (endpoint) (process_cpu_seconds_total{'
                                   'instance="docker.for.mac.localhost:8000", '
                                   'job="monitoring"})')

cpu_max_over_data = prom.custom_query(query='max_over_time(process_cpu_seconds_total{job="monitoring"}'
                                            '[1686219773s:1686228360s]) - '
                                            'process_cpu_seconds_total{job="monitoring"}@1686219773s')

memory_usage = prom.custom_query(query='max_over_time(process_resident_memory_bytes{job="monitoring"}'
                                       '[1686231098s:1686231143s]) - '
                                       'process_resident_memory_bytes{job="monitoring"}@1686231098')

print(cpu_max_over_data)
print(memory_usage)
print("collected metrics")
print("memory data: ", memory_data)
print("CPU data: ", cpu_data)

# Connect to PostgreSQL
# conn = psycopg2.connect(
#     host="localhost",
#     database="mydatabase",
#     user="myuser",
#     password="mypassword"
# )
# cur = conn.cursor()

# Insert the data into the database
for row in memory_data:
    # endpoint = row["metric"]["endpoint"]
    response_time = row["value"][1]
    timestamp = row["value"][0]
    print(response_time, timestamp)
    # cur.execute("INSERT INTO response_times (endpoint, response_time, timestamp) VALUES (%s, %s, %s)",
    #             (endpoint, response_time, timestamp))

# Commit the changes and close the connection
# conn.commit()
# cur.close()
# conn.close()
