# Generated by Django 3.2.12 on 2023-05-16 10:08

from django.db import migrations
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pgpubsub', '0003_notification_db_version'),
    ]

    operations = [
        pgtrigger.migrations.AddTrigger(
            model_name='notification',
            trigger=pgtrigger.compiler.Trigger(name='pgpubsub_notification_set_db_version', sql=pgtrigger.compiler.UpsertTriggerSql(func="\n                    NEW.db_version := (\n                        SELECT max(id)\n                        FROM django_migrations\n                        WHERE app = ((NEW.payload #>> '{}')::jsonb ->> 'app')\n                    );\n                    RETURN NEW;\n                ", hash='95c688aa02a728bc3c8d7b94fc6dfbdf4a79be8b', operation='INSERT', pgid='pgtrigger_pgpubsub_notification_set_db_version_ac4cd', table='pgpubsub_notification', when='BEFORE')),
        ),
    ]
