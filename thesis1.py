import imaplib
from bs4 import BeautifulSoup
import re
s = imaplib.IMAP4_SSL('imap.gmail.com', 993)
#msg_ids = []
def open_connection(verbose = True):
	
	username = "username"
	password = "password"

	print 'Logging in as', username

	s.login(username, password)
	return s

def select_search():
	s.select('[Gmail]/Chats', readonly=True)
	print "You are connected to Chats"
	search_term = raw_input("Enter search term: ")
	msg_ids = s.search(None, '(BODY " %s ")' % search_term)
	print "Here are all the chats having to do with your search, identified by numeric ID: ", msg_ids 

def print_msg():
	msg_choice = raw_input("Input message number: ")
	typ, msg_data = s.fetch(msg_choice, '(BODY[TEXT])')
	soup = BeautifulSoup(repr(msg_data))
	text = soup.html.find_all("div")
	str_text = str(text)
	soup_text = BeautifulSoup(str_text)
	thisistext = soup_text.get_text()
	print thisistext

open_connection()
select_search()
print_msg()