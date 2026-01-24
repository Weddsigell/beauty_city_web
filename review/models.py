from django.db import models


class Review(models.Model):
    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="reviews",
    )
    text = models.TextField()
    grade = models.PositiveSmallIntegerField(
        verbose_name="Оценка", choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-created_at"]

    def __str__(self):
        return self.created_at
