"""
תרגיל 13 – בנה מערכת לוגים מלאה
כתוב מודול py.setup_logging שמספק:
מוגדר logger שמחזירה( get_logger(name פונקציה .1
.2 כל logger כולל StreamHandler( מסך( ו-FileHandler( קובץ(
.3 Formatter אחיד עם זמן, שם, רמה והודעה
.4 הדגם שימוש ב2- מודולים שונים שמשתמשים ב-logger_g


"""

import logging

def get_logger(filename:str)->logging.Logger:
    """
    retutn a defult loger for institct logging to all project
    logger foramt -> ('%(asctime)s - %(name)s - %(levelname)s - %(message)s ')
    logger handeler -> strem, file
    logger level -> info (20)
    logger  name -> defult logger

    parm:
        filename: (str) the path or file name to save this logger info
    
    
    """
    logger = logging.getLogger('defult logger')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s ')
    file_handler = logging.FileHandler(filename=filename)
    stream_handler = logging.StreamHandler()
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.INFO)

    return logger


    
    