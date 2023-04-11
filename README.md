# ez_cards

Create a neat and simple portfolio with this simple python script and host it on Github for free! <a href="https://wlinds.github.io">Demo here!</a>

## How to use:

1. Copy this repo
2. Open main.py, scroll to the bottom, change the variables:

    Github username, case sensitive:
    ```
    github_usr = 'user'
    ```
    Title for your site (this will also become header:
    ```
    site_title = 'My awesome website'
    ```
    Custom meta data:
    ```
    share_prev = 'This text will be displayed when sharing the link to your site on Discord etc.
    site_descr = 'This is a site description, for google search indexing etc.
    ```
    Enter the repositories you want to feature, case sensitive:
    ```
    feat_repos = ['RedViz', 'tpme', 'ITHS-AI22-ML']
    ```
    Enter your about text, will be displayed at bottom:
    ```
    about_site = 'Hello, this is my portfolio of this and that and this and those and so.'
    ```

3. Run the main script (only required package is Pillow, which is only used for dummy image generation.
3.1 You could probably run it without Pillow, just make sure to add images to each card.
4. Rename the repo to *your-username*.github.io

    The repo should look like this:
    ```
    ez_cards/
    ├── Images/
    │ ├── repo_1.png
    │ ├── repo_2.png
    │ └── repo_3.png (etc. for each repo)
    ├── index.html
    ├── readme.md (this is not needed)
    └── styles.css
    ```
    
5. Done! You can now visit the site at *your-username*.github.io.
