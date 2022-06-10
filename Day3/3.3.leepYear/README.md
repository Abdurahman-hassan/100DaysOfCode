
# Leep Year

It's a simple program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

https://www.youtube.com/watch?v=xX96xng7sAE

This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4

**except** every year that is evenly divisible by 100

**unless** the year is also evenly divisible by 400

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)


## Example Input

```
2400
```

## Example OutPut

```
Leap year.
```

## Example Input

```
1989
```

## Example OutPut

```
Not leap year.
```

![Leep years](https://github.com/Abdurahman-hassan/100DaysOfCode/blob/DayThree/Day3/3.3.leepYear/3.3.leap_year.gif?raw=true)
