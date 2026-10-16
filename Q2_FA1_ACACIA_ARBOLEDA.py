{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPJ5cQ8LSshfyI+5hjErUGu",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/pldarboleda31-boop/Distance-calculator/blob/main/Q2_FA1_ACACIA_ARBOLEDA.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Display Operations\n",
        "print(\"1. Addition\")\n",
        "print(\"2. Subtraction\")\n",
        "print(\"3. Multiplication\")\n",
        "print(\"4. Division\")\n",
        "\n",
        "\n",
        "def add_numbers(num1, num2):\n",
        "    return num1 + num2\n",
        "\n",
        "\n",
        "def subtract_numbers(num1, num2):\n",
        "    return num1 - num2\n",
        "\n",
        "\n",
        "def multiply_numbers(num1, num2):\n",
        "    return num1 * num2\n",
        "\n",
        "\n",
        "def divide_numbers(num1, num2):\n",
        "    return num1 / num2\n",
        "\n",
        "\n",
        "# Get user's selected operation\n",
        "choice = int(input(\"Select an operation to use: \"))\n",
        "\n",
        "# Get input numbers\n",
        "num1 = float(input(\"Enter num1: \"))\n",
        "num2 = float(input(\"Enter num2: \"))\n",
        "\n",
        "# Perform the indicated operations\n",
        "if choice == 1:\n",
        "    result = add_numbers(num1, num2)\n",
        "    print(f\"The sum of {num1} and {num2} is {result}\")\n",
        "\n",
        "elif choice == 2:\n",
        "    result = subtract_numbers(num1, num2)\n",
        "    print(f\"The difference of {num1} and {num2} is {result}\")\n",
        "\n",
        "elif choice == 3:\n",
        "    result = multiply_numbers(num1, num2)\n",
        "    print(f\"The product of {num1} and {num2} is {result}\")\n",
        "\n",
        "elif choice == 4:\n",
        "    if num2 != 0:\n",
        "        result = divide_numbers(num1, num2)\n",
        "        print(f\"The quotient of {num1} and {num2} is {result}\")\n",
        "    else:\n",
        "        print(\"Error: You cannot divide by zero.\")\n",
        "\n",
        "else:\n",
        "    print(\"Invalid operation choice.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "g_OsMxC8SYZC",
        "outputId": "7a3cabcf-161a-48be-83f8-43df54e90b4a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1. Addition\n",
            "2. Subtraction\n",
            "3. Multiplication\n",
            "4. Division\n",
            "Select an operation to use: 1\n",
            "Enter num1: 5\n",
            "Enter num2: 2\n",
            "The sum of 5.0 and 2.0 is 7.0\n"
          ]
        }
      ]
    }
  ]
}