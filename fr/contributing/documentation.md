# Documentation

  * [Content guidelines](documentation/content_guidelines.html)
  * [RST cheat sheet](documentation/rst_cheat_sheet.html)
  * [RST guidelines](documentation/rst_guidelines.html)

This introductory guide will help you acquire the tools and knowledge you need
to write documentation, whether you plan to make a minor content change or
document an application from scratch.

Pour plus d'infos

[Discover other ways to contribute to Odoo](../contributing.html)

Read the introduction to the reStructuredText language if you are not familiar
with it. Then, you have two courses of action to start contributing to the
documentation, depending on whether you want to propose minor changes to
existing content or you instead want to work on significant changes to new and
existing content.

  * **For minor changes** , for example, adding a paragraph or fixing a typo, we recommend **using the GitHub interface**. This is the easiest and fastest way to submit your changes, and it is suitable for non-technical people. Jump directly to the Make your first contribution section to get started.

  * **For more complex changes** , it is necessary to **use Git** and work from a local copy of the documentation. Follow the instructions in the Environment setup section to first prepare your environment.

## reStructuredText (RST)

The documentation is written in **reStructuredText** (RST), a [lightweight
markup language](https://en.wikipedia.org/wiki/Lightweight_markup_language)
consisting of regular text augmented with markup, which allows including
headings, images, notes, and so on. This might seem a bit abstract, but there
is no need to worry; RST is not hard to learn, especially if you intend to
make minor changes to the content.

If you need to learn about a specific markup, head over to our [cheat sheet
for RST](documentation/rst_cheat_sheet.html); it contains all the information
you should ever need for the documentation of Odoo.

Important

We kindly ask you to observe a set of
[content](documentation/content_guidelines.html) and
[RST](documentation/rst_guidelines.html) guidelines as you write
documentation. This ensures that you stay consistent with the rest of the
documentation and facilitates the approval of your content changes as the Odoo
team reviews them.

Pour plus d'infos

  * [Content guidelines](documentation/content_guidelines.html)

  * [RST cheat sheet](documentation/rst_cheat_sheet.html)

  * [RST guidelines](documentation/rst_guidelines.html)

## Environment setup

The instructions below help you prepare your environment for making local
changes to the documentation and then push them to GitHub. Skip this section
and go to Make your first contribution if you have already completed this step
or want to make changes from the GitHub interface.

  1. First, you need to [create a GitHub account](https://github.com/join). Odoo uses GitHub to manage the source code of its products, and this is where you will make your changes and submit them for review.

  2. [Generate a new SSH key and register it on your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

  3. Go to [github.com/odoo/documentation](https://github.com/odoo/documentation) and click on the Fork button in the top right corner to create a fork (your own copy) of the repository on your account. This creates a copy of the codebase to which you can make changes without affecting the main codebase. Skip this step if you work at Odoo.

  4. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). It is a command-line (a text interface) tool that allows tracking the history of changes made to a file and, more importantly, working on different versions of that file simultaneously. It means you do not need to worry about overwriting someone else’s pending work when making changes.

Verify that the installation directory of Git is included in your system’s
`PATH` variable.

Linux and macOSWindows

Follow the [guide to update the PATH variable on Linux and
macOS](https://unix.stackexchange.com/a/26059) with the installation path of
Git (by default `/usr/bin/git`).

Follow the [guide to update the PATH variable on
Windows](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-
easy-command-line-access/) with the installation path of Git (by default
`C:\Program Files\Git`).

  5. Configure Git to identify yourself as the author of your future contributions. Enter the same email address you used to register on GitHub.
    
        $ git config --global user.name “Your Name”
    $ git config --global user.email “youremail@example.com”
    

  6. Clone the sources with Git and navigate into the local repository.
    
        $ git clone git@github.com:odoo/documentation.git
    $ cd documentation
    

  7. Configure Git to push changes to your fork rather than to the main codebase. In the commands below, replace `<your_github_account>` with the name of the GitHub account on which you created the fork. Skip this step if you work at Odoo.
    
        $ git remote add dev git@github.com:<your_github_account>/documentation.git
    

  8. Configure Git to ease the collaboration between writers coming from different systems.

Linux and macOSWindows

    
        $ git config --global core.autocrlf input
    $ git config commit.template `pwd`/commit_template.txt
    
    
        $ git config --global core.autocrlf true
    $ git config commit.template %CD%\commit_template.txt
    

  9. Install the latest release of [Python](https://wiki.python.org/moin/BeginnersGuide/Download) and [pip](https://pip.pypa.io/en/stable/installation/) on your machine.

  10. Install the Python dependencies of the documentation with pip.
    
        $ pip install -r requirements.txt
    

Verify that the installation directory of the Python dependencies is included
in your system’s `PATH` variable.

Linux and macOSWindows

Follow the [guide to update the PATH variable on Linux and
macOS](https://unix.stackexchange.com/a/26059) with the installation path of
the Python dependencies (by default `~/.local/bin`).

Follow the [guide to update the PATH variable on
Windows](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-
easy-command-line-access/) with the installation path of the Python
dependencies.

  11. Install Make.

Linux and macOSWindows

    
        $ sudo apt install make -y
    

Follow the [guide to install Make on
Windows](https://www.technewstoday.com/install-and-use-make-in-windows).

  12. [Install pngquant](https://pngquant.org/).

  13. That’s it! You are ready to make your first contribution with Git.

## Make your first contribution

Contribute from the GitHub interfaceContribute with Git

  1. Verify that you are browsing the documentation in the version that you intend to change. The version can be selected from the dropdown in the top menu.

  2. Head to the page that you want to change and click on the Edit on GitHub button in the top right corner of the page.

  3. Click on the Fork this repository button to create a fork (your own copy) of the repository on your account. This creates a copy of the codebase to which you can make changes without affecting the main codebase. Skip this step if you work at Odoo.

![../_images/fork-repository.png](../_images/fork-repository.png)

  4. Make the desired changes while taking care of following the [content](documentation/content_guidelines.html) and [RST](documentation/rst_guidelines.html) guidelines.

Astuce

Click on the Preview changes button to review your contribution in a more
human-readable format. Be aware that the preview is not able to handle all
markups correctly. Notes and tips, for instance, are shown as plain text.

  5. Scroll to the bottom of the page and fill out the small form to propose your changes. In the first text box, write a very short summary of your changes. For instance, « Fix a typo » or « Add documentation for invoicing of sales orders. » In the second text box, explain _why_ you are proposing these changes. Then, click on the Propose changes button.

![../_images/propose-changes.png](../_images/propose-changes.png)

  6. Review your changes and click on the Create pull request button.

  7. Tick the Allow edits from maintainer checkbox. Skip this step if you work at Odoo.

  8. Review the summary that you wrote about your changes and click on the Create pull request button again.

  9. At the bottom of the page, check the mergeability status and address any issues.

  10. As soon as your PR is ready for merging, a member of the Odoo team will be automatically assigned for review. If the reviewer has questions or remarks, they will post them as comments and you will be notified by email. Those comments must be resolved for the contribution to go forward.

  11. Once your changes are approved, the reviewer merges them and they appear online the next day!

Important

Some steps of this guide require to be comfortable with Git. Here are some
[tutorials](https://www.atlassian.com/git/tutorials) and an [interactive
training](https://learngitbranching.js.org/) if you are stuck at some point.

Now that your environment is set up, you can start contributing to the
documentation. In a terminal, navigate to the directory where you cloned the
sources and follow the guide below.

  1. Choose the version of the documentation to which you want to make changes. Keep in mind that contributions targeting an [unsupported version of Odoo](../administration/supported_versions.html) are not accepted. This guide assumes that the changes target the documentation of Odoo 16, which corresponds to branch `16.0`.

  2. Create a new branch starting from branch 16.0. Prefix the branch name with the base branch: `16.0-...`. If you work at Odoo, suffix the branch name with your Odoo handle: `16.0-...-xyz`.

Example

    
        $ git switch -c 16.0-explain-pricelists
    
    
        $ git switch -c 16.0-explain-pricelists-xyz
    

  3. Make the desired changes while taking care of following the [content](documentation/content_guidelines.html) and [RST](documentation/rst_guidelines.html) guidelines.

  4. Compress all PNG images that you added or modified.
    
        $ pngquant path/to/image.png
    $ mv path/to/image-fs8.png path/to/image.png
    

  5. Write a [redirect rule](https://github.com/odoo/documentation/tree/16.0/redirects/MANUAL.md) for every RST file that your renamed.

  6. Build the documentation with **make**. Then, open `_build/index.html` in your web browser to browse the documentation with your changes.

Astuce

Use **make help** to learn about other useful commands.

  7. Commit your changes. Write a clear commit message as instructed in the [Git guidelines](development/git_guidelines.html).
    
        $ git add .
    $ git commit
    

  8. Push your change to your fork, for which we added the remote alias `dev`.

Example

    
        $ git push -u dev 16.0-explain-pricelists
    

If you work at Odoo, push your changes directly to the main codebase whose
remote alias is `origin`.

Example

    
        $ git push -u origin 16.0-explain-pricelists-xyz
    

  9. Open a PR on GitHub to submit your changes for review.

    1. Go to the [compare page of the odoo/documentation codebase](https://github.com/odoo/documentation/compare).

    2. Select **16.0** for the base.

    3. Click on compare across forks.

    4. Select **< your_github_account>/odoo** for the head repository. Replace `<your_github_account>` with the name of the GitHub account on which you created the fork. Skip this step if you work at Odoo.

    5. Review your changes and click on the Create pull request button.

    6. Tick the Allow edits from maintainer checkbox. Skip this step if you work at Odoo.

    7. Complete the description and click on the Create pull request button again.

  10. At the bottom of the page, check the mergeability status and address any issues.

  11. As soon as your PR is ready for merging, a member of the Odoo team will be automatically assigned for review. If the reviewer has questions or remarks, they will post them as comments and you will be notified by email. Those comments must be resolved for the contribution to go forward.

  12. Once your changes are approved, the reviewer merges them and they appear online the next day!

  *[RST]: reStructuredText
  *[PR]: Pull Request

