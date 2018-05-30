# Generated by Django 2.0.5 on 2018-05-18 21:32

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtailstreamforms.conf
import wagtailstreamforms.fields
import wagtailstreamforms.streamfield


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(allow_unicode=True, help_text='Used to identify the form in template tags', max_length=255, unique=True, verbose_name='Slug')),
                ('template_name', models.CharField(choices=wagtailstreamforms.conf.get_setting('FORM_TEMPLATES'), max_length=255, verbose_name='Template')),
                ('fields', wagtailstreamforms.streamfield.FormFieldsStreamField((('singleline', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('help_text', wagtail.core.blocks.CharBlock(required=False)), ('required', wagtail.core.blocks.BooleanBlock(required=False)), ('default_value', wagtail.core.blocks.CharBlock(required=False))), icon='placeholder')), ('multiline', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('help_text', wagtail.core.blocks.CharBlock(required=False)), ('required', wagtail.core.blocks.BooleanBlock(required=False)), ('default_value', wagtail.core.blocks.CharBlock(required=False))), icon='placeholder')), ('date', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('help_text', wagtail.core.blocks.CharBlock(required=False)), ('required', wagtail.core.blocks.BooleanBlock(required=False)), ('default_value', wagtail.core.blocks.CharBlock(required=False))), icon='date')), ('datetime', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('help_text', wagtail.core.blocks.CharBlock(required=False)), ('required', wagtail.core.blocks.BooleanBlock(required=False)), ('default_value', wagtail.core.blocks.CharBlock(required=False))), icon='time')), ('email', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('help_text', wagtail.core.blocks.CharBlock(required=False)), ('required', wagtail.core.blocks.BooleanBlock(required=False)), ('default_value', wagtail.core.blocks.CharBlock(required=False))), icon='mail')), ('url', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('help_text', wagtail.core.blocks.CharBlock(required=False)), ('required', wagtail.core.blocks.BooleanBlock(required=False)), ('default_value', wagtail.core.blocks.CharBlock(required=False))), icon='link')), ('number', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('help_text', wagtail.core.blocks.CharBlock(required=False)), ('required', wagtail.core.blocks.BooleanBlock(required=False)), ('default_value', wagtail.core.blocks.CharBlock(required=False))), icon='placeholder')), ('dropdown', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('help_text', wagtail.core.blocks.CharBlock(required=False)), ('required', wagtail.core.blocks.BooleanBlock(required=False)), ('empty_label', wagtail.core.blocks.CharBlock(required=False)), ('choices', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Option')))), icon='list-ul')), ('multiselect', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('help_text', wagtail.core.blocks.CharBlock(required=False)), ('required', wagtail.core.blocks.BooleanBlock(required=False)), ('choices', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Option')))), icon='list-ul')), ('radio', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('help_text', wagtail.core.blocks.CharBlock(required=False)), ('required', wagtail.core.blocks.BooleanBlock(required=False)), ('choices', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Option')))), icon='radio-empty')), ('checkboxes', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('help_text', wagtail.core.blocks.CharBlock(required=False)), ('required', wagtail.core.blocks.BooleanBlock(required=False)), ('choices', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Option')))), icon='tick-inverse')), ('checkbox', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('help_text', wagtail.core.blocks.CharBlock(required=False)), ('required', wagtail.core.blocks.BooleanBlock(required=False))), icon='tick-inverse')), ('hidden', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('help_text', wagtail.core.blocks.CharBlock(required=False)), ('required', wagtail.core.blocks.BooleanBlock(required=False)), ('default_value', wagtail.core.blocks.CharBlock(required=False))), icon='no-view')), ('singlefile', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('help_text', wagtail.core.blocks.CharBlock(required=False)), ('required', wagtail.core.blocks.BooleanBlock(required=False))), icon='doc-full-inverse')), ('multifile', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('help_text', wagtail.core.blocks.CharBlock(required=False)), ('required', wagtail.core.blocks.BooleanBlock(required=False))), icon='doc-full-inverse'))), verbose_name='Fields')),
                ('submit_button_text', models.CharField(default='Submit', max_length=100, verbose_name='Submit button text')),
                ('success_message', models.CharField(blank=True, help_text='An optional success message to show when the form has been successfully submitted', max_length=255, verbose_name='Success message')),
                ('error_message', models.CharField(blank=True, help_text='An optional error message to show when the form has validation errors', max_length=255, verbose_name='Error message')),
                ('process_form_submission_hooks', wagtailstreamforms.fields.HookSelectField(blank=True, verbose_name='Submission hooks')),
                ('post_redirect_page', models.ForeignKey(blank=True, help_text='The page to redirect to after a successful submission', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Post redirect page')),
            ],
            options={
                'verbose_name': 'Form',
                'verbose_name_plural': 'Forms',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='FormSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_data', models.TextField(verbose_name='Form data')),
                ('submit_time', models.DateTimeField(auto_now_add=True, verbose_name='Submit time')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailstreamforms.Form', verbose_name='Form')),
            ],
            options={
                'verbose_name': 'Form submission',
                'ordering': ['-submit_time'],
            },
        ),
        migrations.CreateModel(
            name='FormSubmissionFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=255, verbose_name='Field')),
                ('file', models.FileField(upload_to='streamforms/', verbose_name='File')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='wagtailstreamforms.FormSubmission', verbose_name='Submission')),
            ],
            options={
                'verbose_name': 'Form submission file',
                'ordering': ['field', 'file'],
            },
        ),
    ]
