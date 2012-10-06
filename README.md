Simple Python Profiler
======================

I made Simple Profiler because I needed a small tool to measure the time of code fragments execution; and the average time a fragment takes  to execute.

This profiler was made to give a general idea of the time your code takes to execute. For more sensitive profiling, check the [Python Profilers](http://docs.python.org/library/profile.html) documentation.

## Usage

### Calculate Single Execution Time

```
# Import the Class
from profiler import profiler

# Create a new instance of simple profiler
my_profiler = profiler()

# Run some Code

profiler.start('code_fragment_1')
# Code Fragment to profile
profiler.end('code_fragment_1')

# Run some Code
```

### Calculate Average Execution Time

```
# Import the Class
from profiler import profiler

# Create a new instance of simple profiler
my_profiler = profiler()

# Run some Code

for x in range(10):
    profiler.start('code_fragment_1', 'average')
    # Code Fragment to profile
    profiler.end('code_fragment_1', 'average')

# Run some Code
```

### Displaying Results

```
# Print the results to the Console
profiler.log('print')
# Return the results as a Python Dictionary
profiler.log('return')
# Output the results to a file
profiler.log('file') 
```

### Output sample

This is an example of the time required by openurl to open different web pages. Simple Profiler calculates both the average time, and the time for each function call.

```
{'step': 3.3061890602111816, 'average': 3.3061890602111816}
{'step': 2.7071549892425537, 'average': 3.0066720247268677}
{'step': 3.155179977416992, 'average': 3.0561746756235757}
{'step': 4.912281036376953, 'average': 3.52020126581192}
{'step': 2.5761477947235107, 'average': 3.3313905715942385}
{'step': 3.3781931400299072, 'average': 3.3391909996668496}
{'step': 2.6141488552093506, 'average': 3.2356135504586354}
{'step': 2.5701470375061035, 'average': 3.152430236339569}
{'step': 3.212183952331543, 'average': 3.159069538116455}
{'step': 3.6222071647644043, 'average': 3.20538330078125}
{'step': 2.62214994430542, 'average': 3.1523620865561743}
{'step': 3.1381800174713135, 'average': 3.1511802474657693}
{'step': 2.661151885986328, 'average': 3.113485758121197}
{'step': 5.874336004257202, 'average': 3.3106893471309116}
```

## License

The code is not licensed. Feel free to use it in both your free and commercial projects. No links or attribution are required. The code also comes with no garantees, use it at your own responsibility.