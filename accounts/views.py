from rest_framework.views import APIView
from accounts.serializers import MeSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

class RegisterAPIView(APIView):
      permission_classes=[AllowAny]
      
      def post (self,request):
            serializer= RegisterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response (
                  data=serializer.data,
                  status=status.HTTP_201_CREATED
            )
                  
            
            
            
            
            
class MeAPIView(APIView):
      permission_classes=[IsAuthenticated]
      def get(self,request):
            
            serializer=MeSerializer(request.user)
            print(serializer.data)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
            