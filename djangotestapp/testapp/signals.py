# myapp/signals.py

from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def my_callback(sender, **kwargs):
    # マイグレーション完了後に実行したい処理
    print("マイグレーション完了後に実行される処理")
