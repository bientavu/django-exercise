from rest_framework import serializers

from sales.models import Sale, Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'


class SalesListBy25Serializer(serializers.ModelSerializer):
    category_article = serializers.SerializerMethodField('get_category_article')
    article_code = serializers.SerializerMethodField('get_article_code')
    article_name = serializers.SerializerMethodField('get_article_name')
    total_price = serializers.SerializerMethodField('get_total_price')

    class Meta:
        model = Sale
        fields = (
            'date',
            'category_article',
            'article_code',
            'article_name',
            'quantity',
            'unit_selling_price',
            'total_price'
        )

    @staticmethod
    def get_category_article(sale):
        category_article = sale.article.category_id
        return category_article

    @staticmethod
    def get_article_code(sale):
        article_code = sale.article.code
        return article_code

    @staticmethod
    def get_article_name(sale):
        article_name = sale.article.name
        return article_name

    @staticmethod
    def get_total_price(sale):
        total_price = sale.unit_selling_price * sale.quantity
        return total_price
