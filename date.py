 

months={}
months ['01']='January'
months ['02']='February'
months ['03']='March'
months ['04']='April'
months ['05']='May'
months ['06']='June'
months ['07']='July'
months ['08']='August'
months ['09']='September'
months ['10']='October'
months ['11']='November'
months ['12']='December'

def date():
  
    
    days=x[0:2]
    month=x[3:5]
    years=x[6:]
    if y=='beginning':
        for s, t in months.iteritems():
            if month==s:
                print t, days, years
    else:
        for s, t in months.iteritems():
            if month==s:
                print days, t, years
if __name__=="__main__":
    y=raw_input('Would you like to type the month at the "beginning" or "middle"? ')
    x=raw_input('Type a date in the form of 0x-0y-z ')
    date()
    
            
