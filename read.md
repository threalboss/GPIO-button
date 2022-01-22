I kept getting the error: /dev/ttyUSB0: Permission denied



I was able to fix it with using this:

echo -e "This is a test.\\n\\n\\n" > /dev/usb/lp0

instead of

echo -e "This is a test.\\n\\n\\n" > /dev/ttyUSB0



This took hours for me to figure out, full credit to this guide: https://www.theamplituhedron.com/articles/How-to-use-a-tiny-thermal-printer-with-Raspberry-Pi/

It would be great if you could add this to the guide!
