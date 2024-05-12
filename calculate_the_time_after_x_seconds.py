"""
[LintCode2330]Calculate the time after x seconds
Link:https://www.lintcode.com/problem/2330/

Your code needs to read the current time from the standard input stream (console). The input format is such as hh:mm:ss, which represents hour, minute, and second respectively, and then a positive integer x is given to find the elapsed time. The time after x seconds is expressed, and the result is calculated and printed to the standard output stream (console).
"""

# write your code here
# read data from console
data = input()
x = int(input())

# output the answer to the console according to the requirements of the question
hour, minute, sec = data.split(":")

seconds = int(hour) * 60 * 60 + int(minute) * 60 + int(sec) + x

result_hour = (seconds // (60 * 60)) % 24
result_minute = seconds % (60 * 60) // 60
result_sec = seconds % 60

print("{:02d}:{:02d}:{:02d}".format(result_hour, result_minute, result_sec))
