from rest_framework.serializers import (
	HyperlinkedIdentityField,
	HyperlinkedRelatedField,
	PrimaryKeyRelatedField,
	ModelSerializer,
)

from .models import (
	User,
	Post,
	Course,
)



class PostSerializer(ModelSerializer):
	author = HyperlinkedRelatedField(view_name='user-detail', read_only=True)

	def get_validation_exclusions(self, *args, **kwargs):
		# exclude the author field as we supply it later on in the
		# corresponding view based on the http request
		exclusions = super(PostSerializer, self).get_validation_exclusions(*args, **kwargs)
		return exclusions + ['author']

	class Meta:
		model = Post
		fields = '__all__'


class UserSerializer(ModelSerializer):

	# posts = PostSerializer(many=True,read_only=True)
	# Должно совпадать с Model

	# Если есть связь в Model то указывать не нужно (может не отображатся в форме)
	# courses = CourseSerializer(many=True,read_only=True)

	class Meta:
		model = User
		fields = '__all__'
		# fields = (
		#     'id',
		#     'username',
		#     'first_name',
		#     'last_name',
		# 	'posts',
		#     'courses',
		# )


class CourseSerializer(ModelSerializer):



	# users = PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
	# users = HyperlinkedRelatedField(User, many=True, read_only=True)
	# user = UserSerializer(many=True)
	# users = UserSerializer(many=True, read_only=True)
	# members = PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
		#fields = '__all__'
	class Meta:
		model = Course
		fields = '__all__'
