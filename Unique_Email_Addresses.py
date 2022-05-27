#Problem statement: 
#Valid emails ignore text after '+' in domain name,and replaces '.' in domain name with null.
#Function returns the number of valid emails in list of 'emails' passed as input for the function.
  
def numUniqueEmails(self, emails):
  #list to store final email list
  email_final = []
        
  #loop through the emails
  for i in emails:
    email_new = ''
    #extract ussername and domain name
    uname = i.split("@",)[0]
    dmain = i.split("@",)[1]
            
   #check for dots and '+'
    if '.' in uname or '+' in uname:
      uname = uname.replace('.','')
            
      uname_new = uname.split("+",)[0]
      #concatenate filtered uname and domain name
      email_new = uname_new + '@'+ dmain  
      
    else:
      email_new = i
      
    #add to final list if not present        
    if email_new not in email_final:
      email_final.append(email_new)
     
  return len(email_final)
