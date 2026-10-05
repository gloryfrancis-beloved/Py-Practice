
# file = open("love letter.txt","w")
# file.write('I love you so much \n')
# file.write('You mean so much to me \n')
# file.write('You are the air that i breathe in \n')
# file.write('You are my only')
# file.write('Please i need your reply')
# file.write('Im waiting,please')
# file.write(f'this is my lover reply ===> {Reply}')
# file.close()

# Reply = input('What do you have in mind about me?')

# with open("letter of apology.json", "w") as file:
    # file.write('I am tending this apology message because i really do regret what I did to you, my darling \n')
    # file.write('I am sincerely sorry for my misconducts \n')
    # file.write('Please forgive me my dearest.')

# file = open('names.txt', 'r')
# print(file.read())
# file.close()

# file = open('message.txt', 'w')
# file.write('I am learning Python file handling')
# file.close()

# file = open('message.txt,' 'a')
# file.write('I am getting better at it')
# with open('about_me.txt','w') as document:
# #     document.write('My name is Glory.\n')
# #     document.write('I am learning Python.\n') 
#     document.write('I am a cybersecurity student.\n')

# with open("about_me.txt", 'a') as document:
#         document.write('\nI want to become good at cybersecurity.')



# line = "2026-09-16 - Glory - Login failed - 192.168.1.15"

# print(f"Date: {line.split(' - ')[0]}")
# print(f"Username: {line.split(' - ')[1]}")
# print(f"Status: {line.split(' - ')[2]}")
# print(f"IP address: {line.split(' - ')[3]}")
        

count = 0
with open("login.log.txt", 'r') as file:
          
    for soul in file:
       name = soul.split(' - ')
       if "failed" in soul:
          print(f'Failed user : {name[1]} | IP: {name[3]}')
          count= count +1
          
    print(f"Total failed login attempts: {count}")
          
          

    
