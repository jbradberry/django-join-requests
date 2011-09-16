from django.db import models
from django.contrib.contenttypes import generic


class JoinRequest(models.Model):
    PENDING = 0
    WITHDRAWN = 1
    REJECTED = 2
    ACCEPTED = 3

    STATE_CHOICES = ((PENDING, "Pending"),
                     (WITHDRAWN, "Withdrawn"),
                     (REJECTED, "Rejected"),
                     (ACCEPTED, "Accepted"))

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    realm = generic.GenericForeignKey()

    user = models.ForeignKey("auth.User")
    message = models.TextField(blank=True)
    response = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=1, choices=STATE_CHOICES,
                             default=PENDING)
