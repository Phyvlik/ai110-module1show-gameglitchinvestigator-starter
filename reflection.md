# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The first time I ran the game, it appeared as a Streamlit web app with a number guessing interface, but it was unplayable due to multiple bugs that made winning impossible and hints misleading.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
1. The hints were backwards: "Go HIGHER" when the guess was too high, and "Go LOWER" when too low.
2. The secret number was inconsistent, sometimes changing or not matching the difficulty range.
3. The attempt counter started incorrectly, showing wrong attempts left.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used GitHub Copilot as the primary AI tool for code analysis, refactoring suggestions, and debugging assistance.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI suggested refactoring the game logic functions from app.py to logic_utils.py and fixing the check_guess function to remove the attempt-based string conversion that caused incorrect hints. I verified this by running pytest, which showed all tests passing, and manually testing the Streamlit app where hints now correctly indicated higher/lower based on numerical comparison.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The AI initially suggested that the test assertions were correct as written, but they were expecting single strings while the function returned tuples. I verified this by running the tests, which failed with assertion errors, and then corrected the tests to check result[0] for the outcome, after which tests passed.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was fixed by running automated tests with pytest to ensure they passed, and by manually testing the Streamlit app to verify correct behavior in the UI.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran pytest on the test_game_logic.py file, which showed that all three tests (winning guess, too high, too low) passed after fixing the check_guess function and updating the test assertions to handle the tuple return value.

- Did AI help you design or understand any tests? How?
The AI helped me understand that the tests were failing because they expected strings but received tuples, and suggested updating the assertions to check result[0], which I implemented and verified with pytest.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing because the app regenerated it on every rerun, and Streamlit reruns the whole script when a button is clicked. There was no persistent session state guarding it, so it reset on every submit.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns the entire Python script from top to bottom whenever the user interacts with the UI. To keep values like a secret number or score consistent across those reruns, you store them in `st.session_state`, which acts like persistent memory between reruns.

- What change did you make that finally gave the game a stable secret number?
I used `st.session_state` to initialize the secret number only when it was missing, and I ensured the secret is only regenerated when the user clicks the "New Game" button. This prevents it from changing on every rerun.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
I want to reuse the habit of running tests after every change to verify fixes, and using AI to help refactor and debug code systematically.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I would be more specific in my prompts to the AI from the start, asking for targeted fixes rather than broad suggestions, to avoid having to iterate on incorrect assumptions.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI-generated code can have subtle bugs that require careful debugging, and that AI is a powerful tool for both creating and fixing code when used collaboratively. It made me more critical of generated code and appreciative of testing and refactoring processes.
