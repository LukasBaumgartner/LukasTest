
# A collection of characters

a = "banana"
print(a[-1])
print(len(a))

# Palindrome - reads same backwards and forwards
# racecar
# Remove punctuation
s="s a m e! e m? a s"

punctuation = "!,.?-<>/\|"
for p in punctuation:
    s=s.replace(p,"")
s=s.replace(" ", "")
s=s.lower()

if s==s[::-1]:
        print("This is a Palindrome!")
else:
        print("This is not a Palindrome!!!")