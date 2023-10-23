# contract-vis

Visualize smart contracts. 

By plotting the raw bytecode as bytes one can generate some interesting 
visualizations of a smart contract. Like this:

![image](https://github.com/shafu0x/contract-vis/blob/main/output/contract-vis.png)

Contracts, as expected, look very similar to x86 or arm64 executables.

Inspired by [this](https://www.youtube.com/watch?v=4bM3Gut1hIk)

## How it works

Given a file of raw bytecode: 6080F3A2...

Plot each pair on a 2D plane like this:

1) 60-80
2) 80-F3
3) F3-A2

and so on....

My explanation in a bit more detail can be found [here](https://twitter.com/shafu0x/status/1716049443227570660)
