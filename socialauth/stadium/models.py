from django.db import models
ROLE = (
    ('admin', 'admin'),
    ('custumer', 'customer')
)
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=12, null=True)
    role = models.CharField(max_length=100, choices=ROLE, null=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Stadium(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    field_count = models.IntegerField()

    def __str__(self):
        return self.name


class TimeFrame(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.start_time} - {self.end_time}'


class StadiumTimeFrame(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.SET_NULL, null=True)
    time_frame = models.ForeignKey(
        TimeFrame, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.stadium.name}: {self.time_frame.start_time} - {self.time_frame.end_time}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    stadium_time_frame = models.ForeignKey(
        StadiumTimeFrame, on_delete=models.CASCADE, null=True)
    field_number = models.IntegerField()
    order_datetime = models.DateTimeField(auto_now_add=True, null=True)
    is_accepted = models.BooleanField(default=False, null=True)
    customer_phone_number = models.CharField(max_length=12, null=True)
    customer_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'Order of {self.user.name}'
