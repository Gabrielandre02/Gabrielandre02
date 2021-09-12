<h1>I'm Gabriel! </h1>
 
 
 Hello world!  <img src="https://github.com/TheDudeThatCode/TheDudeThatCode/raw/master/Assets/Earth.gif" width="24px" style="max-width: 100%;">
<img align="right" width="400" height="400" src="https://i.pinimg.com/originals/4b/1c/51/4b1c51711b920215c3cd654d313195ad.gif">


<p> Hi, I'm in the first period of software engineering </p> 
<a href="https://www.uninter.com/centro-universitario-internacional/" rel="nofollow"> <b>CENTRO UNIVERSITÁRIO INTERNACIONAL - UNINTER </b>. </a>
<br>

 Also, I'm always reading about technology and looking for new things!

:computer: a future backend develop!

:house_with_garden: I’m from Brazil.

:books: I’m currently learning everything.

:outbox_tray: 2021 Goals: looking for an opportunity to grow!


## About me

<a href="https://www.linkedin.com/in/gabriel-andre-01429a213/" rel="nofollow"><img src="https://github.com/TheDudeThatCode/TheDudeThatCode/raw/master/Assets/Linkedin.svg" alt="Linkedin Logo" width="32" style="max-width:100%;"></a>



- Thanks for visiting.

- Enjoy it!! o/

name: Generate Datas

on:
  schedule: # execute every 12 hours
    - cron: "* */12 * * *"
  workflow_dispatch:

jobs:
  build:
    name: Jobs to update datas
    runs-on: ubuntu-latest
    steps:
      # Snake Animation
      - uses: Platane/snk@master
        id: snake-gif
        with:
          github_user_name: gabrielandre02
          svg_out_path: dist/github-contribution-grid-snake.svg

      - uses: crazy-max/ghaction-github-pages@v2.1.3
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
