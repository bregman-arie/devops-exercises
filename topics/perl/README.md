## Perl

### Perl Self Assessment

<details>
<summary>What is Perl?</summary><br><b>

From the official [docs](https://perldoc.perl.org/):

"Perl officially stands for Practical Extraction and Report Language, except when it doesn't."

It's a general purpose programming language developed for manipulating texts mainly. It has been used to perform system administration tasks, networking, building websites and more.
</b></details>

<details>
<summary>What data types Perl has? And how can we define it?</summary><br><b>

- Scalar: This is a simple variable that stores single data items. It can be a string, number or reference.

```
my $number = 5;
```

- Arrays: This is a list of scalars. 

```
my @numbers = (1, 2, 3, 4, 5);
# or using the `qw` keyword (quote word):
my @numbers = qw/1 2 3 4 5/; 
# '/' can be another symbol, e.g qw@1 2 3 4 5@
```

- Hashes (or associative arrays): This is an unordered collection of key-value pairs. We can access to a hash using the keys.

```
my %numbers = (
  First => '1',
  Second => '2',
  Third => '3'
);
```

</b></details>

<details>
<summary>How can you access to a hash value, add and delete a key/value pair and modify a hash?</summary><br><b>

```
my %numbers = (
  'First' => '1',
  'Second' => '2',
  'Third' => '3'
);
```

- Access:

```
print($numbers{'First'});
```

- Add:

```
$numbers{'Fourth'} = 4;
```

- Delete:

```
delete $numbers{'Third'};
```

- Modify:

```
$numbers{'Fifth'} = 6;
$numbers{'Fifth'} = 5;
```

</b></details>

<details>
<summary>How can you iterate an array? And a hash?</summary><br><b>

- Array:

```
my @numbers = qw/1 2 3 4 5/;

# Using `$_` that represents the current iteration in a loop. It starts from index array 0 until the last index.
foreach (@numbers) {
    print($_);
}
# Output: 12345


# "$#" returns the max index of an array. That's the reason because we can iterate accessing to the array from the index 0 to the max index.
for my $i (0..$#numbers) {
    print($numbers[$i]);
}
# Output: 12345


# Using the `map` keyword:
print map {$_} @numbers;
# Output: 12345

# Using `while`. We should take care with this option. When we use `shift` we're deleting the first element of the array and assigning it to the `element` variable. 
# After this `loop` the `numbers` array will not have elements.
while (my $element = shift(@numbers)) {
    print($element);
}
# Output: 12345
```

- Hashes:
 
 ```
 my %capital_cities = (
  'Madrid' => 'Spain',
  'Rome' => 'Italy',
  'Berlin' => 'Germany'
);

# Iterate and get the `keys`:
foreach my $city (keys %capital_cities) {
    print($city . "\n");
}
# Iterate and get the `values`:
foreach my $country (values %capital_cities) {
    print($country . "\n");
}

# Iterate and get the values and keys (first option):
foreach my $city (keys %capital_cities) {
    print("City: $city - Country: $capital_cities{$city}" . "\n");
}

# Iterate and get the values and keys (first option):
while(my ($city, $country) = each %capital_cities) {
    print("City: $city - Country: $capital_cities{$city}" . "\n");
}
```

</b></details>

<details>
<summary>What is a Perl subroutine? How to define it?</summary><br><b>

It's the perl model for user defined functions (this is also called function like other programming languages). We can define a subroutine with the keyword `sub`. 

```
sub hello {
  print "hello";
}
```

</b></details>

<details>
<summary>Describe the different ways to receive parameters in a subroutine</summary><br><b>

- List assignment: Using the `@_` array. It's a list with the elements that are being passed as parameters.

```
sub power {
    my ($b, $e) = @_;
    return $b ** $e; 
}

&power(2, 3);
```

- Individual assignment: We should access to every element of the `@_` array. It starts from zero.

```
sub power {
    my $b = $_[0];
    my $e = $_[1];
    return $b ** $e; 
}

&power(2, 3);
```

- Using `shift` keyword: It's used to remove the first value of an array and it's returned.

```
sub power {
    my $b = shift;
    my $3 = shift;
    return $b ** $e; 
}

&power(2, 3);
```


[Source](https://stackoverflow.com/a/21465275/12771230)

We can also read the best way in the same S.O answer.

</b></details>

<details>
<summary>What is lexical and dynamic scoping?</summary><br><b>
</b></details>

<details>
<summary>How to apply referencing and dereferencing?</summary><br><b>
</b></details>

<details>
<summary>Does Perl have conventions?</summary><br><b>

You can check [perlstyle](https://perldoc.perl.org/perlstyle)

</b></details>

<details>
<summary>What is Perl POD? Can you code an example?</summary><br><b>

From the official [docs](https://perldoc.perl.org/perlpod):

"Pod is a simple-to-use markup language used for writing documentation for Perl, Perl programs, and Perl modules."

```
=item
    This function returns the factorial of a number.
    Input: $n (number you wanna calculate).
    Output: number factorial.
=cut
sub factorial {
    my ($i, $result, $n) = (1, 1, shift);
    $result = $result *= $i && $i++ while $i <= $n;
    return $result;
}
```

</b></details>

### Perl Regex

<details>
<summary>Check if the word `electroencefalografista` exists in a string</summary><br><b>

```
my $string = "The longest accepted word by RAE is: electroencefalografista";
if ($string =~ /electroencefalografista/) {                                                         
    print "Match!";
}
```
</b></details>

<details>
<summary>Check if the word `electroencefalografista` does not exists in a string</summary><br><b>

```
my $string = "The longest not accepted word by RAE is: Ciclopentanoperhidrofenantreno";
if ($string !~ /electroencefalografista/) {
    print "Does not match!";
}
```
</b></details>


<details>
<summary>Replace the word `amazing`</summary><br><b>

```
my $string = "Perl is amazing!";
$string =~ s/amazing/incredible/;
print $string;
# Perl is incredible!
```
</b></details>

<details>
<summary>Extract `hh:mm:ss` with capturing group `()` in the following datetime</summary><br><b>

```
my $date = "Fri Nov 19 20:09:37 CET 2021";
my @matches = $date =~ /(.*)(\d{2}:\d{2}:\d{2})(.*)/;
print $matches[1];
# Output: 20:09:37
```
</b></details>

<details>
<summary>Extract all the elements that are numbers in an array</summary><br><b>

```
my @array = ('a', 1, 'b', 2, 'c', 3);
my @numbers = grep (/\d/, @array);    # Note: \d involves more digits than 0-9
map {print $_ . "\n" } @numbers;
```

</b></details>

<details>
<summary>Print all the linux system users that starts with d or D</summary><br><b>

- With a Perl one liner :D
```
open(my $fh, '<', '/etc/passwd');
my @user_info = <$fh>;
map { print $& . "\n" if $_ =~ /^d([^:]*)/  } @user_info;
close $fh;
```

- Avoiding one-liners

```
foreach my $user_line (@user_info) {
    if ($user_line =~ /^d([^:]*)/) {
        print $& . "\n";
    }
}
```

</b></details>

### Perl Files Handle

<details>
<summary>Mention the different modes in File Handling</summary><br><b>

- Read only: `<`
- Write mode. It creates the file if doesn't exist: `>`
- Append mode. It creates the file if doesn't exist: `>>`
- Read and write mode: `+<`
- Read, clear and write mode. It creates the file if doesn't exist: `+>`
- Read and append. It creates the file if doesn't exist: `+>>`

</b></details>

<details>
<summary>How to write into a file?</summary><br><b>

```
# We can use:
# '>' Write (it clears a previous content if exists).
# '>>' Append.
open(my $fh, '>>', 'file_name.ext') or die "Error: file can't be opened";
print $fh "writing text...\n";
close($fh);
```
</b></details>

<details>
<summary>How can you read a file and print every line?</summary><br><b>

```
open(my $fh, '<', 'file_to_read.ext') or die "Error: file can't be opened";
my @file = <$fh>;
foreach my $line (@file) {
    print $line;
}
```

We can use the file handle without assigning it to an array:

```
open(my $fh, '<', 'file_to_read.ext') or die "Error: file can't be opened";

foreach my $line (<$fh>) {
    print $line;
}
```

</b></details>

### Perl OOP

<details>
<summary>Does Perl have support for OOP?</summary><br><b>

From the official [docs](https://perldoc.perl.org/perlootut):

"By default, Perl's built-in OO system is very minimal, leaving you to do most of the work."

</b></details>

<details>
<summary>What is the purpose of the bless function?</summary><br><b>

The function os the `bless` function is used to turning a plain data structure into an object.

</b></details>

<details>
<summary>How to create a Perl class? How can you call a method?</summary><br><b>

- Let's create the package: `Example.pm`

```
package Example;

sub new {
    my $class = shift;
    my $self = {};
    bless $self, $class;
    return $self;
}

sub is_working {
    print "Working!";
}

1;
```

- Now we can instance the `Example` class and call `is_working` method:

```
my $e = new Example();
$e->is_working();
# Output: Working!
```

</b></details>

<details>
<summary>Does Perl have inheritance? What is the `SUPER` keyword?</summary><br><b>

Yes, Perl supports inheritance. We can read about it in the official [docs](https://perldoc.perl.org/perlobj#Inheritance). 
We also can read about `SUPER` keyword that is used to call a method from the parent class. It gives an example about how we can apply inheritance.
</b></details>

<details>
<summary>Does Perl have polymorphism? What is method overriding?</summary><br><b>

Yes, it has polymorphism. In fact method overriding is a way to apply it in Perl.

Method overriding in simple words appears when we have a class with a method that already exist in a parent class.

Example:

```
package A;

sub new { return bless {}, shift; };
sub printMethod { print "A\n"; };

package B;

use parent -norequire, 'A';

sub new { return bless {}, shift; };
sub printMethod { print "B\n"; };

my $a = A->new();
my $b = B->new();

A->new()->printMethod();
B->new()->printMethod();

# Output:
# A
# B
```

</b></details>

<details>
<summary>How can you call a method of an inherited class?</summary><br><b>

```
# Class `A` with `printA` method.
package A;

sub new { return bless {}, shift; };
sub printA { print "A"; };

# Class `B` that extends or use the parent class `A`.
package B;

use parent -norequire, 'A';

sub new { return bless {}, shift; };

# Instance class `B` allows call the inherited method
my $b = B->new();
$b->printA();
```
</b></details>

### Perl Exception Handling

<details>
<summary>How can we evaluate and capture an exception in Perl?</summary><br><b>

From the official [eval docs](https://perldoc.perl.org/functions/eval):

"`eval` in all its forms is used to execute a little Perl program, trapping any errors encountered so they don't crash the calling program.".

e.g:

```
eval {
    die;
};
if ($@) {
    print "Error. Details: $@";
}
```

If we execute this we get the next output:

```
Error. Details: Died at eval.pl line 2.
```

The `eval` (`try` in another programming languages) is trying to execute a code. This code fails (it's a die), and then the code continues into the `if` condition that evaluates `$@` error variable have something stored. This is like a `catch` in another programming languages. At this way we can handle errors.

</b></details>

### Perl OS

<details>
<summary>What is Perl Open3?</summary><br><b>

From the official [IPC::Open3 docs](https://perldoc.perl.org/IPC::Open3):

"IPC::Open3 - open a process for reading, writing, and error handling using open3()".

With `open3` we can have the full control of the STDIN, STDOUT, STDERR. It's usually used to execute commands.
</b></details>

<details>
<summary>Using Open3: Create a file with the size of 15MB and check it's created successfully</summary><br><b>

- Code:

```
use IPC::Open3;
use Data::Dumper;

sub execute_command {
    my @command_to_execute = @_;
    my ($stdin, $stdout, $stderr);
    eval {
        open3($stdin, $stdout, $stderr, @command_to_execute);
    };
    if ($@) {
        print "Error. Details: $@";
    }
    close($stdin);
    return $stdout;
}

my $file_name = 'perl_open3_test';
&execute_command('truncate', '-s', '15M', $file_name);
my $result = &execute_command('stat', '-c', '%s', $file_name);
print Dumper(<$result>);
```

- Result:

```
$ -> perl command.pl 
$VAR1 = '15728640
';
```

</b></details>

### Perl Packages & Modules

<details>
<summary>What is a Perl package? And a module?</summary><br><b>

With a Perl package we are defining a namespace.
A Perl module in one simple word can be defined as a `class`. When we create a `class` in Perl we use the `package` keyword. A module can be used with the `use` keyword.
</b></details>

<details>
<summary>What is the difference between .pl and .pm extensions?</summary><br><b>

There's no a real difference between a `.pm` and `.pl` extensions. Perl use `.pm` extensions just to difference it as a perl module (a class). `.pl` extensions are usually named for perl scripts without OOP classes.

</b></details>

<details>
<summary>Why a Perl class (or module) should return something at the end of the file? Check the example.</summary><br><b>

If we want to `use` a Perl module (`import` a class), this module should end in a value different than 0. This is necessary because if we try to import the class and it has a false value, we will not be able to use it.

```
package A;

sub new { return bless {}, shift; };
sub printMethod { print "A\n"; };

1;
```

</b></details>

<details>
<summary>What is cpan? And cpanm?</summary><br><b>

CPAN is the Comprehensive Perl Archive Network. 

CPANM From the official [App::cpanminus](https://metacpan.org/pod/App::cpanminus):
"App::cpanminus - get, unpack, build and install modules from CPAN".

[Find CPAN modules](https://metacpan.org/)

</b></details>

<details>
<summary>How can you install cpanm and a Perl module?</summary><br><b>

There are some different alternatives to install Perl modules. We will use `cpanm`.

- Install `cpanm`:

```
$ cpan App::cpanminus
```

- Install the `Test` module with `cpanm`:

```
cpanm Test
```

Now we can test the `Test` installed module:

```
$ perl -M'Test::Simple tests => 1' -e 'ok( 1 + 1 == 2 );'
1..1
ok 1
```

```
$ perl -M'Test::Simple tests => 1' -e 'ok( 1 + 1 == 3 );'
1..1
not ok 1
#   Failed test at -e line 1.
# Looks like you failed 1 test of 1.
```

</b></details>