# UserCreationFormをインポート
from django.contrib.auth.forms import UserCreationForm
# models.pyで定義したカスタムUserモデルをインポート
from .models import CustomUser

class CustomUserUserCreationForm(UserCreationForm):
    '''UserCreationFormのサブクラス
    '''
    class Meta:
        '''UserCreationFormのインナークラス
        
        Attributes:
            model:連携するUserモデル
            fields:フォームで使用するフィールド
        '''
        # 連携するUserモデルを設定
        model = CustomUser
        # フォームで使用するフィールドを設定
        # ユーザ名、メールアドレス、パスワード、パスワード(確認用)
        fields = ('username', 'email', 'password1', 'password2')
