from django.apps import AppConfig
import testapp.signals


class TestappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testapp'

    def ready(self):
        # アプリケーションの初期化処理
        print("アプリケーションの初期化処理を実行します")
        # ここに一度だけ実行したい処理を記述する
