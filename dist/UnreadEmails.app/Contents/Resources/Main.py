import rumps
import yaml
import time
import imaplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


def mark_as_seen(login_file):
    # Function that logs into the email Inbox and then simply marks them all as SEEN
    log_file = "log/log.txt"
    
    # Reads data from the login file | "login.yaml"
    with open(login_file) as f:
        content = f.read()

    # loads up the data from it
    my_credentials = yaml.load(content, Loader=yaml.FullLoader)
    print("Přihlašuji se k adrese: ", my_credentials["user"])
    start_time = time.time()
    time.sleep(1)

    # your credentials to inicialize the login
    user, password = my_credentials["user"], my_credentials["password"]

    # IMAP for Gmail
    imap_url = 'imap.gmail.com'

    # Logs into the gmail
    my_email = imaplib.IMAP4_SSL(imap_url)
    my_email.login(user, password)
    my_email.select('Inbox')
    print("Otevřel jsem tvoji emailovou schránku")

    _, data = my_email.search(None, 'ALL')  # Searches all the emails

    # List of all email ID's
    list_emails = data[0].split()

    # Number of all emails in your Inbox
    num_emails = len(list_emails)

    # Prints out the number
    print("Celkový počet e-mailů:", num_emails)
    print("--------------------------------------")

     # Vyhledá nepřečtené emaily
    _, data = my_email.search(None, 'UNSEEN')
    unseen_email_ids = data[0].split()

    # Počet nepřečtených e-mailů
    global  num_unseen_emails
    num_unseen_emails = len(unseen_email_ids)

    if num_unseen_emails > 0:
        print("Počet nepřečtených e-mailů:", num_unseen_emails)
        print("--------------------------------------")

        for email_id in unseen_email_ids:
            my_email.store(email_id, '+FLAGS', '\Seen')

        print("Označil jsem všechny e-maily jako PŘEČTENÉ")
        global time_in_seconds
        time_in_seconds = time.time() - start_time
 
        log_message = f"{num_unseen_emails} emailů bylo označeno jako přečteno | účet: {user}  | Doba trvání: {time_in_seconds:.2f}s " #| účet: {user}  | Doba trvání: {time_in_seconds:.2f}s
        log_to_file(log_message, log_file)
        global successfull 
        successfull = True
    else:
        successfull = False


    # Logs out of your email
    my_email.logout()

    return num_unseen_emails

def log_to_file(log_message, log_file):
    #timestamp = time.strftime(" %Y-%m-%d %H:%M:%S", time.localtime())
    log_entry = f"{log_message}"
    #separator = '-' * len(log_entry)

    with open(log_file, 'a') as f:
        #f.write(separator + "\n")
        f.write(log_entry + "\n")
        #f.write(separator + "\n")
    
    print("log byl úspěšně uložen!!")


def main2():
    print("----------------------------------")
    print("Zahajuji automatické čtení e-mailů...")
    time.sleep(1)

    # FUNCTION TO MARK ALL EMAILS AS SEEN   
    login_file = "login.yaml"
    mark_as_seen(login_file)  # Call mark_as_seen and get the values



def openEmailAddress(login_file):
    # Reads data from the login file | "login.yaml"
    with open(login_file) as f:
        content = f.read()

    # loads up the data from it
    my_credentials = yaml.load(content, Loader=yaml.FullLoader)
    time.sleep(1)

    # your credentials to inicialize the login
    user, password = my_credentials["user"], my_credentials["password"]

    # IMAP for Gmail
    imap_url = 'imap.gmail.com'

    # Logs into the gmail
    my_email = imaplib.IMAP4_SSL(imap_url)
    my_email.login(user, password)
    my_email.select('Inbox')

    _, data = my_email.search(None, 'ALL')  # Searches all the emails

    # List of all email ID's
    list_emails = data[0].split()

    # Number of all emails in your Inbox
    num_emails = len(list_emails)

    # Searches for unseen emails
    _, data = my_email.search(None, 'UNSEEN')
    unseen_email_ids = data[0].split()
    num_unseen_emails = len(unseen_email_ids)

    return num_unseen_emails

def main():
    def get_unread_emails():
        login_file = "login.yaml"
        unread_emails = openEmailAddress(login_file)
        return f"Unseen emails: {unread_emails}"

    def run_automation(sender):
        login_file = "login.yaml"
        mark_as_seen(login_file)

        app.title = get_unread_emails()

    def extract_emails(sender):
        pass

    def open_settings(sender):
        pass

    app = rumps.App("Fetching data...", icon="logo.png") 
    app.title = get_unread_emails() 

    app.menu = [
        rumps.MenuItem("Read all emails", callback=run_automation),
        rumps.MenuItem("Extract into .xlsx file", callback=extract_emails),
        "Generate report",
        rumps.MenuItem("Settings", callback=open_settings),
    ]

    # Timer to refresh title every 60 seconds
    @rumps.timer(60)  # Update every 60 seconds
    def update_title(_):
        app.title = get_unread_emails()

    app.run()

main()