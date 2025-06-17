
import streamlit as st

st.title("👋 Hi, I'm Pokhrel")
st.write("Welcome to my portfolio app!")

st.header("About Me")
st.write("""
I'm a passionate developer/data scientist/machine learning enthusiast.
I love working on interesting projects and learning new technologies.
""")

st.header("Projects")
st.write("- 🔹 Project 1: Description of project 1")
st.write("- 🔹 Project 2: Description of project 2")
st.write("- 🔹 Project 3: Description of project 3")

st.header("Contact")
st.write("📧 your.email@example.com")
st.write("[💼 LinkedIn](https://www.linkedin.com/in/your-profile)")
st.write("[💻 GitHub](https://github.com/yourusername)")

The app’s code is not connected to a remote GitHub repository. To deploy on Streamlit Community Cloud, please put your code in a GitHub repository and publish the current branch.
how?
1. Create a new GitHub repository.
2. Initialize a git repository in your project folder (if not already done):
   ```
   git init
   ```
3. Add your files to the repository:
   ```
   git add .
   ```
4. Commit your changes:
   ```
   git commit -m "Initial commit"
   ```
5. Link your local repository to the GitHub repository:
   ```
   git remote add origin <your-github-repo-url>
   ```
6. Push your changes to GitHub:
   ```
   git push -u origin main
   ```
