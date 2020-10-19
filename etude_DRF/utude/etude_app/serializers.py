from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """本モデル用のシリアライザ"""

    class Meta:
        # 対象のモデルクラスを指定
        model = Book
        # 利用するモデルのフィールドを指定
        fields = ["id", "title", "price"]


class BookListSerializer(serializers.ModelSerializer):
    """複数の本を扱うためのシリアライザ"""

    # 対象のシリアライザを指定
    child = BookSerializer()
