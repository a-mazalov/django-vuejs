from rest_framework.serializers import (
    HyperlinkedIdentityField,
    HyperlinkedRelatedField,
    ModelSerializer,
)

from .models import (
    User,
    Post,
)


class UserSerializer(ModelSerializer):

    posts = HyperlinkedIdentityField(view_name='user-posts')

    class Meta:
        model = User
        fields = '__all__'
        # fields = (
        #     'id',
        #     'username',
        #     'first_name',
        #     'last_name',
        #     'posts',
        # )


class PostSerializer(ModelSerializer):
    # all_posts = DevelopmentSerializer(read_only=True) 
    author = HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    def get_validation_exclusions(self, *args, **kwargs):
        # exclude the author field as we supply it later on in the
        # corresponding view based on the http request
        exclusions = super(PostSerializer, self).get_validation_exclusions(*args, **kwargs)
        return exclusions + ['author']

    class Meta:
        model = Post
        fields = '__all__'
