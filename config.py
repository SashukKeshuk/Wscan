in_port_php = 6012
ch = 1024
tkn = "6776300881:AAHFxX7txU9l-CuaIJNDuhjKtiJa7Un3L7A"
OAI = "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"
XCC_API = "d1aeeade-1846-443b-90b0-d34708afbfdf"
HOST = "127.0.0.1"
USR_NAME = "root"
USR_PSWD = ""
DB_NAME = "Web_scanner"

EX_PATH = "chromedriver.exe"

LST = [
    "Dotdotpwn",
    "Nuclei",
    "Sn1per",
    "Dirb",
    "SQLmap",
    "Subfinder",
    "WPscan",
    "CMSmap",
    "Nmap",
    "Knocker",
    "PHPvuln",
    "Crlfuzz",
]
CMS = dict()
CMS = {
    "Dotdotpwn" : "dotdotpwn -m http -h ^^^^",
    "Nuclei" : "nuclei -u ^^",
    "Sn1per" : "sniper -t ^^",
    "Dirb" : "dirb ^^ /usr/share/wordlists/dirb/common.txt",
    "SQLmap" : "sqlmap -u ^^",
    "Subfinder" : "subfinder -d ^^",
    "WPscan" : "wpscan --url ^^ --ignore-main-redirect",
    "CMSmap" : "python3 cmsmap.py ^^",
    "Nmap" : "nmap -v -A -sV ^^^^",
    "Knocker" : "knocker --host ^^^^",
    "PHPvuln" : " ",
    "Crlfuzz" : "crlfuzz -u \"^^\"",
}