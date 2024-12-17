from django.db import models
from django.core.validators import validate_comma_separated_integer_list 
import uuid
# Create your models here.

class djangoModelClass(models.Model):

    auto_field = models.AutoField(primary_key=True)
    # big_auto_field = models.BigAutoField()
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    comma_separated_field = models.CharField(
        validators=[validate_comma_separated_integer_list], max_length=255
    )
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file_field = models.FileField(upload_to='files/')
    # file_path_field = models.FilePathField(path='first_app/files')
    float_field = models.FloatField()
    foreign_key = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='foreign_key_rel')
    generic_ip_address_field = models.GenericIPAddressField()
    # image_field = models.ImageField(upload_to='images/')
    integer_field = models.IntegerField()
    json_field = models.JSONField()
    many_to_many_field = models.ManyToManyField('self', blank=True)
    null_boolean_field = models.BooleanField(null=True)
    one_to_one_field = models.OneToOneField(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='one_to_one_rel'
    )
    positive_big_integer_field = models.PositiveBigIntegerField()
    positive_integer_field = models.PositiveIntegerField()
    positive_small_integer_field = models.PositiveSmallIntegerField()
    slug_field = models.SlugField()
    small_integer_field = models.SmallIntegerField()
    text_field = models.TextField()
    time_field = models.TimeField()
    url_field = models.URLField()
    uuid_field = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.char_field}"
