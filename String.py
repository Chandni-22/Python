'''String Methods'''
''

'''Q-1.) Find the length of a String.'''

'''With methods'''
# a=input()
# print(len(a))

'''Without methods'''
# a='aqwsedrftgyhujikolp'
# c=0
# i=0
# while True:
#   if a[i]==a[-1]:
#     c+=1
#     print(c)
#     break
#   else:
#     c+=1
#   i+=1

'''Q-2.) Remove "@" & "." from the string.'''
# a='sweetyvish2511@gmail.org'
# i=0
# c=''
# while i<len(a):
#   if a[i]=='@' or a[i]=='.':
#     print(c,end='')
#     c=''
#   else:
#     c+=a[i]
#   i+=1

'''Q-2.) Replace "q" to "*" in the string. ans="*wdesdf**ewewd**".'''

'''With methods'''
# a='qwdesdfqqewewdqq'
# ans=a.replace('q','*')
# print(ans)

'''Without methods'''
# a='qwdesdfqqewewdqq'
# ans=''
# for i in range(len(a)):
#   if a[i]=='q':
#     ans+='*'
#   else:
#     ans+=a[i]
# print(ans)

'''Q-3.) Insert "n" in 3rd position.'''
# l='abcde'
# i=0
# a=''
# while i<len(l):
#   if i==3:
#       a+='n'
#       a+=l[i]
#   else:
#     a+=l[i]
#   i+=1
# print(a)

'''Q-4.) Find a character in a string and check the smallest index for the same character. (if duplicate else print the only index found with letter in a string like (s='aman' o/p==a0 m1 n3))'''
# a=input()
# i=0
# l=""
# while i<len(a):
#   if a[i] not in l:
#     l+=a[i]
#     l+=str(i)
#     l+=" "
#   i+=1
# print(l)

'''Q-5.) Check if the character is uppercase or lowercase then convert it to vice versa. (i.e, upper to lower and lower to upper)'''
# a=input()
# i=0
# while i<len(a):
#   if a[i]>"a" and a[i]<"z":
#     print(a[i].upper(),end="")
#   else:
#     print(a[i].lower(),end="")
#   i+=1

'''Q-6.) Check if string is a pangram or not (having all 26 letters).'''
# a=input()
# b=""
# i=0
# s=a.lower()
# while i<len(a):
#     if s[i]>="a" and s[i]<="z":
#         if s[i] not in b:
#             b+=s[i]
#     i+=1
# if len(b)==26:
#   print("A Pangram")
# else:
#   print("Not a Pangram")

'''Q-7.) Check whether given two strings are anagram or not (eg:-"A decimal point" can be written as "I'm a dot in place" is a anagram).'''
# a='A decimal point'
# b="I'm a dot in place"
# a=a.lower()
# b=b.lower()
# ans=''
# answ=''
# i=0
# while i<len(b):
#     if b[i]>="a" and b[i]<="z":
#         if b[i] in a:
#             r=b[i]
#             c1=a.count(r)
#             c2=b.count(r)
#             if c1==c2:
#                 ans+=r
#                 answ+=r
#             else:
#                 i=-2
#                 break
#         else:
#             i=-2
#             break
#     i+=1
# if len(ans)==len(answ):
#     print("An anagram")
# else:
#     print("Not an anagram")

'''Q-8.) Check whether a string is palindrome or not (eg:- "MOM", "MALAYALAM").'''
# a=input()
# b=a
# i=0
# j=-1
# count=0
# while i<len(a):
#   if a[i]==b[j]:
#     i+=1
#     j-=1
#     count+=1
#   else:
#     break
# if count==len(a):
#   print("It's a Palindrome")
# else:
#   print("Not a Palindrome")

'''Q-9.) a="I am Bhawna", ans="Bhawna am I".'''
# a="hgtf cftukg c sasa dyrjcf cxytrcfg"
# l=len(a)
# b=""
# s=""
# i=-1
# while i>(-l):
#     if a[i]!=" ":
#         s+=a[i]
#     else:
#         s=s[::-1]
#         b+=s
#         b+=" "
#         s=""
#     i-=1
# s+=a[i]
# s=s[::-1]
# b+=s
# print(b)