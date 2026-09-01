#program to list keywords,print the count,also print given keyword or not
import keyword
print(keyword.kwlist)
print("-------------------------")
print(len(keyword.kwlist))
print("-------------------------")
print(keyword.iskeyword("for"))
print("--------------------------")
print(keyword.iskeyword("hello"))