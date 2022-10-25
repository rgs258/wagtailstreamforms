# Generated by Django 4.0.8 on 2022-10-25 17:11

import cms.query_forms.blocks
import cms.query_forms.validators
import cms.utils.blocks
import data_dictionary.models
from django.db import migrations
import wagtail.blocks
import wagtail.blocks.static_block
import wagtailstreamforms.streamfield


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailstreamforms', '0002_form_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='fields',
            field=wagtailstreamforms.streamfield.FormFieldsStreamField([('singleline', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('help_text', wagtail.blocks.CharBlock(required=False)), ('required', wagtail.blocks.BooleanBlock(required=False)), ('default_value', wagtail.blocks.CharBlock(required=False))], icon='placeholder', label='Text field (single line)')), ('multiline', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('help_text', wagtail.blocks.CharBlock(required=False)), ('required', wagtail.blocks.BooleanBlock(required=False)), ('default_value', wagtail.blocks.CharBlock(required=False))], icon='placeholder', label='Text field (multi line)')), ('date', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('help_text', wagtail.blocks.CharBlock(required=False)), ('required', wagtail.blocks.BooleanBlock(required=False)), ('default_value', wagtail.blocks.CharBlock(required=False))], icon='date', label='Date field')), ('datetime', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('help_text', wagtail.blocks.CharBlock(required=False)), ('required', wagtail.blocks.BooleanBlock(required=False)), ('default_value', wagtail.blocks.CharBlock(required=False))], icon='time', label='DateTime field')), ('email', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('help_text', wagtail.blocks.CharBlock(required=False)), ('required', wagtail.blocks.BooleanBlock(required=False)), ('default_value', wagtail.blocks.CharBlock(required=False))], icon='mail', label='Email field')), ('url', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('help_text', wagtail.blocks.CharBlock(required=False)), ('required', wagtail.blocks.BooleanBlock(required=False)), ('default_value', wagtail.blocks.CharBlock(required=False))], icon='link', label='URL field')), ('number', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('help_text', wagtail.blocks.CharBlock(required=False)), ('required', wagtail.blocks.BooleanBlock(required=False)), ('default_value', wagtail.blocks.CharBlock(required=False))], icon='placeholder', label='Number field')), ('dropdown', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('help_text', wagtail.blocks.CharBlock(required=False)), ('required', wagtail.blocks.BooleanBlock(required=False)), ('empty_label', wagtail.blocks.CharBlock(required=False)), ('choices_source', wagtail.blocks.StreamBlock([('choices', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('value', wagtail.blocks.CharBlock(label='Option Value')), ('label', wagtail.blocks.CharBlock(label='Option Label')), ('selected', wagtail.blocks.BooleanBlock(help_text='Default this dropdown item to be selected. While you can mark multiple items selected, only the last one will be selected on the form. If no items are marked selected then the first, or the empty label, will be selected on the form.', required=False))]))), ('table_choices', cms.query_forms.blocks.TableChooserBlock(help_text='A Table from which variable will be used as choices. The Table choices are limited to those tables that exist within the Product selected on this Query Form and are not deleted. If the table becomes deleted then all variables within it will be automatically hidden from choices.'))], help_text='Choices from all sources are aggregated and sorted'))], icon='arrow-down-big', label='Dropdown field')), ('radio', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('help_text', wagtail.blocks.CharBlock(required=False)), ('required', wagtail.blocks.BooleanBlock(required=False)), ('choices', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('value', wagtail.blocks.CharBlock(label='Option Value')), ('label', wagtail.blocks.CharBlock(label='Option Label')), ('selected', wagtail.blocks.BooleanBlock(help_text='Default this radio button to be selected. While you can mark multiple radio buttons selected, only the last one will be selected on the form. If no radios are marked selected then the first will be selected on the form.', required=False)), ('help_modal', cms.query_forms.blocks.ModalSnippetChooserBlock(help_text="Additional information that will be shown in a modal. The radio item will become a link to show a modal and the ModalSnippet's link text and title will not be used.", required=False))])))], icon='radio-empty', label='Radio buttons')), ('checkboxes', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('help_text', wagtail.blocks.CharBlock(required=False)), ('required', wagtail.blocks.BooleanBlock(required=False)), ('required_min', wagtail.blocks.IntegerBlock(help_text='When required, the minimum number of boxes that may be checked, or -1 to disable this functionality', min_value=-1, required=False)), ('required_max', wagtail.blocks.IntegerBlock(help_text='When required, the maximum number of boxes that may be checked, or -1 to disable this functionality', min_value=-1, required=False)), ('layout', wagtail.blocks.ChoiceBlock(choices=[('default', 'Default'), ('horizontal', 'Horizontal')], label='Checkboxes Layout')), ('choices', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('value', wagtail.blocks.CharBlock(label='Option Value')), ('label', wagtail.blocks.CharBlock(label='Option Label')), ('selected', wagtail.blocks.BooleanBlock(required=False)), ('help_modal', cms.query_forms.blocks.ModalSnippetChooserBlock(help_text="Additional information that will be shown in a modal. The radio item will become a link to show a modal and the ModalSnippet's link text and title will not be used.", required=False))])))], icon='tick-inverse', label='Checkboxes')), ('checkbox', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('help_text', wagtail.blocks.CharBlock(required=False)), ('required', wagtail.blocks.BooleanBlock(required=False))], icon='tick-inverse', label='Checkbox field')), ('hidden', wagtail.blocks.StructBlock([('hidden_fields_block', wagtail.blocks.StreamBlock([('hidden_field', wagtail.blocks.StructBlock([('form_field_name', wagtail.blocks.CharBlock(help_text='Field name used as the key, in the payload, for the values entered by the user, when submitting the resulting Query to Query Manager.')), ('value', wagtail.blocks.CharBlock(help_text='The value associated with this hidden field. The user cannot change this value', required=True))]))]))], icon='placeholder', label='Hidden Fields')), ('singlefile', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('help_text', wagtail.blocks.CharBlock(required=False)), ('required', wagtail.blocks.BooleanBlock(required=False))], icon='doc-full-inverse', label='File field')), ('multifile', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('help_text', wagtail.blocks.CharBlock(required=False)), ('required', wagtail.blocks.BooleanBlock(required=False))], icon='doc-full-inverse', label='Files field')), ('date_range_step', wagtail.blocks.StructBlock([('form_field_name', wagtail.blocks.CharBlock(default='datevar', help_text='Field name used as the key, in the payload, for the values entered by the user, when submitting the resulting Query to Query Manager.')), ('label', wagtail.blocks.CharBlock()), ('date_range_granularity', wagtail.blocks.ChoiceBlock(choices=[('days', 'Days, YYYY-MM-DD'), ('months', 'Months, YYYY-MM'), ('quarters', 'Quarters, YYYY-MM'), ('years', 'Years, YYYY')], help_text='Applies to Date; ignored for Datetime which always requires Day granularity.', label='What is the date granularity?')), ('date_range_block', wagtail.blocks.StreamBlock([('date_variables', wagtail.blocks.StreamBlock([('date_variable_option_set', wagtail.blocks.StructBlock([('temporal_variable', cms.query_forms.blocks.VariableDateCacheChooserBlock(help_text='Date Cache object. This date variable will not be affected by the deleted state of the associated variable. However, if a the Variable Date Cache object itself is removed from Data Dictionary, then this date variable will be automatically hidden on the form.', label='Date Cache Object')), ('default_start_choice', wagtail.blocks.ChoiceBlock(choices=[('default_to_limit', 'Use Cache Default Date'), ('default_to_current', 'Use Today'), ('default_to_other', 'Use Supplied Date')], label='Which date should be used as the default start date?')), ('default_start', wagtail.blocks.DateBlock(help_text='Optionally override the default start date from the cache', label='Supplied Default Start Date', required=False)), ('default_end_choice', wagtail.blocks.ChoiceBlock(choices=[('default_to_limit', 'Use Cache Default Date'), ('default_to_current', 'Use Today'), ('default_to_other', 'Use Supplied Date')], label='Which date should be used as the default end date?')), ('default_end', wagtail.blocks.DateBlock(help_text='Optionally override the default end date from the cache', label='Supplied Default End Date', required=False)), ('max_range_seconds', wagtail.blocks.IntegerBlock(help_text='Optionally, a number of seconds that is the maximum range the user may select. Blank and values less than 1 are interpreted as an unbound range. The max possible constrained range is ~68 years.', label='Max Selectable Range in Seconds', required=False))])), ('arbitrary_variable_option_set', wagtail.blocks.StructBlock([('variable_code', wagtail.blocks.CharBlock(help_text='The code for an arbitrary date variable.', label='Date Variable Code', required=True)), ('label', wagtail.blocks.CharBlock(help_text='Optional, the label for an arbitrary date variable. If left empty, the Date Variable Code will be used.', label='Date Variable Label', required=False)), ('min_temporal', wagtail.blocks.DateBlock(label='Minimum Date', required=True)), ('max_temporal', wagtail.blocks.DateBlock(label='Maximum Date', required=True)), ('default_start_choice', wagtail.blocks.ChoiceBlock(choices=[('default_to_current', 'Use Today'), ('default_to_other', 'Use Supplied Date')], label='Which date should be used as the default start date?')), ('default_start', wagtail.blocks.DateBlock(help_text='Optionally supply the default start date', label='Supplied Default Start Date', required=False)), ('default_end_choice', wagtail.blocks.ChoiceBlock(choices=[('default_to_current', 'Use Today'), ('default_to_other', 'Use Supplied Date')], label='Which date should be used as the default end date?')), ('default_end', wagtail.blocks.DateBlock(help_text='Optionally supply the default end date', label='Supplied Default End Date', required=False)), ('max_range_seconds', wagtail.blocks.IntegerBlock(help_text='Optionally, a number of seconds that is the maximum range the user may select. Blank and values less than 1 are interpreted as an unbound range. The max possible constrained range is ~68 years.', label='Max Selectable Range in Seconds', required=False))]))])), ('datetime_variables', wagtail.blocks.StreamBlock([('date_variable_option_set', wagtail.blocks.StructBlock([('temporal_variable', cms.query_forms.blocks.VariableDateTimeCacheChooserBlock(help_text='Date/time Cache object. This date/time variable will not be affected by the deleted state of the associated variable. However, if a the Variable Date/time Cache object itself is removed from Data Dictionary, then this date/time variable will be automatically hidden on the form.', label='Date/time Cache Object')), ('default_start_choice', wagtail.blocks.ChoiceBlock(choices=[('default_to_limit', 'Use Cache Default Date/time'), ('default_to_current', 'Use Now'), ('default_to_other', 'Use Supplied Date/time')], label='Which date/time should be used as the default start date/time?')), ('default_start', wagtail.blocks.DateTimeBlock(help_text='Optionally override the default start date/time from the cache', label='Supplied Default Start Date/time', required=False)), ('default_end_choice', wagtail.blocks.ChoiceBlock(choices=[('default_to_limit', 'Use Cache Default Date/time'), ('default_to_current', 'Use Now'), ('default_to_other', 'Use Supplied Date/time')], label='Which date/time should be used as the default end date/time?')), ('default_end', wagtail.blocks.DateTimeBlock(help_text='Optionally override the default end date/time from the cache', label='Supplied Default End Date/time', required=False)), ('max_range_seconds', wagtail.blocks.IntegerBlock(help_text='Optionally, a number of seconds that is the maximum range the user may select. Blank and values less than 1 are interpreted as an unbound range. The max possible constrained range is ~68 years.', label='Max Selectable Range in Seconds', required=False))])), ('arbitrary_variable_option_set', wagtail.blocks.StructBlock([('variable_code', wagtail.blocks.CharBlock(help_text='The code for an arbitrary date/time variable.', label='Date/time Variable Code', required=True)), ('label', wagtail.blocks.CharBlock(help_text='Optional, the label for an arbitrary date variable. If left empty, the Date/time Variable Code will be used.', label='Date/time Variable Label', required=False)), ('min_temporal', wagtail.blocks.DateTimeBlock(label='Minimum Date/time', required=True)), ('max_temporal', wagtail.blocks.DateTimeBlock(label='Maximum Date/time', required=True)), ('default_start_choice', wagtail.blocks.ChoiceBlock(choices=[('default_to_current', 'Use Now'), ('default_to_other', 'Use Supplied Date/time')], label='Which date/time should be used as the default start date/time?')), ('default_start', wagtail.blocks.DateTimeBlock(help_text='Optionally supply the default start date/time', label='Supplied Default Start Date/time', required=False)), ('default_end_choice', wagtail.blocks.ChoiceBlock(choices=[('default_to_current', 'Use Now'), ('default_to_other', 'Use Supplied Date/time')], label='Which date/time should be used as the default end date/time?')), ('default_end', wagtail.blocks.DateTimeBlock(help_text='Optionally supply the default end date/time', label='Supplied Default End Date/time', required=False)), ('max_range_seconds', wagtail.blocks.IntegerBlock(help_text='Optionally, a number of seconds that is the maximum range the user may select. Blank and values less than 1 are interpreted as an unbound range. The max possible constrained range is ~68 years.', label='Max Selectable Range in Seconds', required=False))]))]))], max_num=1, min_num=1, required=True))], icon='placeholder', label='Date Range Step')), ('code_entry_step', wagtail.blocks.StructBlock([('code_entry_block', wagtail.blocks.StreamBlock([('supported_code_types', wagtail.blocks.StructBlock([('code_types_header', wagtail.blocks.CharBlock(default='What format are your company codes?', help_text='This is the text that will be shown at the top of this step.', required=False)), ('query_var_name', wagtail.blocks.CharBlock(default='qvar', help_text='The name of the main query variable to pass to SAS.', required=True)), ('code_type_options', wagtail.blocks.StreamBlock([('code_type', wagtail.blocks.StructBlock([('code_type_name', wagtail.blocks.CharBlock(help_text='The value that will be passed to SAS if this option is chosen as the main query variable.', required=True)), ('code_type_display_name', wagtail.blocks.CharBlock(help_text="The text to display for this option in the set of radio buttons. If not set, the code type's name will be used.", required=False)), ('code_attribute_type', cms.utils.blocks.SnippetChooserNoEditBlock(data_dictionary.models.AttributeType, help_text='The common attribute type associated with this code. This field is optional, but must be selected for this code type to participate in attribute search.', required=False)), ('validation', wagtail.blocks.StreamBlock([('validate_words_and_spaces', wagtail.blocks.static_block.StaticBlock(admin_text='Words may consist of characters a-z, A-Z, 0-9, andunderscore', error_message='Please enter codes that are words (a-z, A-Z, 0-9, underscore) separated by spaces.', label='Allow words and spaces', regex_manual='^\\w+( +\\w+)*$', regex_upload='^\\w+$')), ('validate_text_and_spaces', wagtail.blocks.static_block.StaticBlock(admin_text='Text may consist of characters a-z and A-Z', error_message='Please enter codes that are text (a-z, A-Z) separated by spaces.', label='Allow text and spaces', regex_manual='^[a-zA-Z]+( +[a-zA-Z]+)*$', regex_upload='^[a-zA-Z]+$')), ('validate_numbers_and_spaces', wagtail.blocks.static_block.StaticBlock(admin_text='Numbers are 0-9', error_message='Please enter codes that are numbers (0-9) separated by spaces.', label='Allow numbers and spaces', regex_manual='^[0-9]+( +[0-9]+)*$', regex_upload='^[0-9]+$')), ('validate_tickers_and_spaces', wagtail.blocks.static_block.StaticBlock(admin_text="Tickers, as currently implemented, may consist of characters a-z, A-Z, 0-9, ., :, and \\. This definition of 'Ticker' may change at a later time; if you require an immutable definition of 'Ticker', please consider using a custom regular expression instead.", error_message='Please enter codes that contains valid ticker characters (a-z, A-Z, 0-9, ., :, and \\) separated by spaces.', label='Allow tickers and spaces', regex_manual='^[0-9a-zA-Z:\\\\\\.]+( +[0-9a-zA-Z:\\\\\\.]+)*$', regex_upload='^[0-9a-zA-Z:\\\\\\.]+$')), ('validate_custom_regex', wagtail.blocks.StructBlock([('manual_entry_regex', wagtail.blocks.CharBlock(default='^\\w+( +\\w+)*$', help_text="A valid <a href='https://docs.python.org/3/library/re.html#regular-expression-syntax'>regular expression</a> with which to validate manually entered codes. The default, <code>^\\w+( +\\w+)*$</code>, will allow only words and spaces. To allow only digits and spaces, try <code>^\\d+( +\\d+)*$</code>.", required=True, validators=(cms.query_forms.validators.RegexStringValidator(),))), ('file_upload_regex', wagtail.blocks.CharBlock(default='^\\w+$', help_text="A valid <a href='https://docs.python.org/3/library/re.html#regular-expression-syntax'>regular expression</a> with which to validate codes within uploaded files. The default, <code>^\\w+$</code>, will allow only zero or one words per line. To allow only zero or one integers, try <code>^\\d+$</code>.", required=True, validators=(cms.query_forms.validators.RegexStringValidator(),))), ('custom_regex_error_message', wagtail.blocks.CharBlock(default='Please enter codes that are words (a-z, A-Z, 0-9, and underscore) separated by spaces.', help_text='The message to display to the user when their input has violated the custom regex.', required=False))], label='Supply a custom regular expression.'))], help_text='Optionally, impose validation on the entered or uploaded codes.', max_num=1, min_num=0, required=False))]))], required=True))])), ('supported_code_entry_methods', wagtail.blocks.StructBlock([('entry_methods_header', wagtail.blocks.CharBlock(default='Select an option for entering your company codes:', help_text='This is the text that will be shown above the set of radio boxes where the user chooses their code input method.', required=False)), ('allow_manual_entry', wagtail.blocks.BooleanBlock(default=True, help_text='Check this to create a box for manual code entry.', required=False)), ('manual_entry_label', wagtail.blocks.CharBlock(default='Company Codes', help_text='The label the field for screen readers and to be used when referring to the field in error messaging. This value will also be used as the placeholder text, visible in the manual code entry box until the user starts typing .', required=False)), ('manual_entry_caption', wagtail.blocks.CharBlock(default='Please enter company codes separated by a space.', help_text='The caption to put under the manual code entry box.', required=False)), ('code_examples', wagtail.blocks.RichTextBlock(default='Example: IBM MSFT AAPL', features=['bold', 'italic', 'ol', 'ul', 'link'], help_text='Text to use as an example of manual code entry. Should ', required=False)), ('code_lookup_by_form_product', wagtail.blocks.BooleanBlock(default=True, help_text='If a code lookup link should be rendered for the product selected for with this form.', required=False)), ('additional_code_lookups', wagtail.blocks.StreamBlock([('code_lookup_table', cms.query_forms.blocks.TableChooserBlock(help_text='The Table from which a code lookup link should be created. The Table choices are limited to those tables that exist within the Product selected on this Query Form and are not deleted. If the table becomes deleted, this code lookup will will be automatically hidden on the form.', required=False)), ('code_lookup_product', cms.utils.blocks.SnippetChooserNoEditBlock(data_dictionary.models.Product, help_text='An arbitrary Product from which a code lookup link should be created. This is almost always NOT what you want; please see and consider the other options first. If the product becomes deleted, this code lookup will will be automatically hidden on the form.', required=False)), ('code_lookup_vendor', cms.query_forms.blocks.VendorChooserBlock(help_text="An arbitrary Vendor from which a code lookup link should be created. This is almost always NOT what you want; please see and consider the other options first. Only vendors listed publicly on the Vendor List and having a Legacy vendor Code may be selected. If the Vendor becomes unavailable to show on the Vendor List or looses it's Legacy Vendor Code, then this code lookup will will be automatically hidden on the form.", required=False))], block_counts={'code_lookup_product': {'max_num': 100, 'min_num': 0}, 'code_lookup_table': {'max_num': 100, 'min_num': 0}, 'code_lookup_vendor': {'max_num': 100, 'min_num': 0}}, required=False)), ('allow_file_upload', wagtail.blocks.BooleanBlock(default=True, help_text='Check this to create an interface for file upload.', required=False)), ('file_upload_allowed_extensions', wagtail.blocks.RegexBlock(default='txt csv', help_text='File type extensions, files of which will be allowed for upload. Enter a space separated list, or blank to allow any file type.', regex='^\\w+( +\\w+)*$', required=False)), ('file_upload_label', wagtail.blocks.CharBlock(default='Company Codes Upload File', help_text='The label the field for screen readers and to be used when referring to the field in error messaging. This value will also be used as the placeholder text, visible in the browse for file  entry box until the user has selected a file.', required=False)), ('file_upload_caption', wagtail.blocks.CharBlock(default='Upload a plain text file (.txt), having one code per line.', help_text='The caption to put under the file upload box.', required=False)), ('allow_search_entire_database', wagtail.blocks.BooleanBlock(default=True, help_text='Check this to allow users to search the entire database.', required=False)), ('search_entire_database_caption', wagtail.blocks.CharBlock(default='This method allows you to search the entire database of records. Please be aware that this method can take a very long time to run because it is dependent upon the size of the database.', help_text="The caption to put under the 'Search Entire Database' radio button.", required=False))], required=True))]))], label='Code Entry Step')), ('output_options_step', wagtail.blocks.StructBlock([('output_options_block', wagtail.blocks.StreamBlock([('descriptive_text', wagtail.blocks.CharBlock(default='Select the desired format of the output file. For large data requests, select a compression type to expedite downloads. If you enter your email address, you will receive an email that contains a URL to the output file when the data request is finished processing.', help_text='This is the text that will be shown above the output options.', required=True)), ('output_formats', wagtail.blocks.StructBlock([('fixed_width_text', wagtail.blocks.BooleanBlock(default=True, help_text='Fixed-width text (*.txt)', required=False)), ('comma_delimited_text', wagtail.blocks.BooleanBlock(default=True, help_text='Comma-delimited text (*.csv)', required=False)), ('excel_spreadsheet', wagtail.blocks.BooleanBlock(default=True, help_text='Excel spreadsheet (*.xlsx)', required=False)), ('tab_delimited_text', wagtail.blocks.BooleanBlock(default=True, help_text='Tab-delimited text (*.txt)', required=False)), ('html_table', wagtail.blocks.BooleanBlock(default=True, help_text='HTML table (*.htm)', required=False)), ('sas_windows_32_dataset', wagtail.blocks.BooleanBlock(default=True, help_text='SAS Windows_32 dataset (*.sas7bdat)', required=False)), ('sas_windows_64_dataset', wagtail.blocks.BooleanBlock(default=True, help_text='SAS Windows_64 dataset (*.sas7bdat)', required=False)), ('sas_solaris_64_dataset', wagtail.blocks.BooleanBlock(default=True, help_text='SAS Solaris_64 dataset (*.sas7bdat)', required=False)), ('dbase_file', wagtail.blocks.BooleanBlock(default=True, help_text='dBase file (*.dbf)', required=False)), ('stata_file', wagtail.blocks.BooleanBlock(default=True, help_text='STATA file (*.dta)', required=False)), ('spss_file', wagtail.blocks.BooleanBlock(default=True, help_text='SPSS file (*.sav)', required=False))], help_text='Allows the creator to choose which output formats will be available for users ofthis query page.')), ('output_compression', wagtail.blocks.StructBlock([('no_compression', wagtail.blocks.BooleanBlock(default=True, help_text='No compression', required=False)), ('zip', wagtail.blocks.BooleanBlock(default=True, help_text='zip (*.zip)', required=False)), ('gzip', wagtail.blocks.BooleanBlock(default=True, help_text='gzip (*.gz)', required=False))], help_text='Allows the creator to choose which output compression options will be available for users of this query page.')), ('date_formats', wagtail.blocks.StructBlock([('YYMMDDn8', wagtail.blocks.BooleanBlock(default=True, help_text='YYMMDDn8. (e.g. 19840725)', required=False)), ('DATE9', wagtail.blocks.BooleanBlock(default=True, help_text='DATE9. (e.g. 25JUL1984)', required=False)), ('DDMMYY6', wagtail.blocks.BooleanBlock(default=True, help_text='DDMMYY6. (e.g. 250784)', required=False)), ('MMDDYY10', wagtail.blocks.BooleanBlock(default=True, help_text='MMDDYY10. (e.g. 07/25/1984)', required=False)), ('DDMMYY10', wagtail.blocks.BooleanBlock(default=True, help_text='DDMMYY10. (e.g. 25/07/1984)', required=False)), ('YYMMDDs10', wagtail.blocks.BooleanBlock(default=True, help_text='YYMMDDs10. (e.g. 1984/07/25)', required=False))], help_text='Allows the creator to choose which date formats can be selected by users of this query page.'))], block_counts={'date_formats': {'max_num': 1, 'min_num': 0}, 'descriptive_text': {'max_num': 1, 'min_num': 1}, 'output_compression': {'max_num': 1, 'min_num': 0}, 'output_formats': {'max_num': 1, 'min_num': 0}}, max_num=4, min_num=2))], icon='placeholder', label='Output Options Step')), ('variable_picker', wagtail.blocks.StructBlock([('tabs', wagtail.blocks.StreamBlock([('tab', wagtail.blocks.StructBlock([('form_field_name', wagtail.blocks.CharBlock(default='var', help_text='Field name used as the key, in the payload, for the values entered by the user, when submitting the resulting Query to Query Manager.')), ('tab_source', wagtail.blocks.StreamBlock([('table_tab', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(help_text='Optional label of the Variable Picker tab, replaces replaces code/description of the Table from Data Dictionary', required=False)), ('table', cms.query_forms.blocks.TableChooserBlock(help_text='The Table from which this tab allows the selection of Variables. The Table choices are limited to those tables that exist within the Product selected on this Query Form and are not deleted. If the table becomes deleted this tab will be automatically hidden on the form.')), ('variable_inclusion', wagtail.blocks.ChoiceBlock(choices=[('inclusive', 'Inclusive: Show all Variables within the Table, except exclusions selected below'), ('selective', 'Selective: Show only the Variables with extended context below')], help_text='How variables are selected from tables.')), ('variable_order_first_sort', wagtail.blocks.ChoiceBlock(choices=[('form_position', 'Form Position: Order variables the same as they are ordered below'), ('dictionary_position', "Dictionary Position: Order variables according to their 'position' in the Data Dictionary"), ('code', 'Variable Code Position: Order variables lexicographically by their code')], help_text='How variables are ordered in the tab; this sort will be applied first and is required.')), ('variable_order_second_sort', wagtail.blocks.ChoiceBlock(choices=[('form_position', 'Form Position: Order variables the same as they are ordered below'), ('dictionary_position', "Dictionary Position: Order variables according to their 'position' in the Data Dictionary"), ('code', 'Variable Code Position: Order variables lexicographically by their code')], help_text='Optionally, a second sort to apply to variable ordering in the tab.', required=False)), ('variables', wagtail.blocks.StreamBlock([('extended_variable_context', wagtail.blocks.StructBlock([('variable', cms.query_forms.blocks.VariableChooserBlock(help_text='A Variable for which extended context is to be defined. Choices are limited to the Variables that exist within the Table selected for this Tab and are not deleted. If a variable becomes deleted, it will be automatically hidden on the tab.', label='Variable')), ('label', wagtail.blocks.CharBlock(help_text='Optional label, replaces code/description of the Variable from Data Dictionary', label='Label Override', required=False)), ('selection_state', wagtail.blocks.ChoiceBlock(choices=[('enabled', 'Enabled'), ('selected', 'Selected'), ('required', 'Required'), ('disabled', 'Disabled')], help_text='The state of the checkbox when the form page loads')), ('exclude_from_conditional', wagtail.blocks.BooleanBlock(default=False, help_text='If this variable is to be excluded from the conditional builder', required=False))])), ('excluded_variable', wagtail.blocks.StructBlock([('variable', cms.query_forms.blocks.VariableChooserBlock(help_text='This variable is to be excluded from the picker tab. Choices are limited to the Variables that exist within the Table selected for this Tab and are not deleted. The future deleted state of a variable will NOT influence variable exclusion rules.', label='Variable'))])), ('arbitrary_variable', wagtail.blocks.StructBlock([('variable_code', wagtail.blocks.CharBlock(help_text='The code for an arbitrary option in the Variable Picker', label='Variable Code')), ('label', wagtail.blocks.CharBlock(help_text='Optional Label to use in the picker, replaces the Variable Code above.', required=False)), ('selection_state', wagtail.blocks.ChoiceBlock(choices=[('enabled', 'Enabled'), ('selected', 'Selected'), ('required', 'Required'), ('disabled', 'Disabled')], help_text='The state of the checkbox when the form page loads')), ('variable_type', wagtail.blocks.ChoiceBlock(choices=[(1, 'Integer'), (2, 'Small Integer'), (3, 'Big Integer'), (4, 'Boolean'), (5, 'Decimal'), (6, 'Float'), (7, 'Date'), (8, 'Date Time'), (9, 'Time'), (10, 'Character Fixed'), (11, 'Character Varying'), (12, 'Text'), (13, 'UUID'), (14, 'Interval'), (15, 'JSON'), (16, 'Text Search Vector')], help_text='The type of this arbitrary option')), ('exclude_from_conditional', wagtail.blocks.BooleanBlock(default=False, help_text='If this variable is to be excluded from the conditional builder', required=False))]))], help_text='Optionally, choose variables for selective display, define additional context, and/or exclude variables. Additional variable context with duplicate/overlapping Variable chosen will produce unpredictable results. Variable exclusion supersedes all other settings.', required=False))])), ('arbitrary_tab', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(help_text='Required label of the Variable Picker arbitrary tab.')), ('variables', wagtail.blocks.StreamBlock([('arbitrary_variable', wagtail.blocks.StructBlock([('variable_code', wagtail.blocks.CharBlock(help_text='The code for an arbitrary option in the Variable Picker', label='Variable Code')), ('label', wagtail.blocks.CharBlock(help_text='Optional Label to use in the picker, replaces the Variable Code above.', required=False)), ('selection_state', wagtail.blocks.ChoiceBlock(choices=[('enabled', 'Enabled'), ('selected', 'Selected'), ('required', 'Required'), ('disabled', 'Disabled')], help_text='The state of the checkbox when the form page loads')), ('variable_type', wagtail.blocks.ChoiceBlock(choices=[(1, 'Integer'), (2, 'Small Integer'), (3, 'Big Integer'), (4, 'Boolean'), (5, 'Decimal'), (6, 'Float'), (7, 'Date'), (8, 'Date Time'), (9, 'Time'), (10, 'Character Fixed'), (11, 'Character Varying'), (12, 'Text'), (13, 'UUID'), (14, 'Interval'), (15, 'JSON'), (16, 'Text Search Vector')], help_text='The type of this arbitrary option')), ('exclude_from_conditional', wagtail.blocks.BooleanBlock(default=False, help_text='If this variable is to be excluded from the conditional builder', required=False))]))], help_text='Define arbitrary variables for this tab.', min_num=1, required=True))]))], help_text='Tabs should be build from Data Dictionary tables whenever possible.', max_num=1, min_num=1, required=True))], help_text="Each tab must define it's own Form Field Name, but multiple tabs may use the same Form Field Name."))], block_counts={'tab': {'max_num': 99, 'min_num': 1}}, help_text='Web Forms allow the selection of Variables. "Variables" are the column names of WRDS\' financial data tables. A Variable Picker will allow you, the creator of this Web Form, to select one or more Tables (constrained to the tables within the selected Product - a.k.k. Schema), and then define which Variables from those Tables that the user may select for extraction into the output.<hr>One or more tabs are presented in a Variable Picker. When two or more tabs are present, the "Search All" tab also appears.'))], label='Variable Picker')), ('conditional_query_builder', wagtail.blocks.StructBlock([('date_format', wagtail.blocks.ChoiceBlock(choices=[('YYYY-MM-DD', "ISO 8601, 'YYYY-MM-DD[ HH:mm:dd]'"), ('DDMMMYYYY', "SAS DATE9, 'ddMMMyyyy[:HH:mm:dd]'9")], help_text='Applies to Date and Datetime', label='What is the date format?'))], label='Conditional Query Builder')), ('recaptcha', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('help_text', wagtail.blocks.CharBlock(required=False))], icon='success', label='ReCAPTCHA field')), ('time', wagtail.blocks.StructBlock([('form_field_name', wagtail.blocks.CharBlock(help_text='Field name used as the key, in the payload, for the values entered by the user, when submitting the resulting Query to Query Manager.<br><br>Within time field, this key will be entered into the payload three times, one each suffixed by _hh, _mm, and _ss, and will include the hours, minutes, and seconds, respectively, of the time selected by the user.')), ('label', wagtail.blocks.CharBlock()), ('help_text', wagtail.blocks.CharBlock(required=False)), ('required', wagtail.blocks.BooleanBlock(required=False)), ('default_value', wagtail.blocks.TimeBlock(format='%H:%M:%S', required=False))], icon='time', label='Time field'))], use_json_field=True, verbose_name='Fields'),
        ),
    ]
