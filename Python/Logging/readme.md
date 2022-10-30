# Logging in Python

## 1. Introduction

In this notebook it's shown how to use logging module in Python. The `logging` module is a part of Python. The whole documentation can be found in [logging - Logging facility for Python](https://docs.python.org/3/library/logging.html).

To import he module we just write:

```python
import logging
```

There are many different logging levels that can be used for logging messages.There are 5 levels of logging by order of importance. The debug and info logs are not printed on the terminal by default.

```python
logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()
```

By running the script we get the following output on the terminal:

```
WARNING:root:warning
ERROR:root:error
CRITICAL:root:critical
```

## 2. Configuration of the loggers

By placing the level, for example "DEBUG" we will log all the levels (from debug and above). Let's say we want to log only `error` and `critical` levels we will then type `logging.error`

```python
logging.basicConfig(level = logging.INFO)
```

To write the log to a file we have to specify the path to the log file and the name of the file and filemode ("w").

```python
logging.basicConfig(level = logging.WARNING, filename="logs/log.log", filemode="w")
```

To add the formating option we have to add another argument called "format" to add the formating string to the config.

```python
logging.basicConfig(level = logging.INFO, filename="logs/log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")
```

Where the arguments are:

- **_asctime_** - shows human readable timestamps
- **_levelname_** - is the name of the logging level
- **_message_** - is the log message

By running the last code we write log messages to the log file in the logs folder.

```
2022-10-30 16:13:50,723 - INFO - info
2022-10-30 16:13:50,723 - WARNING - warning
2022-10-30 16:13:50,723 - ERROR - error
2022-10-30 16:13:50,724 - CRITICAL - critical
```

## 3. Logging variable values

For example we have an variable `x=2` and we want to logg it we simply use an _f-string_ to input the variable in the log message.

```python
import logging

logging.basicConfig(level = logging.INFO, filename="logs/log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

x = 2

logging.info("The value of x is {x}")
```

And the output is:

```
2022-10-30 16:31:18,972 - INFO - The value of x is 2
```

## 4. Logging a stack trace (logging exceptions)

There are several ways to log a stack trace. The first one is to log the exception as it follows:

```python
import logging

logging.basicConfig(level = logging.INFO, filename="logs/log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

try:
    1/0
except ZeroDivisionError as e:
    logging.error("ZeroDivisionError", exc_info=True)
```

We use the `exc_info` argument to show the error message. This code generates the following log file:

```
2022-10-30 16:34:57,031 - ERROR - ZeroDivisionError
Traceback (most recent call last):
  File "C:\Users\Goran\Desktop\Python\Notebooks\Python\Logging\log.py", line 8, in <module>
    1/0
    ~^~
ZeroDivisionError: division by zero
```

The second way to do this is to use `logging.exception()`. In this case we dont have to pass in the `exc_info` argument.

```python
import logging

logging.basicConfig(level = logging.INFO, filename="logs/log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

try:
    1/0
except ZeroDivisionError as e:
    logging.exception("ZeroDivisionError")
```

And we get the same output as above.

## 5. Custom loggers

To define a custom logger we use the `getLogger` function which will search for a logger and get the logger for us. If there is no logger by that name the function will create a logger by that name. The practice is to use the `__name__` because this will create a logger by the name of the python module. The practice is also to have one logger per module.

```python
logger = logging.getLogger(__name__)
```

To use the custom logger we have to write:

```python
import logging

logging.basicConfig(level = logging.INFO, filename="logs/log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)
logger.info("Test the custom logger")
```

And we get the output log file:

```
2022-10-30 16:43:58,371 - INFO - Test the custom logger

```

But as we can see the log file has been overwritten. If we want to use a different configuration for a logger we have to create a handler for that.

## 6. Handles and Formatters

To create a handler we have to use `.FileHandler()` and define the file name and the file location. After that we have to create a formatter by using the `.Formatter()` method and define what we want to save to the log file.

```python
import logging

logging.basicConfig(level = logging.INFO, filename="logs/log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)

handler = logging.FileHandler('logs/test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Test the custom logger")
```

After running the script we can see that there was a new log file createt in thhe logs folder and the old one was untouched because the script hasn't overwritten the old log file.
