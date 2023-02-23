import datetime

import psycopg2
import pytz
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

DATABASE_URL = os.environ['DATABASE_URL']
#DATABASE_URL='postgres://scylfjyygeactf:4a059e54ad264651837df64a3a7248a11225b7b75571db39590c37d7b8e4a6fa@ec2-23-20-140-229.compute-1.amazonaws.com:5432/de14p785paocd3'

admins=['a__.r_.u_.n__', 'user_not_found_x20']


temp_count = 0
admin_count=0
thank_you = [ 'THANK YOU', 'TQ', 'TQ U', 'THANKS', 'THANK', 'THANK U', 'THANKYOU', 'TNQ', 'TNX','TQS' ]
options = Options()
path ="/Users/sameershaik/Downloads/chromedriver 2"
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.add_argument('--disable-notifications')
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
web = webdriver.Chrome(service=Service(os.environ.get("CHROMEDRIVER_PATH")), options=options)
web.implicitly_wait(2)

def send_att_time():
    conn=psycopg2.connect(DATABASE_URL, sslmode='require')
    '''conn=psycopg2.connect(database="dqe54aoft23do", host="ec2-34-199-68-114.compute-1.amazonaws.com",
                         user="cgncgmtvnnnjki", port="5432",
                         password="9c67b17c47ac756d8b94edf5b9a65dc71f9da48e272a73e77860aa057b20204f")'''
    cur=conn.cursor()
    cur.execute("select insta_username from instad where book_req=true;")
    bo_data=cur.fetchall()
    conn.close()
    for roll in bo_data:
        try:
            WebDriverWait(web, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='_aa4m _aa4p']/button"))).click()
        except:
            print('Not clickable')
            web.get('https://www.instagram.com/direct/inbox/general/')
            continue
        WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class=' _aa2u']/input"))).send_keys(roll)
        time.sleep(1)
        try:
            usern = WebDriverWait(web, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                 "//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _ab9v _abcm']/div[1]//div[@class='_aacl _aaco _aacw _aacx _aad6']"))).text
            i = 1
            while True:
                if i == 5:
                    break
                if roll[0] == usern:
                    WebDriverWait(web, 10).until(
                        EC.presence_of_element_located(
                            (
                            By.XPATH, f"//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _ab9v _abcm']/div[{i}]"))).click()
                    break
                else:
                    usern = WebDriverWait(web, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                         f"//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _ab9v _abcm']/div[{i + 1}]//div[@class='_aacl _aaco _aacw _aacx _aad6']"))).text
                    i += 1
                    continue
        except:
            web.get('https://www.instagram.com/direct/inbox/general/')
            continue
        try:
            time.sleep(1)
            WebDriverWait(web, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@class='_acan _acao _acas _acav']"))).click()
            try:
                info=provide_rollno(roll [0])
                send_msg(
                    f'Hello, {info.get("name")}\nThis Is Your Attendance Till Now: {info.get("attendance")}\n From AttBot Subscribed Data')
            except:
                pass
            finally:
                web.get('https://www.instagram.com/direct/inbox/general/')
        except:
            web.get('https://www.instagram.com/direct/inbox/general/')
            continue


def login(web):
    try:
        user = web.find_element(By.XPATH, '//*[@id="username"]')
        user.send_keys('rohini')
        passw = web.find_element(By.XPATH, '//*[@id="password"]')
        passw.send_keys('rohini')
        sub = web.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[2]/td/form/table/tbody/tr[6]/td/input')
        sub.click()
        print("attendance site logined")
    except Exception as error:
        pass


def provide_rollno(username):
    conn=psycopg2.connect(DATABASE_URL, sslmode='require')
    '''conn=psycopg2.connect(database="dqe54aoft23do", host="ec2-34-199-68-114.compute-1.amazonaws.com",
                          user="cgncgmtvnnnjki", port="5432",
                          password="9c67b17c47ac756d8b94edf5b9a65dc71f9da48e272a73e77860aa057b20204f")'''
    cur=conn.cursor()
    cur.execute(f"select rolid from instad where insta_username='{username}';")
    rollno = cur.fetchone()[0]
    conn.close()
    info = get_data(rollno)
    return info
def get_data(rollno):
    att = None
    try:
        data = requests.get(f'https://attnbkrist.live/attapi?roll={rollno}')
        data = data.json()
        if 'status' in data:
            return att
        return data
    except Exception as error:
        return att
def login_insta(usern, passw):
    try:
        web.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(usern)
        time.sleep(2)
        web.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(passw)
        time.sleep(2)
        web.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
        print('Login Successful')
    except Exception as error:
        print('Not Logined')


