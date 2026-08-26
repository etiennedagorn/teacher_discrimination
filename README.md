# Teacher Survey oTree Experiment

Replication package for the oTree implementation of the teacher survey used in:

**Monnet, Marion, Philippe Colo, and Etienne Dagorn.**  
*Determinants of Gender Discrimination by Teachers: Evidence from an Online Experiment.*  
Conditionally accepted at the **European Economic Review**.  
Working paper available on SSRN: <https://ssrn.com/abstract=5254180>.

The participant-facing text is in French. Code comments and replication notes are in English.

## Suggested Citation:

**Article**:

```latex
@misc{monnet_colo_dagorn_2025_gender_discrimination_teachers,
  title        = {Determinants of Gender Discrimination by Teachers: Evidence from an Online Experiment},
  author       = {Monnet, Marion {\textcircled{R}} Colo, Philippe {\textcircled{R}} Dagorn, Etienne},
  year         = {2025},
  month        = may,
  day          = {14},
  note         = {Available at SSRN},
  url          = {https://ssrn.com/abstract=5254180},
  doi          = {10.2139/ssrn.5254180}
}
```

**Replication Package**

```latex
@misc{monnet_colo_dagorn_2025_replication_package,
  title        = {Replication Package for ``Determinants of Gender Discrimination by Teachers: Evidence from an Online Experiment''},
  author       = { Dagorn, Etienne and Monnet, Marion and Colo, Philippe},
  year         = {2025},
  note         = {Replication package},
  url          = {https://github.com/etiennedagorn/teacher_discrimination}
}
```

## Contents

- `settings.py`: main oTree configuration and session sequence.
- `intro/`: consent/device check, respondent characteristics, and treatment assignment.
- `bulletins_blind/`: blind report-card evaluation condition.
- `bulletins/`: non-blind report-card evaluation condition.
- `iat/`: IAT shown before the dictator-game block.
- `dictator_game/`: dictator-game allocation decisions.
- `iat_2/`: IAT shown after the dictator-game block.
- `survey/`: final survey and elicitation items.
- `random_number/`: contact information and participant identifier page.
- `_static/`: shared JavaScript, CSS, and image assets.
- `_templates/`: shared oTree template overrides.
- `REPLICATION.md`: light reproduction instructions and packaging checklist.

## Quick Start

Use Python 3.9 or another Python version compatible with the oTree dependency
range in `requirements.txt`.

```bash
python3.9 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
otree resetdb
otree devserver
```

Open `http://localhost:8000/demo` and start the `main` session config.

The configured session uses 40 participants:

```python
app_sequence = [
    'intro',
    'bulletins_blind',
    'bulletins',
    'iat',
    'dictator_game',
    'iat_2',
    'survey',
    'random_number',
]
```

## IAT Stimuli

IAT stimuli is the app-level CSV file:

- `iat/stimuli.csv` for the pre-dictator-game IAT.
- `iat_2/stimuli.csv` for the post-dictator-game IAT.

Both files must contain `category` and `stimulus` columns. 

## Randomization

- `intro` assigns `participant.vars['treatment']`. Participants with
  `treatment=False` see the IAT before the dictator-game block; participants
  with `treatment=True` see the IAT after the dictator-game block.
- `intro` assigns `participant.vars['treatment_blind']` with probability 0.1.
  Participants in this condition see `bulletins_blind`; others see `bulletins`.
- `bulletins` randomizes the order of the 16 available non-blind report cards
  and displays 10 of them.
- `bulletins_blind` randomizes and displays 8 blind report cards.
- `dictator_game` randomizes the color framing branch and the task order once
  per participant.
- `survey` randomizes the order of selected survey items within each page.
