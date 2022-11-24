from webargs import fields
from marshmallow import validate


smtp_args = {
    "host" : fields.String(required=True, validate=validate.Length(min=5)),
    "port" : fields.Integer(required=True),
    "username" : fields.String(required=True, validate=validate.Length(min=3)),
    "password" : fields.String(required=True, validate=validate.Length(min=5)),
    "email_to" : fields.String(required=True, validate=validate.Email()),
    "email_from" : fields.String(missing=None, validate=validate.Email())
}

sendinblue_send_args = {
    "apikey" : fields.String(required=True, validate=validate.Length(min=30)),
    "sender" : fields.String(required=True),
    "content" : fields.String(required=True),
    "recipient" : fields.Integer(required=True) 
}

sendinblue_check_args = {
    "apikey" : fields.String(required=True)
}