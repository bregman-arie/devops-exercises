## Shell Scripting

### Shell Scripting Exercises

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
|Hello World|Variables|[Exercise](hello_world.md)|[Solution](solutions/hello_world.md) | Basic
|Basic date|Variables|[Exercise](basic_date.md)|[Solution](solutions/basic_date.md) | Basic
|Great Day|Variables|[Exercise](great_day.md)|[Solution](solutions/great_day.md) | Basic
|Factors|Arithmetic|[Exercise](factors.md)|[Solution](solutions/factors.md) | Basic
|Argument Check|Conditionals|[Exercise](argument_check.md)|[Solution](solutions/argument_check.md) | Basic
|Files Size|For Loops|[Exercise](files_size.md)|[Solution](solutions/files_size.md) | Basic
|Count Chars|Input + While Loops|[Exercise](count_chars.md)|[Solution](solutions/count_chars.md) | Basic
|Sum|Functions|[Exercise](sum.md)|[Solution](solutions/sum.md) | Basic
|Number of Arguments|Case Statement|[Exercise](num_of_args.md)|[Solution](solutions/num_of_args.md) | Basic
|Empty Files|Misc|[Exercise](empty_files.md)|[Solution](solutions/empty_files.md) | Basic
|Directories Comparison|Misc|[Exercise](directories_comparison.md)|[Solution](solutions/directories_comparison.md) | Basic
|It's alive!|Misc|[Exercise](host_status.md)|[Solution](solutions/host_status.md) | Intermediate

## Shell Scripting - Self Assessment

<details>
<summary>What does this line in shell scripts means?: <code>#!/bin/bash</code></summary><br><b>


`#!/bin/bash` is She-bang

/bin/bash is the most common shell used as default shell for user login of the linux system. The shell’s name is an acronym for Bourne-again shell. Bash can execute the vast majority of scripts and thus is widely used because it has more features, is well developed and better syntax.

</b></details>

<details>
<summary>True or False? When a certain command/line fails in a shell script, the shell script, by default, will exit and stop running</summary><br><b>

Depends on the language and settings used.
If the script is a bash script then this statement is true. When a script written in Bash fails to run a certain command it will keep running and will execute all other commands mentioned after the command which failed.

Most of the time we might actually want the opposite to happen. In order to make Bash exist when a specific command fails, use 'set -e' in your script.
</b></details>

<details>
<summary>What do you tend to include in every script you write?</summary><br><b>

Few example:

  * Comments on how to run it and/or what it does
  * If a shell script, adding "set -e" since I want the script to exit if a certain command failed

You can have an entirely different answer. It's based only on your experience and preferences.
</b></details>

<details>
<summary>Today we have tools and technologies like Ansible, Puppet, Chef, ... Why would someone still use shell scripting?</summary><br><b>

  * Speed
  * Flexibility
  * The module we need doesn't exist (perhaps a weak point because most CM technologies allow to use what is known as "shell" module)
  * We are delivering the scripts to customers who don't have access to the public network and don't necessarily have Ansible installed on their systems.
</b></details>

#### Shell Scripting - Variables

<details>
<summary>How to define a variable with the value "Hello World"?</summary><br><b>

`HW="Hello World`
</b></details>

<details>
<summary>How to define a variable with the value of the current date?</summary><br><b>

`DATE=$(date)`
</b></details>

<details>
<summary>How to print the first argument passed to a script?</summary><br><b>

`echo $1`
</b></details>

<details>
<summary>Write a script to print "yay" unless an argument was passed and then print that argument</summary><br><b>

```
echo "${1:-yay}"
```
</b></details>

<details>
<summary>What would be the output of the following script?

```
#!/usr/bin/env bash
NINJA_TURTLE=Donatello
function the_best_ninja_turtle {
        local NINJA_TURTLE=Michelangelo
        echo $NINJA_TURTLE
}
NINJA_TURTLE=Raphael
the_best_ninja_turtle
```
</summary><br><b>
Michelangelo
</b></details>

