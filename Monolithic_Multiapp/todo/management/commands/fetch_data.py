import json
import sys
from django.core.management.base import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder

from todo.models import TodoItem
class Command(BaseCommand):
    help = "Extracting Todoitem data to JSON format"

    def handle(self, *args, **options):
        # Get User Data from User Model in monolith        
        list_microservice_data = TodoItem.objects.all()
        for list_data in list_microservice_data:
            data = {
                "model": "TodoItem",
                "id": list_data.id,
                "content": list_data.content,
                "time_created": list_data.created,
                "last_updated": list_data.updated,
            }
            # Dumping Data into JSON Format
            json.dump(data, sys.stdout, cls=DjangoJSONEncoder)
            sys.stdout.write("\n")