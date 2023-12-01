from app.service import top_10_hosts, top_10_hosts_top_5_pages, top_10_pages, top_10_unsuccessful_requests, successful_requests_percentage, unsuccessful_requests_percentage
import logging
from flask import Flask, jsonify


# Function that create the app
def create_app():
    # create and configure the app
    app = Flask(__name__)

    log = logging.getLogger("DeepSea Technologies Test Logs")

    @app.route('/top10Pages')
    def top_10_page():
        result = top_10_pages.top_10_pages()

        return jsonify(result)

    @app.route('/successPercentage')
    def success_percentage():
        result = successful_requests_percentage.success_percentage()

        return jsonify(result)

    @app.route('/unsuccessfulPercentage')
    def unsuccessful_percentage():
        result = unsuccessful_requests_percentage.unsuccessful_percentage()

        return jsonify(result)

    @app.route('/top10Unsuccessful')
    def top_10_unsuccessful_request():
        result = top_10_unsuccessful_requests.top_10_unsuccessful()

        return jsonify(result)

    @app.route('/top10Hosts')
    def top_10_host():

        result = top_10_hosts.top_10_hosts()
        return jsonify(result)

    @app.route('/top10HostsDetailed')
    def top_10_hosts_detailed():
        detailed_result = top_10_hosts_top_5_pages.top_10_hosts_detailed()

        return jsonify(detailed_result)

    return app
