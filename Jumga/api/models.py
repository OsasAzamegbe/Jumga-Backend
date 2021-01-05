from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=255, unique=True, primary_key=True)
    flw_json = models.JSONField()
    sender = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        blank=True, null=True, 
        related_name="outgoing_transactions"
    )
    receiver = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
        related_name="incoming_transactions"
    )
    amount_charged = models.IntegerField(default=0)
    processing_fee = models.IntegerField(default=0)
    jumga_fee = models.IntegerField(default=0)
    amount_paid = models.IntegerField(default=0)
    created = models.DateTimeField(editable=False)

    def __save__(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return f'transaction id: {self.tx_id}'


class Merchant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    shop_name = models.CharField(max_length=255, default="", unique=True)
    dispatch_rider = models.OneToOneField('DispatchRider', on_delete=models.CASCADE)
    revenue = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.shop_name}'


class DispatchRider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    revenue = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Dispath Rider'
