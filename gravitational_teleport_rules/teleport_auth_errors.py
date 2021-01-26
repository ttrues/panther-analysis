def rule(event):
    return bool(event.get('error')) and event.get('event') == 'auth'


def title(event):
    return 'A high volume of SSH errors was detected from user [{}]'.format(
        event.get('user', '<UNKNOWN_USER>'))
