mporting the requests library 
import requests 
  
# api-endpoint 
url = 'http://10.10.10.171/internal/main.php'

# location given here 
location = "delhi technological university"
      
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location} 
        
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
          
# printing the output 
print("%s"%(r))            
