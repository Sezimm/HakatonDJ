from django.db import models




class Hospital(models.Model):
    REGIONS = (
        ('O', 'OSH'),
        ('T', 'TALAS'),
        ('C','CHUI'),
        ('B', 'BATKEN'),
        ('I','ISSYK-KUL'),
        ('N','NARYN'),
        ('J','JALAL-ABAD')
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, verbose_name='ОКПО', unique=True)
    region = models.CharField(max_length=100, choices=REGIONS)
    person = models.CharField(max_length=2, default=10)
    gos = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class GL_Doctor(models.Model):
    full_name = models.CharField(max_length=255)
    pin_id = models.IntegerField()
    age = models.IntegerField()
    staj = models.IntegerField()
    phone = models.IntegerField()
    work = models.OneToOneField(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

class Doctor(models.Model):
    PROFETION = (
        ('ter', 'Terapeft'),
        ('hit', 'Hirurg')
    )
    napravlenie = models.CharField(max_length=100, choices=PROFETION, default=PROFETION[0][1])
    full_name = models.CharField(max_length=255)
    pin_id = models.IntegerField()
    age = models.IntegerField()
    staj = models.IntegerField()
    phone = models.IntegerField()

    work = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    work_gl = models.ForeignKey(GL_Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name



class Nurse(models.Model):
    full_name = models.CharField(max_length=255)
    pin_id = models.IntegerField()
    age = models.IntegerField()
    phone = models.IntegerField()

    work = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    work_gl = models.ForeignKey(GL_Doctor, on_delete=models.CASCADE)
    work_doc = models.OneToOneField(Doctor, on_delete=models.CASCADE)


    def __str__(self):
        return self.full_name


class Pacient(models.Model):
    full_name = models.CharField(max_length=255)
    pin_id = models.IntegerField()
    age = models.IntegerField()
    phone = models.IntegerField()
    story = models.CharField(max_length=255)

    hos = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    nur = models.ForeignKey(Nurse, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
