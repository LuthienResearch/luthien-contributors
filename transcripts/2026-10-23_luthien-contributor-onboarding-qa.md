# 2026-10-23 Luthien contributor onboarding + Q&A

**Date:** Friday, October 23, 2026, 6:30am Pacific, about 40 minutes (Google Meet)  
**Participants:** Scott Wofford, Allister Lundberg, Kirill Novikov, Matt Broerman, Paolo Calvi, Dan Alexander, Paul Chelarescu, Deneille Guiseppi  
**Recording:** not shared (this meeting has redacted passages; a recording can't have lines cut).

**Redactions:** 00:05:27 (partner's non-public plans); 00:06:46 (partner's non-public plans); 00:08:25 (partner's non-public plans); 00:25:58 (unreleased security research). Unredacted original retained privately, outside this repository.

## Sources

| Capture | Supplied | Coverage | Authoritative for |
|---|---|---|---|
| Gemini Transcript tab (Notes by Gemini doc, kept private because it contains the redacted passages) | words, speaker names (Meet accounts) | 00:00:15 to 00:40:27 | everything; the only capture |

**Speaker map:** Speaker names come from each person's Google Meet account; Matthew Broerman and Daniel Alexander are shown as Matt and Dan, the names they gave on the call. No Plaud recording exists for this call.

**Merge notes:** built 2026-11-06 by Claude from the captures above; not yet reviewed by a participant. Spacing glitches from the Gemini export ("Luthien.I", "Allisterand") and lowercase "faculty" for the company Faculty were fixed without notes. Each turn is listed under the Gemini timestamp of its section.

## Transcription fixes

### Errors fixed

| Time | Heard (capture) | Fixed to | Evidence |
|---|---|---|---|
| 00:00:15 | "Jay" (Gemini) | Jai | Jai Dhyani, Luthien co-founder (now on Separatrix) |
| 00:03:43 | "Equestamp" (Gemini) | EquiStamp | partner's own spelling |
| 00:10:09 | "Paulo" (Gemini) | Paolo | Paolo Calvi's Meet account name |
| 00:10:09 | "Alistar" (Gemini) | Allister | Allister Lundberg's Meet account name |
| 00:15:52 | "Curl" (Gemini) | Kirill | Kirill Novikov, named with Paul for the sandbox idea |
| 00:15:52 | "myth class" (Gemini) | Mythos-class | Anthropic's Claude Mythos; Scott names "mythos" on the Oct 29 call |
| 00:17:05 | "harnesser teaming" (Gemini) | harness red teaming | the harness red teaming brief Matt names at 00:35:50 |
| 00:17:05 | "sub aent" (Gemini) | sub-agent | context |
| 00:17:05 | "open soas" (Gemini) | open source | context |
| 00:22:12 | "Sarth" (Gemini) | Sarthak | Sarthak Siddha, met at EAG New York; on the Oct 29 call |
| 00:22:12 | "wrapping on" (Gemini) | ramping up on | Scott repeats "ramping up" in the same sentence |
| 00:22:12 | "EG" (Gemini) | EAG | EAG New York, the conference Scott attended Oct 2026 |
| 00:25:58 | "Jurgus" (Gemini) | Jurgis | Jurgis Kemeklis, Redwood Research |
| 00:25:58 | "Jurga says" (Gemini) | Jurgis says | Jurgis Kemeklis, Redwood Research |
| 00:25:58 | "Luian" (Gemini) | Luthien | org name |
| 00:28:33 | "side of the land" (Gemini) | lay of the land | context |
| 00:28:33 | "right access" (Gemini) | write access | repository write access |
| 00:28:33 | "Lucian-contributor" (Gemini) | luthien-contributors | Slack channel name |
| 00:28:33 | "Lucian" (Gemini) | Luthien | org name |
| 00:28:33 | "Ryan Greenblat" (Gemini) | Ryan Greenblatt | Redwood Research chief scientist |
| 00:31:56 | "metal level" (Gemini) | meta level | context |
| 00:37:53 | "Fabian Rogers" (Gemini) | Fabien Roger | Anthropic researcher, author of the cited auto-mode paper |

### Uncertainties

| Time | Passage | Best reading | Why unsure |
|---|---|---|---|
| 00:00:15 | "we're missing Olo" | Paolo | Paolo Calvi speaks later; no other attendee name fits |
| 00:00:15 | "we're missing Danielle" | Dan | Scott says "Welcome Dan" a minute later |
| 00:05:27 | "we must pace a frontier" | unknown essay title | not checked against the essay |
| 00:13:22 | "Sammy" | as heard | Trajectory Labs agent wrangler; spelling not verified |
| 00:17:05 | "Datrace Con" | unknown project name | Kirill's cyber deception project for Kubernetes; not verified |
| 00:17:05 | "mostly in files" | "mostly in evals" | on Oct 29 Deneille says "mostly in eval fellowships" |
| 00:30:04 | "PHP attacks" | unknown | a security incident in the news; not identified |

## Transcript

### 00:00:15

**Scott Wofford:** Morning.

**Allister Lundberg:** Morning.

**Kirill Novikov:** Morning.

**Allister Lundberg:** Morning.

**Scott Wofford:** Are you back in Austria?

**Kirill Novikov:** Uh yes. So actually it's not a morning for me.

**Scott Wofford:** All right. I think we may meet. Yeah. Let's see. So, we're missing Olo. Um, Peter can't make it. And, uh, we're missing Danielle. So, um, perhaps we start with just some some quick intros, um, and what we're going to cover in this call today. Um, my name is Scott, uh, co-founder of Luthien. Um, as background context, um, a guy named Jai [was: Jay] and I started Luthien in 2025\. Um, and we built an open source proxy. Um, we originally started as a nonprofit and then in early 2026, we um, converted to a PBC to participate in the Seldon Labs accelerator program. And, um, let's see. Um after the accelerator program, we decided to pivot. Jai [was: Jay] decided to work on a separate project named Separatrix. Um and we decided to pivot from general developers to AI control researchers as well as um frontier AI lab auditors.

### 00:03:43

**Scott Wofford:** Um and um the objective of this call is to answer any questions that this group has on um contributing to building open source software for this new set of users. Welcome Dan. Um, and so, um, I'm going to provide at the top of the call just a little bit of context on, um, kind of who we're talking to and and where we're at with those conversations. Um so basically starting in let's see go starting in I think it was August or September um we uh started an engagement with Redwood to work on a um project named control tower. Control Tower is basically a framework built on Inspect that um allows researchers to send their projects to the team and have their results replicated on a public dashboard. So they can um compare their results apples to apples and download datas and and compare the efficacy of different um monitor pro monitors protocols and red team and blue team strategies in different um like essentially like simulated docker environments. Um and so this was exciting because um we got a chance to work um really closely with Redwood on this as well as with EquiStamp [was: Equestamp].

### 00:05:27

**Scott Wofford:** Um then uh in parallel uh we um so um if you recall um a few weeks ago Dario from Anthropic put out an essay um about we must pace a frontier. In that essay, one of the first bullet points was, hey, unilaterally, um, we're going to grant access to some embedded, um, evaluators and anthropic, and they're going to have employee level access. A few weeks later, the blog post on the left um uh they announced that they'd actually be working with Accenture is specifically that fact that um engagement will be led by Faculty, which is a UK based shop um that does like um AI work. *[Redacted: partner's non-public plans.]*

### 00:06:46

**Scott Wofford:** *[Redacted: partner's non-public plans.]*

### 00:08:25

**Scott Wofford:** *[Redacted: partner's non-public plans.]* Okay, that's like a bit of a highle overview of where we're at in terms of Luthien. I think um for the next section of this call, I would suggest that folks uh hop into this document and please type in uh under two uh your name and then a bunch of links where other members of the team can learn about you and your work. Um, and then we'll just go around the room. And then for the remainder of the call, we'll do Q&A on what I've said or what you read ahead of the call. And then finally, uh, with, um, five minutes remaining, we will go into these next steps. Um, I put in here, yeah, like my GitHub and my website. Basically, I'm a um product manager by training or like well no official training but just kind of learning on the job and um little bit of finance and I tend to think about um problems in terms of like limiting factor and how might we like lay out all the background context that a cross functional technical team would need to um think about all different aspects of a problem.

### 00:10:09

**Scott Wofford:** For example, um imagine if you are Tom and you're given um you know a few days or hours to evaluate the claims that a lab is making and okay and and you know it's just you and perhaps a few colleagues uh and you have a lab with like I don't know 10,000 employees and like on the order of like 100,000 to a million transcripts to analyze. Um what software tools would be really useful? And so working backwards from that um uh this kind of like my thinking process um why don't we go with um Allister and then Matt next. Um and then uh Paolo [was: Paulo] uh Paolo [was: Paulo] has worked with us on the building of the Luthien proxy which I'll paste in a link here too. Um Allister

**Allister Lundberg:** Yeah. Hey, very nice to meet everyone. Looking forward to working with with you all. Uh my name's Allister [was: Alistar]. I'm a longtime software engineer. Also was a longtime product manager. Um and uh you know, lots of uh software backend experience and uh AI experience.

### 00:11:31

**Allister Lundberg:** That's That's me.

**Matt Broerman:** Hi,

**Allister Lundberg:** I met

**Matt Broerman:** I'm Matt. Um, I'm a statistician uh by training and uh that was my job for uh in a medical center for a handful of years. Um and in pursuing that a lot of kind of bio stuff generally and data sciency sort of stuff. Um um and then I've been working on eval uh broadly speaking uh for the last uh I don't know year and a half or so.

**Paolo Calvi:** myself. Uh I'm Paolo [was: Paulo]. I had uh the beautiful uh opportunity to start off pretty early with Scott on the Luthien proxy. Uh this brought me to um develop further um uh knowledge about AI security. Um I'm participating also in other projects um regarding this uh um approach and um I'm more I'm u uh by the time in the meantime discovering that testing AI is a completely different uh thing that any anything else we have uh encountered until now in uh So it's a very interesting thing and um I think uh whoever digs into this uh area will find that is really a very important and completely unexpected uh uh world.

### 00:13:22

**Scott Wofford:** And I'll actually just interject uh a bit here. So um on our website we have kind of like whoers we're working with. Um as part of Seldon Labs we got a chance to um get introduced and work with this group named Trajectory Labs. um they maintain a public fork of the proxy we built and um Paolo [was: Paulo] did a lot of our work just to understand like um Sammy who's the um agent wrangler who uh is working over there and um a bit of a prolific open- source contributor like what is he doing like how is he doing it and and how did he change our proxy to help with the observability that he um uses to run his like um autonomous as he calls like a legion of agents. Um, and so to the extent like this type of stuff is useful to folks. Um, I think it'd be nice to like yeah share tips around like this is moving fast, what what are folks seeing and and how might we uh like uh learn from Sammy and and you guys on um uh yeah, how how you're leveraging this stuff.

### 00:14:33

**Scott Wofford:** Um, let's go. Daniel, do you want to go next?

**Dan Alexander:** Uh yeah, I'm I'm Dan. Uh I have a background in economics and data science and I've done research reproducibility and like research uh auditing at Cornell for four years. Um, I'm just starting or trying to start to get into evals, but I'm very interested in proper scoring rules and all sorts of statistical stuff with that. Um, I don't know if I feel like I haven't introduced myself too well, but uh, yeah.

**Scott Wofford:** Great. Great. No, that's perfect. Perhaps Paul, uh, do you want to go next?

**Paul Chelarescu:** Yeah, I'll go next. Hi, I'm Paul. I'm a machine learning engineer. Uh I have about six years uh six years of experience. I've worked with um a safety a while back. Uh but I've also done um recently cyber security uh AI workflow evaluations. So that would be probably the most relevant uh recent experience I have for this. I built uh agent evals and model evals before.

### 00:15:52

**Paul Chelarescu:** Um and I'm excited to yeah help uh this project out and learn more about what I can do. Um I've dropped three links. I have u all uh three linked in a um GitHub and a personal website. But uh right now I'm really looking to re understand what's currently happening at the frontier and um yeah what's currently uh needed.

**Scott Wofford:** Um, interjecting again. I have a project idea in my head that has to do with secure sandboxes. I haven't had the chance to write that down in this project brief, but it occurs to me that um at least me, Paul, and potentially Kirill [was: Curl] um might have some takes on like at least gaps that we we see in the like uh secure sandbox space with the problem statement at a high level being like you got a Mythos-class [was: myth class] model with you want to like um evaluate the underlying capabilities and like the effectiveness of safety benchmarks, but you don't want it um leak out. Um so maybe we can take that as an action item to to put some thoughts on paper.

### 00:17:05

**Scott Wofford:** Um why don't we go with Kirill next?

**Kirill Novikov:** Uh yeah, hi I'm Kirill. Sorry that I'm without a camera. Uh my background is a security and open source. I've contributed to projects like Datrace Con which does cyber deception for Kubernetes. I'm most interested in harness red teaming [was: harnesser teaming] and also in the swarm monitor since it builds on the sub-agent [was: sub aent] distribution work. So that's it. Nice to meet you everyone.

**Scott Wofford:** All right, then. Yeah.

**Deneille Guiseppi:** Hi, I'm Deneille. Um, I'm a software engineer. Um, I've I'm like I've built a company from like the ground up from scratch. So, I've been in within like the startup world. Um I've worked a quite a bit in open source [was: open soas] as well. Um and I've been doing a bit of AI safety research for the past year or so. Um mostly in files, mostly in like um with coding agents. Uh uh that's what I've like my background has been in. But um yeah, I am just excited to be here and excited to build stuff.

### 00:18:26

**Scott Wofford:** Awesome. So, um, let's move into the Q&A section of this meeting. Um, this is meant to just be an open I recognize we're kind of um throwing a lot of documents at you folks. Um, but the idea is to um yeah, be transparent about what we're thinking, how we're thinking of working. Um, like uh compensation is out of scope for this meeting. We'll we'll talk about that like um uh separately like on a case by case basis but if that's like a blocker um please let me know like in the um short term uh we are aiming to raise some like apply for some funding um from coefficient giving um over the next few weeks I'm headed to San Francisco um this weekend uh to chat with folks about that um but yeah I am opening it up to Q&A about Um, anything and everything. Uh, Luthien

**Dan Alexander:** Uh, so I I have a question. it might be slightly out of scope or I don't know but so when I was reading through the documents and stuff I'm kind of new to the space and so I was wondering it it seems like a lot there's a lot of um emphasis being placed on detection of if there is or whatever but is there also work or or thoughts about like detecting or predicting what the attack was intended to be rather than just if there was or was not an attack.

### 00:20:03

**Matt Broerman:** Could you say a little bit more what you're imagining?

**Dan Alexander:** Uh well, just just um because it it it sort of uh struck me that like a lot of the detection from what my understanding is like is if there you know is something weird happening. But that could also be caused by a mistake or it does and it also makes it very difficult to separate the degree of damage of the detected attack, right? Like if it's just trying to steal all the weights of the model, like that's really bad. But if it's just trying to steal like a config file, like that I mean I'm not going to say who cares, but like that's very different things. And so I if the models are are they able to or are they detecting at all just something weird is happening or are they looking at I think that this is trying to steal something and then what if that would we be able to score on what it thinks the damage is going to be done or or not? And again, that might be out of scope for this meeting, but um that was just the first thing that jumped to my mind and and I've been like struggling to to stop thinking about it um the more we uh I look into this stuff.

### 00:21:10

**Matt Broerman:** maybe I could say just two brief things and then pass it off to somebody else who knows more. Um I know that one of uh who isn't here present um his name is Byron. Um he has a cyber security background and sort of his his specialty is threat modeling. Um and so I think maybe one of the proposals uh or one one of the briefs uh uh and certainly one that we've talked about previously to the brief structure we've adopted uh is this sort of threat modeling. Um and I know that yeah person you need to sort of contemplate you know like the the the variety of the sort of risks possible. Uh so like you know impact is is certainly an important thing um and something that's on my mind also maybe relevant is just um you'd like to know um it seems slightly related to your question um how like if a if a if a you know auditor is going in to detect you'd like to know all of their um sort of false false negatives right you you'd like to get some handle on what they might not actually

### 00:22:12

**Dan Alexander:** Yeah, exactly.

**Matt Broerman:** see Um uh and so that's that's I don't think that's like a direct uh uh consideration in any of the present or any of the the briefs currently. Um, but I know it's on my mind and I have it in mind in some some stuff that I've written up about um ways to get at that and and effectively like try to uh uh assess the you know audit the auditors, you know, try to get a sense of their effectiveness. This

**Dan Alexander:** Yeah. Yeah. Sorry that thanks that that perfectly answers and also that I'm not totally off base or like Yeah. Yeah. Perfect. Thank you.

**Allister Lundberg:** Scott, you're mute.

**Scott Wofford:** Uh, building on what Matt said, met a guy named Sarthak [was: Sarth] at um, EAG [was: EG] and we we were just kind of riffing earlier this week on like what would be the first step of this threat modeling project which you can read about here in uh, um, that I will say like I think a lot of people are ramping up on [was: wrapping on] for a lot of people in AI safety are ramping up on cyber um and so we're kind of doing it all together and um that's uh fun place to be.

### 00:23:28

**Scott Wofford:** Lots to learn really really quick. Other questions

**Paolo Calvi:** Well, uh uh Scott, my question will be uh maybe when we can uh have a little chat because since we have had such tight collaboration, I will have more precise and detailed questions that uh uh yeah not might be not interesting for everybody at this moment.

**Scott Wofford:** Yeah. Yeah,

**Paolo Calvi:** This

**Scott Wofford:** definitely. Um, let's do that next week. Um, mainly the um, uh, objective is of this call is to answer any questions that are kind of like blockers and understanding for folks that want to read about this or think about this over the weekend. Um, ne next week we'll we'll kind of get into logistics and and um figure out how this is all going to work. Um, but um, over to you Matt.

**Matt Broerman:** Um,

**Paolo Calvi:** Yep.

**Matt Broerman:** uh, I I like some of these briefs and maybe I'd like to improve one, you know.

**Scott Wofford:** Yeah. Um, so you all have like um edit access to this document.

### 00:24:43

**Scott Wofford:** Um, please write down your full thoughts. Um if things we there's great BA basically we'd like to set up a nice healthy marketplace for ideas and so in this marketplace for ideas uh everyone can contribute ideas and everyone can offer constructive feedback on everyone else's ideas and then based on this feedback and this process I think that uh we'll come up with some like really excellent ideas um once we hit like the diminishing returns like Okay, this seems like we should just do it. Then we just do it. Matt

**Matt Broerman:** Good. So that sets up the next question I had is like yeah so we all contribute uh maybe we make improvements there's some phase of discussion maybe we have one-on- ones after this meeting to discuss or you know in a smaller groups um to discuss details of one or the other of the briefs um what happens next? What do we what are we imagining that's going to happen and on what time uh on what calendar?

**Scott Wofford:** Yeah, fantastic. So, um let's take for example um this um number one uh red team harness.

### 00:25:58

**Scott Wofford:** So, um uh there's a researcher named uh Jurgis [was: Jurgus] at Redwood. I'm headed over to um the Bay. So, yeah, after this um I'm going to chat with Jurgis [was: Jurgus] on Sunday morning. Um, and let's say that someone was interested on working on this project with Jurgis [was: Jurgus]. *[Redacted: unreleased security research.]* Um, and so if someone, for example, were excited about working on this project, what we'd do, um, is set up a kick up call kickoff call with Jurgis [was: Jurgus]. uh think about, you know, what type of work you want to contribute. Um we'd create a Slack channel um in the Seattle AI safety slack uh with Jurgis um members of the core Luthien [was: Luian] team and anyone who's interested to work on this project. Um and um we'd kind of have like a project kickoff meeting um where Jurgis says [was: Jurga says] like yeah this works makes sense here's what's in scope where's what's out of scope.

### 00:27:07

**Scott Wofford:** Um the um team would have an opportunity to ask any questions about um what's the most effective like thing to start on first um and then we get going. as an example.

**Matt Broerman:** So, it does sound like there's a step there where whatever kind of revised version of one of the briefs that we uh we like um we do have to sort of like take that back to to Jurgis [was: Jurgus] or or whomever might be a good sort of mentor or sort of contact within an organization somewhere um to help like you know offer helpful input. make sure that that continues to be a project that seems like in scope for their concerns or something that they think is valuable to be working on. But presuming that then we would sort of get started as a small team um with some of that input on some cadence.

**Scott Wofford:** Yeah, I I believe that like the we we can have the hard highest um marginal impact by getting feedback early and often from uh the folks who are going to be um like using the software we build or um advising on like the research agenda.

### 00:28:33

**Scott Wofford:** Although like I definitely consider Luthien [was: Lucian] more of like an open source software shop than a research shop. But I do think that like because um uh the like the existing lay of the land [was: side of the land] is like look Ryan Greenblatt [was: Ryan Greenblat] is like both a AI control and security researcher and a third party auditor. So there's a decent amount of overlap such that this like user discovery process is like um useful and and so we can learn a lot from both of these like user personas with like tight feedback loops. Cool. Um to try and like uh be respectful of everyone's time, we'll move on just to the next steps here. Um, please do uh share your availability in the um luthien-contributors [was: Luthien [was: Lucian]-contributor] Slack channel. And also um I'm going to make this repo way better. Um, and this we can consider this um it's a it's a public repo and I'll I'll give everyone um write access [was: right access] and we can just um dump ideas and and um context Next. that might be useful for building uh great software in this repo.

### 00:30:04

**Scott Wofford:** Um other questions on next steps or how we shall proceed.

**Allister Lundberg:** Just to be super clear, can you actually highlight them just so everyone sees them?

**Scott Wofford:** Yeah, sure. So, any questions on these next steps?

**Paul Chelarescu:** Just quickly, Scott, do you have a link of a calendar to highlight or should we just type our availability?

**Scott Wofford:** Yeah, I put in when to meet. Let me find that and repost it to the contributors. I'll I'll do that after this call.

**Paul Chelarescu:** Okay.

**Scott Wofford:** Um that said, like yeah, have a low bar for posting in the Slack channel. Like um I'd be interested in folks thoughts on the um PHP attacks on like stuff in the news. Um it's good to have a spot where we can just uh share ideas.

**Paul Chelarescu:** Yeah, I I guess like the overarching question would be how will like this how will we all decide how who works on what?

**Scott Wofford:** Yeah. Um, as an input to that decision, I think the first step is like what projects are you most excited about working on?

### 00:31:56

**Scott Wofford:** And then once we have we feel like um folks have a sense for that then let's have a meeting to to discuss it and or um do what I described about like debating red teaming uh the ideas because um let's say Paul you're like um excited about a project that's um that I had uh or you know Matt had um healthy debate will make the idea stronger and um it's helpful to be in to

**Paul Chelarescu:** Mhm.

**Scott Wofford:** swap seats. Um we can all be in the seat of like hey I'm proposing an idea and then we can switch our seat and all be in the seat of like how can we make this idea better. This is like essentially the loop I would like to spin. Uh practically, yeah, like let's just dump our availability uh in there and we can communicate on Slack. Maybe it makes sense to have like a smaller, more focused meeting on a certain project. We can set that up next week. Maybe it makes sense to have a meta level [was: metal level] like, "Oh man, everyone's like I I am having trouble deciding between these projects or like I like the kind of problem statement of this project, but I actually don't like the implementation.

### 00:33:24

**Scott Wofford:** Let's talk about that.

**Paul Chelarescu:** Okay.

**Scott Wofford:** Yeah. Um I I'll answer this question another way because it it's um we're still in a bit of like an ambiguous phase on like what is it? Like some some of this is like specific like I I I think like the auditor tooling, the claims wiki, the harness checker, like some of the threat modeling research are like we could get started immediately. Um, however, there are some like higher level strategic questions about like, well, what makes most sense to do first now given like limited time. Um, I think that's a great discussion to have as a group next week. Um, as a norm, we just record all our meetings. If you aren't able to make a meeting, no worries. We'll post it in there and you can watch it. Um, or or type the transcript like put your transcript into Claude and and just ask, "Hey, what do we talk about? anything relevant here related to my interests. And that's it. That's how that's how I would like to operate going forward.

### 00:34:29

**Scott Wofford:** Um, and yeah, hey, we're we're we're building this plane as we fly it. So, ping me if like you're confused or blocked or um uh anything like that. Cool. Final thoughts.

**Matt Broerman:** I I'll if anybody wants to discuss something and I've I've read all of them. Um um so if anybody wants to just have a conversation about any of these like now and has a little bit of time to spare, I'm I'll I'll stay on and see if anybody stays.

**Scott Wofford:** Sounds good. Thanks everyone. I actually got to go. my uh it's uh 7 a.m. here in Seattle and I got to wake up the kiddos, take them to daycare and and then go to the airport. But thanks everyone for joining.

**Paolo Calvi:** Thank you.

**Kirill Novikov:** Thank you.

**Paul Chelarescu:** Thank you. Okay, they all

**Dan Alexander:** Uh, you're muted.

**Matt Broerman:** cool. Well, nice to meet you, Daniel.

**Dan Alexander:** Yep.

**Matt Broerman:** Um,

**Dan Alexander:** Uh, I go by Dan, but Daniel's fine,

**Matt Broerman:** and yeah,

### 00:35:50

**Dan Alexander:** but whatever.

**Matt Broerman:** I go by Matt.

**Dan Alexander:** Yeah.

**Matt Broerman:** There you go.

**Dan Alexander:** Yeah.

**Matt Broerman:** Um, um, yeah. Yeah. So, was there like one uh I I I'll say up top I I'm actually working on a um a revision of the agent red teaming or the harness red teaming thing. um trying to make it a bit more specific um and incorporate what I know about um the most um widely used like open source uh eval framework for doing it which is this inspect um which I've worked with before um and trying to yeah like get it to go in that um um and then I have like more thoughts about like which part why this might be more valuable or what we would do. Um, but it's mostly informed by what like uh what some of the stuff that um is cited there, but just like flushed out a bit more.

**Dan Alexander:** Yeah. Yeah. I mean, so my main I guess my main question was if you wanted So I don't have really the cyber background at all.

### 00:36:54

**Dan Alexander:** Uh and so for the briefs and stuff, if you had a suggestion for for ones I should pay special attention to or or be directed towards, um I'd appreciate that.

**Matt Broerman:** Maybe Allister has a point of view about it.

**Allister Lundberg:** I would uh don't don't even restrict yourself, you know,

**Dan Alexander:** Okay.

**Allister Lundberg:** like it doesn't matter like so just because they're only like a page or two each.

**Dan Alexander:** Okay. Okay.

**Allister Lundberg:** just read them all and like let yourself be confused and and uh and then just

**Dan Alexander:** Okay.

**Allister Lundberg:** because you may you may say oh actually even though I don't know about this this is the one what or you may say

**Dan Alexander:** Yeah. Okay.

**Allister Lundberg:** actually none of these are good and I need a new one so just like I would you just just just yeah

**Dan Alexander:** Yeah. I mean, because the to kind of build a little bit on the the previous thing I I brought up in the meeting was just it occurred to me that normally it it seems like the the model is like you have the the agent that's like the potential attacker and then the uh the person wa watching it.

### 00:37:53

**Dan Alexander:** But you could also have a third one that doesn't have the ability to intervene and all they're doing is attempting to discern what the attacker or potential attacker is doing. And so then that would allow you a like have a ground truth of you know what the attacker is doing because that was provided to them. But that would also allow you to assess how well these agents are able to monitor each other both in terms of just monitor and intervene which is already what we have but then just just monitor or just predict or just guess if the like what the original brief was but um or not brief but but task was but I don't know that's just something I've been kicking around but um thank you guys so much Okay.

**Matt Broerman:** If you take a look at the there's um I guess like very specifically on that in the um the the agent or there's a harness red team there's a paper linked to by um Fabien Roger [was: Fabian Rogers] uh and and and co-authors um like red team auto mode um and in fact like um um the coding agent harnesses now um like the ones that you know if you use the app it's like if you use any of their apps like they're kind of like connecting to those under the hood and this sort of stuff or if you just like run it on your terminal um they have um now like yeah these like classifiers which are very like light models that um are trying to review everything as they come.

### 00:39:14

**Matt Broerman:** Um uh so this would be your kind of like um uh roughly your partly your idea, but if you look at like their table two and that you see that they're like promoting I don't know exactly promoting but they're sort of suggesting like well what if you like gave them like all some more affordances like so that they were more full full-fledged like agents themselves. So like they they aren't just like sort of reviewing the last you know like message and tool call but in addition they're going to go able to like read certain files and see if it's like relevant to anything that like you know and this sort of stuff. So like um it's definitely in on their minds about like how to do this and and in that

**Dan Alexander:** Okay. Yeah.

**Matt Broerman:** table too they're sort of I mean they're anthropic researchers so they're like saying like like this would be

**Dan Alexander:** Yeah.

**Matt Broerman:** like maybe something we consider for a future implementation or something like that.

**Dan Alexander:** Okay. Cool. Uh I think that that was the main questions. If you guys have anything for me or any questions, I'd be happy to answer, but um happy to give you you guys time back. Thank you so much. Really appreciate it. Bye.

**Matt Broerman:** Take it easy. Bye.
