contacts = {
    'number':4,
    'students':[
        {'name':"sree vidya",'email':"sree@gmail.com"},
        {'name':"vihaan",'email':"vihaan@gmail.com"},
        {'name':"kasyap",'email':"kasyap@gmail.com"},
        {'name':"home",'email':"home@gmail.com"}
    ]
}
#if we want both key and value pairs
for key,value in contacts.items():
    print(key,value)
#if we want only value we can use this logic
for value in contacts['students']:
    print(value['email'])