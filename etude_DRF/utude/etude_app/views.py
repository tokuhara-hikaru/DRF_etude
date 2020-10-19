from django_filters import rest_framework as filters
from rest_framework import status, views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Book
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer


class BookCreateAPIVew(views.APIView):
    """本モデルの登録APIクラス"""

    def post(self, request, *args, **kwargs):
        """本モデルの登録APIクラスに対応するハンドラメソッド"""

        # シリアライザオブジェクトを作成
        serializer = BookSerializer(date=request.data)
        # バリデーションを実行
        serializer.is_valid(raise_exception=True)
        # モデルオジェクトを登録
        serializer.save()
        # レスポンスオブジェクトを作成し返す
        return Response(serializer.data, status.HTTP_201_CREATED)


class BookFilter(filters.FilterSet):
    """本モデル用フィルタクラス"""

    class Meta:
        model = Book
        fields = "__all__"


class BookListAPIView(views.APIView):
    """本モデルの取得（一覧）APIクラス"""

    def get(self, request, *args, **kwargs):
        """本モデルの取得（一覧）APIに対応するハンドラメソッド"""

        # 　モデルオブジェクトをクエリ文字列を使ってフィルタリングした結果を取得
        filterset = BookFilter(request.query_params, queryset=Book.objects.all())

        if not filterset.is_valid():
            # バリデーションがエラーの場合は400エラー
            raise ValidationError(filterset.errors)

        # 　シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=filterset.qs, many=True)

        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data, status.HTTP_200_OK)


class BookRetrieveAPIView(views.APIView):
    """本モデルの取得（詳細）APIに対応するハンドラメソッド"""

    def get(self, request, pk, *args, **kwargs):
        """本モデルの取得（詳細）APIに対応するハンドラメソッド"""

        # モデルオブジェクトの取得
        book = get_object_or_404(Book, pk=pk)
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book)
        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data, status.HTTP_200_OK)


class BookUpdateAPIView(views.APIView):
    """本モデルの更新・一部更新APIクラス"""

    def put(self, request, pk, *args, **kwargs):
        """本モデルの更新APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book, data=request.data, partial=True)
        # バリデーションを実行
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを一部更新
        serializer.save()
        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        """本もセルの一部更新に対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book, data=request.data, partial=True)
        # バリデーションを実行
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを一部更新
        serializer.save()
        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data, status.HTTP_200_OK)


class BookDestroyAPIView(views.APIView):
    """本モデルの削除APIクラス"""

    def delete(self, request, pk, *args, **kwargs):
        """本モデルの削除APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)
        # モデルオブジェクトを削除
        book.delete()
        # レスポンスオブジェクトを作成して返す
        return Response(status=status.HTTP_204_NO_CONTENT)
