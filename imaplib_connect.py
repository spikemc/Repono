import imaplib
#import ConfigParser
import os

def open_connection(verbose=False):
    # Read the config file
    #config = ConfigParser.ConfigParser()
    #config.read([os.path.expanduser('~/.pymotw')])

    # Connect to the server
   # hostname = config.get('server', 'hostname')
    #if verbose: print 'Connecting to', hostname
    connection = imaplib.IMAP4_SSL('imap.gmail.com', 993)

    # Login to our account
    username = 'spikemccue@gmail.com'
    password = 'brookemccue123'
    if verbose: print 'Logging in as', username
    connection.login(username, password)
    return connection

if __name__ == '__main__':
    c = open_connection(verbose=True)
    try:
        print c
    finally:
        c.logout()