# FutureFly

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://gitlab.com/team-10HR/travel-saver-app">
    <img src="images/futurefly_logo.svg" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Future Fly</h3>

  <p align="center">
    Save Now, Soar Later.
    <br />
    <a href="https://gitlab.com/team-10HR/travel-saver-app"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://gitlab.com/team-10HR/travel-saver-app">View Demo</a>
    ·
  </p>
</div>


## Save Now, Soar Later.

Every journey starts with a single step – and a smart savings plan. Start yours with FutureFly!

### About the Project

[![Project Name Screen Shot][project-screenshot]](https://gitlab.com/team-10HR/travel-saver-app)

Our platform is designed for the budget-conscious traveler who yearns for new horizons but is mindful of expenses.

By visualizing your savings and breaking down your travel costs month by month, FutureFly empowers you to plan ahead and make those dream destinations a reality. Whether you're a solo adventurer or planning a family getaway, FutureFly is your co-pilot in turning travel aspirations into tangible adventures.

Start your journey with FutureFly, where your next adventure is just a plan away.

### Design

#### Project Wireframe
[![Project Wireframe][FutureFly_wireframe]](https://gitlab.com/team-10HR/travel-saver-app)

#### API Models Map
[![Project API Models][FutureFly_API_Models]](https://gitlab.com/team-10HR/travel-saver-app)

### Built With

[![React][React.js]][React-url] [![Bootstrap][Bootstrap.com]][Bootstrap-url] [![FastAPI][Fastapi.tiangolo.com]][Fastapi-url] [![React][React.js]][React-url] [![ReactRouter][ReactRouter.com]][ReactRouter-url] [![Docker][Docker.com]][Docker-url] [![Bootstrap][Bootstrap.com]][Bootstrap-url] [![HTML5][HTML5.com]][HTML5-url] [![Python][Python.org]][Python-url] [![Javascript][Javascript.com]][Javascript-url] [![PostgreSQL][PostgreSQL.org]][PostgreSQL-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started
### Prerequisities

The installation instructions assume your system has the following software: [Google Chrome](https://www.google.com/chrome/) and [Docker](https://www.docker.com/).

If you don't have these (or equivalent) software, please install them before proceeding.

To get a local copy of FutureFly up and running on your machine follow these simple steps.

### Installation

1. Fork and clone the [repository](https://gitlab.com/team-10HR/travel-saver-app)

2. Rename the .env.sample file to .env

3. Remove the .gitlab-ci.yml file

4. Run `docker volume create tsa`

5. Run `docker compose build`

6. Run `docker compose up`

7. Navigate to [localhost:3000](http://localhost:3000/)

## Roadmap

- [x] Build Plans, Savings, and transactions
- [x] Switch to Vite + React
- [ ] Add TripAdvisor destinations cards to search through suggestions
- [ ] Build a travel suggestions feature
- [ ] Use Redux Toolkit

## Contact

[![Contributors][britley-desir]][britley-url]
[![Contributors][dominick-cross]][dom-url]
[![Contributors][tamekia-n]][tamekia-url]
[![Contributors][jose-sirven]][jose-url]


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[project-screenshot]: images/futurefly_sameple.jpeg

[FutureFly_wireframe]: images/FutureFly-wireframe.png

[FutureFly_API_Models]: images/Futurefly_API_Model.png

[Fastapi.tiangolo.com]: https://img.shields.io/badge/Fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white
[FastAPI-url]: https://fastapi.tiangolo.com/

[React.js]: https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=white
[React-url]: https://reactjs.org/

[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com

[Docker.com]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/

[HTML5.com]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML5-url]: https://developer.mozilla.org/en-US/docs/Web/HTML

[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Javascript.com]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white
[Javascript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript

[PostgreSQL.org]: https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/

[ReactRouter.com]: https://img.shields.io/badge/React_Router-CA4245?style=for-the-badge&logo=reactrouter&logoColor=white
[ReactRouter-url]: https://reactrouter.com/en/main

[britley-desir]: https://img.shields.io/badge/Britley_Desir-0A66C2?logo=linkedin&style=for-the-badge
[britley-url]: https://www.linkedin.com/in/britleydesir/

[jose-sirven]: https://img.shields.io/badge/Jose_Sirven-0A66C2?logo=linkedin&style=for-the-badge
[jose-url]: https://www.linkedin.com/in/joesirven/

[tamekia-n]: https://img.shields.io/badge/Tamekia_N.-0A66C2?logo=linkedin&style=for-the-badge
[tamekia-url]: https://www.linkedin.com/in/tamekia-n-95a15916a/

[dominick-cross]: https://img.shields.io/badge/Dominick_Cross-0A66C2?logo=linkedin&style=for-the-badge
[dom-url]: https://www.linkedin.com/in/dominick-cross/



<!--
## Install Extensions

- Prettier: <https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode>
- Black Formatter: <https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter>

## Deliverables

- [ ] Wire-frame diagrams
- [ ] API documentation
- [ ] Project is deployed to Caprover (BE, DB) & GitLab-pages (FE)
- [ ] GitLab issue board is setup and in use (or project management tool of choice)
- [ ] Journals

## Project layout

The layout of the project is just like all of the projects
you did with `docker-compose` in module #2. You will create
a directory in the root of the repository for each service
that you add to your project just like those previous
projects were setup.

### Directories

Several directories have been added to your project. The
directories `docs` and `journals` are places for you and
your team-mates to, respectively, put any documentation
about your project that you create and to put your
project-journal entries. See the _README.md_ file in each
directory for more info.

The other directories, `ghi` and `api`, are services, that
you can start building off of.

Inside of `ghi` is a minimal React app that has an "under
construction" page. It is setup similarly to all of the
other React projects that you have worked on.

Inside of `api` is a minimal FastAPI application.
"Where are all the files?" you might ask? Well, the
`main.py` file is the whole thing, and go take look inside
of it... There's not even much in there..., hmm? That is
FastAPI, we'll learn more about it in the coming days. Can
you figure out what this little web-application does even
though you haven't learned about FastAPI yet?

Also in `api` is a directory for your migrations.
If you choose to use PostgreSQL, then you'll want to use
migrations to control your database. Unlike Django, where
migrations were automatically created for you, you'll write
yours by hand using DDL. Don't worry about not knowing what
DDL means; we have you covered. There's a sample migration
in there that creates two tables so you can see what they
look like.

The Dockerfile and Dockerfile.dev run your migrations
for you automatically.

### Other files

The following project files have been created as a minimal
starting point. Please follow the guidance for each one for
a most successful project.

- `docker-compose.yaml`: there isn't much in here, just a
  **really** simple UI and FastAPI service. Add services
  (like a database) to this file as you did with previous
  projects in module #2.
- `.gitlab-ci.yml`: This is your "ci/cd" file where you will
  configure automated unit tests, code quality checks, and
  the building and deployment of your production system.
  Currently, all it does is deploy an "under construction"
  page to your production UI on GitLab and a sample backend
  to CapRover. We will learn much more about this file.
- `.gitignore`: This is a file that prevents unwanted files
  from getting added to your repository, files like
  `pyc` files, `__pycache__`, etc. We've set it up so that
  it has a good default configuration for Python projects.
- `.env.sample`: This file is a template to copy when
  creating environment variables for your team. Create a
  copy called `.env` and put your own passwords in here
  without fear of it being committed to git (see `.env`
  listed in `.gitignore`). You can also put team related
  environment variables in here, things like api and signing
  keys that shouldn't be committed; these should be
  duplicated in your deployed environments.

## How to complete the initial deploy

There will be further guidance on completing the initial
deployment, but it just consists of these steps:

### Setup GitLab repo/project

- make sure this project is in a group. If it isn't, stop
  now and move it to a GitLab group
- remove the fork relationship: In GitLab go to:

  Settings -> General -> Advanced -> Remove fork relationship

- add these GitLab CI/CD variables:
  - PUBLIC_URL : this is your gitlab pages URL
  - REACT_APP_API_HOST: enter "blank" for now

#### Your GitLab pages URL

You can't find this in GitLab until after you've done a deploy
but you can figure it out yourself from your GitLab project URL.

If this is your project URL

https://gitlab.com/GROUP_NAME/PROJECT_NAME

then your GitLab pages URL will be

https://GROUP_NAME.gitlab.io/PROJECT_NAME

### Initialize CapRover

1. Attain IP address and domain from an instructor
1. Follow the steps in the CD Cookbook in Learn.

### Update GitLab CI/CD variables

Copy the service URL for your CapRover service and then paste
that into the value for the REACT_APP_API_HOST CI/CD variable
in GitLab.

### Deploy it

Merge a change into main to kick off the initial deploy. Once the build pipeline
finishes you should be able to see an "under construction" page on your GitLab
pages site. -->
