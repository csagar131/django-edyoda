from django.db.models.signals import post_save
from django.dispatch import receiver
from caremain.models import CareRequests,Transaction

@receiver(post_save,sender=CareRequests)
def create_transaction_object(sender,created,instance,**kwargs):
    if instance.status == 'completed' and not created:
        transaction=Transaction.objects.create(careseeker = instance.careseeker,caregiver = instance.caregiver)
        


