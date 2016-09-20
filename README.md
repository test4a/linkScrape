# linkScrape

      ___                __      ____                                             
      /\_ \    __        /\ \    /\  _`\                                           
      \//\ \  /\_\    ___\ \ \/'\\ \,\L\_\    ___   _ __    __     _____      __   
        \ \ \ \/\ \ /' _ `\ \ , < \/_\__ \   /'___\/\`'__\/'__`\  /\ '__`\  /'__`\ 
         \_\ \_\ \ \/\ \/\ \ \ \\`\ /\ \L\ \/\ \__/\ \ \//\ \L\.\_\ \ \L\ \/\  __/ 
         /\____\\ \_\ \_\ \_\ \_\ \_\ `\____\ \____\\ \_\\ \__/.\_\\ \ ,__/\ \____\
         \/____/ \/_/\/_/\/_/\/_/\/_/\/_____/\/____/ \/_/ \/__/\/_/ \ \ \/  \/____/
                                                                     \ \_\         
                                                                      \/_/ 
    Description: Enumerates employee names from LinkedIn.com
    Created by: Nick Sanzotta/@beamr
***
Installation:

    git clone https://github.com/NickSanzotta/linkScrape.git
    cd linkScrape
    python linkScrape.py --help

***
Default Values:

    If a parameter is not defined it's default value will be choosen.
    Default values listed below.
  
    companyName= 'acme' (used as an example)
    formatValue = 7
    pageResults = 5
    timeout = 5
    
***
Usage(CLI):

    Usage: python linkScrape.py <OPTIONS>
    Example: python linkScrape.py -e LinkedInUser@email.com -c acme -r 1 -t 3 -m 7 -d acme.com
    Example: python linkScrape.py -m 7 -i ~/Company/names.txt
    Raw output saved to: linkedIn/linkScrape-data/Company_time.txt
    Formatted output saved to: linkedIn/linkScrape-data/Company-mangle[x]_time.txt
    
    Login options:
    -e <email> Your LinkedIn.com Email Address.
    -p <pass>  Your LinkedIn.com Password.
    
    Search options:
    -c <company> Company you want to enumerate.(Prepends to filename if used with -i) 
    -r <results> Searches x amount of LinkedIn.com pages (Default is 5).
    -t <secs>    Sets timeout value. (Default is 5.)
  ***
Mangle Options: 
    
    -m <mangle>
        1)FirstLast        ex:nicksanzotta
        2)LastFirst        ex:sanzottanick
        3)First.Last       ex:nick.sanzotta
        4)Last.First       ex:sanzotta.nick
        5)First_Last       ex:nick_sanzotta
        6)Last_First       ex:sanzotta_nick
        7)FLast            ex:nsanzotta
        8)LFirst           ex:snick
        9)FirstL           ex:nicks
        10)F.Last           ex:n.sanzotta
        11)L.Firstname      ex:s.nick
        12)FirLa            ex:nicsa
        13)Lastfir          ex:sanznic  
  
    -d <domain> Append @domain.com to enumerated user list."
    -i <input>  Use local file instead of LinkedIn.com to perform name formatting against."
    Misc:
    
    -h <help>  Prints this help menu.
  
 

***
Usage(Wizard):

    Tip:
    If no paramters are defined the Wizard menu will be launched.

***
To Do:

