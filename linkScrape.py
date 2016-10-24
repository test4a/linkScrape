
#!/usr/bin/python
# Nick Sanzotta
# Description: Enumerates employee names from LinkedIn.com based off company search results.
# Version v 1.9222016
import os, sys, getopt, getpass, re, requests, time
from sys import argv 
from bs4 import BeautifulSoup

timestr = time.strftime("%Y%m%d-%H%M")
curr_time = time.time()

class colors:
   white = "\033[1;37m"
   normal = "\033[0;00m"
   red = "\033[1;31m"
   blue = "\033[1;34m"
   green = "\033[1;32m"
   lightblue = "\033[0;34m"

banner = colors.lightblue + r"""
 ___                __      ____                                             
/\_ \    __        /\ \    /\  _`\                                           
\//\ \  /\_\    ___\ \ \/'\\ \,\L\_\    ___   _ __    __     _____      __   
  \ \ \ \/\ \ /' _ `\ \ , < \/_\__ \   /'___\/\`'__\/'__`\  /\ '__`\  /'__`\ 
   \_\ \_\ \ \/\ \/\ \ \ \\`\ /\ \L\ \/\ \__/\ \ \//\ \L\.\_\ \ \L\ \/\  __/ 
   /\____\\ \_\ \_\ \_\ \_\ \_\ `\____\ \____\\ \_\\ \__/.\_\\ \ ,__/\ \____\
   \/____/ \/_/\/_/\/_/\/_/\/_/\/_____/\/____/ \/_/ \/__/\/_/ \ \ \/  \/____/
                                                               \ \_\         
                                                                \/_/         
"""+'\n' \
+ colors.lightblue + '\n linkScrape.py v1.9222016' \
+ colors.normal + '\n Description: Enumerates employee names from LinkedIn.com '\
+ colors.normal + '\n Created by: Nick Sanzotta/@beamr' + '\n'\
+ colors.normal + ' ' + '*' * 95 +'\n' + colors.normal

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def connection(email, password, companyName, pageResults, timeout, output):
    outputTitle = 'linkScrape-data/'+companyName+'_employee-title_'+timestr+'.txt'
    client = requests.Session()
    homepage = 'https://www.linkedin.com'
    login = 'https://www.linkedin.com/uas/login-submit'
    html = client.get(homepage).content
    soup = BeautifulSoup(html,'lxml')
    csrf = soup.find(id="loginCsrfParam-login")['value']
    login_information = {
        'session_key': email,
        'session_password': password,
        'loginCsrfParam': csrf,
        }
    client.post(login, data=login_information)
    companyInfo = ''
    
    # Company Info
    request1 = client.get('https://www.linkedin.com/company/'+companyName)
    m3 = re.findall(r"companyName\"\:\"[\w]*.[\w]", request1.text)
    m4 = re.findall(r"industry\"\:\"[\w]*.[\w][\W]*.[\w]*", request1.text)
    m5 = re.findall(r"size\"\:\"[\w]*.[\w][\W]*.[\w]*", request1.text)
    m6 = re.findall(r"employeeCount\"\:[\w]*.[\w]", request1.text)
    try:
        company = re.sub('companyName":"','', m3[0])
        industry = re.sub('industry":"','', m4[0])
        size = re.sub('size":"','', m5[0])
        employeeCount = re.sub('employeeCount":','', m6[0])
    except IndexError:
      print('[*]Company information not available. ')
    else:
        info= """ 
Company Name: {0}
industry: {1}
{2} + employees
Employees on LinkedIn: {3}
    """
        companyInfo = info.format(company,industry,size,employeeCount)
    print(companyInfo)
    
    r1=client.get('https://www.linkedin.com/vsearch/p?type=people&keywords='+companyName)
    for z in range(1, pageResults):
        time.sleep(timeout)
        r1=client.get('https://www.linkedin.com/vsearch/p?type=people&keywords='+companyName+'&page_num='+str(z))
        m1 = re.findall(r"formatted_name\"\:\"[\w]*.[\w][\W]*.[\w]*", r1.text)
        m2 = re.findall(r"fmt_heading\"\:\"[\w]*.[\w][\W]*.[\w]*", r1.text)
        for i, j in zip(m1,m2):
           x1 = i
           x2 = j
           employee = re.sub('formatted_name":"','', x1)
           title = re.sub('fmt_heading":"','', x2)
           print(employee+' '+':'+' '+title)
           with open(output, 'a') as f:
            x=employee.encode("utf-8")
            f.write(x+"\n")
           with open(outputTitle, 'a') as f:
            x=employee.encode("utf-8")
            y=title.encode("utf-8")
            f.write(x+' '+':'+' '+y+"\n")
    cls()
    print(banner)
    print(companyInfo)
    print("\nEmployee/Title list Saved to: " + outputTitle)
    with open(outputTitle, 'r') as f:
        x = f.read()
    print(x)
    print("Raw Employee list Saved to: " + output)
    with open(output, 'r') as f:
        x = f.read()
    print(x)

