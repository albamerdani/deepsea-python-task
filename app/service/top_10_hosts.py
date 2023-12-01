from collections import Counter
from app.service.read_log_file import LogFile


def top_10_hosts() -> dict:
    """
        Generate a detailed report of the top 10 hosts based on the number of requests.

        Returns:
        dict: A dictionary containing detailed information about the top 10 hosts.
        For each entry is the page name and number of requests to those.

        Example:
        {
          "top_10_hosts": [
            {
              "count": 6530,
              "host": "edams.ksc.nasa.gov"
            },
            {
              "count": 4846,
              "host": "piweba4y.prodigy.com"
            },
            {
              "count": 4791,
              "host": "163.206.89.4"
            },
            {
              "count": 4607,
              "host": "piweba5y.prodigy.com"
            },
            {
              "count": 4416,
              "host": "piweba3y.prodigy.com"
            },
            {
              "count": 3889,
              "host": "www-d1.proxy.aol.com"
            },
            {
              "count": 3534,
              "host": "www-b2.proxy.aol.com"
            },
            {
              "count": 3463,
              "host": "www-b3.proxy.aol.com"
            },
            {
              "count": 3423,
              "host": "www-c5.proxy.aol.com"
            },
            {
              "count": 3411,
              "host": "www-b5.proxy.aol.com"
            }
          ]
        }
    """
    log_file = LogFile()

    hosts = log_file.extract_hosts()

    # Count the occurrences of each host
    host_counts = Counter(hosts)

    # Get the top 10 hosts with the most requests
    top_10_hosts = host_counts.most_common(10)

    # Create a dictionary for the JSON response
    result = {'top_10_hosts': [{'host': host, 'count': count} for host, count in top_10_hosts]}

    return result
