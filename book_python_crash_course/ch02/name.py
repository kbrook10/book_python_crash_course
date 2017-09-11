# Using the title() method we uppercase the first letter of each word
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
print("< ----- Next Section ---- >")

# Combining and concatenating strings

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)
message = "Hello, " + full_name.title() + "!"
print(message)
print("< ----- Next Section ---- >")

# Adding whitespace to strings with tabs and newlines

print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavascript")

print("< ----- Next Section ---- >")

# Stripping Whitespace

favorite_language = 'python'
print(favorite_language)
print(favorite_language.rstrip())
