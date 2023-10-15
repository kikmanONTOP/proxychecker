import requests
from colorama import Fore

ascii = '''
                                                                                                                     ..                              
                                                      ..                        .uef^"                         < .z@8"`                              
 .d``            .u    .          u.      uL   ..    @L                       :d88E                             !@88E                      .u    .   
 @8Ne.   .u    .d88B :@8c   ...ue888b   .@88b  @88R 9888i   .dL           .   `888E            .u          .    '888E   u         .u     .d88B :@8c  
 %8888:u@88N  ="8888f8888r  888R Y888r '"Y888k/"*P  `Y888k:*888.     .udR88N   888E .z8k    ud8888.   .udR88N    888E u@8NL    ud8888.  ="8888f8888r 
  `888I  888.   4888>'88"   888R I888>    Y888L       888E  888I    <888'888k  888E~?888L :888'8888. <888'888k   888E`"88*"  :888'8888.   4888>'88"  
   888I  888I   4888> '     888R I888>     8888       888E  888I    9888 'Y"   888E  888E d888 '88%" 9888 'Y"    888E .dN.   d888 '88%"   4888> '    
   888I  888I   4888>       888R I888>     `888N      888E  888I    9888       888E  888E 8888.+"    9888        888E~8888   8888.+"      4888>      
 uW888L  888'  .d888L .+   u8888cJ888   .u./"888&     888E  888I    9888       888E  888E 8888L      9888        888E '888&  8888L       .d888L .+   
'*88888Nu88P   ^"8888*"     "*888*P"   d888" Y888*"  x888N><888'    ?8888u../  888E  888E '8888c. .+ ?8888u../   888E  9888. '8888c. .+  ^"8888*"    
~ '88888F`        "Y"         'Y"      ` "Y   Y"      "88"  888      "8888P'  m888N= 888>  "88888%    "8888P'  '"888*" 4888"  "88888%       "Y"      
   888 ^                                                    88F        "P'     `Y"   888     "YP'       "P'       ""    ""      "YP'                 
   *8E                                                     98"                      J88"                                                             
   '8>                                                   ./"                        @%                                                               
    "                                                   ~`                        :"                                                                 
                                                        made by https://github.com/kikmanONTOP with love :3
    
    
    
    '''

print(Fore.CYAN + ascii)

def check_proxy(proxy, proxy_type, checked_proxies):
    if proxy in checked_proxies:
        return
    
    proxies = {
        "http": f"{proxy_type}://{proxy}",
        "https": f"{proxy_type}://{proxy}"
    }
    
    try:
        response = requests.get("http://www.google.com", proxies=proxies, timeout=0.1)
        if response.status_code == 200:
            print(Fore.LIGHTGREEN_EX + f"Proxy {proxy} is valid ({proxy_type}).")
            with open("working_proxies.txt", "a") as file:
                file.write(f"{proxy} ({proxy_type})\n")
        else:
            print(Fore.RED + f"Proxy {proxy} is not valid ({proxy_type}).")
    except requests.exceptions.RequestException:
        print(Fore.RED + f"Proxy {proxy} is not valid ({proxy_type}).")
    
    checked_proxies.add(proxy)

def main():
    proxy_file = input(Fore.LIGHTMAGENTA_EX + "name of file with proxies: ")
    
    checked_proxies = set()
    
    with open(proxy_file, "r") as file:
        proxies = file.readlines()
    
    for proxy in proxies:
        proxy = proxy.strip()
        check_proxy(proxy, "http", checked_proxies)
        check_proxy(proxy, "socks4", checked_proxies)
        check_proxy(proxy, "socks5", checked_proxies)

if __name__ == "__main__":
    main()
