'''
Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса. По результатам проверки должно
выводиться соответствующее сообщение.
'''

import ipaddress
from task01 import host_ping, is_ipaddr


def get_start_addr():
    '''
    Функция возвращает объект начального IP-адреса или None
    '''
    start_ipaddr = input('Введите начальный IP-адрес: ')

    while start_ipaddr != 'q':
        if not is_ipaddr(start_ipaddr):
            print()
            print('Вы ввели неправильный IP-адрес')
            start_ipaddr = input('Введите начальный IP-адрес или q для выхода: ')
        else:
            break    
    
    if start_ipaddr == 'q':
        return None
    else:
        return ipaddress.ip_address(start_ipaddr)


def get_num_hosts():
    '''
    Функция возвращает число хостов для проверки или None
    '''
    num_hosts = input('Введите количество хостов для проверки: ')

    while num_hosts != 'q':
        if not num_hosts.isdigit():
            print()
            print('Вы ввели не число')
            num_hosts = input('Введите количество хостов или q для выхода')
        else:
            break
    
    if num_hosts == 'q':
        return None
    else:
        return int(num_hosts)


# Главная функция
def host_range_ping():
    start_addr = get_start_addr()
    if start_addr is None:
        print('IP-адрес не был получен')
        print('Выход')
        return
    
    num_hosts = get_num_hosts()
    if num_hosts is None:
        print('Количество хостов не было получено')
        print('Выход')
        return
    
    # Создаём генератор объектов IP-адресов для проверки
    hosts_gen = (str(start_addr + i) for i in range(num_hosts))
    
    # Вызываем функцию проверки доступности 
    all_ipaddrs_dict = host_ping(hosts_gen)
    return all_ipaddrs_dict


if __name__ == '__main__':
    host_range_ping()