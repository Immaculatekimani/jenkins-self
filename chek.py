import os.path

readme_path = './README.md'

license_path = './LICENSE'
alert = True

if (os.path.isfile(readme_path)):
    print("Read me file exists")
    alert =False
if (os.path.isfile(license_path)):
    print("LICENSE exists")
    alert = False
if(alert):
    print("The files do not exist")

