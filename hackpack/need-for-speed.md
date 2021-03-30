Opening the binary we recieved and navigating to the main function gives us this for our main function:

```c
undefined8 main(void)

{
  header();
  set_timer();
  get_key();
  print_flag();
  return 0;
}
```

This looks fairly interesting, because there's some pretty readable function names as well as a `print_flag()` which is obviously of interest to us.

Peeping into the set_timer() function we discover that the function creates a signal handler that runs on a one second time - exiting afterwards.  
The `alarm` call that works on the signal sends that signal after a given number of seconds - one, in our case. After, it simply exits the program.

The internals of the other functions aren't super important, but we can decipher that it does some expensive operations to purposely take a long time to complete and print a flag. 

Given this, we can decipher that we probably need to modify the `set_timer()` function to execute either after a long amount of time, or not exit after execution. \

So, to summarize, we've deduced the that the program sets a timer that internally creates a callback that exits after 1 second, then generates a key and prints out the flag.   

My preferred approach is to us LD_PRELOAD to preload our own version of `alarm` as a shared library. This just means figuring out the function signature of alarm, which is trivial (unsigned int return and unsigned int argument) with Ghidra. After, we just compile alarm.c with an empty function (printing a message for debugging) and the --shared flag. Then, we run `LD_PRELOAD=./alarm.so ./need-for-speed` and bam, flag.
