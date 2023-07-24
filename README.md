# 2048-game-base-on-python_flask

## 1  The basic algorithm and framework

We used minimax algorithm and alpha-beta pruning algorithm to make optimal decisions for our 2048 game. The entire game is developed on the web using flask as a framework. In front and back end processing, jquery library is used to process data asynchronously, so as to achieve the effect of data interaction.

## 2 minimax and alpha-beta algorithm 

minimax algorithm is a negative algorithm. In the interaction with the machine, we take the evaluation function as the evaluation value and obtain the minimum value of the evaluation value. Our need is to get the maximum of the minimum set of values to get the least bad decision.

## 3 environment

For convenience, we downloaded both the jquery library and the handlebars library locally in case we couldn't connect to external links when debugging locally.

~~~python
pip install -r requirements.txt
~~~

