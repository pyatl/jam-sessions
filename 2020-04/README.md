Since we are stuck at home, it has been a good time for me to play my favorite video game, Factorio. Which I play way too much.

This week's challenge is to write a calculator that can help us play the game.

Table of Contents:
* [1. First steps](#1-first-steps)
* [2. More science!](#2-more-science)
* [3. Automating the Boring Stuff](#3-automating-the-boring-stuff)
* [4. Striking Oil](#4-striking-oil)

In Factorio, your goal is to build a factory that can collect then transform raw materials into increasingly refined items. Your complex network of machinery eventually ingests iron, copper, stone, and coal then makes rockets or nuclear reactors come out of the other side.

## 1. First steps

Here is an example of some very simple recipes:

* you need **1 Iron Ore** to make **1 Iron Plate**
* you need **1 Copper Ore** to make **1 Copper Plate**
* you need **2 Iron Plates** to make **1 Iron Gear Wheel**
* you need **1 Copper Plate and 1 Iron Gear Wheel** to make **1 Automation Science Pack**

**Question 1:** How much Iron Ore and Copper Ore does it take to manufacture 10 Automation Science Packs?

Try to write code that can solve this problem. You may solve it by hand and check that your answers match.

## 2. More science!

*Science Packs* are used in Factorio to do research and unlock new technologies. In order to keep things interesting, science packs become increasingly difficult to manufacture the more you progress!

Here are some new recipes for a new Science Pack:

* you need **1 Iron Plate and 1 Iron Gear Wheel** to make **2 Transport Belts** 
* you need **1 Copper Plate** to make **2 Copper Cables**
* you need **1 Iron Plate and 3 Copper Cables** to make **1 Electronic Circuit**
* you need **1 Iron Plate, 1 Iron Gear, and 1 Electronic Circuit** to make **1 Inserter**
* you need **1 Transport Belt and 1 Inserter** to make **1 Logistic Science Pack**

**Question 2:** How much Iron Ore and Copper Ore does it take to manufacture 200 Automation Science Packs and 200 Logistic Science Packs?

## 3. Automating the Boring Stuff

Doing all of this crafting by hand is possible but very time-consuming. The main gameplay element of Factorio is to build a network of machines and conveyors to do the job for you!

Machines take time to run their recipes, therefore you need to build enough machines to meet your production throughput targets. In this part, we will implement a tool that can compute how many machines we will need.

### Example

Let's look at the recipes from the first part. The time it takes to run each recipe are:

* to mine **1 Iron Ore**: 2 s
* to mine **1 Copper Ore**: 2 s
* to smelt **1 Iron Plate**: 3.2 s
* to smelt **1 Copper Plate**: 3.2 s
* to make **1 Iron Gear Wheel**: 1 s
* to make **1 Automation Science Pack**: 10 s

Let's say we want to make 10 Automation Science Packs per minute. Since it takes 10 seconds for one machine to make one, a single machine will be able to output 60 ÷ 10 = 6 items per minute. Therefore, we will need **2 machines** to build the science packs.

To meet this quota, we will also need to make every minute: 

* 10 Iron Gear Wheels; **1 machine** will be enough (60 ÷ 1 = 60 items/min)
* 10 Copper Plates; **1 machine** is also enough (60 ÷ 3.2 = 18.75 items/min)
* 20 Iron Plates; **2 machines** are required, barely (same as above)
* 10 Copper Ore; **1 machine** enough again (60 ÷ 2 = 30 items/min)
* 20 Iron Ore; **1 machine** as well (same as above)

Therefore, we will need a total **8 machines** to run the full production chain for our production quota of 10 Automation Science Packs per minute. 

### In Practice

Here are the timings for the recipes defined in part 2:

* to make **2 Transport Belts**: 1 s
* to make **2 Copper Cables**: 1 s
* to make **1 Electronic Circuit**: 1 s
* to make **1 Inserter**: 1 s
* to make **1 Logistic Science Pack**: 12 s

**Question 3:** How many machines do you need to sustain a production of 50 Automation Science Packs and 50 Logistic Science Packs per minute?

## 4. Striking Oil

Later in the game you discover oil processing, and to your dismay its production process is quite a bit more complicated. The recipes are as follows:

* **100 Crude Oil** can be refined into **25 Heavy Oil, 45 Light Oil and 55 Petroleum Gas** in 5 s,
* **40 Heavy Oil** can be cracked into **30 Light Oil** in 2 s,
* **30 Light Oil** can be cracked into **20 Petroleum Gas** in 2 s.

In general, Petroleum Gas is the resource we need but refining oil to make it generates excess Light Oil and Heavy Oil. To make the process work without any excess produce, cracking operations need to be used to eliminate the excess oil.

**Question 4:** How much Crude Oil is needed to make 950 units of Petroleum Gas without any excess oil?

In practice, Heavy Oil and Light Oil are also useful in their own right and need to be produced (in smaller quantities) as well.

**Question 5:** How much Crude Oil is needed to make 2,000 units of Petroleum Gas, 800 units of Light Oil and 225 units of Heavy Oil?

### Tips:

There are two approaches to solving the oil processing problem:
1. do the math and find the solutions to the system,
2. use iterative calculation to find a stable result in steps.

From a programming perspective, the second approach is a lot more fun. And it has the added advantage to be easy to fix if the recipes change (which _does_ happen in Factorio).

I find it useful in this situation to use "production cycles per minute" as variables to solve with, and write down how to adjust each variable in function of the other. It can take so trial and error to find a stable solution.
