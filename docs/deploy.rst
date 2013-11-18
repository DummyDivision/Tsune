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
To be added...