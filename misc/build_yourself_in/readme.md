# Build yourslef in

We have to resolve 500 equations very fast, so we have to automate it!

The script is made by my friend [Chema](https://github.com/cedelasen)

```python
import nclib

HOST='188.166.172.13'
PORT=31547

def main():

    nc = nclib.Netcat((HOST, PORT), udp=False, verbose=False, echo_hex=True)
    response = nc.recv()

    nc.send(b'1\n')
    response = nc.recv()+nc.recv()

    #Generate dictionary
    dict_string = response.decode('utf-8').splitlines()[2]
    elements = dict_string.split(' ') #separate by space
    keys = elements[0:-1:3] #-1 to delete space not necessary, only icons
    values = elements[2::3] #only operators
    dictionary = dict(zip(keys, values))
    print(dictionary)

    #Process operation
    nc.send(b'2\n')
    response = nc.recv()

    for i in range(0,500):
        operation = response.decode('utf-8').splitlines()[5]
        ops = operation.split('  ')[0].split(" ") #delete '  = ?' and separate by space
        print(ops)
        toEval=''
        for j in range (0, len(ops)):
            if j % 2: #its operator
                toEval+=ops[j]
            else: #its operand
                toEval+=dictionary.get(ops[j])
        res=eval(toEval)
        print(res)
        nc.send((str(res)+'\n').encode('utf-8'))
        response = nc.recv()

    print(response.decode('utf-8'))

    nc.shutdown()
    nc.close() 

if __name__ == "__main__":
    main()

```

```shell
$ python3 buildyourself.py

...
```