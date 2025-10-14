---
title: The versatility of the const keyword in C++ and the ensuing confusion
---

I dove deep into the usages of the const keyword. As you might be aware, the const keyword is extremely context dependent in C++ (CPP). This article is a summary of the various ways in which const can be used and what each of them means. 

1) Method returning const reference.


![const keyword example](/assets/images/posts/const_keyword_cpp/1.png)

Method returning const reference.
The above method returns a const integer reference. In C++, a reference is nothing but an alias. A change of value in the reference will reflect as a change of value in the original variable.

For example, below we can see that a change in var2 reflects as a change in var1.

![](/assets/images/posts/const_keyword_cpp/2.png)

Showcasing references in C++
The getSecret_constRef() method earlier returns a constant integer reference to the private variable "_secret". This means the reference cannot be changed. Since, a change in the reference value would result in a change in the value of "_secret", we can be sure that value of "_secret" also cannot be changed via the reference.

1.1) Let's see how this plays out in the main() function -

![](/assets/images/posts/const_keyword_cpp/3.png)

storing const int& in variables in main()
1.1.1) Line 47 - OK. 

local_const_var not a ref of _secret. Instead local_const_var is an independent variable that has the same value as _secret. local_const_var cannot be changed. Even if it could be changed, the change would not reflect in the value of _secret since local_const_var is simply not a reference to _secret.

1.1.2) Line 49 - OK. 

local_var again is not a reference of _secret. Instead, local_var is an independent variable that is initialized with the same value as _secret. However, any change in local_var will not reflect in _secret.

1.1.3) Line 51 - OK.

local_const_ref is a constant integer reference. This is an actual reference of _secret. But const keyword means local_const_ref cannot change its value and in turn cannot change the value of _secret.

1.1.4) Line 53 - NOT OK.

local_non_const_ref is trying to get an actual reference to _secret BUT make the reference local_non_const_ref modifiable. This betrays the return type of getSecret_constRef() which is "const int&". Hence, this causes compilation error.

2) Method returning const pointer


2.1) Use of const in pointers
Pointers is where the const keyword stars becoming really tricky. Take a look at the following table - 

![](/assets/images/posts/const_keyword_cpp/4.png)

Diff. types of pointers in C++
int *ptr --> This is a simple pointer pointing to an int value. ptr can be made to point to some other int variable. Also, ptr can be used to change the value at the address it is pointing to. 

const int *ptr --> ptr is pointing to a constant integer. ptr can be made to point to some other variable. BUT ptr cannot change the value at the address it is pointing to. It is read only. 

int *const ptr --> ptr is a constant pointer pointing to an int variable. ptr cannot be reassigned to point to some other int variable. But ptr can indeed change the value at the address it is currently pointing to. 

const int *const ptr --> ptr can neither be reassigned to point to some other int value nor can it change the value at the location it is currently pointing to. 

2.2) Method returning const int *

![](/assets/images/posts/const_keyword_cpp/5.png)

Method returning const int *
This method returns a pointer to a constant integer (_secret). This means the variable assigned with the return value of this method can be used to read the value of "_secret" but it cannot be use to change the value of _secret.

2.3) Let's see how this plays out in main()

![](/assets/images/posts/const_keyword_cpp/6.png)

Main() counterpart of const int * getter().
2.3.1) Line 71 - OK

Type of local_normal_ptr_const_int matches the return type of the getter. local_normal_ptr_const_int can only dereference and read value in _secret. But it cannot modify value of _secret.

The error in line 75 proves this.

2.3.2) Line 80 - OK

local_const_ptr_const_int cannot change the address it points to AND cannot change value in the address being pointed to (_secret). This satisfies the return type of the getter.

2.3.3) Line 85 - NOT OK

Because, if compiler error was not raised, this would mean local_normal_ptr_normal_int can easily be dereferenced and change value of _secret. This is however explicitly forbidden by return type of getSecret_Normal_Pointer_constInt() i.e. "const int*".

2.3.4) Line 88 - NOT OK

Because, here local_const_ptr_normal_int cannot be reassigned to point to a new address, but the value at the address being pointed to can be changed. This is not what getSecret_Normal_Pointer_constInt() lets us do with a return type of "const int*".



3) const instances (objects) of classes


3.1) Understanding const class objects
const objects promise that the internal state (value of member variables) will remain unchanged throughout the scope of the object. It can only be assigned values at the time of object creation using a constructor for example.  

const objects can ONLY call const member functions. const member functions CANNOT modify member variables. const member functions can ONLY call other const member functions.

non-const objects can also call const-member functions.

3.2) Defining const methods in User class

![](/assets/images/posts/const_keyword_cpp/7.png)

const methods in class
This usage of const after the parameter list promises that it will not alter the values of any member variables. However, it is permitted to declare variables and assign and reassign values to these variables locally within the const method. This is because these local variable do not form part of the internal state of the class. 

3.3) Let's see how this plays out in main()

![](/assets/images/posts/const_keyword_cpp/8.png)

Calling const methods from main()
3.3.1) Line 99 - OK

Note that const objects can call const method without an error.

3.3.2) Line 101 - NOT OK

const object cannot call normal methods like getSecret() that make no guarantee about preserving the internal state of the object.

3.3.3) Line 103 and 105 - OK

Not const objects like the previously used "User u" can call non-const methods like getSecret() as well as const methods like getSecret_constMethod().
