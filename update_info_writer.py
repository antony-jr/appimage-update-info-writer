#!/usr/bin/env python3
# MIT License
# Copyright (c) 2021 Antony Jr.
import sys

def is_ascii(n):
    if n > 0 and n < 127:
        return True
    return False

print("AppImage Update Information Writer, Write Custom AppImage Update Information.")
print("Copyright (C) 2021 Antony Jr.\n")

if len(sys.argv) < 3:
    print("Usage: update_info_writer.py [APPIMAGE] [NEW UPDATE INFORMATION]")
    sys.exit(0)

appimage = sys.argv[1]
new_update_info = sys.argv[2]
kb_limit = 1024 * 2 # The update information should be in top 2 MiB
kb_read = 0
data = ''
buf_size = 1024
fp = open(appimage, "rb+")

while True:
    data = fp.read(buf_size)
    if data == '':
        break

    kb_read += 1
    if kb_read > kb_limit:
        break

    count = 0
    while count < buf_size:
        possible_update_info = ''
        if is_ascii(data[count]):
            starting = count
            pos = count
            possible_update_info = ''
            # Read till a non ascii character and stop.
            while pos < buf_size and is_ascii(data[pos]):
                    possible_update_info += chr(data[pos])
                    pos += 1

            if "zsync|" in possible_update_info:
                offset = fp.tell() - buf_size + starting
                fp.seek(offset)
                fp.write(new_update_info.encode())
                fp.close()
                print("SUCCESS: Wrote '{}' as the update information.".format(possible_update_info))
                print("Finished.")
                sys.exit(0)
        count += 1
print("FATAL: cannot find existing update information.")
fp.close()
