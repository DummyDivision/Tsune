==================
Deploying Tsune...
==================

...to Heroku
#############

To deploy Tsune on Heroku, just push the repository to it:

``$ git push heroku master``

After that, you should set the SECRET\_KEY environment variable.
To generate a new key, run the following from a python prompt::

    from django.utils.crypto import get_random_string

    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    print get_random_string(50, chars)

Now set the SECRET\_KEY environment variable for your app.
Run the following in your repository root:

``heroku config:set SECRET_KEY="paste the generated key here"``

...on Ubuntu Server
#####################

1. ``$ sudo apt-get update``

2. ``$ sudo apt-get install chef``

3. Do not input anything when prompted to select a chef-server. Just press Enter.

4. ``wget https://dl.dropboxusercontent.com/s/pcnysdzaie6wr58/postgres.json``

5. ``chef-solo -j postgres.json -r https://dl.dropboxusercontent.com/s/fh3dxy0tbjuoulm/dependencies.tar.gz``

6. ``sudo apt-get -y install libpq-dev python-dev firefox xvfb graphviz git-core``

7. ``git clone https://github.com/DummyDivision/Tsune ``

8. ``cd Tsune && python manage.py syncdb && python manage.py migrate && python manage.py runserver``