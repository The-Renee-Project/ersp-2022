adb backup -f data.ab org.nativescript.AudioMoth9
java -jar abp.jar unpack data.ab data.tar
tar -xf data.tar
rm data.tar
rm data.ab
