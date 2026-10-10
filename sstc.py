from coordinator import Coordinator
from colorama import Fore
import argparse
import help
import sys


class SSTC:
    def __init__(self):
        self.colors = ["red", "green"]
        
        # general option
        self.them = "red"
        self.updt = None
        self.mode = None
        self.zone = None
        self.tout = None
        
        # ip , port
        self.host = None
        self.port = None
        
        self.__sstc()
        #timezone


    def excute(self):
        excut = Coordinator(
            self.host,
            self.port,
            self.mode,
            self.them,
            self.tout,
        )
        excut.run()
    
    
    def __sstc(self):
        
        if "--help" in sys.argv:
            help.Help()
            sys.exit()
        
        parser = argparse.ArgumentParser(description="sstc", add_help=False)
        
        # --- general option ---
        parser.add_argument("--log",   action="store_true", help="Enable Log Mode")
        parser.add_argument("--update",action="store_true", help="Update Settings and Library")
        parser.add_argument("--them",  type=str,            help="Select Them Color (green, red)")
        
        # --- listener option ---
        parser.add_argument("-l",  "--listen",      action="store_true", help="Run in listening/server mode")
        parser.add_argument("-li", "--listen-ip",   type=str,            help="IP address to listen on (e.g., 0.0.0.0)")
        parser.add_argument("-lp", "--listen-port", type=int,            help="Port number to listen on")
        parser.add_argument("-tz", "--timezone",    type=str ,help="Specify the timezone for server operations (e.g., 'UTC', 'Asia/Tehran')")
        parser.add_argument("-to", "--timeout",     type=int ,help="Maximum time to wait for a connection in seconds")
        
        # --- client option ---
        parser.add_argument("-c", "--client", action="store_true", help="Run in client mode to connect to a remote server")
        parser.add_argument("-h", "--host",   type=str, help="Target host IP address to connect to")
        parser.add_argument("-p", "--port",   type=int, help="Target port number on the host to connect to")
        
        # --- encryption optoin ----
        # for the next update
        
        # --- display timezones ---
        parser.add_argument("--timezone-asia",      action="store_true", help="Display Asia timezones")
        parser.add_argument("--timezone-europe",    action="store_true", help="Display Europe timezones")
        parser.add_argument("--timezone-america",   action="store_true", help="Display America timezones")
        parser.add_argument("--timezone-africa",    action="store_true", help="Display Africa timezones")
        parser.add_argument("--timezone-australia", action="store_true", help="Display Australia & Pacific timezones")

        # --- ---
        args = parser.parse_args()

        # --- general option ---
        if args.log:
            self.log = True
            print(Fore.RED + "[!] Log activated" + Fore.RESET)


        if args.them:
            if args.them in self.colors:
                self.them = args.them
            else:
                print(Fore.RED + "[!] There is no color in the list" + Fore.RESET)
                sys.exit()

        if args.update:
            print(Fore.RED + "[?] in the next updates" + Fore.RESET)
            sys.exit()
        
        # --- listener/clinet option ---
        if args.listen and args.client:
            print(Fore.RED + "[!] Error: Cannot use --listen and --client modes simultaneously." + Fore.RESET)
            sys.exit()


        elif args.listen:
            self.mode = "listen"
            if args.listen_ip:
                self.host = args.listen_ip

            if args.listen_port is not None:
                self.port = args.listen_port
            
            if self.host is None or self.port is None:
                print(Fore.RED + "[!] For listen mode, --listen-ip and --listen-port are required." + Fore.RESET)
                sys.exit()


        elif args.client:
            self.mode = "client"
            if args.host:
                self.host = args.host

            if args.port is not None:
                self.port = args.port
        
            if self.host is None or self.port is None:
                print(Fore.RED + "[!] For listen mode, --listen-ip and --listen-port are required." + Fore.RESET)
                sys.exit()
            
        else:
            help.Help()
            sys.exit()
            
            
        if args.timezone:
            self.zone = args.timezone

        if args.timeout:
            self.tout = args.timeout
        else:
            self.tout = 30
         
        # --- display timezones ---
        if args.timezone_asia:
            help.Asia()
            sys.exit()

        if args.timezone_europe:
            help.Europe()
            sys.exit()

        if args.timezone_america:
            help.America()
            sys.exit()

        if args.timezone_africa:
            help.Africa()
            sys.exit()

        if args.timezone_australia:
            help.Australia()
            sys.exit()

if __name__ == "__main__":
    app = SSTC()
    app.excute()