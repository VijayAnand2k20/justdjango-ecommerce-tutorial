import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Renames Django Project"

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The new Django project name')

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        # Logic to rename the project:
        files_to_rename = [
            'ecommerce/settings/base.py',
            'ecommerce/wsgi.py',
            'manage.py'
        ]
        folder_to_rename = 'ecommerce'

        for file in files_to_rename:
            with open(file,'r') as fileObj:
                fileData = fileObj.read()
            
            fileData = fileData.replace('ecommerce', new_project_name)
            with open(file,'w') as fileObj:
                fileObj.write(fileData)
        
        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS('Project has been renamed to %s successfully.' % new_project_name))