from . import smtp
from flask import jsonify, request
from webargs.flaskparser import use_args
from .params import smtp_args
from .controller import smtp_check

@smtp.route('/smtp', methods=['POST'])
@use_args(smtp_args, location="json")
def smtpcheck(args):
    return jsonify(smtp_check(args['host'], args['port'], 
                              args['username'], args['password'], 
                              args['email_to'], args['email_from']))