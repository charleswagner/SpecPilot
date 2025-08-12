SpecPilot Terminal Simulation
This is a simulation of what a user would see when running the SpecPilot installer and starting their first session in a new project.

$ python3 bootstrap.py init

(The full animated intro with the ASCII art rocket and title would play here...)

-----------------------------------------------------------------
Pilot Mode Engaged.
Welcome to the SpecPilot Interactive Installer.

🚦 Initializing...
>>> Initialization Mode is your project's pre-flight check...
>>> It validates your environment and ensures readiness for development.

    - Analyzing current directory: /Users/cwagner/Code/MyNewAwesomeApp ... [OK]

Switching to 🚀 Pilot Mode to begin guided setup...

>>> Pilot Mode is your proactive guide...
>>> It analyzes your project's state...
>>> ...and recommends the next logical step.

🚀 Pilot Mode will now walk you through setting up all modes.
    - 🚦 Initialization Mode: Project startup with comprehensive validation
    - 🌱 Bootstrap Mode: Creates new projects with full structure
    - 🏛️ Architecture Mode: Collaborative architectural design and validation
    - 🎨 Design Mode: Creates specification documents
    - 📐 Spec Mode: Implements code based on specifications
    - 🍄 Vibe Mode: Debugging and troubleshooting
    - 🕵️ Deep Check Mode: Comprehensive project auditing
    - 🛠️ Scripts Mode: Utility script management
    - 🎁 Commit Mode: Intelligent commit analysis and generation

>>> Switching to 🌱 Bootstrap Mode...
>>> ...we will define your project's identity and goals.

🌱 Bootstrap Mode...

>>> Bootstrap Mode sets up new projects from scratch...
>>> Let's define your project's DNA together.

First, let's define the project's identity.

? What is the official title of your project? (e.g. "MyProject")
> My New Awesome App

? What is the directory for the project? (e.g. "./MyProject")
> .
    << Analyzing directory '.'... This looks like a new project. >>

? What is your user name? This will be used to create your personal workspace.
> cwagner
    - Creating user workspace for 'cwagner' ... [OK]
    - Installing core engine to .specpilot/ ... [OK]

---
Let's configure your notepad.
  Your notes will be in .specpilot/workspace/cwagner/notepads/
  I'll write an initial note at .specpilot/workspace/cwagner/notepads/default.md
  You can always organize your Notes with the command "Organize Notepad".

? Would you like a summary of your notepad after every command?
  We recommend 'one-line'.
  (Enter for 'one-line', or type 'verbose' or 'none') > 

? In one sentence, what is the core purpose of this product? (enter to skip)
> A web service that helps teams track their weekly goals.

✅  Excellent. You can always update your product goals in `docs/plans/product_roadmap.md`.

---
? How do you want your Project Conventions to be configured?
    - 🥇 Enterprise Scale - We'll default to strict rules for everything.
    - 🦄 Scalable MVP - We'll add solid separations of concerns.
    - 🍄 Vibe Time - No project conventions. You can add them later.
> 1
    ... Bootstrapping Enterprise Scale conventions ...
    .... 🥇 Convention 1: Strict Golden Thread enforced.
    .... 🥇 Convention 2: TDD-style testing recommended.

🌱 Bootstrap Mode Configured...

>>> Switching to 🏛️ Architecture Mode for configuration...

Let's configure your architectural philosophy.

? What is our primary architectural goal for the MVP?
    - 🥇 Enterprise Scale - Design for high security and reliability from day one.
    - 🦄 Scalable MVP - Build a solid foundation that can grow.
    - 🍄 Vibe Time - No formal architecture. Just get it working.
> 1
    ... Bootstrapping Enterprise Scale Architecture Rules ...
    .... 🥇 Architecture Rule 1: All secrets must be in environment variables.
    .... 🥇 Architecture Rule 2: All public endpoints must have rate limiting.

---

🎨  **Configuring Design Mode...**
? Do you have any product requirements you would like me to create initial specs for?
  You can always add product requirements in `docs/plans/product_roadmap.md` later.
  (Enter requirement, press Enter to skip) > Create user login API

✅  We will add a placeholder in `technical_roadmap.md` for your requirement.
   You can always add to and modify your `technical_roadmap.md` later.

---

📐  **Configuring Spec Mode...**
I see there is one spec to implement based on your product requirements.
I'll add a default spec file for you to fill out.
You will find it at `docs/specs/spec_user_login_api.md`.

---

🍄  **Configuring Vibe Mode...** 🍄

Vibe Mode is great for debugging and quick prototyping...
Sometimes you need to break the rules.

       Engaging....

               🍄🍄🍄🍄🍄
           🍄🍄🍄🍄🍄🍄🍄🍄🍄
        🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄
      🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄
     🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄
               🍄🍄🍄🍄🍄
               🍄🍄🍄🍄🍄
               🍄🍄🍄🍄🍄
               🍄🍄🍄🍄🍄

Oh no, it looks like there was a bug in our ASCII art generator... Give us a minute...
Fixing...........
✅  Emoji ASCII art Fixed.

Vibe Mode is now configured with the "Pragmatic Escape Hatch."

---

🕵️  **Configuring Deep Check & Session Check...**
>>> If you want a quick check on your work, you can run a `Session Check`.
>>> It checks all files edited in the current session against your project's rules.

>>> Before you commit, we recommend a `Deep Check`.
>>> It makes sure your entire codebase is semantically covered from the README to the code.

---

🎁  **Configuring Commit Mode...**
Commit Mode gives you feedback to become a better AI Orchestrator.
 - Frustration Feedback - Were you frustrated?
 - Effectiveness - Quality of prompts
 - Machine Effectiveness - Quality of Execution
 - Vibe Dependency - Using vibe over config.

SpecPilot Score = (Effectiveness + MachineEffectiveness) - (Vibe + Frustration)

? Would you like SpecPilot to calculate these on each Commit?
  (Enter for yes, for no type this exactly: No I don't want these awesome features.) >

✅  *Perfect. The "Intelligent Appendix" is now active. Your commit history will become a rich, searchable record of your entire development journey.*

---

OK, SpecPilot is about to write the following files:
 - .specpilot/engine/... (15 files)
 - .specpilot/workspace/cwagner/... (4 files)
 - docs/plans/... (3 files)
 - docs/specs/spec_user_login_api.md

Proceed with installation? (y/n) > y
 - Writing files..... [OK]



✅  **SpecPilot installation complete!**
>>> You are now in 🚀 Pilot Mode. I am ready to guide you.
>>> The next step is to formally design the architecture for the 'Create user login API' task.
>>> **My recommendation is to switch to 🏛️ Architecture Mode.**

Now you can always update your requiremetns with these files. 
 -> Table of all editable files and what it is used for. 






