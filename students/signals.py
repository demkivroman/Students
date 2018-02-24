from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import logging

from .models import Students

@receiver(post_delete, sender=Students)
def log_student_deleted_event(sender, **kwargs):
    """ Writes information about deleted student into log file """

    logger = logging.getLogger(__name__)

    student = kwargs['instance']
    logger.info("Student deleted: %s %s (ID: %d)", student.first_name, student.last_name, student.id)
   

