
# ssconvert is provided by gnumeric
# sudo apt-get install gnumeric

rm uefi-pnp-export
wget http://www.uefi.org/uefi-pnp-export
ssconvert uefi-pnp-export uefi-pnp.csv
cat uefi-pnp.csv | python3 conv.py > pnpid.c
cat uefi-pnp.csv | python3 test.py > test.c
gcc -std=c99 -Wall -Wextra pnpid.c test.c -o testbin
./testbin

