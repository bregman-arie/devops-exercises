## How to prepare for DevOps/SRE/Production Engineer interviews?
 
Note: the following is opinionated.
 
### Skills you should have
 
#### Linux
 
Every DevOps Engineer should have a deep understanding of at least one operating system and if you have the option to choose then I would say it should definitely be Linux as I believe it's a requirement of at least 90% of the DevOps jobs postings out there.
 
Usually, the followup question is "How extensive should my knowledge be?" Out of all the DevOps skills, I would say this, along with coding, should be your strongest skills. Be familiar with OS processes, debugging tools, filesystem, networking, ... know your operating system, understand how it works, how to manage issues, etc.

Not long ago, I've created a list of Linux resources right [here](https://dev.to/abregman/collection-of-linux-resources-3nhk). There are some good sites there that you can use for learning more about Linux.
 
#### Coding
 
My personal belief is that any DevOps engineer should know coding, at least to some degree. Having this skill you can automate manual processes, improve some of the open source tools you are using today or build new tools & projects to provide a solution to existing problems. Knowing how to code =  a lot of power.

When it comes to interviews you'll notice that the level of knowledge very much depends on the company or position you are interviewing for. Some will require you just to be able to write simple scripts while others will deep dive into common algorithms, data structures, etc. It's usually clear from the job requirements or phone interview.

The best way to practice this skill is by doing some actual coding - scripts, online challenges, CLI tools, web applications, ... just code :)

Also, the following is probably clear to most people but let's still clarify it: when given the chance to choose any language for answering coding tasks/questions, choose the one you have experience with! Some candidates prefer to choose the language they think the company is using and this is a huge mistake since giving the right answer is always better than a wrong answer, no matter which language you have used :)
 
I recommend the following sites for practicing coding:
                                                 
