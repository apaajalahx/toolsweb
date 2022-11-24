from flask import current_app, Blueprint, jsonify

main = Blueprint('main', __name__)

@main.app_errorhandler(500)
def internal_server_error(exception):
    current_app.logger.error(exception)
    return jsonify({ 'error' : True, 'messages' : 'Internal Server Error'}), 500

@main.app_errorhandler(404)
def not_found(exception):
    return jsonify({ 'error' : True, 'messages' : 'Not Found' }), 404

@main.app_errorhandler(405)
def method_not_allowed(exception):
    return jsonify({ 'error' : True, 'messages' : 'Method Not Allowed'}), 405

@main.errorhandler(422)
def unprocessable_entity(exception):
    messages = exception.data.get('messages').get('json')
    return jsonify(messages)