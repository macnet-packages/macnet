GITHUB="https://github.com"
echo "--> Starting Package Manager..."
echo "--> Downloading $2"
git clone "$GITHUB/$2" "/tmp/installing_package"
cd /tmp/installing_package
if ! command -v make &> /dev/null; then
  echo "E: You Need Make To use MacNet"
else
  $1
fi
cd -
echo "The Output files can be found in /tmp/installing_package."
