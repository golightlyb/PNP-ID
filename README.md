README
======

*"Given a PNP (Plug and Play) industry-unique Vendor ID, return the Vendor name"*

This is free-to-use C code that, given a PNP (Plug and Play) industry-unique
Vendor ID, returns the Vendor name. You might find this ID when querying
[Computer Monitor EDID](https://en.wikipedia.org/wiki/Extended_Display_Identification_Data).

This file contains a script, `update.sh` to automatically download the
[PNP ID REGISTRY](http://www.uefi.org/pnp_id_list) from the UEFI Forum body,
and generate and compile a C program and a test binary. The C program uses
a binary search to efficiently resolve a PNP Vendor ID to the Vendor name.

If you're writing code for Linux, the proper way to do this is with libudev.
But! If you're writing cross platform code / udev might not be available /
this is all you need / want to keep things simple... this'll do it! :)

If this code saved you some time, please consider
[making a donation](https://www.patreon.com/golightlyb) to the author.


**Features:**

    * Exhaustively tested
    * Efficient binary search lookup


**Optional requirements:**

These are only needed if you want to download the latest list from the UEFI
Forum body and use it to generate updated C code.

    * python3
    * gnumeric for ssconvert (xls -> csv)


**Usage Example:**

    // gcc -std=c99 -Wall -Wextra pnpid.c example.c -o examplebin

    // function prototype
    const char *pnp_name(const char *key);

    int main(void)
    {
        const char *id = "SAM";
        const char *name = pnp_name(id);

        if (name == NULL)
        {
            printf("Couldn't find the name for PNP ID %s", id);
        }
        else
        {
            printf("%s => %s\n", id, name);
            // prints SAM => Samsung Electric Company
        }
    }


**License**

I believe the generated file should be free to use. The UEFI Forum states:

"**There is no charge for use of the specification itself.** The promoters of
UEFI specifications have agreed that any IP needed to implement the
specification will be made available on reasonable and non-discriminatory
terms."

