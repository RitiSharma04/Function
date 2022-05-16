## Teens drink coke.
## Young adults drink beer.
## Adults drink whisky.
## Make a function that receive age, and return what they drink.
## Rules:-
## Children under 14 old.Teens under 18 old.
## Young under 21 old.
## Adults have 21 or more.
## Examples: (Input --> Output)
## 13 --> "drink toddy"
## 17 --> "drink coke"
## 18 --> "drink beer"
## 20 --> "drink beer"
## 30 --> "drink whisky".



def age(a):
    if a<18:
        print("drink toddy")
    elif a>=18 and a<=21:
        print("drink beer")
    elif a>21:
        print("drink whisky")
a=int(input("enter the age:-"))
age(a)              