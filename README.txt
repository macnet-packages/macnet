MacNet: The Package Manager For macOS.
INSTALL:

git clone https://github.com/macnet-packages/macnet.git /tmp/macnet # Clone the repo
cd /tmp/macnet # Open The Repo
python3 -m pip install . # Install Mac Net ( FOR MAC & LINUX )
python -m pip install . # Install Mac Net ( FOR WINDOWS )
echo "alias macnet='python3 -m macnet'" # Alias Mac Net ( FOR MAC & LINUX )
echo "alias macnet='python -m macnet'" # Alias Mac Net ( FOR WINDOWS )

NOTE: MacNet is not fully supprted on Windows and Linux.
