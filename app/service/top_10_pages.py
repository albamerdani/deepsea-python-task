from collections import Counter
from app.service.read_log_file import LogFile


def top_10_pages() -> dict:
    """
        Generate a detailed report of the top 10 pages based on the number of requests.

        Returns:
        dict: A dictionary containing detailed information about the top 10 pages.
        For each entry is the page name and number of requests to those.

        Example:
        {
            "top10_pages": [
                {
                    "page": "ksc.html",
                    "requests": 43382
                },
                {
                    "page": "shuttle/missions/sts-69/mission-sts-69.html",
                    "requests": 24544
                },
                {
                    "page": "shuttle/missions/missions.html",
                    "requests": 22341
                },
                {
                    "page": "software/winvn/winvn.html",
                    "requests": 10059
                },
                {
                    "page": "history/history.html",
                    "requests": 10040
                },
                {
                    "page": "history/apollo/apollo.html",
                    "requests": 8957
                },
                {
                    "page": "shuttle/countdown/liftoff.html",
                    "requests": 7836
                },
                {
                    "page": "history/apollo/apollo-13/apollo-13.html",
                    "requests": 7158
                },
                {
                    "page": "shuttle/technology/sts-newsref/stsref-toc.html",
                    "requests": 6452
                },
                {
                    "page": "shuttle/missions/sts-69/images/images.html",
                    "requests": 5258
                }
            ]
        }
    """
    log_file = LogFile()

    pages = log_file.extract_pages()

    # Count the occurrences of each page
    page_counts = Counter(pages)

    # Get the top 10 pages
    top_10_pages = page_counts.most_common(10)

    # Create a dictionary for the JSON response
    result = {'top10_pages': [{'page': page, 'requests': count} for page, count in top_10_pages]}

    return result
