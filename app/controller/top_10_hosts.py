import re
from flask import Flask, jsonify
from collections import Counter

app = Flask(__name__)


@app.route('/top10Hosts')
def top_10_hosts():
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

    # Create a dictionary for the JSON response
    result = {'top10_hosts': [{'host': host, 'count': count} for host, count in top_10_hosts]}

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
