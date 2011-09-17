from django.db import models
from django.contrib.contenttypes import generic


class JoinRequest(models.Model):
    PENDING = 0
    ACCEPTED = 1
    REJECTED = 2

    STATE_CHOICES = ((PENDING, "Pending"),
                     (ACCEPTED, "Accepted"),
                     (REJECTED, "Rejected"),)

    content_type = models.ForeignKey("contenttypes.ContentType")
    object_id = models.PositiveIntegerField()
    realm = generic.GenericForeignKey()

    user = models.ForeignKey("auth.User")
    message = models.TextField(blank=True)
    state = models.IntegerField(choices=STATE_CHOICES, default=PENDING)

    host_user = models.ForeignKey("auth.User", null=True)
    host_message = models.TextField(blank=True)
    host_state = models.IntegerField(choices=STATE_CHOICES, default=PENDING)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
