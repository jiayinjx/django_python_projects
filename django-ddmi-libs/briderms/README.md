- Run the application: `python manage.py runserver 8081`

- Run migrations: `python manage.py migrate`

- Create app: `rulestore`
  - `python manage.py startapp rulestore`

- Auto-generate the models from the existing database via `inspectdb`
  - `python manage.py inspectdb` (to stdout)
  - `python manage.py inspectdb > models.py` (save as a file in the current directory)
- other options for `inspectdb`
  - `inspectdb` command by default without any argument, outputs all the tables from the database.
  - for introspect particular table(s), pass table names as an argument separated by space after the command.
    - `python manage.py inspectdb table1name table2name`

- Notice: `inspectdb` cannot recognize foreign key constraints so these have to be defined manually.

- Next, synchronize the database:
  - `python manage.py syncdb` and answer "yes" to the prompt to create a superuser.


- Start the development web server, port number is optional
  - `python manage.py runserver <port>`