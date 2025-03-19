# Oldest trick in the book


```console
$ tshark -r older_trick.pcap -Y 'icmp and ip.src == 192.168.1.7' -T fields -e data.data > data_book.txt

$ cat poc.txt |  tr -d ':' > data_book_wc.txt

```

We extract some bytes of the txt with a python script

```python
with open('data_book_wc.txt') as f:
	lines = f.read().split('\n')

res = ""
for line in lines:
	res += line[-(32+16):-16]
with open('leak_data.bin', 'wb+') as f: f.write(codecs.decode(res, 'hex'))

```

```console
$ file leak_data.bin

leak_data.bin: Zip archive data, at least v2.0 to extract


$ mv leak_data.bin leak_data.zip
$ unzip leak_data.zip
```

And we have and firefox profile, the `fini` folder contains some encrypted stored passwords in logins.json.

```
$ git clone https://github.com/lclevy/firepwd.git
$ python3 firepwd/firepwd.py -d fini/

...
https://rabbitmq.makelarid.es:b'Frank_B',b'CHTB{long_time_no_s33_icmp}'
```