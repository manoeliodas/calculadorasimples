{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMpJOUn11WLDK2XP9nevo0O",
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
        "<a href=\"https://colab.research.google.com/github/manoeliodas/calculadorasimples/blob/main/calculadora.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "\n",
        "  numeroum= int(input(\" digite o primeiro numero \"))\n",
        "  numerodois= int(input(\" digite o segundo numero \"))\n",
        "  operador= input(\" digite o operador numero \")\n",
        "\n",
        "  if operador == \"+\":\n",
        "    conta = numeroum  + numerodois \n",
        "  elif operador == \"-\":\n",
        "    conta = numeroum  - numerodois  \n",
        "  elif operador == \"*\":\n",
        "    conta = numeroum  * numerodois  \n",
        "  elif operador == \"/\":\n",
        "    conta = numeroum  / numerodois\n",
        "  else:\n",
        "    print(\"operador errado seu animal\")\n",
        "    conta = 0\n",
        "\n",
        "  print(conta)\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "id": "VVmZAzLy_EUt"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}