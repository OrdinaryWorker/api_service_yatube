from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='posts')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts')
        ref_name = 'ReadOnlyUsers'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.SlugRelatedField(read_only=True, slug_field='id')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=('user', 'following'),
                message='Подписка на данного автора уже оформлена'
            )
        ]

    def validate_following(self, value):
        if self.context.get('request').user == value:
            raise serializers.ValidationError(
                'Пользователь не может подписаться на самого себя'
            )
        return value
