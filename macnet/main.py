import sys
import os

print(f"--> MacNet Is Installing {sys.argv[2]}, and building with {sys.argv[1]}.")
c1 = input("Proceed? [Y/n]: ")
if c1 == "Y":
    pass
elif c1 == "n":
    sys.exit(0)
else:
    pass
print(f"--> Cloning {sys.argv[2]}...")
name = sys.argv[2].rsplit("/")
for i in range(0, 100):
    if i == 34:
        try:
            os.system(f"git clone 'https://github.com/{sys.argv[2]}' '~/.macnet/{name}'")
            os.chdir(f"~/.macnet/{name}")
            os.system(sys.argv[1])
        except FileNotFoundError:
            print("~/.macnet folder is not found. Run 'mkdir ~/.macnet'.")
