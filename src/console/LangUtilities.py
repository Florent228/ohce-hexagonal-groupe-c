import locale

def getSystemLanguageLocale():
    langue_locale = locale.getlocale()[0]
    code_langue = langue_locale.split('_')[0]
    return code_langue
