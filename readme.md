# Dot Kernel

The dot kernel for jupyter!

There is an awesome dot language tutorial in Chinese: [learn-dot](https://github.com/laixintao/learn-dot).

![demo.jpeg](https://github.com/laixintao/jupyter-dot-kernel/raw/master/readme_assets/demo.jpeg)

## Install

You should have graphviz first. 
- Install by brew: `brew install graphviz`.
- or `sudo apt-get install graphviz` for ubuntu

Then,

```
pip install dot_kernel
```

Add kernel to your jupyter:

```
install-dot-kernel
```

ALL DONE! 🎉🎉🎉

Run using:

```
jupyter notebook
```

Select new -> dot

![new_dot.png](https://github.com/laixintao/jupyter-dot-kernel/raw/master/readme_assets/new_dot.png)

and try run this:

```
 // The graph name and the semicolons are optional
 graph graphname {
     a -- b -- c;
     b -- d;
 }
```

You will see:

![first_try.png](https://github.com/laixintao/jupyter-dot-kernel/raw/master/readme_assets/first_try.png)

## Running in Docker

A container based on `jupyter/datascience` named `garo/jupyter-dot` is available on Docker Hub.
If you have docker you can run it as you would any [other jupyter container](https://jupyter-docker-stacks.readthedocs.io/en/latest) without having to install anything.
A quick example: `docker run -d -rm -p 8888:8888 garo/jupyter-dot`


## TODO

1. update [this](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).
2. add more render tools not just `dot`
3. add more filetype support not just `png`
4. auto indent
