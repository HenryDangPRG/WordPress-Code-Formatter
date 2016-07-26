# WordPress-Code-Formatter

WordPress Code Formatter is a script that fixes issues caused by WordPress's WYSIWYG editor when code blocks are used. 

It finds common things that Wordpress's editor will change inside code blocks, and reverts them back to their original state.

Below are a list of changes that Wordpress Code Formatter will fix :

* `&lt;` into `<`
* `&gt;` into `>`
* `&quot;` into `"`

For example, if you have code in Java, WordPress will turn this :
```
[code language = "Java"]
List<Integer> list = new ArrayList<Integer>();
[/code]
```
Into this :

```
[code language = "Java"]
List&lt;Integer&gt; list = new ArrayList&lt;Integer&gt;();
[/code]
```

WordPress Code Formatter changes those HTML character entities back into their standard form.

# Installation and Usage

You will need [Python](https://www.python.org/) 2 or 3 to use this script.

1. Clone the directory : 


  `git clone https://github.com/HenryDangPRG/Wordpress-Code-Formatter.git`
  
2. Copy your WordPress post as a text file (.txt/plain text)into the same directory.

3. Run the following command : 


   `python wordpress-code-formatter.py <FILE_NAME>`
   
4. A copy of the file named `fixed_<FILE_NAME>` will be created in the same directory, with the HTML character entities replaced. <br><br>
You can now copy all of its contents back into your WordPress editor.

# Authors

Henry Dang

# License

WordPress Code Formatter is licensed under the [MIT License](http://www.opensource.org/licenses/MIT).


