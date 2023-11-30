from collections import Counter
from service.read_log_file import LogFile


def top_10_hosts():
    hosts = LogFile.extract_hosts()

    # Count the occurrences of each host
    host_counts = Counter(hosts)

    # Get the top 10 hosts with the most requests
    top_10_hosts = host_counts.most_common(10)

    # Create a dictionary for the JSON response
    result = {'top_10_hosts': [{'host': host, 'count': count} for host, count in top_10_hosts]}

    return result
