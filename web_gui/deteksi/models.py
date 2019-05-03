from django.db import models

# Create your models here.
class File(models.Model):
  file = models.FileField(blank=False, null=False)
  remark = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return "{} {}".format(self.remark,self.timestamp)

class img_bnc(models.Model):
    title = models.TextField()
    img = models.ImageField(upload_to='bnc/')

    def __str__(self):
        return self.title

class img_h(models.Model):
    title = models.TextField()
    img = models.ImageField(upload_to='h/')

    def __str__(self):
        return self.title

class img_s(models.Model):
    title = models.TextField()
    img = models.ImageField(upload_to='s/')

    def __str__(self):
        return self.title

class img_v(models.Model):
    title = models.TextField()
    img = models.ImageField(upload_to='v/')

    def __str__(self):
        return self.title

class img_gray(models.Model):
    title = models.TextField()
    img = models.ImageField(upload_to='gray/')

    def __str__(self):
        return self.title

class tb_ciri(models.Model):
  h = models.FloatField(default=0.0000000000000000, null=True)
  s = models.FloatField(default=0.0000000000000000, null=True)
  v = models.FloatField(default=0.0000000000000000, null=True)
  cont0 = models.FloatField(default=0.0000000000000000, null=True)
  cont45 = models.FloatField(default=0.0000000000000000, null=True)
  cont90 = models.FloatField(default=0.0000000000000000, null=True)
  cont135 = models.FloatField(default=0.0000000000000000, null=True)
  diss0 = models.FloatField(default=0.0000000000000000, null=True)
  diss45 = models.FloatField(default=0.0000000000000000, null=True)
  diss90 = models.FloatField(default=0.0000000000000000, null=True)
  diss135 = models.FloatField(default=0.0000000000000000, null=True)
  asm0 = models.FloatField(default=0.0000000000000000, null=True)
  asm45 = models.FloatField(default=0.0000000000000000, null=True)
  asm90 = models.FloatField(default=0.0000000000000000, null=True)
  asm135 = models.FloatField(default=0.0000000000000000, null=True)
  ener0 = models.FloatField(default=0.0000000000000000, null=True)
  ener45 = models.FloatField(default=0.0000000000000000, null=True)
  ener90 = models.FloatField(default=0.0000000000000000, null=True)
  ener135 = models.FloatField(default=0.0000000000000000, null=True)
  homo0 = models.FloatField(default=0.0000000000000000, null=True)
  homo45 = models.FloatField(default=0.0000000000000000, null=True)
  homo90 = models.FloatField(default=0.0000000000000000, null=True)
  homo135 = models.FloatField(default=0.0000000000000000, null=True)
  corr0 = models.FloatField(default=0.0000000000000000, null=True)
  corr45 = models.FloatField(default=0.0000000000000000, null=True)
  corr90 = models.FloatField(default=0.0000000000000000, null=True)
  corr135 = models.FloatField(default=0.0000000000000000, null=True)
  def __str__(self):
      return "{}".format(self.id)