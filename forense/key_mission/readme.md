# Key mission


We have an `.pcap` with USB data and it seems like data of keyboard strokes, with tshark we analyze the data we want and then we decode it.


[Here](https://github.com/TeamRocketIst/ctf-usb-keyboard-parser) you can search the official repository and [here](https://book.hacktricks.xyz/forensics/pcaps-analysis/usb-keyboard-pcap-analysis) more information about USB Keyboard pcap analysis

```
$ tshark -r ./key_mission.pcap -Y 'usb.capdata && usb.data_len == 8' -T fields -e usb.capdata > usbPcapData.txt

$ python3 usbkeyboard.py usbPcapData.txt

I am sending secretary's location over this totally encrypted channel to make sure no one else will be able to read it except of us. This information is confidential and must not be shared with anyone else. The secretary's hidden location is CHTB{a_plac3_fAr_fAr_away_fr0m_earth}
```
