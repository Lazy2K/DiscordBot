#instagram stat finder
import requests

def stat_find(username):
    x = requests.get("https://www.instagram.com/" + username + "/")
    if x.text[201:209:] == "Page Not":
        return "non"
    else:
        start = 9400
        output = ""
        a = 0
        b = 0
        stats = ""
        stats2 = []
        for i in range(9450, 9600):
            if x.text[i:i + 7:] == "content":
                a = i
                stats = (x.text[a + 9:a + 9 + 70:])
                

        stats2 = stats.split("-")
        return stats2[0]

                        
                    
            
            

            
                
                        
                    
                
                

        

stat_find("__douglasc")
