## Test internet connection

* used async aiohttp request  
* any request with self aiohttp session  
* after request session will be closed  

#### Python version
3.7

#### Install libs
```bash
pip install -r requirements.txt
```

#### Run cmd
```bash
python3 main.py
```

##### Addition arguments
`--repeats` (int) How much requests (default: `10`)  
`--url` (str) Request url  (default: `http://google.com`)  

###### Example
```bash
python3 main.py --repeats 400 --url http://yahoo.com
```

-- will be `400` requests to `http://yahoo.com`

#### Output (example)
```text
Accepted:   298
Inited:     300
Percentage: 99 %
```