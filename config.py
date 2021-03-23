import os
from dotenv import load_dotenv

load_dotenv()

ON_START = '```diff\n--- Runtime reset ---```'
SESSION_START = '```diff\n--- Session Started ---\n```'
SESSION_CLOSE = '```diff\n --- Session Closed ---\n```'
TOKEN_CREATION = lambda t: f'```diff\n+ GENERATED TOKEN: ``` ||{t}||'
AUDIT_LOG = int(os.getenv('AUDIT_LOG'))
CLIENT_ID = int(os.getenv('CLIENT_ID'))
REACTION = '✉️'
GET_USERNAME = lambda u: u.name + '#' + u.discriminator
NEW_REQUEST = lambda u: 'New request from user: ```' + u + f'``` <@&{os.getenv("HIRING_ROLE")}>'
DM_ENTER_TOKEN = 'You should\'ve received an access token from a staff member prior to being invited to the server. ' \
                 'Please enter this token below: '
GUILD_ID = int(os.getenv('GUILD_ID'))
NEW_MEMBER = lambda u: 'New member authorized: ' + u + f' <@&{os.getenv("HIRING_ROLE")}>'
BOT_COMMANDS = int(os.getenv('BOT_COMMANDS'))
AUTHORIZED = '```You were successfully authorized.```'
ACCESS_DENIED = '```diff\nAccess denied, please try again later...```'
TOKEN_NOTIF = lambda u: 'Token created from user: ' + u + f' <@&{os.getenv("HIRING_ROLE")}>'
TOKEN = os.getenv('TOKEN')
