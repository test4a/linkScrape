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
    
    3rd Party Python libraries may be required:
    pip install beautifulsoup4
    pip install bs4
    pip install lxml

***
Caveats

    Does not utilize LinkedIn's API.(This is a pure Web Scraper)
    LinkedIn Account may be flagged or banned.
    LinkedIn.com account will need 10+ connections/profile strength to perform searches.
    (This is a rough estimate based on current feedback)
    Company search results have a monthly cap.
    Script still has some minor bugs when scraping some character sets.

***
Default Values:

    If a parameter is not defined it's default value will be choosen.
    Default values listed below.
  
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
        10)F.Last          ex:n.sanzotta
        11)L.Firstname     ex:s.nick
        12)FirLa           ex:nicsa
        13)Lastfir         ex:sanznic  
  
    -d <domain> Append @domain.com to enumerated user list."
    -i <input>  Use local file instead of LinkedIn.com to perform name Mangle against."
    Misc:
    
    -h <help>  Prints this help menu.
  
 

***
Usage(Wizard):

    [*]You did not specify a parameter the wizard has launched:
      [*]Example: python linkScrape.py -e user@email.com -c acme
      [*]For help & command line options please use: python linkScrape.py --help
      
      Enter LinkedIn Email account[user@email.com]: 
      ENTERED: "user@email.com"
      
      Enter LinkedIn Password: 
      Enter Company[acme]: 
      ENTERED: "acme"
      
      
       Mangle options:
      
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
              
      Enter name Managle choice[ex:7]: 
      ENTERED: "7"
      
      [*]TIP: This value will determine how many page results will be returned.
      Enter number of pages results[ex:2]: 
      ENTERED: "5"
      
      [*]TIP: This value will determine how long of a delay(in seconds) each page will be scraped.
      Enter timeout value[ex:5]: 
      ENTERED: "5"
      
      [*]TIP: This value will be added to the end of each mangled result[ex:jsmith@acme.com].
      Enter Domain suffix[ex:acme.com]: 
      ENTERED: ""


***
Output Sample:

      Employee/Title list Saved to: linkScrape-data/acme_employee-title_20160920-1523.txt
      Robert Dukes : Security Lead
      Chang Xiu : President
      Danny Glover : Alliances Manager
      Rob Becker : SQA Engineer

      Raw Employee list Saved to: linkScrape-data/acme_20160920-1523.txt
      Robert Dukes
      Chang Xiu
      Danny Glover
      Rob Becker
      
      Mangled option chosen: 7
      Mangled list Saved to: linkScrape-data/acme-mangle-7_20160920-1523.txt
      rdukes
      cxiu
      dglover
      rbecker
      
      Completed in: 21.9s



