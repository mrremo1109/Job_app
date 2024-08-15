from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job_Seeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    address = models.TextField(max_length=80, blank=True, null=True)
<<<<<<< HEAD
    resume = models.FileField(upload_to='resumes/')
=======
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
>>>>>>> cea0c8b141975ab6ace93ba729c91aad997cb299
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.user.first_name +' '+ self.user.last_name
    
<<<<<<< HEAD
=======

>>>>>>> cea0c8b141975ab6ace93ba729c91aad997cb299
class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    company = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.company 

class Job_Post(models.Model):
    user = models.ForeignKey("Recruiter", on_delete=models.CASCADE)
    post = models.CharField(max_length=50)
    salary = models.IntegerField()
    description = models.TextField()
    posted_on = models.DateField()
    upto = models.DateField()

    def __str__(self):
        return self.post

<<<<<<< HEAD
=======
    
>>>>>>> cea0c8b141975ab6ace93ba729c91aad997cb299
class AppliedPost(models.Model):
    applied_by = models.ForeignKey("Job_Seeker", on_delete=models.CASCADE)
    job = models.ForeignKey("Job_Post", on_delete=models.CASCADE)
    applied_on = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('reviewing', 'Reviewing'),
        ('selected', 'Selected'),
        ('rejected', 'Rejected')
    ], default='reviewing')

    def __str__(self):
        return f'{self.applied_by.user.first_name} {self.applied_by.user.last_name} - {self.job.post}'
    
<<<<<<< HEAD
=======

>>>>>>> cea0c8b141975ab6ace93ba729c91aad997cb299
class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    feedback = models.TextField()

    def __str__(self):
        return self.name
<<<<<<< HEAD

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.username} to {self.receiver.username}'
=======
    

    




>>>>>>> cea0c8b141975ab6ace93ba729c91aad997cb299
