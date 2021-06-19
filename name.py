names_list = [ "bob", "jimmy", "max b", "Bernie", "Jordan", "future Hendrix"]


longest_name =""

for n in names_list:

   if len(n)>len(longest_name):

       longest_name=n

print(longest_name)