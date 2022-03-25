from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('content', required=True)
parser.add_argument('is_private', required=True, type=bool)
parser.add_argument('is_published', required=True, type=bool)
parser.add_argument('user_id', required=True, type=int)

parser_user = reqparse.RequestParser()
parser_user.add_argument('name', required=True)
parser_user.add_argument('about', required=True)
parser_user.add_argument('email', required=True)
parser_user.add_argument('password', required=True)