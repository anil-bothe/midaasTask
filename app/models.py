from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class PrimeNo(Base):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ALGO_TYPE = (
        (0, 'Normal'),
        (1, 'Sieve Eratosthenes.')
    )
    algo_id = models.IntegerField(null=True)
    input_range = models.CharField(max_length=20, null=True)
    elapsed_time = models.FloatField(null=True)
    result = models.TextField(null=True)
    
    def __str__(self) -> str:
        return str(self.user)
    
    class Meta:
        db_table = 'prime_no_gen'
