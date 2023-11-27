MacNet: The Package Manager For macOS.
INSTALL:

git clone https://github.com/macnet-packages/macnet.git /tmp/macnet # Clone the repo
cd /tmp/macnet # Open The Repo
python3 -m pip install . # Install Mac Net ( FOR MAC & LINUX )
echo "alias macnet='python3 -m macnet'" >> ~/.zshrc # Alias Mac Net ( FOR MAC & LINUX )

NOTE: MacNet is not fully supprted on Linux and not at all on Windows.