<details>
<summary>Explain what would be the result of each command:

  * <code>echo $0</code>
  * <code>echo $?</code>
  * <code>echo $$</code>
  * <code>echo $#</code></summary><br><b>
</b></details>

<details>
<summary>What is <code>$@</code>?</summary><br><b>
</b></details>

<details>
<summary>What is difference between <code>$@</code> and <code>$*</code>?</summary><br><b>

`$@` is an array of all the arguments passed to the script
`$*` is a single string of all the arguments passed to the script
</b></details>

<details>
<summary>How do you get input from the user in shell scripts?</summary><br><b>

Using the keyword <code>read</code> so for example <code>read x</code> will wait for user input and will store it in the variable x.
</b></details>

<details>
<summary>How to compare variables length?</summary><br><b>

```
if [ ${#1} -ne ${#2} ]; then
    ...
```
</b></details>

#### Shell Scripting - Conditionals

<details>
<summary>Explain conditionals and demonstrate how to use them</summary><br><b>
</b></details>

<details>
<summary>In shell scripting, how to negate a conditional?</summary><br><b>
</b></details>

<details>
<summary>In shell scripting, how to check if a given argument is a number?</summary><br><b>

```
regex='^[0-9]+$'
if [[ ${var//*.} =~ $regex ]]; then
...
```
</b></details>

#### Shell Scripting - Arithmetic Operations

<details>
<summary>How to perform arithmetic operations on numbers?</summary><br><b>

One way: `$(( 1 + 2 ))`
Another way: `expr 1 + 2`
</b></details>

<details>
<summary>How to perform arithmetic operations on numbers?</summary><br><b>
</b></details>

<details>
<summary>How to check if a given number has 4 as a factor?</summary><br><b>

`if [ $(($1 % 4)) -eq 0 ]; then`
</b></details>

#### Shell Scripting - Loops

<details>
<summary>What is a loop? What types of loops are you familiar with?</summary><br><b>
</b></details>

<details>
<summary>Demonstrate how to use loops</summary><br><b>
</b></details>

#### Shell Scripting - Troubleshooting

<details>
<summary>How do you debug shell scripts?</summary><br><b>

Answer depends on the language you are using for writing your scripts. If Bash is used for example then:

  * Adding -x to the script I'm running in Bash
  * Old good way of adding echo statements

If Python, then using pdb is very useful.
</b></details>

<details>
<summary>Running the following bash script, we don't get 2 as a result, why?

```
x = 2
echo $x
```
</summary><br><b>

Should be `x=2`
</b></details>

#### Shell Scripting - Substring

<details>
<summary>How to extract everything after the last dot in a string?</summary><br><b>

`${var//*.}`
</b></details>

<details>
<summary>How to extract everything before the last dot in a string?</summary><br><b>

${var%.*}
</b></details>

#### Shell Scripting - Misc

<details>
<summary>Generate 8 digit random number</summary><br><b>

shuf -i 9999999-99999999 -n 1
</b></details>

<details>
<summary>Can you give an example to some Bash best practices?</summary><br><b>
</b></details>

<details>
<summary>What is the ternary operator? How do you use it in bash?</summary><br><b>

A short way of using if/else. An example:

[[ $a = 1 ]] && b="yes, equal" || b="nope"
</b></details>

<details>
<summary>What does the following code do and when would you use it?

<code>diff <(ls /tmp) <(ls /var/tmp)</code>

</summary><br>
It is called 'process substitution'. It provides a way to pass the output of a command to another command when using a pipe <code>|</code> is not possible. It can be used when a command does not support <code>STDIN</code> or you need the output of multiple commands.
https://superuser.com/a/1060002/167769
</details>

<details>
<summary>What are you using for testing shell scripts?</summary><br><b>

bats
</b></details>

