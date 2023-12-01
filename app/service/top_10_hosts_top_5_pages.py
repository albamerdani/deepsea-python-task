from collections import Counter
from app.service.read_log_file import LogFile


def top_10_hosts_detailed() -> dict:
    """
       Generate a detailed report of the top 10 hosts based on the number of requests.

       Returns:
       dict: A dictionary containing lists with detailed information about the top 10 hosts.
             Each entry includes the host's IP address or domain and the corresponding
             number of requests made for top 5 pages including the page name.

       Example:
       {
          "163.206.89.4": {
            "count": 4791,
            "host": "163.206.89.4",
            "top5_paths": [
              {
                "count": 568,
                "path": "/images/NASA-logosmall.gif"
              },
              {
                "count": 360,
                "path": "/htbin/cdt_main.pl"
              },
              {
                "count": 347,
                "path": "/shuttle/countdown/images/countclock.gif"
              },
              {
                "count": 251,
                "path": "/ksc.html"
              },
              {
                "count": 237,
                "path": "/images/USA-logosmall.gif"
              }
            ]
          },
          "edams.ksc.nasa.gov": {
            "count": 6530,
            "host": "edams.ksc.nasa.gov",
            "top5_paths": [
              {
                "count": 1020,
                "path": "/ksc.html"
              },
              {
                "count": 870,
                "path": "/images/WORLD-logosmall.gif"
              },
              {
                "count": 869,
                "path": "/images/NASA-logosmall.gif"
              },
              {
                "count": 867,
                "path": "/images/MOSAIC-logosmall.gif"
              },
              {
                "count": 867,
                "path": "/images/USA-logosmall.gif"
              }
            ]
          }
        }
    """
    log_file = LogFile()

    hosts = log_file.extract_hosts()

    # Count the occurrences of each host
    host_counts = Counter(hosts)

    # Get the top 10 hosts with the most requests
    top_10_hosts = host_counts.most_common(10)

    # Create a dictionary for the detailed JSON response
    detailed_result = {}
    log_data = log_file.read_log_file()

    for host, count in top_10_hosts:
        # Filter log entries for the current host
        host_entries = [line for line in log_data if host in line]

        # Extract paths requested by the current host
        paths = log_file.extract_paths(host_entries)

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
