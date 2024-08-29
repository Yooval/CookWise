"""
Test custom Django management commands.
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2OpError

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')# this patch is for mocking the check the status of the database. we are simulating the response(can return an exepetion or a value).
class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, patched_check):#patched chek os the response
        """Test waiting for database if database ready."""
        patched_check.return_value = True # get the response

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default']) # insures that mocking patch called with right parameters.