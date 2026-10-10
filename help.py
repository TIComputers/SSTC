from colorama import Fore
import platform
import os


def clear():
    if platform.system() == "Windows":
        cmd = "cls"
    else:
        cmd = "clear"
    os.system(cmd)


def Help():
    clear()
    option = f"""{Fore.RED}

       |                 |          ┏┓┏┓╋┏┓
       |!               !|          ┗┓┗┓┃┃ 
       |!               !|          ┗┛┗┛┗┗┻
       |1               1|          SECURE AND SIMPLE TERMINAL COMMUNICATION
       |@               @|                
       |@!             !@|             
       |@!             !@|          {Fore.LIGHTWHITE_EX}SSTC is a command-line application that allows{Fore.RED}    
       |@@             @@|          {Fore.LIGHTWHITE_EX}two users to establish text-based communication.{Fore.RED}   
       |@!@           @!@|          {Fore.LIGHTWHITE_EX}The goal is to provide a secure and simple connection{Fore.RED}   
         |@!@       @!@|            {Fore.LIGHTWHITE_EX}in a terminal environment. In future updates, a server{Fore.RED}      
           |@!@   @!@|              {Fore.LIGHTWHITE_EX}will also be available, enabling account creation,{Fore.RED}   
             |@!@!@|                {Fore.LIGHTWHITE_EX}chat message storage, group creation, and timezone setting.{Fore.RED} 
              _|@|_                      
            _|@| |@|_                   
          _|@|     |@|_                
         |@|_       _|@|                 
           |@|_   _|@|               
             |@|_|@|                      
               |@|


{Fore.LIGHTYELLOW_EX}--- General Options ---{Fore.RESET}{Fore.LIGHTWHITE_EX}
 --help                             Show this help message and exit
 --update                           For The Next Update
 --log                              Enable logging (save to Log file)
 --them <color>                     red, green (Default is red)

{Fore.LIGHTYELLOW_EX}--- Server (Listener) Mode Options ---{Fore.RESET}{Fore.LIGHTWHITE_EX}
 -l    --listen                     Run in listening/server mode
 -li   --listen-ip                  IP address to listen on (e.g., 0.0.0.0)
 -lp   --listen-port                Port number to listen on
 -z    --timezone <timezone_name>   Specify the timezone for server operations (e.g., 'UTC', 'Asia/Tehran')
 -t    --timeout <seconds>          Maximum time to wait for a connection in seconds

{Fore.LIGHTYELLOW_EX}--- Client Mode Options ---{Fore.RESET}{Fore.LIGHTWHITE_EX}
 -c    --client                     Run in client mode to connect to a remote server
 -h    --host <ip_address>          Target host IP address to connect to
 -p    --port <port_number>         Target port number on the host to connect to

{Fore.LIGHTYELLOW_EX}--- EnCryption Mode Options ---{Fore.RESET}{Fore.LIGHTWHITE_EX}
 For The Next Update

{Fore.LIGHTYELLOW_EX}--- Display Timezones ---{Fore.RESET}{Fore.LIGHTWHITE_EX}
 --timezone-asia                    Display Asia timezones
 --timezone-europe                  Display Europe timezones
 --timezone-america                 Display America timezones
 --timezone-africa                  Display Africa timezones
 --timezone-australia               Display Australia & Pacific timezones

{Fore.RESET} 
"""
    print(option)


def Asia():
    zones = f'''
{Fore.YELLOW}--- Asis TimeZones ---{Fore.LIGHTWHITE_EX}
 -z Asia/Almaty
 -z Asia/Baghdad
 -z Asia/Baku
 -z Asia/Bangkok
 -z Asia/Dhaka
 -z Asia/Dubai
 -z Asia/Hong_Kong
 -z Asia/Islamabad        Not IANA official, use Asia/Karachi
 -z Asia/Jakarta
 -z Asia/Jerusalem
 -z Asia/Kabul
 -z Asia/Karachi
 -z Asia/Kathmandu
 -z Asia/Kolkata
 -z Asia/Manila
 -z Asia/Novosibirsk
 -z Asia/Riyadh
 -z Asia/Seoul
 -z Asia/Shanghai
 -z Asia/Singapore
 -z Asia/Tehran
 -z Asia/Tbilisi
 -z Asia/Tokyo
 -z Asia/Urumqi
 -z Asia/Yerevan

Please copy this...{Fore.RESET} '''
    print(zones)
    
    
def Africa():
    zones = f'''
{Fore.YELLOW}--- Africa Timezones ---{Fore.LIGHTWHITE_EX}
 -z Africa/Accra
 -z Africa/Addis_Ababa
 -z Africa/Algiers
 -z Africa/Bamako
 -z Africa/Cairo
 -z Africa/Casablanca
 -z Africa/Dakar
 -z Africa/Harare
 -z Africa/Johannesburg
 -z Africa/Khartoum
 -z Africa/Lagos
 -z Africa/Luanda
 -z Africa/Nairobi
 -z Africa/Tripoli
 -z Africa/Tunis
 -z Africa/Windhoek

Please copy this...{Fore.RESET} '''
    print(zones)


def Australia():
    zones = f'''
{Fore.YELLOW}--- Australia Timezones ---{Fore.LIGHTWHITE_EX}
 -z Australia/Adelaide
 -z Australia/Brisbane
 -z Australia/Darwin
 -z Australia/Hobart
 -z Australia/Melbourne
 -z Australia/Perth
 -z Australia/Sydney
 -z Pacific/Auckland           New Zealand
 -z Pacific/Fiji
 -z Pacific/Guam
 -z Pacific/Port_Moresby

Please copy this...{Fore.RESET} '''
    print(zones)


def America():
    zones = f'''
{Fore.YELLOW}--- America Timezones ---{Fore.LIGHTWHITE_EX}
 -z America/Anchorage
 -z America/Argentina/Buenos_Aires
 -z America/Bogota
 -z America/Caracas
 -z America/Chicago
 -z America/Denver
 -z America/El_Salvador
 -z America/Guatemala
 -z America/Halifax
 -z America/Lima
 -z America/Los_Angeles
 -z America/Managua
 -z America/Mexico_City
 -z America/Montevideo
 -z America/New_York
 -z America/Phoenix
 -z America/Sao_Paulo
 -z America/Toronto
 -z America/Vancouver

Please copy this...{Fore.RESET} '''
    print(zones)


def Europe():
    zones = f'''
{Fore.YELLOW}--- Europe Timezones ---{Fore.LIGHTWHITE_EX}
 -z Europe/Amsterdam
 -z Europe/Athens
 -z Europe/Belgrade
 -z Europe/Berlin
 -z Europe/Bucharest
 -z Europe/Copenhagen
 -z Europe/Helsinki
 -z Europe/Istanbul
 -z Europe/Kiev
 -z Europe/Lisbon
 -z Europe/London
 -z Europe/Madrid
 -z Europe/Moscow
 -z Europe/Oslo
 -z Europe/Paris
 -z Europe/Prague
 -z Europe/Rome
 -z Europe/Sofia
 -z Europe/Stockholm
 -z Europe/Vienna
 -z Europe/Warsaw
 -z Europe/Zurich

Please copy this...{Fore.RESET} '''
    print(zones)


if __name__ == "__main__":
    pass