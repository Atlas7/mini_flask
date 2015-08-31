# Intro

This project is taken from the [Flaskr Tutorial](http://flask.pocoo.org/docs/0.10/tutorial/) - create a micro blogging system.

Assumptions:

- this is a sandpit "playaround" exercise.
- support only one user `admin` (with password embedded within the code itself!).
- user is trusted. i.e. this blog is not guarded against SQL Injection, etc.
- this is a sandpit "playaround" exercise - the blog is not built for production. It merely inspires improvement and learning opportunities.

# Run the Flaskr Micro Blog!

Follow these instructions to get the blog up and running.

## Create Sqlite3 database

(One-off) Create a database at the `/tmp` directory. Run this:

```
sqlite3 /tmp/flaskr.db < schema.sql
```

Note: restarting the virtual machine will effectively clear out the `/tmp` directory. i.e. this sandpit project enable us to clear the entire database by a simple `vagrant reload`. This is ok for experimenting with things. For a more production-like blogging system, a more persistent database mechanism would be required.

## Run the web server (blog)

Issue this:

```
python flaskr.py
```

Hit `Ctrl C` to stop web server. (Issue the above command again to fire it up again.)

# Thoughts

Try and understand how this blog work as much as you can. Create something better.
