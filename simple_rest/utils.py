from social_app.serializers import GetFullUserSerializer

def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token' : token,
        'user' : GetFullUserSerializer(user, context={'request' : request}).data
    }