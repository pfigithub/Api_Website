from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=Category.objects.all()
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "image",
            "content",
            "category",
            "status",
            "created_date",
            "published_date",
        ]
        read_only_fields = ["author"]

    def to_representation(self, instance):
        # request = self.context.get("request")
        rep = super().to_representation(instance)
        # exmple for seprating
        # if request.parser_context.get('kwargs').get('pk'):
        #     rep.pop('somthing...',None)
        # else:
        #     rep.pop('somthing...',None)
        # example for using this function
        # rep['category'] = CategorySerializer(instance.category).data
        # rep.pop('status', None)
        return rep

    def create(self, validated_date):
        validated_date["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_date)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
