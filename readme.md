# Dot Kernel

The dot kernel for jupyter!

There is an awesome dot language tutorial in Chinese: [learn-dot](https://github.com/laixintao/learn-dot).

![](./readme_assets/demo.jpeg)

## Install

You should have graphviz first. 
- Install by brew: `brew install graphviz`.
- or `sudo apt-get inatall graphviz` for ubuntu

Then, for python 2

```
pip install dot_kernel
```

Add kernel to your jupyter:

For python 2

```
install-dot-kernel
```

For python 3

```
git clone https://github.com/laixintao/jupyter-dot-kernel.git
cd jupyter-dot-kernel
jupyter kernelspec install dot_kernel_spec --user
```


ALL DONE! 🎉🎉🎉

Run using:

```
jupyter notebook
```

Select new -> dot

![](readme_assets/new_dot.png)

and try run this:

```
 // The graph name and the semicolons are optional
 graph graphname {
     a -- b -- c;
     b -- d;
 }
```

You will see:

![](readme_assets/first_try.png)

## TODO

1. update [this](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).
2. add more render tools not just `dot`
3. add more filetype support not just `png`
4. auto indent
