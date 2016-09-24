
# ssconvert is provided by gnumeric
# sudo apt-get install gnumeric

echo "Cleaning old files"
rm uefi-pnp-export
rm uefi-pnp.csv
rm pnpid.c
rm test.c
rm testbin

echo "Downloading PNP ID REGISTRY from uefi.org"
wget http://www.uefi.org/uefi-pnp-export
ssconvert uefi-pnp-export uefi-pnp.csv
echo "Generating C code"
cat uefi-pnp.csv | python3 conv.py > pnpid.c
cat uefi-pnp.csv | python3 test.py > test.c
echo "Compiling test program"
gcc -std=c99 -Wall -Wextra pnpid.c test.c -o testbin
echo "Running test program"
./testbin
echo "Done"