def name(companyName, output, formatValue, domain):
    filename = "linkScrape-data/"+companyName+"-"+"mangle-"+str(formatValue)+"_"+timestr+".txt"
    print('Mangled option chosen: '+ str(formatValue))
    print('Mangled list Saved to: '+filename)
    for x in open(output, 'r'):
        full_name = ''.join([c for c in x if  c == " " or  c.isalpha()])
        full_name = full_name.lower().split()
        first_name = full_name[0]
        last_name = full_name[-1]

        if formatValue == 1:
            newname=first_name + last_name
            if domain != '':
                newname = newname+"@"+domain
                write(companyName, formatValue, newname)
                print(newname)
            else:
                write(companyName, formatValue, newname)
                print(newname)
        elif formatValue == 2: 
            newname = last_name + first_name
            if domain != '':
                newname = newname+"@"+domain
                write(companyName, formatValue, newname)
                print(newname)
            else:
                write(companyName, formatValue, newname)
                print(newname)
        elif formatValue == 3:
            newname = first_name + "." + last_name
            if domain != '':
                newname = newname+"@"+domain
                write(companyName, formatValue, newname)
                print(newname)
            else:
                write(companyName, formatValue, newname)
                print(newname)
        elif formatValue == 4:
            newname = last_name + "." + first_name
            if domain != '':
                newname = newname+"@"+domain
                write(companyName, formatValue, newname)
                print(newname)
            else:
                write(companyName, formatValue, newname)
                print(newname)
        elif formatValue == 5:
            newname = first_name + "_" + last_name
            if domain != '':
                newname = newname+"@"+domain
                write(companyName, formatValue, newname)
                print(newname)
            else:
                write(companyName, formatValue, newname)
                print(newname)
        elif formatValue == 6:
            newname = last_name + "_" + first_name
            if domain != '':
                newname = newname+"@"+domain
                write(companyName, formatValue, newname)
                print(newname)
            else:
                write(companyName, formatValue, newname)
                print(newname)
        elif formatValue == 7:
            newname = first_name[0] + last_name
            if domain != '':
                newname = newname+"@"+domain
                write(companyName, formatValue, newname)
                print(newname)
            else:
                write(companyName, formatValue, newname)
                print(newname)
        elif formatValue == 8:
            newname = last_name[0] + first_name
            if domain != '':
                newname = newname+"@"+domain
                write(companyName, formatValue, newname)
                print(newname)
            else:
                write(companyName, formatValue, newname)
                print(newname)
        elif formatValue == 9:
            newname = first_name + last_name[0]
            if domain != '':
                newname = newname+"@"+domain
                write(companyName, formatValue, newname)
                print(newname)
            else:
                write(companyName, formatValue, newname)
                print(newname)
        elif formatValue == 10:
            newname = first_name[0] + "." + last_name
            if domain != '':
              newname = newname+"@"+domain
              write(companyName, formatValue, newname)
              print(newname)
            else:
              write(companyName, formatValue, newname)
              print(newname)
        elif formatValue == 11:
            newname = last_name[0] + "." + first_name
            if domain != '':
              newname = newname+"@"+domain
              write(companyName, formatValue, newname)
              print(newname)
            else:
              write(companyName, formatValue, newname)
              print(newname)
        elif formatValue == 12:
            newname = last_name[0:3] + first_name[0:2]
            if domain != '':
                newname = newname+"@"+domain
                write(companyName, formatValue, newname)
                print(newname)
            else:
                write(companyName, formatValue, newname)
                print(newname)     
        elif formatValue == 13:                               
            newname = last_name[0:4] + first_name[0:3]
            if domain != '':
                newname = newname+"@"+domain
                write(companyName, formatValue, newname)
                print(newname)
            else:
                write(companyName, formatValue, newname)
                print(newname)  
        else:
            sys.exit(2)

def write(companyName, formatValue, newname):
    filename = "linkScrape-data/"+companyName+"-"+"mangle-"+str(formatValue)+"_"+timestr+".txt"
    with open(filename, 'a') as f:
        f.write(newname+"\n")


