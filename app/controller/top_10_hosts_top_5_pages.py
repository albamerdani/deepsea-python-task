import re
from flask import Flask, jsonify
from collections import Counter

app = Flask(__name__)


@app.route('/top10HostsDetailed')
def top_10_hosts_detailed():
    log_file_path = 'D:\\Merdani_ITServices\\DeepSea\\deepsea-python-task\\app\\http_log_file\\new_final_final_01.log'  # Update with the actual path to your log file

    # Read the log file and extract hosts (IP addresses or domains)
    with open(log_file_path, 'r') as file:
        log_data = file.readlines()

    # Extract hosts using a regular expression
    # Assuming the format is the host immediately following the first space in the line
    hosts = []

    # Extract requested hosts using regular expressions
    for line in log_data:
        pattern = r'^(\S+)\s+-\s+-\s+\['
        match = re.search(pattern, line)
        if match:
            # Count the occurrences of each host
            host = match.group(1)
            hosts.append(host)

    # Count the occurrences of each host
    host_counts = Counter(hosts)

    # Get the top 10 hosts with the most requests
    top_10_hosts = host_counts.most_common(10)

    # Create a dictionary for the detailed JSON response
    detailed_result = {}

    for host, count in top_10_hosts:
        # Filter log entries for the current host
        host_entries = [line for line in log_data if host in line]

        # Extract paths requested by the current host
        paths = []
        for line in host_entries:
            pattern = r'"GET\s([^"]+)\sHTTP/1.0"'
            match = re.search(pattern, line)
            if match:
                # Count the occurrences of each path
                path = match.group(1)
                paths.append(path)

        # Count the occurrences of each path
        path_counts = Counter(paths)

        # Get the top 5 paths requested by the current host
        top_5_paths = path_counts.most_common(5)

        # Create a dictionary for the current host's detailed information
        host_info = {'host': host, 'count': count, 'top5_paths': [{'path': path, 'count': path_count} for path, path_count in top_5_paths]}

        # Add the current host's information to the detailed result dictionary
        detailed_result[host] = host_info

    return jsonify(detailed_result)


if __name__ == '__main__':
    app.run(debug=True)
