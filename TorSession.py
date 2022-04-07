from stem import Signal
from stem.control import Controller
from stem.process import launch_tor_with_config
import stem
from requests_toolbelt.cookies.forgetful import ForgetfulCookieJar
from requests_html import AsyncHTMLSession
from requests import Session 
from anti_useragent import UserAgent
from colorama import Fore, init 
import asyncio


def check_connection():
    """Checks to see if your connection is alive or dead if dead it will activate tor for you"""
    init(True)
    session = Session()
    session.proxies = {'http': 'socks5h://127.0.0.1:9050','https': 'socks5h://127.0.0.1:9050'}
    print(Fore.LIGHTYELLOW_EX + "[>>] Checking Connection to Tor...")

    try:
        resp = session.get("https://httpbin.org/ip")
        if resp.json():
            print(Fore.LIGHTGREEN_EX + "[+] You are Connected To Tor...")
            return 
    except:
        print(Fore.LIGHTYELLOW_EX + "[!] Tor Is Not Activated on your device so we are going to connect it for you")
        print(Fore.LIGHTYELLOW_EX + "[>>] Connecting to tor...")
        activate_Tor()
        print(Fore.LIGHTGREEN_EX + "[+] Tor Has been Activated and You have now been connected to tor")



def activate_Tor(tor_path:str):
    """Turns on tor on ControlPort 9051 You will need to properly setup your path to your 
    tor.exe , Do Not Edit your torrc file!"""

    def print_lines(line):
        if('Bootstrapped' in line):
            print(line)
    tor = launch_tor_with_config(tor_cmd = tor_path, init_msg_handler = print_lines, config = {'ControlPort': '9051'})
    try:
        _ = Controller.from_port()
    except stem.SocketError as exc:
        print("Unable to connect to tor on port 9051: %s" % exc)
    finally:
        tor.terminate()

def roate_tor_curcit():
    """Roates IP Before Starting allowing for a unique Combanation everytime"""
    with Controller.from_port() as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)


async def TorSession(authenticate:bool = False, random:bool = True):
    """Creates a tor Session to used As long as you have made no changes to your torrc file"""
    if authenticate:
        await asyncio.to_thread(check_connection)
    ua = UserAgent(min_version=50)
    Session = AsyncHTMLSession(mock_browser = False)
    # this will be used to kill of Google's Tracking cookies on twitter and other places when were finsihed 
    Session.cookies = ForgetfulCookieJar()
    Session.proxies = {'http': 'socks5h://127.0.0.1:9050','https': 'socks5h://127.0.0.1:9050'}
    Session.headers["User-Agent"] =  ua.random if random else ua.firefox
    return Session
