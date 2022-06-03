// Load all suffixes in an array  
static readonly string[] suffixes = {
    "Bytes",
    "KB",
    "MB",
    "GB",
    "TB",
    "PB"
};

///
/// Function to convert bytes to a human readable string (e.g. 1.23 MB)

public string FormatSize(Int64 bytes) {
    int counter = 0;
    decimal number = (decimal) bytes;
    while (Math.Round(number / 1024) >= 1) {
        number = number / 1024;
        counter++;
    }
    return string.Format("{0:n1}{1}", number, suffixes[counter]);
}