def not_now():
    try:
        #notnow
        WebDriverWait(web, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button'))).click()
        #notnow
        time.sleep(3)
        WebDriverWait(web, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@class="_a9-- _a9_1"]'))).click()
        print('Not Now clicked')
    except NoSuchElementException:
        print('Not Found And passed')
        pass
    except Exception as error:
        print(error.args[0])
        pass


web.get('https://www.instagram.com/direct/inbox/general/')
print('Login initiated')
login_ins()
not_now()


def read_unread_msgs():
    global temp_count,admin_count
    if (((datetime.datetime.now(pytz.timezone('Asia/Kolkata')).hour == 12) or (datetime.datetime.now(
            pytz.timezone('Asia/Kolkata')).hour == 16)) and temp_count == 0):  # checks for booking slots reservation
        send_att_time()
        print('time_slots_send')
        temp_count += 1
    elif (datetime.datetime.now(pytz.timezone('Asia/Kolkata')).hour == 13 or datetime.datetime.now(
            pytz.timezone('Asia/Kolkata')).hour == 17) and temp_count != 0:
        temp_count = 0
    '''try:
        web.get('https://www.instagram.com/direct/requests/')
        WebDriverWait(web, 1).until(EC.presence_of_element_located((By.XPATH, "//div[@class=' _ab8s _ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p _abcm']/a"))).click()
        WebDriverWait(web, 1).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Accept')]"))).click()
        WebDriverWait(web, 1).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_a9-z']/*[contains(text(),'General')]"))).click()
    except:'''
    web.get('https://www.instagram.com/direct/inbox/general/') #clicks general
    try:
        WebDriverWait(web, 300).until(EC.presence_of_element_located(
            (By.XPATH, '//div[@aria-label="Unread"]'))).click()
        print('msg found')
    except:
        read_unread_msgs()
def move_general():
    try:
        time.sleep(0.2)
        web.find_element(By.XPATH, "//*[local-name()='svg' and @aria-label='View thread details']").click()
        time.sleep(0.5)
        web.find_element(By.XPATH, "//button[@class='_acan _acap _acat']").click()
        time.sleep(0.5)
        web.find_element(By.XPATH,"//*[local-name()='svg' and @aria-label='Navigate back to chat from thread details']").click()
    except:
        print('Error in moving')

def send_msg(msg_data):
    global username, msg, msg_count
    try:
        msg_data = msg_data.replace("\n", (Keys.SHIFT + Keys.ENTER + Keys.ENTER + Keys.SHIFT))
        WebDriverWait(web, 15).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Message...']"))).send_keys(msg_data)
        time.sleep(1)
        WebDriverWait(web, 15).until(EC.presence_of_element_located((By.XPATH,"//button[contains(text(),'Send')]"))).click()
    except:
        username = None
        msg = None
        msg_count = 0
        print('msg send error')


def get_username():
    '''try:
        time.sleep(0.2)
        web.find_element(By.XPATH, "//*[local-name()='svg' and @aria-label='View thread details']").click()
        time.sleep(0.2)
        username=web.find_element(By.XPATH, "//div[@class='_aacl _aaco _aacw _adda _aacx _aad6']").text
        time.sleep(0.2)
        web.find_element(By.XPATH,"//*[local-name()='svg' and @aria-label='Navigate back to chat from thread details']").click()
    except:'''
    WebDriverWait(web, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='_acan _acao _acaq _acat']"))).click()
    try:
        username = WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[@class='_aacl _aacs _aact _aacx _aada']"))).text
    except:
        username = WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[@class='_aacl _aacs _aact _aacx _aada']"))).text
    finally:
        time.sleep(0.5)
        web.back()
    return username


temp = ''


def readmsg(oldmsg):
    global username, msg, msg_count
    count = 0
    while (True):
        time.sleep(1)
        msg = WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='_acqt _acqu'])[last()]"))).text
        try:
            if msg.isdigit():
                pass
            else:
                msg = msg.upper()
        except Exception as error:
            print(error)
            readmsg(msg)
        if count == 30:
            send_msg("click on 'http://attnbkrist.live' for more details")
            username = None
            msg = None
            msg_count = 0
            return None
        if oldmsg == msg:
            count += 1
            continue
        else:
            break
    print(msg)
    return msg


