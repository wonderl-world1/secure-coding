from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User, Product, ChatMessage, BlockedUser, Payment
from .serializers import (
    UserSerializer, ProductSerializer, ChatMessageSerializer,
    BlockedUserSerializer, PaymentSerializer
)
from django.db.models import Q


# 회원가입
class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# 로그인 (토큰 발급)
class UserLoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

# 사용자 정보 보기
class UserInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# 상품 등록 및 전체 상품 조회
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

# 개별 상품 상세 보기, 수정, 삭제
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

# 채팅 보내기 및 조회
class ChatMessageView(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all().order_by('-timestamp')
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

# 유저 차단하기
class BlockUserView(generics.CreateAPIView):
    queryset = BlockedUser.objects.all()
    serializer_class = BlockedUserSerializer
    permission_classes = [permissions.IsAuthenticated]

# 송금 기능
class PaymentView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

# 상품 검색 기능
class ProductSearchView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Product.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).order_by('-created_at')

# Admin 유저의 차단 상태 토글 기능
class AdminUserBlockToggleView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.is_blocked = not user.is_blocked
            user.save()
            return Response({'status': 'success', 'blocked': user.is_blocked})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
