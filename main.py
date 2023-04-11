from image_generation import gen_card
import os

# Meta data and header
def get_header():
    github_url = 'https://github.com/' + github_usr
    io_address = 'https://' + github_usr + '.github.io'
    site_head = f'<!DOCTYPE html>\n<html>\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1">\n  <title>{site_title}</title>\n  <link rel="stylesheet" href="styles.css">\n  <meta property="og:title" content={share_prev}>\n  <meta property="og:description" content={site_descr}>\n  <meta property="og:image" content="seo-image.png">\n  <meta property="og:url" content={io_address}>\n  <meta name="twitter:card" content="summary_large_image">\n</head>\n'
    beginbody = f'<body>\n  <header>\n    <h1 style="margin-left: 10px;">{site_title}</h1>\n  </header>\n  <main class="container">\n    <section>\n      <div class="cards-main">\n        <br><br>\n'
    with open('index.html', 'w') as f:
        f.write(site_head + beginbody)

# Add cards
def add_cards():
    github_url = 'https://github.com/' + github_usr
    with open('index.html', 'a') as f:
        # Iterate over the repo list and generate HTML for each repo
        for i, repo in enumerate(feat_repos):
            n = i + 1
            cards = f"""
            <div class="card">       
              <a href={github_url + '/' + feat_repos[i]}>
              <img src="Images/repo_{n}.png" alt="">
              <img src="https://github-readme-stats-sigma-five.vercel.app/api/pin/?username={github_usr}&repo={feat_repos[i]}" alt="">
              <p>Description for repo number {n}</p></a>
            </div>"""
            f.write(cards)

            # Generate card images for each repo
            gen_card(n)

        # Close card section
        f.write('</div>\n    </section>')

# About section
def about_section():
    with open('index.html', 'a') as f:
        f.write(f"""
        <section>\n
          <div class="about-2">\n
          <br>\n
          <h2>About Me</h2>\n
          <p>Hello!</p>\n
          <p>{about_site}</p>\n
          </div>\n
        </section>\n
    """)

def close_body():
    # Footer
    with open('index.html', 'a') as f:
        f.write(f"""
     <footer>
        <div class="footer">
        <p>&copy; 2023 This website was generated with <a href="https://github.com/wlinds/ez_cards">wlinds/ez_cards</a></p>
        </div>    
      </footer>
    """)
    # Close body
    with open('index.html', 'a') as f:
        f.write('\n</body></html>')

if __name__ == "__main__":

    # Enter your github username
    github_usr = 'wlinds'

    # Enter the title for your site (this will also become header)
    site_title = 'My awesome website'

    share_prev = 'This text will be displayed when sharing the link to your site.'
    site_descr = 'This is a site description, for google search indexing etc.'

    get_header()

    # Enter which repositories you want to feature as cards
    feat_repos = ['RedViz', 'tpme', 'ITHS-AI22-ML']

    add_cards()

    # Enter your about text, will be displayed at bottom
    about_site = 'Hello, this is my portfolio of this and that and this and those and so.'

    about_section()
    close_body()
