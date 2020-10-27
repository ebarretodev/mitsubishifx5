import socket
from time import sleep

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connectPLC(dest):
    client.connect(dest)
    return True

def disconnectPLC():
    client.close()
    return True

def read_D(start_digit, device_num=1):

    subheader = '5000'
    network_number = '00'
    destination_station = 'FF'
    destination_IO_number = '03FF'
    request_multi_drop = '00'
    reserved_data = '0000'
    command = '0401'
    subcommand = '0000'
    device_code = 'D*'
    head_device = format(start_digit, '06')
    number_device = format(device_num, '04')

    str2= reserved_data + command + subcommand + device_code +head_device +number_device
    request_data_length = format(len(str2), '04X')

    str1 = subheader + network_number + destination_station + \
           destination_IO_number + request_multi_drop + request_data_length +str2

    res = ''

    while res == '':
        try:
            client.send(bytes(str1, 'utf-8'))
            print('send')
            res = str(client.recv(1024), 'utf-8')
            print('receive')
        except:
            pass


    if res[0:4] == 'D000' and res[4:14] == str1[4:14]:
        # print(res[14:])
        if res[18:22] == '0000':
            # print('quantidade: ' + res[14:18])
            # print('data: ' + res[22:])
            return int(res[22:], 16)
        else:
            return res[18:22]
    else:
        # print('Error Communication')
        return 'E9999'

def write_D(start_digit, value, device_num=1):

    subheader = '5000'
    network_number = '00'
    destination_station = 'FF'
    destination_IO_number = '03FF'
    request_multi_drop = '00'
    reserved_data = '0000'
    command = '1401'
    subcommand = '0000'
    device_code = 'D*'
    head_device = format(start_digit, '06')
    number_device = format(device_num, '04')
    value_device = format(value, '04X' )

    str2= reserved_data + command + subcommand + device_code +head_device +number_device +value_device
    request_data_length = format(len(str2), '04X')

    str1 = subheader + network_number + destination_station + \
           destination_IO_number + request_multi_drop + request_data_length +str2

    res=''
    while res=='':
        try:
            client.send(bytes(str1, 'utf-8'))
            print('send')
            res = str(client.recv(1024), 'utf-8')
            print('receive')

        except:
            pass

    if res[0:4] == 'D000' and res[4:14] == str1[4:14]:
        if res[18:22] == '0000':
            return value
        else:
            return res[18:22]
    else:
        # print('Error Communication')
        return 'E9999'


if __name__ == "__main__":
    host = '192.168.3.250'
    port = 3000
    dest = (host, port)
    connectPLC(dest)
    # a = is_open(host)
    for i in range(11):
        a = read_D(100)  # read the contents of a register
        print('Value from D100: ' + str(a))
        b = read_D(101)
        print('Value from D101: ' + str(b))
        c = write_D(102, i*10)
        print('Value D102 set to: ' + str(c))
        d = write_D(103, i*15 )
        print('Value D103 set to: ' + str(d))
        sleep(2)

    disconnectPLC()