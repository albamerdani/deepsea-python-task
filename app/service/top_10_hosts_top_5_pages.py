from collections import Counter
from service.read_log_file import LogFile


def top_10_hosts_detailed():
    hosts = LogFile.extract_hosts()

    # Count the occurrences of each host
    host_counts = Counter(hosts)

    # Get the top 10 hosts with the most requests
    top_10_hosts = host_counts.most_common(10)

    # Create a dictionary for the detailed JSON response
    detailed_result = {}
    log_data = LogFile.read_log_file()

    for host, count in top_10_hosts:
        # Filter log entries for the current host
        host_entries = [line for line in log_data if host in line]

        # Extract paths requested by the current host
        paths = LogFile.extract_paths(host_entries)

        # Count the occurrences of each path
        path_counts = Counter(paths)

        # Get the top 5 paths requested by the current host
        top_5_paths = path_counts.most_common(5)

        # Create a dictionary for the current host's detailed information
        host_info = {'host': host, 'count': count, 'top5_paths': [{'path': path, 'count': path_count}
                                                                  for path, path_count in top_5_paths]}

        # Add the current host's information to the detailed result dictionary
        detailed_result[host] = host_info

    return detailed_result
