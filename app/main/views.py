from . import main
from flask import jsonify
from webargs.flaskparser import use_args
from .params import smtp_args, sendinblue_send_args, sendinblue_check_args
from .controller import smtp_check, sendinblue_check, sendinblue_send

@main.route('/smtp', methods=['POST'])
@use_args(smtp_args, location="json")
def smtpcheck(args):
    return jsonify(smtp_check(args['host'], args['port'], 
                              args['username'], args['password'], 
                              args['email_to'], args['email_from']))

@main.route('/sendinblue-send', methods=['POST'])
@use_args(sendinblue_send_args, location="json")
def sendinblusend(args):
    return jsonify(sendinblue_send(args['apikey'], args['sender'],
                                   args['content'], args['recipient']))

@main.route('/sendinblue-check', methods=['POST'])
@use_args(sendinblue_check_args, location="json")
def sendinbluecheck(args):
    return jsonify(sendinblue_check(args['apikey']))