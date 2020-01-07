"""
In python dictionary is a unordere set of key value pair
"""

#  Let’s say you use many if/else clauses in your code
name = input("Enter the name")
if name == "Josh":
   print("This is Josh, he is an artist")
elif name == "Ted":
   print("This is Ted, he is an engineer")
elif name == "Kennedy":
   print("This is Kennedy, he is a teacher")

# By using a dictionary, we can write the same code like this
name_job_dict = {
   "Josh": "This is John, he is an artist",
   "Ted": "This is Ted, he is an engineer",
   "Kenedy": "This is Kennedy, he is a teacher",
}
print(name_job_dict[name])


