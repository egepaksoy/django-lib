from django.db import models


class User(models.Model):
  uname = models.CharField(verbose_name="Kullanıcı Adı", max_length=50)
  passwd = models.CharField(verbose_name="Şifre", max_length=100)
  isloged = models.BooleanField(verbose_name="Giriş durumu", default=False)

  
  def __str__(self):
      return self.uname