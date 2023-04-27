import c_modules
import ez_cards_gui
import os

# Enter your github username
github_usr = 'wlinds'

# Enter the title for your site (this will also become header)
site_title = 'My awesome website'
share_prev = 'This text will be displayed when sharing the link to your site.'
site_descr = 'This is a site description, for google search indexing etc.'

# Enter which repositories you want to feature as cards
feat_repos = ['RedViz', 'tpme', 'ITHS-AI22-ML']

# Enter your about text, will be displayed at bottom
about_site = 'Hello, this is my portfolio of this and that and this and those and so.'


if __name__ == "__main__":

    kwargs = {
    'github_usr': github_usr,
    'site_title': site_title,
    'share_prev': share_prev,
    'site_descr': site_descr,
    }

    c_modules.get_header(**kwargs)
    c_modules.add_cards(github_usr=github_usr, feat_repos=feat_repos)
    c_modules.about_section(about_site=about_site)
    c_modules.close_body()
