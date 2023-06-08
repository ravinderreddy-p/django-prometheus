import datetime

from prometheus_api_client import PrometheusConnect

host = "http://localhost:9090"

prom = PrometheusConnect(url=host, disable_ssl=True)

start_time = '1686219773'
end_time = '1686228360'


cpu_usage = prom.custom_query(query='max_over_time(process_cpu_seconds_total{job="monitoring"}'
                                    f'[{start_time}s:{end_time}s]) - '
                                    f'process_cpu_seconds_total{{job="monitoring"}}@{start_time}')

memory_usage = prom.custom_query(query='max_over_time(process_resident_memory_bytes{job="monitoring"}'
                                       f'[{start_time}s:{end_time}s]) - '
                                       f'process_resident_memory_bytes{{job="monitoring"}}@{start_time}')


print(cpu_usage[0]["value"][1])
print(memory_usage[0]["value"][1])

