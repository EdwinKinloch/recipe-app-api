"""
Unit Test for testing the wait_for_db code
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, patch_check):
        """Test waiting for database if database ready."""
        patch_check.return_value = True
        call_command('wait_for_db')
