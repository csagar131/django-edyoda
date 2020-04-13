from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from django.contrib.auth.models import Group


@receiver(post_save,sender = User)
def create_user_profile(sender,instance,**kwargs):
    if instance.is_author:
        author = Group.objects.get(name = "Author")
        user = Group.objects.get(name = 'User')
        instance.groups.add(author,user)


        
        

