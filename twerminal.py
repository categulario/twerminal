#!/usr/bin/python
# -*- coding:utf-8 -*-

from libturpial.api.core import Core
from libturpial.api.models.account import Account

id_cuenta = 'categulario-twitter'

account = Account.load(id_cuenta)

#~ url = account.request_oauth_access()
#~ print url
#~ PIN = raw_input("PIN: ")
#~
#~ account.authorize_oauth_access(PIN)

core = Core()

friend_list = core.get_all_friends_list()
friend_list.sort()

columnas = {
    'T': 'timeline',
    'D': 'directs',
    'R': 'replies'
}

while True:
    comando = raw_input('>>> ')
    if comando.upper() in ['T', 'D', 'R']:
        timeline = core.get_column_statuses(id_cuenta, columnas[comando.upper()])
        timeline.reverse()
        for status in timeline:
            print '----------'
            print "@%s: %s" % (status.username, status.text)
            print status.datetime, status.id_
    elif comando.upper() == 'Q':
        break
    elif comando.upper().startswith('RT '):
        id_status = comando.split()[1]
        core.repeat_status(id_cuenta, id_status)
    elif comando.upper().startswith('RE '):
        id_status = comando.split()[1]
        core.update_status(id_cuenta, comando[21:], in_reply_id=id_status)
    elif comando.upper().startswith('D '):
        arr = comando.split()
        core.send_direct_message(id_cuenta, arr[1], comando[2+len(arr[1]):])
    elif comando.upper() == 'L':
        for friend in friend_list:
            print '  ', friend
    elif comando.upper() == 'H':
        print """
        Un twitter de consola, comandos:
        T   Obtener timeline
        D   Mensajes directos o enviar un mensaje
        R   Respuestas a tus mensajes
        L   Lista de amigos
        H   Ayuda
        RT  retuitea un tweet
        Q   Salir
        """
    elif comando == '':
        pass
    else:
        core.update_status(id_cuenta, comando)
print 'bye'