* [HackerRank](https://www.hackerrank.com)
* [LeetCode](https://leetcode.com)               
* [Exercism](https://exercism.io)
 
Starting your own project is also a good idea. More on that later on.

#### Architecture and Design
  
This is also an important aspect of DevOps. You should be able to describe how to design different systems, workflows, and architectures. Also, the scale is an important aspect of that. A design which might work for a dozen of hosts or X amount of data, will not necessarily work well with bigger scale.
 
Some ideas for you to explore: 
                               
* How to design and implement a CI pipeline (or pipelines) for verifying PRs, run multiple different types of tests, package the project and deploy it somewhere
* How to design and implement secured ELK architecture which will get logs from 10,000 apps and will display the data eventually to the user
* Microservices designs are also quite popular these days
                       
I recommend going over the following GitHub projects as they are really deep-diving into System Design:
                               
* https://github.com/donnemartin/system-design-primer
                               
#### Tools           
                               
Some interviews will focus on specific tools or technologies. Which tools? this is mainly based on a combination of what you mentioned in your C.V & those that are mentioned in the job posting and used in the company. Here are some questions I believe anyone should know to answer regarding the tools he/she is familiar with:
                               
* What the tool does? What it allows us to achieve that we couldn't do without it?                            
* What its advantages over other tools in the same area, with the same purpose? Why you specifically using it?
* How it works?                
* How to use it?               
                               
Let's deep dive into practical preparation steps
                               
### Scenarios || Challenges || Tasks              
                               
This is a very common way to interview today for DevOps roles. The candidate is given a task which represents a common task of DevOps Engineers or a piece of common knowledge and the candidate has several hours or days to accomplish the task.<br>
                               
This is a great way to prepare for interviews and I recommend to try it out before actually interviewing. How? Take requirements from job posts and convert them into scenarios. Let's see an example:
                               
"Knowledge in CI/CD" -> Scenario: create a CI/CD pipeline for a project.
                               
At this point, some people ask: "but what project?" and the answer is: what about GitHub? it has only 9125912851285192 projects...and a free way to set up CI to any of them (also a great way to learn how to collaborate with others :) )
                               
Let's convert another scenario:                                                                                                                                              
                               
"Experience with provisioning servers" -> Scenario: provision a server (to make it more interesting: create a web server).

And the last example:                                                                                                                                                        
  
"Experience with scripting" -> Scenario: write a script. Don't waste too much time thinking "what script should I write?". Simply automate something you are doing manually or even implement your own version of common small utils.
  
### Start your own DevOps project
  
Starting a DevOps project is a good idea because:
  
* It will make you practice coding
* It will be something you can add to your resume and talk about with the interviewer
* Depends on size and complexity, it can teach you something about design in general
* Depends on adoption, it can teach you about managing Open Source projects
  
Same here, don't overthink what your project should be about. Just go and build something :)
  
### Sample interview questions
  
Make a sample list of interview questions on various topics/areas like technical, company, role, ... and try to answer them.
See if you can manage to answer them in a fluent, detailed way.
  
Better yet, ask a good friend/colleague to challenge you with some questions. Your self-awareness might be an obstacle in objective self-review of your knowledge :)
  
### Networking
  
For those who attend technical meetups and conferences, it can be a great opportunity to chat with people from other companies on their interviewing process. But don't start with it, it can be quite awkward. Say at least hello first... (:
  
Doing so can give you a lot of information on what to expect from an interview at some companies or how to better prepare.
  
### Know your resume
  
It may sound trivial but the idea here is simple: be ready to answer any question regarding any line you included in your resume.
Sometimes candidates surprised when they are asked on a skill or line which seems to be not related to the position but the simple truth is: if you mentioned something on your resume, it's only fair to ask you about it.


### Know the company

Be familiar with the company you are interviewing at. Some ideas:

  * What the company does?
  * What products it has?
  * Why its products are unique (or better than other products)? This can also be a good question for you to ask

### Books

From my experience, this is not done by many candidates but it's one of the best ways to deep dive into topics like operating system, virtualization, scale, distributed systems, etc.    

In most cases, you will do fine without reading books but for the AAA interviews (hardest level) you'll want to read some books and overall if you inspire to be better DevOps Engineer, books (also articles, blog posts) is a great way :)

### Consider starting in non-DevOps position

While not a preparation step, you should know that landing DevOps as a first position can be challenging. No, it's not impossible but still, since DevOps covers many different practices, tools, ... it can be quite challenging and also overwhelming for someone to try and achieve it as a first position.<br>
A possible path to becoming a DevOps engineer is to start with actually a different (but related) position and switch from there after 1-2 years or more.

Some ideas:

* System Administrator - This is perfect because every DevOps Engineer should have a solid understanding of the OS and sysadmins know their OS :)
* Software Developer/Engineer - A DevOps should have coding skills and this position will provide more than the required knowledge in most cases
* QA Engineer - This is a more tricky one because IMHO there are less overlapping areas/skills with DevOps Engineer. Sure, DevOps engineers should have some knowledge about testing but usually, it seems their solid skills/background is mainly composed out of system internals and coding skills.
                                                                           
### What to expect from a DevOps interview?                                
                                                                           
DevOps interviews can be very different. Some will include design questions, some will focus on coding, others will include short technical questions and you might even have an interview where the interviewer only goes over your resume and discussing your past experience.
                                                                           
There are a couple of things you can do about it so it will be a less overwhelming experience:
                                                                           
1. You can and probably should ask the HR (in some cases even the team lead) how the interview process looks like. Some will be kind enough to even tell you how to prepare.
2. Usually, the job posting gives more than a hint on where the focus will be and what you should focus on in your preparations so read it carefully.
3. There are plenty of sites that have notes or a summary of the interview process in different companies, especially big enterprises.
                                                                           
### Don't forget to be an interviewer as well                              
                                                                           
Some people tend to look at interviews as a one-way road of "Determining whether a candidate is qualified" but in reality, a candidate should also determine whether
the company he/she is interviewing at, is the right place for him/her.            
                                                                                                                 
* Do I care about team size? More specifically, do I care about being a one-man show or being part of a bigger team?
* Do I care about work-life balance?                                       
* Do I care about personal growth and how it's practically done?           
* Do I care about knowing what are my responsibilities as part of the role?                                                                                                  
                                                                           
If you do, you should also play the interviewer role :)

### One Last Thing                                
                                                  
[Good luck](https://youtu.be/AFUrG1-BAt4?t=59) :)
