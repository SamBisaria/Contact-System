from contact import Contact
import json
def main():
  contacts = []
  try:
    f = open("contact.json", "r+")
    data = json.load(f)
    contacts = [Contact(contact["name"], contact["number"], contact["email"]) for contact in data]
  except IOError:
    f = open("contact.json", "w")

  while True:
    print("1. Add contacts")
    print("2. Remove contacts")
    print("3. Edit contacts")
    print("4. Search contacts")
    print("5. View contacts")
    print("6. Quit")
    request = input("Enter your choice(1-6): ").strip()
    if request == "1":
      print("\nAdd contacts")
      name = input("\tEnter contact's name: ").strip()
      number = input("\tEnter contact's phone number: ").strip()
      email = input("\tEnter contact's email: ").strip()
      print("\tContact added")
      print()
      contact = Contact(name,number,email)
      contacts.append(contact)
    elif request == "2":
      print("\nRemove contacts")
      number = input("\tEnter phone number of contact to remove: ")
      index = -1
      for i,contact in enumerate(contacts):
        if contact.number == number:
          index = i
      if index > -1:
        contacts.pop(index)
        print("\tContact removed")
      else:
        print("\tContact not found")
      print()
    elif request == "3":
      print("\nEdit contacts")
      number = input("\tEnter phone number of contact to edit: ")
      foundcontact = None
      for contact in contacts:
        if contact.number == number:
          foundcontact = contact
      if foundcontact != None:
        name = input("\tEnter contact's name ("+foundcontact.name+"): ").strip()
        number = input("\tEnter contact's phone number ("+foundcontact.number+"): ").strip()
        email = input("\tEnter contact's email ("+foundcontact.email+"): ").strip()
        if name != "":
          foundcontact.name = name
        if number != "":
          foundcontact.number = number
        if email != "":
          foundcontact.email = email
        print("\tContact edited")
      else:
        print("\tContact not found")
      print()
    elif request == "4":
      print("\nSearch contacts")
      search = input("\tEnter contact to search for: ")
      foundcontacts = []
      for contact in contacts:
        if search in contact.number or search in contact.name or search in contact.email:
          foundcontacts.append(contact)
      if len(foundcontacts) != 0:
        for contact in foundcontacts:
          print()
          print("\t" + str(contact))
      else:
        print("\tNo contacts found")
      print()
    elif request == "5":
      print("\nView contacts\n")
      for contact in contacts:
        print (contact)
      print()
    elif request == "6":
      break
  f.seek(0)
  f.truncate()
  json.dump([contact.__dict__ for contact in contacts],f)

main()