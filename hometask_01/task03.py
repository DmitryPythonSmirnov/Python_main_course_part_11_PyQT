'''
Написать функцию host_range_ping_tab(), возможности которой основаны на функции из
примера 2. Но в данном случае результат должен быть итоговым по всем ip-адресам,
представленным в табличном формате (использовать модуль tabulate).
'''

from tabulate import tabulate
from task02 import host_range_ping

def host_range_ping_tab():
    all_ipaddrs_dict = host_range_ping()
    print(tabulate(all_ipaddrs_dict, headers='keys', tablefmt='grid'))


if __name__ == '__main__':
    host_range_ping_tab()
