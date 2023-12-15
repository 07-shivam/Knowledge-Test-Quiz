{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "id": "vFQen5r51EKG"
      },
      "outputs": [],
      "source": [
        "# main.py\n",
        "from questions import Question\n",
        "from quiz import Quiz\n",
        "from player import Player\n",
        "import csv\n",
        "\n",
        "def load_questions_from_csv(file_path):\n",
        "    questions = []\n",
        "    with open(file_path, newline='', encoding='utf-8') as csvfile:\n",
        "        reader = csv.DictReader(csvfile)\n",
        "        for row in reader:\n",
        "            text = row['text']\n",
        "            options = [row[f'option{i}'] for i in range(1, 5)]\n",
        "            correct_option = int(row['correct_option'])\n",
        "            questions.append(Question(text, options, correct_option))\n",
        "    return questions\n",
        "\n",
        "def main():\n",
        "    player_name = input(\"Enter your name: \")\n",
        "    player = Player(player_name)\n",
        "\n",
        "    # Load questions from CSV\n",
        "    questions = load_questions_from_csv('questions.csv')\n",
        "\n",
        "    quiz = Quiz(questions)\n",
        "    quiz.run_quiz()\n",
        "\n",
        "    player.update_score(quiz.score)\n",
        "    print(f\"{player.name}, your final score is {player.score}/{len(questions)}.\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "oNC6Rxo51OtA"
      },
      "execution_count": None,
      "outputs": []
    }
  ]
}
