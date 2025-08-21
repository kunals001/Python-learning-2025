print("website Checker ")

url = input("\nEnter your website url here")

if url.startswith("https://"):
    print("valid url this website uses https protocol (secure)")

elif url.startswith("http://"):
    print("this website uses http protocol (insecure)") 

else:
    print("invalid url")