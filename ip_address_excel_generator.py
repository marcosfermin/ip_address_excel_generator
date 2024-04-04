# IP Address Range Excel Generator
# Author: Marcos Fermin
# This Python script generates an Excel file containing IP addresses within a specified range of IP addresses.
# The script generates IP addresses from the start IP address to the end IP address.
# The IP addresses are generated in the 3rd and 4th octets of the IP address.
# The script generates an Excel file with the IP addresses in the first column.
# The Excel file is saved as 'IP_addresses.xlsx' in the same directory as the script.

from openpyxl import Workbook

def generate_ips(start_ip, end_ip):
    start_octets = list(map(int, start_ip.split('.')))
    end_octets = list(map(int, end_ip.split('.')))

    ips = []

    for i in range(start_octets[2], end_octets[2] + 1):
        for j in range(start_octets[3], end_octets[3] + 1):
            ips.append(f'{start_octets[0]}.{start_octets[1]}.{i}.{j}')

    return ips

def generate_excel_file(ips):
    wb = Workbook()
    ws = wb.active
    ws.append(['IP Address'])

    for ip in ips:
        ws.append([ip])

    wb.save('IP_addresses.xlsx')
    print("Excel file 'IP_addresses.xlsx' has been generated successfully.")

start_ip = '192.168.0.0'
end_ip = '192.168.255.255'

ips = generate_ips(start_ip, end_ip)
generate_excel_file(ips)
