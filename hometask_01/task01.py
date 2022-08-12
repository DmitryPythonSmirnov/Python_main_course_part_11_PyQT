'''
Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться
доступность сетевых узлов. Аргументом функции является список, в котором каждый сетевой
узел должен быть представлен именем хоста или ip-адресом. В функции необходимо
перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с
помощью функции ip_address().
'''

import subprocess
import os
import ipaddress


def get_count_flag():
    '''
    Функция возвращает ключ для количества пингов
    в зависимости от ОС
    '''
    count_flag = None
    if os.name == 'nt':
        count_flag = '-n'
    elif os.name == 'posix':
        count_flag = '-c'

    return count_flag


def is_ipaddr(ipaddr):
    '''
    Проверка, является ли переданный аргумент 'ipaddr'
    IP-адресом или нет
    '''
    try:
        ipaddress.ip_address(ipaddr)
        return True
    except ValueError:
        return False


# Основная функция
def host_ping(ipaddrs_list, ping_count='1'):

    # Список доступных адресов в виде строк
    reachable_list = []

    # Список недоступных адресов в виде строк
    unreacheable_list = []


    all_ipaddrs_dict = {
        'Reachable': reachable_list,
        'Unreachable': unreacheable_list
    }

    count_flag = get_count_flag()
    if count_flag is None:
        print('Неизвестная ОС')
        return

    for host in ipaddrs_list:
        if is_ipaddr(host):
            # Если host - строка в виде IP-адреса, то преобразуем host
            # в объект IPv4Address или IPv6Address
            host = ipaddress.ip_address(host)

        # Для любого варианта имени хоста преобразуем его в str
        host_str = str(host)

        # Пингуем и сохраняем результат в res
        res = subprocess.call(['ping', count_flag , ping_count, host_str], stdout=subprocess.DEVNULL)

        '''
        Параметр таймаута в команду ping не передаю, так как он разный для разных платформ
        (применяется таймаут по умолчанию в каждой ОС, который может быть разным для разных ОС).
        
        Windows:
        -w timeout     Timeout in milliseconds to wait for each reply.

        Linux:
        -w deadline
           Specify a timeout, in seconds, before ping exits regardless of how many packets have been sent or received.
           In this case ping does not stop after count packet are sent, it
           waits either for deadline expire or until count probes are answered or for some error notification from network.

        -W timeout
           Time to wait for a response, in seconds. The option affects only timeout in absence of any responses,
           otherwise ping waits for two RTTs.

        Mac OS X:
        -W waittime
            Time in MilliSeconds to wait for a reply for each packet sent.
            If a reply arrives later, the packet is not printed as replied, but considered as replied when
            calculating statistics. n.b. Many other Unix variants specify this option in Seconds.
        '''

        if res == 0:
            print(f'{host_str}: Узел доступен')
            reachable_list.append(host_str)
        else:
            print(f'{host_str}: Узел недоступен')
            unreacheable_list.append(host_str)
    
    return all_ipaddrs_dict


if __name__ == '__main__':
    ipaddrs_list = ['ya.ru', 'gb.ru', '10.10.10.10', '8.8.8.8', '1.1.1.1', '172.16.0.1']
    host_ping(ipaddrs_list)
