{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "turtle.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPhi1lqLNLhr2aFGB1YXOnA",
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
        "<a href=\"https://colab.research.google.com/github/instone1031/code/blob/master/turtle.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 386
        },
        "id": "lkCt6vdOw0n1",
        "outputId": "e930fbee-b35a-4da9-c4db-c19bad660022"
      },
      "source": [
        "import turtle\n",
        "import random\n",
        "\n",
        "t = turtle.Turtle()\n",
        "t.shape(\"turtle\")\n",
        "t.pencolor(\"black\")\n",
        "\n",
        "\n",
        "def draw_square(x, y, c):\n",
        "    t.color(c)\n",
        "    t.pencolor(\"black\")\n",
        "    t.penup()\n",
        "    t.goto(random.randint(-100, 100), random.randint(-100, 100))\n",
        "    t.pendown()\n",
        "    t.begin_fill()\n",
        "    for i in range(2):\n",
        "        t.fd(x)\n",
        "        t.lt(90)\n",
        "        t.fd(y)\n",
        "        t.lt(90)\n",
        "    t.end_fill()\n",
        "\n",
        "\n",
        "for i in ['yellow', 'red', 'purple', 'blue']:\n",
        "    draw_square(100, 100, i)\n",
        "\n",
        "turtle.mainloop()\n",
        "turtle.bye()\n"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TclError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTclError\u001b[0m                                  Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-4-f41a99de158e>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mrandom\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0mt\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mturtle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mTurtle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m \u001b[0mt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"turtle\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0mt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpencolor\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"black\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, shape, undobuffersize, visible)\u001b[0m\n\u001b[1;32m   3810\u001b[0m                  visible=_CFG[\"visible\"]):\n\u001b[1;32m   3811\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mTurtle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_screen\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3812\u001b[0;31m             \u001b[0mTurtle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_screen\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mScreen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3813\u001b[0m         RawTurtle.__init__(self, Turtle._screen,\n\u001b[1;32m   3814\u001b[0m                            \u001b[0mshape\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36mScreen\u001b[0;34m()\u001b[0m\n\u001b[1;32m   3660\u001b[0m     else return the existing one.\"\"\"\n\u001b[1;32m   3661\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mTurtle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_screen\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3662\u001b[0;31m         \u001b[0mTurtle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_screen\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_Screen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3663\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mTurtle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_screen\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3664\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m   3676\u001b[0m         \u001b[0;31m# preserved (perhaps by passing it as an optional parameter)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3677\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0m_Screen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_root\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3678\u001b[0;31m             \u001b[0m_Screen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_root\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_root\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_Root\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3679\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_root\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtitle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m_Screen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_title\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3680\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_root\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mondestroy\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_destroy\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    432\u001b[0m     \u001b[0;34m\"\"\"Root class for Screen based on Tkinter.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    433\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 434\u001b[0;31m         \u001b[0mTK\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mTk\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    435\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    436\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0msetupcanvas\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mwidth\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheight\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcwidth\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcheight\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.7/tkinter/__init__.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, screenName, baseName, className, useTk, sync, use)\u001b[0m\n\u001b[1;32m   2021\u001b[0m                 \u001b[0mbaseName\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mbaseName\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mext\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2022\u001b[0m         \u001b[0minteractive\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2023\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtk\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_tkinter\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcreate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mscreenName\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbaseName\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mclassName\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0minteractive\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mwantobjects\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0museTk\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msync\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0muse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2024\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0museTk\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2025\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_loadtk\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTclError\u001b[0m: no display name and no $DISPLAY environment variable"
          ]
        }
      ]
    }
  ]
}