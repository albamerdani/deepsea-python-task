import re
import logging
from flask import APIRouter, jsonify
from collections import Counter

router = APIRouter()

log = logging.getLogger("DeepSea Technologies Test Logs")
log_file_path = 'path/to/your/logfile.log'  # Update with the actual path to your log file


def read_log_file():
    try:
        with open(log_file_path, 'r') as file:
            return file.readlines()
    except Exception as e:
        return [{'error': str(e), 'line': None}]


def extract_hosts():
    log_data = read_log_file()
    hosts = []
    for line in log_data:
        try:
            host_match = re.search(r'^\S+\s(\S+)', line)
            if host_match:
                hosts.append(host_match.group(1))
        except Exception as e:
            return [{'error': str(e), 'line': line}]
    return hosts


def extract_paths(host):
    log_data = read_log_file()
    paths = []
    for line in log_data:
        try:
            if host in line:
                path_match = re.search(r'"GET\s([^"]+)\sHTTP/1.0"', line)
                if path_match:
                    paths.append(path_match.group(1))
        except Exception as e:
            return [{'error': str(e), 'line': line}]
    return paths


@router.get('/top10Hosts')
def top_10_hosts():
    hosts = extract_hosts()
    if 'error' in hosts[0]:
        return jsonify({'error': hosts[0]['error'], 'line': hosts[0]['line']})

    host_counts = Counter(hosts)
    log.info("Extracting top 10 hosts ...")
    top_10_hosts = host_counts.most_common(10)
    result = {'top10_hosts': [{'host': host, 'count': count} for host, count in top_10_hosts]}
    return jsonify(result)


@router.get('/top10HostsDetailed')
def top_10_hosts_detailed():
    hosts = extract_hosts()
    if 'error' in hosts[0]:
        return jsonify({'error': hosts[0]['error'], 'line': hosts[0]['line']})

    host_counts = Counter(hosts)
    top_10_hosts = host_counts.most_common(10)

    detailed_result = {}
    for host, count in top_10_hosts:
        paths = extract_paths(host)
        if 'error' in paths[0]:
            return jsonify({'error': paths[0]['error'], 'line': paths[0]['line']})

        path_counts = Counter(paths)
        top_5_paths = path_counts.most_common(5)
        host_info = {'host': host, 'count': count,
                     'top5_paths': [{'path': path, 'count': path_count} for path, path_count in top_5_paths]}
        detailed_result[host] = host_info

    return jsonify(detailed_result)
