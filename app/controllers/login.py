from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from app.serializers.users import UserTokenSerializer


class LoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            user_serializer = UserTokenSerializer(data=data)

            if user_serializer.is_valid():
                user, is_created = User.objects.get_or_create(username=data.get('username'))
                if is_created:
                    user.set_password(data.get('password'))
                    user.save()

                token = Token.objects.get_or_create(user=user)
            
                return Response({
                    'success':True,
                    'token': str(token[0].key),
                    'user_id': user.pk,
                })
            return Response({
                'success':False,
                'msg': ', '.join(i for i in user_serializer.errors),
            })
        except Exception as e:
            msg = str(e.args[0])
            return Response({
                'success':False,
                'msg': msg,
            })
