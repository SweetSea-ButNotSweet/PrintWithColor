# **PrintWithColor**

A little Python wrapper that enhances the print() syntax by enabling text coloring on the screen.


> **NOTE:** This ReadMe.md file which you are seeing or reading here is in English, but the Vietnamese version is also available! If you want to see it,  [click here!](https://github.com/SweetSea-ButNotSweet/PrintWithColor/blob/master/ReadMe_VI.md)

# **Installion**
To install this package via PyPi, type like this command below to the Terminal or Command Prompt:

```batch
pip install PrintWithColor
```
> For those of you who are wondering why I don't put the \$ character in front of the command as others do in other projects, here's why.

> Because ***forgetting*** to __DELETE__ ***the extra \$ character*** while pasting the command will result in the command __*FAILING!*__.
> This command may also be used on Windows, however on Linux, you should replace pip with pip3 (if you use pip, maybe Linux will call Python 2 instead Python 3!)

# **Usage**
This is the basic usage of **PrintWithColor**



```python
from PrintWithColor import printc as print
print('Hello, I am a green line!', f = 'green', b= 'black')
print('Or a line with a cyan background', f = 'black', b = 'cyan')
```

### Đối số trong lệnh print() **của Python**

| Argument      | Description                                                                                                                                                                                                                                                                                                                  | DefaultValue |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| textfrominput | The content you want to display on the screen, allows you to enter many arguments                                                                                                                                                                                                                                            | Any          |
| sep           | A separate sign between the arguments (if there is only one argument in textfrominput, it will not appear anywhere)                                                                                                                                                                                                          | ' '          |
| end           | Ending character, when there is only one argument or when textfrominput has reached its final argument, the ending character appears.                                                                                                                                                                                        | '\n'         |
| file          | Where should the text be output? The default in Python is sys.stderr or your screen.<br> If the file argument is a __writable file__, Python will automatically __write to the file__ provided in the file argument instead of writing to the screen.<BR>If that file cannot be written, __an exception will be raised__ [1] | None         |
| flush         | Should the buffer be cleaned up once the results are printed?                                                                                                                                                                                                                                                                | False        |

### All argument in Print() syntax **from PrintWithColor**

| Argument      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Default |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| textfrominput | The content you want to display on the screen, allows you to enter many arguments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Any     |
| sep           | A separate sign between the arguments (if there is only one argument in textfrominput, it will not appear anywhere)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | ' '     |
| end           | Ending character, when there is only one argument or when textfrominput has reached its final argument, the ending character appears.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | '\n'    |
| file          | Where should the text appear? This wrapper will use the Colorama library's proxy object by default.<br>If the file argument is a __writeable file__, PrintWithColor will write the output to that file, ***just like the original print() syntax***.<br>PrintWithColor will __skip the file__ provided in it and __display the text on the screen__ if it is not writeable.<br>You should also be aware that in order to use Colorama's proxy object, this argument will __exclude__ ***all objects other than a writeable file!*** (Because this wrapper is cross-platform, I should use it to avoid any bugs/issues that may happen!) | None    |
| flush         | Should the buffer be cleaned up once the results are printed?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | False   |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |         |
| f             | Foreground color [2] [3]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | WHITE   |
| b             | Background color [2] [3]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | BLACK   |
| s             | Style of the foreground colour [2] [4]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | NORMAL  |

> **NOTE FOR PRINT() SYNTAX BETWEEN PYTHON AND PRINTWITHCOLOR**

1. If the file argument is a read-only file. It will throw an exception in Python, but PrintWithColor will automatically ignore that parameter and print the output directly to the screen. (For more infomation about colorama's proxy object, [click here]())
2. You can write the colour in uppercase or lowercase as well
2. Acceptable color ranges are ['WHITE', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'BLACK']
3. Acceptable color styles are ['NORMAL', 'DIM', 'BRIGHT']


> **WARNING!** Windows will **NOT** correctly display dark (dim) and regular colors. So, in most cases, you won't notice a change. :cry:
> **For more infomation:** Please look down to the last line of colorama's description: https://github.com/tartley/colorama#description

# **Additional configuration**

> **WARNING!**: If any of these settings are invalid, they will be reset to their **DEFAULT** values!
> **How to change configuration?** using print.change_settings() syntax

## **1. DoNotResetColor**

> **Effect:** Not reset color after every print() syntax is performed
> **Default value:** False **(boolean)**
> **Acceptable value:** True, False **(boolean)**


```python
print.change_settings(1, True)
# Hoặc là
print.change_settings('DoNotResetColor', True)
# đều như nhau

# Khi dùng
print('Line 1', f='black', b='green')
print('Line 2 must be formatted in the same color as line 1!')
```

## **2. DefaultForegroundColor**

> **Effect:** Change the default foreground color (When you're done with the print() syntax and the variable **DoNotResetColor = False**, the following print() syntax will use the color you specified!)
> **Default value:** WHITE **(string)**
> **Acceptable value:** WHITE, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, BLACK


```python
print.change_settings(2, 'GREEN')
# Hoặc là
print.change_settings('DefaultForegroundColor', 'GREEN')
# đều như nhau

# Khi sử dụng
print('Even without the f argument, this line must be green!')
```

## **3. DefaultBackgroundColor**

> **Effect:** Change the default background color (When you're done with the print() syntax and the variable **DoNotResetColor = False**, the following print() syntax will use the color you specified!)
> **Default value:** BLACK **(string)**
> **Acceptable value:** DIM, NORMAL, BRIGHT


```python
print.change_settings(3, 'GREEN')
# Hoặc là
print.change_settings('DefaultBackgroundColor', 'GREEN')
# đều như nhau

# Khi sử dụng
print('This line will have nice green background, although I don\'t use b argument')
```

## **4. DefaultStyle**

> **Effect:** Thay đổi kiểu màu nền mặc định (khi dùng xong lệnh print mà **DoNotResetColor = False** thì lệnh print tiếp theo sẽ dùng màu này!)
> **Default value:** NORMAL **(string)**


```python
print.change_settings(4, 'NORMAL')
# Hoặc là
print.change_settings('DefaultStyle', 'NORMAL')
```

## **5. clear_settings()** (Đặt toàn bộ giá trị về mặc định)

> **Effect:** Clear all PrintWithColor's settings!
> **NO ARGUMENT & NO WARNING & NO OUTPUT!**


```python
print.clear_settings()
```
