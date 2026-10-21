# BeeLabs | Beverly Cotten

My software development portfolio, with projects in **Python, HTML, CSS, and JavaScript**. BeeLabs documents how I turn ideas into working programs while building my skills for a software engineering role.

Start with the portfolio website for front-end work, or the Virtual Stylist for an interactive Python application.

## Featured software projects

| Project | Technologies | What to explore |
| --- | --- | --- |
| [BeeLabs Portfolio Website](Projects/002-BeeLabs-Website/) | HTML, CSS, JavaScript | Responsive layouts, mobile navigation, DOM event handling, and scroll interactions. |
| [Virtual Stylist](Projects/001-Python-Fundamentals/virtual_stylist.py) | Python standard library | Outfit recommendations based on occasion and weather, randomized accessories, and an interactive approve/restyle loop. |
| [Career Matcher](Projects/001-Python-Fundamentals/day4.py) | Python | Text input normalization and conditional logic that map interests to suggested technology career paths. |

### BeeLabs Portfolio Website

A personal portfolio that presents projects, skills, and a development learning journey.

- Uses CSS variables and media queries to organize styling across screen sizes.
- Opens and closes mobile navigation with JavaScript, updating the button's accessibility labels and expanded state.
- Highlights navigation links as the current section changes during scrolling.
- Uses `IntersectionObserver` for reveal effects and skill-bar animations.
- Includes CSS rules for visitors who prefer reduced motion.

**View locally:** open `Projects/002-BeeLabs-Website/index.html` in a browser. The site uses plain HTML, CSS, and JavaScript and has no package installation or build step.

### Virtual Stylist

A command-line application that asks for a name, occasion, and weather, then suggests an outfit and accessory. Users can approve the look or request another accessory. Unrecognized approval choices prompt the user to try again.

The recommendations use explicit Python conditions and the standard-library `random` module.

**Run with Python 3 from the repository root:**

```sh
python Projects/001-Python-Fundamentals/virtual_stylist.py
```

### Career Matcher

A small command-line exercise that maps interests such as building, analyzing, and designing to technology career suggestions. Combined interests are handled before individual interests.

```sh
python Projects/001-Python-Fundamentals/day4.py
```

## Supporting projects

**[Sales Analysis](Projects/003-Data-Analyst/)** — A seven-product sample dataset and an Excel analysis workbook. The CSV contains units sold and prices; the sample revenue totals $4,298. This project practices data organization, spreadsheet calculations, and communicating results.

**[Adventures with Limi](Projects/004-Kids-Show/)** — A separate creative production project containing scripts, storyboards, recording guides, and visual references. It demonstrates production planning and documentation. Its generated artwork and animation are creative assets, separate from the software implementations above. Some media assets remain local.

## Repository guide

```text
Notes/                         Development learning notes
Projects/
  001-Python-Fundamentals/      Python applications and practice exercises
  002-BeeLabs-Website/          Portfolio website source
  003-Data-Analyst/             Sample sales data and Excel workbook
  004-Kids-Show/                Adventures with Limi production materials
```

The Python folder also contains early learning exercises. The featured applications above provide the most direct starting point for reviewing the software work.

## Connect

[GitHub](https://github.com/BevCotten) · [LinkedIn](https://www.linkedin.com/in/beverlycotten)
