<div align="center" id="top"><p>
    <a href="#status"><img src="https://img.shields.io/badge/Maintained-yes-green.svg?style=flat-square"></a>
    </p>
  <br>
  <h1>ABEL</h1>
  <h5>How to decay your learning rate</h5>
  <p>
  <b>ABEL</b> is a <b>learning rate decay scheme</b> that could be useful in your project.
  </p></div>

# Table Of Contents

*   [Features](#features)

*   [Quick Start](#quick-start)

*   [Installation](#installation)

*   [Authors](#authors)

*   [License](#license)


# Features

*   Easy To Use 

*   Reliable


# Quick Start

1. Python Interface 

```python
lr_producer = LR_Producer(0.1, epoc_step, warmup_steps = epoc_step, warmup_lr = 0.01)
now_lr = lr_producer.get_now_lr(now_wnorm, g_step)
```


# Installation


## Package Managers

#### Just Clone 

```bash
git clone https://github.com/Zhengtq/How-to-decay-your-learning-rate.git
```


​    
## Version 

*   Minified Version: v1.0.0.0 


# Authors

| [Zhengtq](https://github.com/Zhengtq) |
| :----------------------------------------------------------: |
| [Github](https://github.com/Zhengtq) |
| [Email](mailto:1553866519@qq.com) |


# License
```
MIT License

Copyright (c) 2021 Zhengtq

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

# Status

This project is currently being maintained. And Will Be Maintained. If You Like This Project And Want This Project To Never Exhaust. Please Consider Donating.

