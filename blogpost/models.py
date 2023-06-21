from django.db import models



# Create your models here.
CATEGORY = (('business','公開許可'),('life','公開不許可'),('other','その他'))

#class SampleModel(models.Model):
#    title = models.CharField(max_length=100)
#    number = models.IntegerField()

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(max_length = 50 , choices = CATEGORY)
    def __str__(self):
        return self.title



class ESIComModel(models.Model):
    compound_name = models.CharField()
    smiles = models.CharField()
    molecular_weight = models.FloatField( max_length=10)
    pubchemid = models.IntegerField()
    def __str__(self):
        return self.compound_name

class ESI_descriptor_Model(models.Model):
    compound_name = models.CharField()
    smiles = models.CharField()
    lpv = models.FloatField( max_length=10)
    c_s0 = models.FloatField( max_length=10)
    s0_c = models.FloatField( max_length=10)
    eav = models.FloatField( max_length=10)
    a_s0 = models.FloatField( max_length=10)
    s0_a = models.FloatField( max_length=10)
    stv = models.FloatField( max_length=10)
    t1_s0 = models.FloatField( max_length=10)
    s0_t1 = models.FloatField( max_length=10)
    esolv = models.FloatField( max_length=10)
    dm = models.FloatField( max_length=10)
    vmol =  models.FloatField( max_length=10)
    b1 = models.FloatField(max_length=10, null=True, default=None)
    b2 = models.FloatField(max_length=10, null=True, default=None)
    b3 = models.FloatField(max_length=10, null=True, default=None)
    def __str__(self):
        return self.smiles

#6/13
PP = (('approval','approval'),('disapproval','disapproval')) #publish permission
QS = (('answered','answered'),('unanswered','unanswered'),('on_hold','on_hold')) #question situation
class question_Model(models.Model):
    date = models.DateTimeField(auto_now=True)
    question_title = models.CharField(max_length=255)
    question = models.TextField()
    public_permission = models.CharField(max_length = 50 , choices = PP)
    email_adress = models.CharField(max_length=255, blank=True, null=True)
    question_situation = models.CharField(max_length = 50 , choices = QS ,default='unanswered')
    reply = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.question_title

