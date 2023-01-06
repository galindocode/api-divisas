from flask import jsonify, Response


def success(data: dict, message: str = "", status_code: int = 200):
    return jsonify({
        "data": data,
        "message": message,
        "status_code": status_code,
        "success": 1,
        "error": 0
    }), status_code


def error(message: str = "", status_code: int = 400):
    return jsonify({
        "message": message,
        "status_code": status_code,
        "success": 1,
        "error": 0
    }), status_code
