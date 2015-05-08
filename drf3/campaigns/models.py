from django.db import models

CAMPAIGN_TYPES = (('shirt', 'shirt'),
                  ('sticker', 'sticker'))


class Campaign(models.Model):
    name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey('auth.User', related_name='campaigns', default=None, null=True)

    class Meta:
        pass

