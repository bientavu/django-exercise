from django.db import models


class ArticleCategory(models.Model):
    """
    Category of an article
    """

    class Meta:
        verbose_name = "Article Category"
        verbose_name_plural = "Article Categories"

    objects = models.Manager()

    display_name = models.CharField("Display name", max_length=255)

    def __str__(self):
        return f"{self.display_name}"


class Article(models.Model):
    """
    An article is an item that can be sold.
    """

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    objects = models.Manager()

    code = models.CharField("Code", max_length=6, unique=True)
    category = models.ForeignKey(
        ArticleCategory,
        verbose_name="Category",
        related_name="articles",
        on_delete=models.PROTECT,
    )
    name = models.CharField("Name", max_length=255)
    manufacturing_cost = models.DecimalField(
        "Manufacturing Cost", max_digits=11, decimal_places=2
    )

    def __str__(self):
        return f"{self.code} - {self.name}"


class Sale(models.Model):
    """
    A sale of an article.
    """

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    objects = models.Manager()

    date = models.DateField("Date")
    author = models.ForeignKey(
        "users.User",
        verbose_name="Author",
        related_name="sales",
        on_delete=models.PROTECT,
    )
    article = models.ForeignKey(
        Article, verbose_name="Article", related_name="sales", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField("Quantity")
    unit_selling_price = models.DecimalField(
        "Unit selling price", max_digits=11, decimal_places=2
    )

    def __str__(self):
        return f"{self.date} - {self.quantity} {self.article.name}"
