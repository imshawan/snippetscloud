#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef _WIN32
    #define OS_COMMAND_FORMAT "start %s"
#elif __APPLE__
    #define OS_COMMAND_FORMAT "open %s"
#elif __linux__
    #define OS_COMMAND_FORMAT "xdg-open %s"
#else
    #error "Unsupported operating system"
#endif

int main() {
    const char *url = "https://www.imshawan.dev/";
    
    char command[256];

    // Form the command based on the OS
    snprintf(command, sizeof(command), OS_COMMAND_FORMAT, url);

    // Execute the command
    int result = system(command);

    // Check for errors
    if (result != 0) {
        fprintf(stderr, "Failed to open the URL. Please check your system settings.\n");
        return 1;
    }

    printf("URL opened successfully!\n");
    return 0;
}


// For Compiling
// gcc open_links.c -o open_links
