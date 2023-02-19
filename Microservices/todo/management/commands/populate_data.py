import json
import sys
import logging
from dateutil import parser
from django.core.management.base import BaseCommand
from todo.models import TodoItem
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Populating TodoItem data obtained in JSON from Monolith."

    def handle(self, *args, **options):
        for line in sys.stdin:
            data = json.loads(line)

            # Populating TodoItem Model
            if data["model"] == "TodoItem":
                item= TodoItem(
                    id=data["id"],
                    content=data["content"],
                    created=parser.parse(data["time_created"]),
                    updated=parser.parse(data["last_updated"]) 
                )
                item.save()
                logger.debug("TodoItem populated:{}".format(item.id))