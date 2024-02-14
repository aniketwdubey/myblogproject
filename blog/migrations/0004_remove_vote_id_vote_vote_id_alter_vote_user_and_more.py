# Generated by Django 4.2.2 on 2024-02-14 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_rename_voter_vote_user_alter_vote_unique_together_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vote",
            name="id",
        ),
        migrations.AddField(
            model_name="vote",
            name="vote_id",
            field=models.AutoField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="vote",
            name="user",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="vote",
            name="vote_type",
            field=models.CharField(
                choices=[("upvote", "Upvote"), ("downvote", "Downvote")], max_length=400
            ),
        ),
    ]