from django.core.management.base import BaseCommand, CommandError
import inventory.models
import core.models
import change_management.models


class Command(BaseCommand):
    help = "Set up the Database with initial data"

    def handle(self, *args, **options):

        cistatus = ['Active', 'Setup', 'Deleted', 'Decommissioning',]
        citype = ['NETW', 'SERV', 'OS', 'MDLW', 'MDLSINST', 'APP', 'BC',]
        vendors = [
            {'name': 'Dell', 'contact_email': 'dell@example.com', 'contact_phone': '+3611234567'},
            {'name': 'Cisco', 'contact_email': 'cisco@example.com', 'contact_phone': '+3611234567'},
            {'name': 'HP', 'contact_email': 'hp@example.com', 'contact_phone': '+3611234567'},
        ]
        companies = [
            {'name': 'Example Company', 'contact_name': 'Someone', 'contact_phone': '+3611234567'},
            {'name': 'Corporation Great', 'contact_name': 'Someone', 'contact_phone': '+3611234567'},
            {'name': 'IT sollutions Ltd.', 'contact_name': 'Someone', 'contact_phone': '+3611234567'},
            {'name': 'Big Datacollector', 'contact_name': 'Someone', 'contact_phone': '+3611234567'},
        ]

        task_status = ['Planning', 'Initial', 'Execution', 'Closed']
        change_state = ['Planning', 'Implementation', 'Done']
        closure = ['Successful', 'Failed', 'Successful with issues']

        tech_groups = ['Server Engineering', 'Network Engineering', 'Application Engineering', 'Service Management',
                       'Middleware Engineering', 'Sysadmins', 'Network Admins', 'Application Admins']

        management_groups = ['Special Management', 'Corporate Management', 'Spy Management', 'Something Management']

        users = [
            {'username': 'user1', 'first_name': 'Jakab', 'last_name': 'Gipsz', 'email': 'gipsz.jakab@example.com'},
            {'username': 'user2', 'first_name': 'Max', 'last_name': 'Power', 'email': 'power.max@example.com'},
            {'username': 'user3', 'first_name': 'Homer', 'last_name': 'Simpson', 'email': 'simpson.homer@example.com'},
            {'username': 'user4', 'first_name': 'Eric', 'last_name': 'Cartman', 'email': 'cartman.eric@example.com'},
            {'username': 'user5', 'first_name': 'Sherlock', 'last_name': 'Holmes', 'email': 'sherlock@example.com'},

        ]

        managers = [
            {'username': 'manager1', 'first_name': 'Mortimer', 'last_name': 'Duke', 'email': 'morty.duke@example.com'},
            {'username': 'manager2', 'first_name': 'Lando', 'last_name': 'Calrissian', 'email': 'lando@cloudcity.com'},
            {'username': 'manager3', 'first_name': 'James', 'last_name': 'T. Kirk',
             'email': 'james.t.kirk@enterprise.com'},
        ]

        for item in cistatus:
            inventory.models.CiStatus.objects.get_or_create(name=item)

        for item in citype:
            inventory.models.CiType.objects.get_or_create(name=item)

        for item in vendors:
            inventory.models.Vendors.objects.get_or_create(**item)

        for item in companies:
            inventory.models.Companies.objects.get_or_create(**item)

        for item in task_status:
            change_management.models.TaskStatus.objects.get_or_create(name=item)

        for item in change_state:
            change_management.models.ChangeState.objects.get_or_create(name=item)

        for item in closure:
            change_management.models.ClosureCode.objects.get_or_create(name=item)

        for item in tech_groups:
            core.models.TechnicalGroups.objects.get_or_create(name=item)

        for item in management_groups:
            core.models.ManagementGroups.objects.get_or_create(name=item)

        for item in users:
            core.models.UserProfile.objects.get_or_create(password='qwe12345', **item)

        for item in managers:
            core.models.ManagerProfile.objects.get_or_create(password='qwe12345', **item)
