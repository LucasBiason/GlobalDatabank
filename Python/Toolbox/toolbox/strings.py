import re


def erase_inject_text(text: str) -> str:
    ''' Removes any extra spaces at the beginning, middle and end 
    of the string and any HTML tags.
    '''
    if not text:
        return ""

    MALICIOUS_LIST = [
        'SELECT', 'DELETE', 'UPDATE', 'INSERT', 'CREATE',
    ]
    for value in MALICIOUS_LIST:
        if value in text.upper():
            return ""

    REMOVE_LIST = [
        '<[^<]+?>',
    ]
    for value in REMOVE_LIST:
        text = re.sub(value, '', text)
    
    REPLACE_DICTS = {
        u'\xa0': '',
        '[\s]{2,n}': '\s',
    }
    for key, value in REPLACE_DICTS.items():
        text = text.replace(key, value)

    text = text.strip()
    return text
