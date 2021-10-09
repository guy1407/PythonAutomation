from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup  # web scraping
import datetime
import requests  # http requests
import smtplib

# #####################################
# read email parameters

# open the data file:
file = open("emailparams.txt")
# read the file as a list
emailParams = file.readlines()
# close the file
file.close()
# #####################################
# put email parameters into variables:
serverLogin = emailParams[0].split(':')[1].rstrip('\n')
serverPassword = emailParams[1].split(':')[1].rstrip('\n')
SMTPServer = emailParams[2].split(':')[1].rstrip('\n')
portNumber = emailParams[3].split(':')[1].rstrip('\n')
fromAddress = emailParams[4].split(':')[1].rstrip('\n')
recipients = emailParams[5].split(':')[1].rstrip('\n')
# #####################################
timeStamp = datetime.datetime.now()

# extracting Hacker News Stories
def extract_news(url):
    print('Extracting Hacker News Stories...')
    pageContent = ''
    pageContent += ('<b>HN Top Stories:</b>\n' + '<br>' + '-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        pageContent += ((str(i+1)+' :: ' + tag.text + "\n" + '<br>')
                if tag.text != 'More' else '')
        # print(tag,prettify) #find all ('span', attrs={'class':'sitestr''}))
    return (pageContent)

# email content placeholder
emailBody = extract_news('https://news.ycombinator.com/')
emailBody += ('<br>------<br>')
emailBody += ('<br><br>End of Message')

# lets send the email

print('Composing Email ...')
# Create a text/plain message
msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + \
    str(timeStamp.day) + '/' + str(timeStamp.month) + '/' + str(timeStamp.year)
msg['From'] = fromAddress
msg['To'] = recipients
msg.attach(MIMEText(emailBody, 'html'))


print('Initiating Server...')
server = smtplib.SMTP(SMTPServer, int(portNumber))
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(serverLogin, serverPassword)
server.sendmail(fromAddress, recipients, msg.as_string())

print('Email Sent...')

server.quit()
