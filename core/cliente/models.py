from django.db import models
import core.models


class User(core.models.Log, core.models.PessoaLog):
    user = models.OneToOneField('user.User', on_delete=models.DO_NOTHING, null=True)

    endereco = models.ForeignKey('core.Endereco', on_delete=models.DO_NOTHING, null=True, related_name='endereco')
    is_cliente = models.BooleanField(default=False)

    class Meta:
        db_table = 'cliente'