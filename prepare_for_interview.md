## How to prepare for an DevOps interview?

Note: the following is opinionated.

### Technical subjects you should be familiar with

#### Linux

Every DevOps Engineer should have knowledge about operating systems and specifically Linux which is probably in 95% of the DevOps jobs postings out there.
Usually next question is "How extensive my knowledge should be?" - this should be your strongest area. Be familiar with processes, debugging tools, filesystem, networking, ... you got this :)

#### Coding

Some DevOps interviews include coding tasks/questions. Be prepared for those by doing actual coding. It should be at least scripting level but some companies (especially top 5) will require more than that which means you should be familiar with common algorithms, data structures, etc.
 
Also, the following is probably clear to most people but let's still clarify it: when given the chance to choose any language for answering coding tasks/questions, choose the one you have experience with! Some candidates prefer to to choose the language they think the company is using and this is a huge mistake because right answer > wrong answer in any language.

#### Architecture and Design

This is also an important aspect of DevOps. You should be able to describe how to design systems, workflows and in a way which will s-c-a-l-e. This is important because sometimes candidates will describe something that works great with 5 hosts or data of 100GB but will not scale to 100,000 hosts or big amounts of data.

Some ideas:

* How to design and implement a CI pipeline (or pipelines) for verifying PRs, run multiple different types of tests, package the project and deploy it somewhere
* How to design and implement secured ELK architecture which will get logs from 10,000 apps and will display the data eventually to the user

#### Tools

Some interviews will focus on specific tools. Which tools is mainly based on what you mentioned in your C.V + those that are mentioned in the job posting and used in the company. Here are some questions I believe anyone should know to answer regarding the tools he/she is familiar with:

* What the tool does? What it allow us to achieve that we couldn't do without it?
* What its advantages over other tools in the same area, with the same purpose?
* How it works?
* How to use it? (general usage, no need to start memorizing flags)

Let's deep dive into practical preparation steps

### Sample interview questions

Make a sample list of interview questions on various topics/areas like technical, company, role, ... and try to answer them.
See if you can manage answering them in a fluent, detailed way.

### Know your resume

It may sounds strange but the idea here is simple: be ready to answer any question regarding any line you included in your resume.
Sometimes candidates surprised when they are asked on a skill or line which seems to be not related to the position but the simple truth is: if you mentioned something on your resume, it's only fair to ask you about it.

### Know the company

Be familiar with the company you are interviewing at. Some ideas:

  * What the company does
  * What products it has
  * Major achievements

### Books

From my experience this is not done by many candidates but it's one of the best ways to deep dive into topics like operating system, virtualization, scale, distributed systems, ...

In most cases, you will do fine with reading books but for the AAA interviews (hardest level) you'll want to read some books and overall, if you inspire to be better DevOps Engineer, books is a great way.

### Scenarios

This is a very common way to interview today for DevOps roles. The candidate is given a task which represents a common task of DevOps Engineers or common knowledge and the candidate has several hours or days to accomplish the task.<br>

This is a great way to prepare to interviews and I recommend to try it out before actually interviewing. How? Take requirements from job posts and convert them to scenarios. Let's see an example:

"Knowledge in CI/CD" -> Scenario: create a CI/CD pipeline for a project.

At this point some people ask: "but what project?" and the answer is: what about GitHub? it has only 9125912851285192 projects...and a free way to set up CI to any of them (also a great way to learn how to collaborate with others :) )

Let's convert another scenario:

"Experience with provisioning servers" -> Scenario: provision a server (to make it more interesting: create a web server).

And the last example:

"Experience with scripting" -> Scenario: write a script which helps to accomplish some of the DevOps goals. For example, a script for generating Travis YAML for projects based on their content. If you need more ideas, open an issue and we'll help!

### Start your own DevOps project

Starting a DevOps is a good idea because:

* It will make you practice coding
* It will be something you can add to your resume and talk about with the interviewer
* Depends on size and complexity, it can teach you one thing or two about design
* Depends on adoption, it can you teach you about managing Open Source projects

### Consider starting in non-DevOps position

Landing DevOps as a first position can be challenging. No, it's not impossible but still, since DevOps covers many different practices, tools, ... it can be quite challanging. A possible path to become a DevOps engineer is to start with actually a different position and switch from there after 1-2 years or more.

Some ideas:

* System Administrator - This is perfect because every DevOps Engineer should have solid understanding of the OS and sys admins know their OS :)
* Software Developer/Engineer - A DevOps should have coding skills and this position will provide more than the required knowledge
* QA Engineer - This is more tricky one because IMHO there are less overlapping areas/skills with DevOps Engineer but some people done it so it's not impossible :)

### One Last Note

DevOps interviews can be very different. Some will include design questions, some will focus on coding, others will include short technical questions and you might even have an interview where the focus is only about going over your resume and discussing your past experience.
There are a couple of things you can do about about it:

1. You can and probably should ask the HR (in some cases even the team lead) how the interview process looks like. Some will be kind enough to even tell you how to prepare.
2. Usually the job posting gives more than an hint on where the focus will be and what you should focus on in your preparations so read it carefully.
3. There are plenty of sites that have notes or summary of the interview process in different companies, especially the big enterprises.

One last thing, [good luck](https://youtu.be/Xz-UvQYAmbg?t=29) :) 
