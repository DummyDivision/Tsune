import os

SECRETS_PRESENT = True

# Google

if os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY") is not None:
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
else:
    SECRETS_PRESENT &= False

if os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET") is not None:
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")
else:
    SECRETS_PRESENT &= False

# Facebook

if os.environ.get("SOCIAL_AUTH_FACEBOOK_KEY") is not None:
    SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get("SOCIAL_AUTH_FACEBOOK_KEY")
else:
    SECRETS_PRESENT &= False

if os.environ.get("SOCIAL_AUTH_FACEBOOK_SECRET") is not None:
    SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get("SOCIAL_AUTH_FACEBOOK_SECRET")
else:
    SECRETS_PRESENT &= False

# Dropbox

if os.environ.get("SOCIAL_AUTH_DROPBOX_OAUTH2_KEY") is not None:
    SOCIAL_AUTH_DROPBOX_OAUTH2_KEY = os.environ.get("SOCIAL_AUTH_DROPBOX_OAUTH2_KEY")
else:
    SECRETS_PRESENT &= False

if os.environ.get("SOCIAL_AUTH_DROPBOX_OAUTH2_SECRET") is not None:
    SOCIAL_AUTH_DROPBOX_OAUTH2_SECRET = os.environ.get("SOCIAL_AUTH_DROPBOX_OAUTH2_SECRET")
else:
    SECRETS_PRESENT &= False