import voxbot
import gevent

SETTINGS = {
    'server': 'irc.voxinfinitus.net', 
    'nick': 'Kaa', 
    'realname': 'Kaa the Python', 
    'port': 6697, 
    'ssl': True, 
    'channels': ['#testing'], 
    'owners': ['doraemon']
    }

try:
    jobs = [gevent.spawn(voxbot.bot, SETTINGS)]
    gevent.joinall(jobs)
finally:
    gevent.killall(jobs)
