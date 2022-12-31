from django.db import models




class dept(models.Model):
    dept_name=models.CharField(max_length=40)
    dept_code=models.CharField(max_length=40)
    headofdept=models.CharField(max_length=50)
    dept_desc=models.TextField(blank=False)
    dept_specialization=models.TextField(blank=False)
    
    def __str__(self):
        return self.dept_name


Dept= (
    ("dept1", "dept1"),
    ("dept2", "dept2"),
    ("dept3", "dept3"),
    ("dept4", "dept4"),
    ("dept5", "dept5"),
)
slot= (
    ("morning", "morning"),
    ("Evening", "Evening"),
    ("day", "day"),)
    

    

# Create your models here.
class booking_Appointments(models.Model):
    appointemnt_id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=30)
    Email=models.EmailField(max_length=30)
    Phone_no=models.PositiveIntegerField()
    department = models.ForeignKey(dept,null=True,on_delete=models.CASCADE,
        name='department'
        )
    description=models.TextField(default="Describe your problem")
    slot=models.CharField(
        max_length=40,
        choices = slot,
    )
    date=models.DateField()



    def __str__(self):
        return self.Name


class package(models.Model):
    package_name=models.CharField(max_length=40)
    package_code=models.CharField(max_length=40)
    price=models.CharField(max_length=10)
    package_desc=models.TextField(blank=False)
    related_dept=models.ForeignKey(dept,null=True,on_delete=models.CASCADE)
    duration=models.CharField(max_length=45)

    def __str__(self):
        return self.package_name





class have_query(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField(max_length=30)
    phone_no=models.CharField(max_length=10)
    short_desc=models.TextField()
    related_dept=models.ForeignKey(dept, null=True,on_delete=models.CASCADE,default="All_dept")

    def __str__(self):
        return self.Name


class subscription(models.Model):
    subs_id=models.AutoField(primary_key=True)
    Email=models.EmailField()
    Whatsapp_no=models.CharField(max_length=12)

    def __str__(self):
        return self.Email