#web.execute_script("window.open('');")
print('Bot is Online')
read_unread_msgs()
username = None
msg = None
msg_count = 0
while (True):
    conn=psycopg2.connect(DATABASE_URL, sslmode='require')
    '''conn=psycopg2.connect(database="dqe54aoft23do", host="ec2-34-199-68-114.compute-1.amazonaws.com",
                          user="cgncgmtvnnnjki", port="5432",
                          password="9c67b17c47ac756d8b94edf5b9a65dc71f9da48e272a73e77860aa057b20204f")'''
    cur=conn.cursor()
    try:
        msg = readmsg(msg)
        if msg == None:
            username = None
            msg_count = 0
            read_unread_msgs()
            conn.close()
            continue
        try:
            if msg.isdigit():
                msg_count = 0
        except:
            pass
        if not username:
            username = get_username()
            print(username)
        cur.execute(f"select insta_username,active_status,rolid from instad where insta_username='{username}';")
        status=cur.fetchone()
        #cur.execute(f"select active_status from instad where insta_username='{username}';")
        if msg and not(status):
            if len(msg)==10:
                cur.execute(f"select count(*) from main where rollno='{msg}'")
                ch=cur.fetchone()[0]
            else:
                ch=False
            if ch:
                cur.execute(f"insert into instad(rolid,insta_username) values('{msg}','{username}');")
                conn.commit()
                cur.execute(f"select name from main where rollno='{msg}'")
                send_msg(f'Hi,{cur.fetchone()[0]}\nYour ROLL NO Registered Successfully')
                send_msg('Type "1" For Attendance\nType "2" to Book Requests By Time')
                conn.close()
                continue
            else:
                send_msg('Hello, This is An ATT | BOT \nPlease Enter your ROLL NO\n')
                msg=readmsg(msg)
                if msg == None:
                    username=None
                    msg=None
                    msg_count=0
                    conn.close()
                    read_unread_msgs()
                    continue
                if len(msg)==10:
                    cur.execute(f"select count(*) from main where rollno='{msg}'")
                    ch=cur.fetchone()[0]
                else:
                    ch=False
                if ch:
                    cur.execute(f"select count(*) from instad where rolid='{msg}'")
                    if not cur.fetchone()[0]:
                        cur.execute(f"insert into instad(rolid,insta_username) values('{msg}','{username}');")
                        conn.commit()
                        cur.execute(f"select name from main where rollno='{msg}'")
                        send_msg(f'Hi,{cur.fetchone()}\nYour ROLL NO Registered Successfully')
                        send_msg('Type "1" For Attendance\nType "2" to Book Requests By Time')
                        conn.close()
                        continue
                    else:
                        send_msg('Your RollNo Already Linked with another InstaId.\nPlease Contact Admin by Type "admin".')
                        username=None
                        msg=None
                        msg_count=0
                        conn.close()
                        read_unread_msgs()
                        continue
                else:
                        send_msg('Roll No not available\nPlease try Again')
                        username=None
                        msg=None
                        msg_count=0
                        conn.close()
                        read_unread_msgs()
                        continue
        elif not status[1] and msg == 'START':
            cur.execute(f"update instad set active_status=true where insta_username='{username}'")
            conn.commit()
            send_msg('Status:Active')
            username=None
            msg=None
            msg_count=0
            conn.close()
            read_unread_msgs()
            continue
        elif not status[1]:
            username=None
            msg=None
            msg_count=0
            conn.close()
            read_unread_msgs()
            continue
        elif msg == '1':
            info=provide_rollno(username)
            name=info.get('name') #fetches student_name
            att=info.get('attendance') #fetches att
            incRate = info.get('incRate') #fetches incr_rate
            decRate = info.get('decRate') #fetches decr_rate
            send_msg(f'Hi, {name}\nThis is Your Attendance Till Now: {att}.')
            cur.execute(f"select book_req,dm_link from instad where insta_username='{username}'")
            book_req=cur.fetchone()
            #cur.execute(f"select book_req from instad where insta_username='{username}'")
            #book_req=cur.fetchone()
            if not book_req[0]:
                send_msg('Type "1" If you want Again\nType "2" to Book Requests By Time\nType "admin" to get Support')
                msg = None
                username = None
                msg_count = 0
                read_unread_msgs()
                conn.close()
                continue
            else:
                send_msg('Type "1" If you want Again\nType "admin" to get Support')
                msg=None
                username=None
                msg_count=0
                read_unread_msgs()
                conn.close()
                continue
        elif msg == '2':
            cur.execute(f"select book_req,rolid from instad where insta_username='{username}'")
            book_req=cur.fetchone()
            if book_req[0]:
                cur.execute(f"select name from main where rollno='{book_req[1]}'")
                send_msg(f"Don't worry...\n{cur.fetchone()[0]}\nYou Subscribed Already.\nType 'admin' to get Support")
                username = None
                msg = None
                msg_count = 0
                read_unread_msgs()
                conn.close()
                continue
            else:
                send_msg('Now you will get attendance twice a day automatically\n01:00 PM and 4:30 PM\nType "yes" to Confirm\nType "no" to cancel')
                msg = readmsg(msg)
                if msg == None:
                    read_unread_msgs()
                    conn.close()
                    continue
                elif msg == 'YES':
                    cur.execute(f"select name from main where rollno='{book_req[1]}'")
                    send_msg(f'Thanks {cur.fetchone()[0]} For Subscribe.')
                    cur.execute(f"update instad set book_req=true where insta_username='{username}'")
                    conn.commit()
                    time.sleep(0.5)
                    msg = None
                    username = None
                    msg_count = 0
                    read_unread_msgs()
                    conn.close()
                    continue
                elif msg == 'NO':
                    send_msg('Not a Problem\nThank you')
                    username = None
                    msg = None
                    msg_count = 0
                    read_unread_msgs()
                    conn.close()
                    continue
                else:
                    send_msg("Sorry, I can't understand")
                    username = None
                    msg = None
                    msg_count = 0
                    read_unread_msgs()
                    conn.close()
                    continue
        elif msg == '3':
            send_msg('Enter Roll No.')
            msg=readmsg(msg)
            cur.execute(f"select count(*) from main where rollno='{msg}'")
            if cur.fetchone()[0]:
                cur.execute(f"select count(*) from instad where rolid='{msg}'")
                rd=cur.fetchone()
                if not rd[0]:
                    cur.execute(f"update instad set rolid='{msg}' where insta_username='{username}';")
                    conn.commit()
                    cur.execute(f"select name from main where rollno='{msg}'")
                    send_msg(f'Hello {cur.fetchone()[0]},\nRollNo changed.')
                else:
                    send_msg('Ur rollno already linked to another username.\ncontact support@attnbkrist.live\nType "admin" to get Support')
            else:
                send_msg('Rollno is not found.\nTry Again\nType "admin" to get Support')
            username = None
            msg = None
            msg_count = 0
            read_unread_msgs()
            conn.close()
            continue
        elif msg in thank_you:
            send_msg('You are welcome')
            username = None
            msg = None
            msg_count = None
            read_unread_msgs()
            conn.close()
            continue
        elif msg == 'SEND' and username in admins:
            cur.execute("select count(rolid) from instad where book_req=true;")
            book_count=cur.fetchone()[0]
            send_msg(
                f'You want to send att to your {book_count} subscribers\n"Yes" to confirm \n "No" to cancel')
            msg = readmsg(msg)
            if msg == 'YES':
                send_msg('Sending')
                send_att_time()
                msg = None
                username = None
                msg_count = 0
                read_unread_msgs()
                conn.close()
                continue
            elif msg == 'NO':
                send_msg('Ok, Not A Problem chinna Bot\nEnjoy pandago')
                msg = None
                username = None
                msg_count = 0
                read_unread_msgs()
                conn.close()
                continue
            else:
                send_msg('Enduku Bot Time Waste Chestav\nChaduvuko First malli chudam bye')
                msg = None
                username = None
                msg_count = 0
                read_unread_msgs()
                conn.close()
                continue
        elif msg == 'C' and username in admins:
            cur.execute("select count(rolid) from instad;")
            count=cur.fetchone()[0]
            cur.execute("select count(rolid) from instad where book_req=true;")
            book_count=cur.fetchone()[0]
            send_msg(f"Total {count} Registered users\n{book_count} subscribers")
            msg = None
            username = None
            msg_count = 0
            read_unread_msgs()
            conn.close()
            continue
        elif msg == 'OK' or msg == 'KK' or msg == 'K':
            send_msg('Fine')
            msg = None
            username = None
            msg_count = 0
            read_unread_msgs()
            conn.close()
            continue
        elif msg == 'ADMIN':
            try:
                cur.execute(f"update instad set active_status=false where insta_username='{username}'")
                conn.commit()
                send_msg('Send Your Problem')
            except:
                print('skip')
            msg = None
            username = None
            msg_count = 0
            read_unread_msgs()
            conn.close()
            continue
        elif status and msg and msg_count == 0:
            msg_count += 1
            cur.execute(f"select rolid from instad where insta_username='{username}'")
            cur.execute(f"select name from main where rollno='{cur.fetchone()[0]}'")
            send_msg(
                f'Hello,{cur.fetchone()[0]}\nYou registered already\nType "1" for Attendance\nType "2" to Book Requests By Time.\n Type "3" to change RollNo.\nType "admin" to get Support')
            conn.close()
            continue
        else:
            send_msg("Sorry, I can't understand")
            username = None
            msg = None
            msg_count = 0
            read_unread_msgs()
            conn.close()
            continue
    except Exception as error:
        print(error)
        username = None
        msg = None
        msg_count = 0
        read_unread_msgs()
    conn.close()
