# CharacterCounter
This is the bloody final project for CSc 113: Programming in Python

## Libraries
In this project, there is an explicit limitation on the libraries that we are allowed to use which simply consists of:
* tkinter
* turtle

## Approach
The user enters a text file to be parsed using a simple GUI written 
using tkinter library and enters the number of _n_ slices of most common characters 
in the text file that should be displayed. The remaining characters are then aggregated together 
into one slice.

The method that performs the actual parsing reads one line of the file content at a time, 
scans each character where for every occurrence of the said element, 
a dictionary whose key is the character currently being read will have its associated key-value pair, 
which is nothing more than an integer counter, incremented by one. 
This process continues for ___every___ characters in the line currently being read, 
for every line of the text file, until the point where EOF (End of File) is reached.