def help():
    print banner
    print " Usage: python linkScrape.py <OPTIONS> \n"
    print " Example: python linkScrape.py -e LinkedInUser@email.com -c acme -r 1 -t 3 -m 7 -d acme.com\n"
    print " Example: python linkScrape.py -m 7 -i ~/Company/names.txt\n"
    print " Raw output saved to: linkedIn/linkScrape-data/Company_time.txt "
    print " Formatted output saved to: linkedIn/linkScrape-data/Company-mangle[x]_time.txt \n"
    print colors.lightblue + " Login options:\n" + colors.normal
    print "\t -e <email>\t\tYour LinkedIn.com Email Address. "
    print "\t -p <pass>\t\tYour LinkedIn.com Password. "
    print colors.lightblue + "\n Search options:\n" + colors.normal
    print "\t -c <company>\t\tCompany you want to enumerate.(Prepends to filename if used with -i) "
    print "\t -r <results>\t\tSearches x amount of LinkedIn.com pages (Default is 5)."
    print "\t -t <secs>\t\tSets timeout value. (Default is 5.)"
    print colors.lightblue + "\n Mangle options:\n" + colors.normal
    print """\t -m <mangle>\t\t  
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
    """
    print "\t -d <domain>\t\tAppend @domain.com to enumerated user list."
    print "\t -i <input>\t\tUse local file instead of LinkedIn.com to perform name Mangle against."
    print colors.lightblue + "\n Misc:\n" + colors.normal
    print "\t -h <help>\t\tPrints this help menu."
    sys.exit(2)

def main(argv):
    print(banner)
    email= ''
    password= ''
    companyName= ''
    formatValue = 7
    pageResults = 5
    timeout = 5
    domain = ''
    outputTitle = ''

    if not os.path.exists("linkScrape-data/"):
        os.mkdir("linkScrape-data/")

    if len(argv) < 1:
        print('\n')
        #WIZARD Menu: If no args are defined the wizard will be launched.
        print('['+colors.red+'*'+colors.normal+']You did not specify a parameter the wizard has launched:')
        print('['+colors.lightblue+'*'+colors.normal+']Example: python linkScrape.py -e user@email.com -c acme')
        print('[*]For help & command line options please use: python linkScrape.py --help\n')
        email = raw_input('Enter LinkedIn Email account[user@email.com]: ') or email
        print('ENTERED: "%s"' % email + '\n')
        
        password = getpass.getpass('Enter LinkedIn Password: ') or password
        
        companyName = raw_input('Enter Company[ex:acme]: ') or companyName
        output = 'linkScrape-data/'+companyName+'_'+timestr+'.txt'
        print('ENTERED: "%s"' % companyName + '\n')
        
        print colors.lightblue + "\n Mangle options:\n" + colors.normal
        print """\t -m <mangle>\t\t  
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
        """
        formatValue = raw_input('Enter name Managle choice[ex:7]: ') or formatValue
        formatValue = int(formatValue)
        print('ENTERED: "%s"' % formatValue + '\n')

        print('[*]TIP: This value will determine how many page results will be returned.')
        pageResults = raw_input('Enter number of pages results[ex:5]: ') or pageResults
        pageResults = int(pageResults)
        pageResults+=1
        print('ENTERED: "%s"' % pageResults + '\n')

        print('[*]TIP: This value will determine how long of a delay(in seconds) each page will be scraped.')
        timeout = raw_input('Enter timeout value[ex:5]: ') or timeout
        timeout = int(timeout)
        print('ENTERED: "%s"' % timeout + '\n')

        print('[*]TIP: This value will be added to the end of each mangled result[ex:jsmith@acme.com].')
        domain = raw_input('Enter Domain suffix[ex:acme.com]: ') or domain
        print('ENTERED: "%s"' % domain + '\n')
        cls()
        print(banner)
        connection(email, password, companyName, pageResults, timeout, output)
        name(companyName, output, formatValue, domain)
        print "\nCompleted in: %.1fs\n" % (time.time() - curr_time)

    else:
        try:
            opts, args = getopt.getopt(argv, 'e:c:r:t:o:m:d:i:h',['email=','company=','results=','timeout=','output=','mangle=','--domain=','--input=','help'])
            #GETOPT Menu: 
            for opt, arg in opts:
                if opt in ('-h', '--help'):
                    help()
                    sys.exit(2)
                elif opt in ('-e', '--email'):
                    email = arg
                    password = getpass.getpass(r'Enter password: ')
                elif opt in ('-c', '--company'):
                    companyName = arg
                    output = 'linkScrape-data/'+companyName+'_'+timestr+'.txt'
                elif opt in ('-r', '--results'):
                    pageResults = int(arg)
                    pageResults+=1
                elif opt in ('-t', '--timeout'):
                    timeout = int(arg)
                elif opt in ('o','--output'):
                    output = arg
                elif opt in ('-m', '--mangle'):
                    formatValue = int(arg)
                elif opt in ('-d','--domain'):
                    domain = arg
                elif opt in ('-i','--input'):
                    inputfile = arg
                    output = inputfile
                    name(companyName, output, formatValue, domain)
                    sys.exit(2)
                else:
                    help()
                    sys.exit(2)
            connection(email, password, companyName, pageResults, timeout, output)
            name(companyName, output, formatValue, domain)
            print "\nCompleted in: %.1fs\n" % (time.time() - curr_time)

        except getopt.GetoptError:
            help()
            sys.exit(2)


if __name__ == "__main__":
    main(argv[1:])
