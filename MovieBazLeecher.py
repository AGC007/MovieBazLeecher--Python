# - MovieBazLeecher [v1] By AGC007™
# - GitHub : AGC007

import os

print("""          _____  _____ ___   ___ ______ 
    /\   / ____|/ ____/ _ \ / _ \____  |
   /  \ | |  __| |   | | | | | | |  / / 
  / /\ \| | |_ | |   | | | | | | | / /  
 / ____ \ |__| | |___| |_| | |_| |/ /   
/_/    \_\_____|\_____\___/ \___//_/    
                                        
----------------------------------------------                                        
                                        """)

MovieLink = input("Please Enter MovieBaz Link : ")

ServerName_Split = str(MovieLink.split('server=')[1])[0]
URL_Split = str(MovieLink.split('url=')[1])

MovieLink = "http://dl" + ServerName_Split + ".mvbz.bid/" + URL_Split

os.system('cls')

print("""          _____  _____ ___   ___ ______ 
    /\   / ____|/ ____/ _ \ / _ \____  |
   /  \ | |  __| |   | | | | | | |  / / 
  / /\ \| | |_ | |   | | | | | | | / /  
 / ____ \ |__| | |___| |_| | |_| |/ /   
/_/    \_\_____|\_____\___/ \___//_/    
                                        
----------------------------------------------                                        
                                        """)

print("**** Download Link : " , MovieLink , "****")

