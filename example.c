// link with pnpid.c

#include <stdio.h>

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
