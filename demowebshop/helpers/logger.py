import json
import logging

import allure
import requests
from allure_commons.types import AttachmentType


def get_logger(module_name: str, level: int = logging.INFO):
    logger = logging.getLogger(module_name)
    if not logger.hasHandlers():
        logger.setLevel(level)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            "%(asctime)s %(filename)-15s %(funcName)-20s - %(levelname)-6s -  %(message)s"
        ))
        logger.addHandler(handler)
    return logger


def parse_response_body(response: requests.Response):
    try:
        response_body = response.json()
    except Exception as e:
        response_body = response.text
    return response_body


def log_http_response(response: requests.Response):
    request = response.request
    request_body = request.body
    response_body = parse_response_body(response)

    log_message = f"""
    ======= HTTP Request =======
    URL:     {request.method} {request.url}
    Body:    {request_body}

    ======= HTTP Response =======
    Status Code: {response.status_code}
    Body:        {response_body}
    """
    basic_logger.info(log_message)


def log_http_response_in_allure(response: requests.Response):
    request = response.request
    request_body = request.body

    allure.attach(
        body = f'Method: {request.method}\nURL: {request.url}',
        name = 'Request Info',
        attachment_type = AttachmentType.TEXT,
        extension = 'txt'
    )
    allure.attach(
        body = request_body,
        name = 'Request Body',
        attachment_type = AttachmentType.TEXT,
        extension = 'txt'
    )

    allure.attach(
        body = f'Status code: {response.status_code}',
        name = 'Response status code',
        attachment_type = AttachmentType.TEXT,
        extension = 'txt'
    )

    try:
        response_json = response.json()
        allure.attach(
            body = json.dumps(response_json, indent = 4, ensure_ascii = False),
            name = "Response",
            attachment_type = AttachmentType.JSON,
            extension = "json",
        )
    except ValueError:
        allure.attach(
            body = response.text,
            name = "Response",
            attachment_type = AttachmentType.TEXT,
            extension = "txt",
        )

    cookies_dict = {cookie.name: cookie.value for cookie in response.cookies}
    allure.attach(
        body = json.dumps(cookies_dict, indent = 4),
        name = 'Cookies',
        attachment_type = AttachmentType.TEXT,
        extension = 'json'
    )


basic_logger = get_logger(__name__, logging.INFO)
