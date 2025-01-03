
## True/False Quiz

A simple Python-based True/False quiz game that uses the [OpenTDB API](https://opentdb.com/). The program fetches 10 
unique questions per session, tracks how many you answer correctly, and ends when all questions have been answered.

### Features

- **Dynamic Questions**: Fetches new questions from OpenTDB API every time you run the game.
- **Score Tracking**: Keeps a count of correct answers.
- **User-Friendly**: Simple interface to answer True/False questions.
- **Replayability**: Enjoy a fresh set of questions each time you play.

### Prerequisites

- Python 3.6+ installed on your system
- Internet connection (required to fetch questions)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AenuHub/true-false-quiz.git
   cd true-false-quiz
   ```

2. Install required libraries:

   ```bash
   pip install requests
   ```

### Usage

1. Run the program:

   ```bash
   python true_false_quiz.py
   ```

2. Follow the prompts to answer the questions.
3. At the end, your total score will be displayed.

### How It Works

1. Fetches 10 True/False questions using the OpenTDB API.
2. Displays each question and waits for the user input (`True` or `False`).
3. Validates the user's answer and updates the score.
4. Ends the game after all questions are answered.

### Customization

Want to fetch more than 10 questions or change the question, category type? Modify the API call parameters in the 
source code.

### Acknowledgments

- [OpenTDB API](https://opentdb.com/) for providing a database of trivia questions.
