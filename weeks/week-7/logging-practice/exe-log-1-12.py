import logging

logging.basicConfig(filename='data.log', level=10)

logger = logging.getLogger(__name__)


"""
1:

 __x_ print ו-logging הם שקולים לחלוטין
 __v_ DEBUG מתאים למידע מפורט בזמן פיתוח
 __x_ מותר לכתוב סיסמה בלוג אם היא מוצפנת
 __x_ WARNING אומר שהמערכת קרסה
__v_ FileHandler שומר לוגים לקובץ
stack trace גם כולל logger.exception _v__ 
__x_ כדאי להשתמש ברמת לוג אחת בלבד לפשטות


"""


"""
תרגיל 2 – התאמת רמת לוג
לכל תיאור, ציין את רמת הלוג המתאימה )ERROR / WARNING / INFO / DEBUG):
.1 משתמש התחבר בהצלחה: info
.2 קובץ קונפיגורציה לא נמצא: warnnig
.3 כניסה לפונקציה עם ערכי הפרמטרים: debug 
.4 מסד הנתונים לא זמין: error
.5 מלאי מוצר נמוך מ5- יחידות: warning
.6 תהליך הזמנה הסתיים בהצלחה: info



"""

"""
תרגיל 3 – זיהוי בעיות
מצא את הבעיה בכל לוג ותקן:
# לוג א
logger.error('User logged in successfully')
בעיה ותיקון: you should use 'info' -> logger.info('User logged in successfully')


# לוג ב
logger.info('Login', email, password)
בעיה ותיקון: you shold not add a password, -> logger.info(f'Login with { email} ,enter password {bool(password)}')

 לוג ג
print('ERROR: payment failed')
בעיה ותיקון: you shold use log to save it -> logger.warning('payment failed')



"""


"""
תרגיל 4 – מה מייצג כל שדה?
הסבר מה מייצג כל שדה בפורמט הבא:
'%(asctime)s | %(levelname)s | %(name)s | %(message)s'
%(asctime)s: time the log created
%(levelname)s: massege level
%(name)s: logger name
%(message)s: the massage you added to the log



"""


"""
תרגיל 5 – השלם קוד
השלם כך שהקוד יריץ basicConfig עם INFO ויכתוב לוג אחד:
import ___
logging.___(level=logging.___, format='%(levelname)s | %(message)s')
logger = logging.___(__name__)
logger.___('Application started')


"""

logging.basicConfig(level=logging.INFO, format='%(levelname)s | %(message)s')
logger = logging.getLogger(__name__)
logger.info('Application started')


"""
תרגיל 6 – הפוך print ללוגים
שכתב את הקוד הבא כך שישתמש ב-logging במקום print:
def process_payment(user_id, amount):
print(f'Starting payment for user {user_id}')
if amount <= 0:
    print('ERROR: Invalid amount')
    return
if amount > 10000:
    print('WARNING: Large transaction')
print(f'Payment of {amount} completed for user {user_id}')




"""


def process_payment(user_id, amount):
    logger.info(f'Starting payment for user {user_id}')
    if amount <= 0:
        logger.error('ERROR: Invalid amount')
        return
    if amount > 10000:
        logger.warning('WARNING: Large transaction')
    logger.info(f'Payment of {amount} completed for user {user_id}')


"""
תרגיל 7 – הוסף FileHandler
כתוב קוד שמגדיר logger ששומר לוגים לקובץ log.app:
.1 צור logger בשם 'payments'
encoding utf-8 עם FileHandler הגדר .2
.3 הוסף Formatter עם זמן, רמה ושם
.4 כתוב 3 לוגים בפונקציה פשוטה

"""

app_logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
filehandler = logging.FileHandler(filename='app.log', encoding='utf-8')
filehandler.setFormatter(formatter)
app_logger.addHandler(filehandler)


def login(user):
    app_logger.info('try to log in user')
    if user:
        app_logger.info('user logged in')
    else:
        app_logger.warning('faild!')


"""
תרגיל 8 – לוגים סביב except/try
הוסף לוגים מתאימים לקוד הבא:
def read_config(filepath):
לפני הניסיון filepath עם DEBUG הוסף :TODO #
try:
with open(filepath) as f:
data = f.read()
על הצלחה INFO הוסף :TODO #
return data
except FileNotFoundError:
לוג exception הוסף :TODO #
return None


"""


def read_config(filepath):
    logger.debug('useing read_confing to read the configiritions')
    try:

        with open(filepath) as f:
            data = f.read()
            logger.info(f'data reutun succefuly from {filepath}')
            return data
    except FileNotFoundError:
        logger.exception(f'error bring the file from {filepath}')
        return None


"""
תרגיל 9 – בנה פורמט JSON
ומדפיסה extra**-ו level, module, message שמקבלת write_structured_log פונקציה כתוב
:JSON
:פלט רצוי #
# {"timestamp": "2026-04-20T10:30:00", "level": "INFO",
# "module": "auth", "message": "User logged in", "user_id": 42}

"""

logging.basicConfig(level=20, format='%(message)s')

logger = logging.getLogger('structured log')
def write_structured_log(level,module,message, **extra):
    entry = {
        'level' :level,
        'module': module,
        'message': message,
        **extra
    }
    logger.info(entry)

write_structured_log("INFO", "auth", "User logged in", request_id="req-88", user_id=15)


"""
תרגיל 10 – מצא מה חסר
לכל לוג, ציין מה חסר בו ואיך לשפר:
logger.info('done')
מה חסר ואיך לשפר:  information about *what* has been done and with what status, we shold add 'prosess x done in status y'
logger.error('failed')
מה חסר ואיך לשפר: information about what faild, why, and how to continue from here.
logger.info('user=%s', user_id)
מה טוב ומה עוד אפשר להוסיף
good to add the user info, but important to explain what appand (user x get into y)


"""


"""

תרגיל 11 – חלוקת אירועים לרמות
סווג כל אירוע מהמערכת לרמת הלוג הנכונה:
• אדמין נכנס למערכת הניהול - error
• שירות חיצוני לא מגיב warning
• פונקציית חישוב מס החלה לרוץ- info
• - warning תעודת SSLעומדת לפוג בעוד 7 ימים
• הזמנה בוטלה על ידי לקוח- info
• תשלום נכשל 3 פעמים ברצ- warnign 



"""


"""
הקוד הבא עובד אך הלוגים גרועים. שפר כל לוג:
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
def register_user(email, password, age):
logger.debug('register')
if age < 18:
logger.error('bad')
return
logger.info('ok email=%s password=%s', email, password)
logger.info('done')
כתוב את הגרסה המשופרת



"""


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
def register_user(email, password, age):
    logger.debug(f' get into registering user procsess for mail {email}. age- {age} ')
    if age < 18:
        logger.error(f'registering not complited for email{email} -> age - {age} under 18 ')
        return
    logger.info(f'regitering {email} compited, passpord has given = {bool(password)}')
    logger.info('prosess has done succsefully')

    