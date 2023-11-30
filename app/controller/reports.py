from service import top_10_hosts, top_10_hosts_top_5_pages, top_10_pages, top_10_unsuccessful_requests, successful_requests_percentage, unsuccessful_requests_percentage
import logging
from flask import APIRouter, jsonify

router = APIRouter()

log = logging.getLogger("DeepSea Technologies Test Logs")


@router.get('/top10Pages')
def top_10_hosts_detailed():
    result = top_10_pages.top_10_pages()

    return jsonify(result)


@router.get('/successPercentage')
def top_10_hosts_detailed():
    result = successful_requests_percentage.success_percentage()

    return jsonify(result)


@router.get('/unsuccessfulPercentage')
def top_10_hosts_detailed():
    result = unsuccessful_requests_percentage.unsuccessful_percentage()

    return jsonify(result)


@router.get('/top10UnsuccessfulRequests')
def top_10_hosts_detailed():
    result = top_10_unsuccessful_requests.top_10_unsuccessful()

    return jsonify(result)


@router.get('/top10Hosts')
def top_10_hosts():

    result = top_10_hosts.top_10_hosts()
    return jsonify(result)


@router.get('/top10HostsDetailed')
def top_10_hosts_detailed():
    detailed_result = top_10_hosts_top_5_pages.top_10_hosts_detailed()

    return jsonify(detailed_result)

