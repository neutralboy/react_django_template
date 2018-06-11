from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class current_user_data(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		return Response({'status': 200, 'username':request.user.username, 'first_name':request.user.first_name, 'last_name':request.user.last_name})


		