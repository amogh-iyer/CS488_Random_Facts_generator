import socket
import random

biriyani = ['Biriyani originated from the persian word Birian.', 'Its a popular dish in South India.', 'It has a lot of spices.', 'It tastes really good.', 'Its popular around the world.', 'There is a variety of flavours for biriyani from north to south.' ] 
cats = ['Cats can jump up to six times their length.', 'Cats have 230 bones, while humans only have 206.', 'Cats live longer when they stay indoors.', 'Cats rough tongues can lick a bone clean of any shred of meat.', 'There are cats who have more than 18 toes.']
dogs = ['A dog’s nose print is unique much like a person’s fingerprint.', 'Forty-five percent of U.S. dogs sleep in their owner’s beds.', 'Seventy percent of people sign their dog’s name on their holiday cards.', ' Dogs are not color-blind. They can see blue and yellow.', 'All puppies are born deaf.']
sloth = ['Everything is slow for them.', 'They spend most of their time on trees.', 'They are good at swimming.', 'They are picky for pooping.', 'They are vulnerable to deforestation.' ]


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server.bind(("127.0.0.1",5555))
server.listen(5)

print("Server Running...")


while True:
    conn, addr = server.accept()
    print("Connection From:", addr)
    data = conn.recv(1024)
    msg = data.decode()
    print("I received:", msg)
    #response = "Echo: " + msg
    if msg == 'cats':
        catfact = random.choice(cats)
        response = catfact
        conn.sendall(response.encode())
    elif msg == 'dogs': 
        dogfact = random.choice(dogs)
        response = dogfact
        conn.sendall(response.encode())
    elif msg == 'sloths':
        slothfact = random.choice(sloth)
        response =  slothfact
        conn.sendall(response.encode())
    elif msg == 'biriyani':
        biriyanifact = random.choice(biriyani)
        response = biriyanifact
        conn.sendall(response.encode())
    elif msg == 'quit':
       exit =  print("User wants to exit")
       response = exit
       conn.sendall(response.encode())
    conn.sendall(response.encode())
    

