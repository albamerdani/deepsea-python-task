import unittest
from app.service import top_10_pages, top_10_hosts, top_10_hosts_top_5_pages, successful_requests_percentage, \
    unsuccessful_requests_percentage, top_10_unsuccessful_requests
from app.service.read_log_file import LogFile


class TestLogAnalyzer(unittest.TestCase):

    def test_read_log_file(self):
        log_file = LogFile()
        # Assuming the read_log_file function returns a list of lines from the log file
        log_lines = log_file.read_log_file()
        self.assertTrue(isinstance(log_lines, list))
        self.assertTrue(len(log_lines) > 0)

    def test_extract_hosts(self):
        log_file = LogFile()
        # Assuming the extract_hosts function returns a list of hosts from the log file
        hosts = log_file.extract_hosts()
        self.assertTrue(isinstance(hosts, list))

    def test_extract_paths(self):
        log_file = LogFile()
        # Assuming the extract_paths function returns a list of paths for a given host
        paths = log_file.extract_paths('example_host')
        self.assertTrue(isinstance(paths, list))

    def test_top_10_pages(self):
        # Assuming the top_10_pages function returns a JSON with the top 10 pages
        response = top_10_pages.top_10_pages()
        self.assertTrue(isinstance(response, dict))
        self.assertTrue('top10_pages' in response)

    def test_top_10_unsuccessful(self):
        # Assuming the top_10_unsuccessful function returns a JSON with the top 10 unsuccessful requests
        response = top_10_unsuccessful_requests.top_10_unsuccessful()
        self.assertTrue(isinstance(response, dict))
        self.assertTrue('top_10_unsuccessful_requests' in response)

    def test_success_percentage(self):
        # Assuming the success_percentage function returns a JSON with the success percentage
        response = successful_requests_percentage.success_percentage()
        self.assertTrue(isinstance(response, dict))
        self.assertTrue('success_percentage' in response)

    def test_top_10_hosts(self):
        # Assuming the top_10_hosts function returns a JSON with the top 10 hosts
        response = top_10_hosts.top_10_hosts()
        self.assertTrue(isinstance(response, dict))
        self.assertTrue('top_10_hosts' in response)

    def test_top_10_hosts_detailed(self):
        # Assuming the top_10_hosts_detailed function returns a detailed JSON with top hosts and their paths
        response = top_10_hosts_top_5_pages.top_10_hosts_detailed()
        self.assertTrue(isinstance(response, dict))
        # Check if the expected structure is present in the response
        self.assertTrue(key in response for key in ['host', 'count', 'top5_paths'])

    def test_unsuccess_percentage(self):
        # Assuming the unsuccessful_percentage function returns a JSON with the unsuccessful percentage
        response = unsuccessful_requests_percentage.unsuccessful_percentage()
        self.assertTrue(isinstance(response, dict))
        self.assertTrue('unsuccessful_percentage' in response)


if __name__ == '__main__':
    unittest.main()
