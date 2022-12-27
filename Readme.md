# Installation
## Install the django-package
* From pypi

		pip install django-introspectmodels

* Or from github

		pip install git+https://github.com/jbarreau/Forest-test/

* Or from sources

		pip install setuptools>=40.8.0
		git clone https://github.com/jbarreau/Forest-test/
		python3 setup.py sdist
		#in your project environement :
		pip install dist/django-introspectmodels-0.1.tar.gz

## Add the package to your project
In your project settings.py, add  "introspectmodels" to your INSTALLED_APPS setting like this:

	INSTALLED_APPS = [
		...
		'introspectmodels',
	]

# Usage
The '.forestadmin-schema.json' is generated at server startup ; but you can recreate it  using :

		python manage.py introspectmodels --output-file .forestadmin-schema.json
Without the '--output-file' parameter, it will print the file in stdout

# Output file format
An exemple of output json file:

	{
		"apps": [  # list of apps
			{
				"app_name": "music",  # name of the app
				"models": [  # models of the app
					{
						"model_name": "Band",  # name of the model
						"fields": [
							{
								"field_name": "name",  # name
								"field_type": "CharField",  # django field type
								"is_nullable": false,  # can be null
								"is_relation": false,  # is a relation
								"db_type": "varchar(60)",  # sql type
								"unique_constraint": false,  # unicity contrstraint on the field
								"is_primary_key": false,  # primary key
								"verbose_name": "name",  # verbose name
								"related_model": null  # if it is a relation, target relation model
							},
							{
								"field_name": "id",
								"model_type": "BigAutoField",
								"is_nullable": false,
								"is_relation": false,
								"db_type": "integer",
								"unique_constraint": true,
								"is_primary_key": true,
								"verbose_name": "ID",
								"related_model": null
							},
							{
								"field_name": "album",
								"field_type": "ManyToOneRel",
								"is_nullable": true,
								"is_relation": true,
								"db_type": "bigint",
								"related_model": "Album",  # target of the relation
								"unique_constraint": null,
								"is_primary_key": null,
								"verbose_name": null
							},
							{
								"field_name": "retired",
								"field_type": "BooleanField",
								"is_nullable": false,
								"is_relation": false,
								"db_type": "bool",
								"unique_constraint": false,
								"is_primary_key": false,
								"verbose_name": "retired",
								"related_model": null
							},
							{
								"field_name": "artists",
								"field_type": "ManyToManyField",
								"is_nullable": false,
								"is_relation": true,
								"db_type": null,
								"related_model": "Artist",
								"unique_constraint": null,
								"is_primary_key": null,
								"verbose_name": null
							}
						]
					}
				]
			}
		]
	}

# launch test for 'test_project'
Use the the command `./launch_test.sh` it will :
- remove virtual env (test_project/venv) if exists
- build the package
- make a new venv from scratch
- install packages (requirements.txt)
- launch tests with coverage (generate coverage.xml file)
- launch flake8 linter (generate flake8.txt file)


# Limitations / what to do for next releases
- implement include/exclude models/apps in settings.py. To have a file that describe just that we want
- make the introspect package work with multiple databases projects for the db field introspection
- package a wheel file
- improve compatibility with older versions of python and django
- implement more tests (never enough)

## and further
- auto create serializers and viewsets for django-rest-framework
- generate a diagram of the introspected models

# Other
## Test Project explainations
A simple music library with limited features that can provides most of the classic fields type and relations.\
Some relations, abstract class, ... are useless for this dummy app. The only pupose of them is to test the comportement of introspect model package.
