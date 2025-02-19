{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5de76e2b-f15a-407b-ab7b-51667ff3fa3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the number of Fibonacci terms:  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fibonacci Sequence: 0 1 1 2 3 5 8 13 21 34\n"
     ]
    }
   ],
   "source": [
    "def fib(n):\n",
    "    if n <= 0:\n",
    "        return 0\n",
    "    elif n == 1:\n",
    "        return 1\n",
    "    else:\n",
    "        return fib(n - 1) + fib(n - 2)\n",
    "\n",
    "def fib_sequence(n):\n",
    "    return [fib(i) for i in range(n)]\n",
    "\n",
    "num_terms = int(input(\"Enter the number of Fibonacci terms: \"))\n",
    "print(\"Fibonacci Sequence:\", *fib_sequence(num_terms))\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
