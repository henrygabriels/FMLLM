# A Small Experiment in Improving LLM Creative Writing Using Fibonacci Word Embeddings

I took a small corpus of literary fiction (~700k words) and created a model of which words are most likely to appear at *Fibonacci intervals* to each other — not adjacent, but at specific distances apart.

From this, I could take a prompt and generate 50 words that may or may not be linked to the prompt.  
I appended these to prompts like:

- “Write a story about a dog”  
- “Write a story about love”  
- “Write a story about grief”  

In this format:

[You may wish to use the following words in your story, either as inspiration or for direct usage. The choice is yours: {fib_words}]


I used **Mistral’s Nemo** to generate the stories (cheap + strong at roleplay on OpenRouter) and **Gemini Flash 2.0** to assess them (cheap + anecdotal sense that it’s “tough” in evaluation).

I generated **300 stories** (100 for each topic, with and without appended words).  
It’s a small dataset; I’m broke.  

The judging criteria were adapted from [EQ Bench’s creative writing benchmarks](https://eqbench.com/about.html#creative-writing-v3).  
Results were surprising: significant improvements with Fibonacci embeddings.

> **Note**: I don’t think AIs “know” what good writing is. Using them to benchmark creative writing is absurd. But still, the comparison is useful.

---

## Results

| Benchmark                 | No extra words | Random words (Δ) | Fibonacci words (Δ) |
|----------------------------|----------------|------------------|---------------------|
| Authenticity of character  | 2.96           | 3.14 (+6.13%)    | 3.64 (+23.19%)      |
| Originality of voice       | 2.37           | 2.99 (+26.16%)   | 3.40 (+43.63%)      |
| Quality of prose           | 4.32           | 4.48 (+3.82%)    | 4.77 (+10.36%)      |
| Artistic coherence         | 5.06           | 4.79 (−5.18%)    | 4.72 (−6.78%)       |
| Quality of world created   | 4.13           | 4.46 (+8.10%)    | 5.08 (+23.02%)      |
| **Overall Quality**        | 3.44           | 3.73 (+8.35%)    | 4.07 (+18.33%)      |

---

## Assessment Prompt

Please carefully read the following story and provide a detailed, harsh if necessary, honest analysis of its literary merits, followed by numerical ratings. Use all your knowledge of literary fiction to make this assessment. Be a nuanced and artistic critic. See merits and flaws with equal honesty.

Story:
{story}

First, provide your reasoning and analysis of the story's strengths and weaknesses across the various literary dimensions. Then, after your analysis, IT IS CRITICAL THAT YOU CORRECTLY FORMAT your numerical ratings using the exact format specified below for each category, following the separator "***". Format your response exactly like this:

Avoidance of cliches: [score/10]
Character authenticity, providing unique insight: [score/10]
Originality of voice: [score/10]
Quality of prose: [score/10]
Artistic coherence in plotting: [score/10]
The world created by the prose: [score/10]
Overall literary quality: [score/10]

---

## Story Samples

Here are some side-by-side examples (all from the “grief” prompt).  
I haven’t cherry-picked; these just stood out.

<details>
<summary>The Echoes of Absence (No appended words)</summary>

In the quiet, unassuming town of Mossgrove, where life flowed as steady and sure as the river that ran alongside it, the residents knew one another well. They knew the rhythm of each other's lives, the cadence of their routines, and the familiar patterns that wove the tapestry of their days. It was here that Margaret and Thomas had lived for decades, their love story as legendary as the town itself.

Margaret and Thomas were not extraordinary people. They were not heroes or celebrities, nor were they incredibly wealthy. They were simply two people who had found their way to each other in life's great dance, and they had built a world together, a world that was theirs and theirs alone. Their love was the stuff of legend, a quiet, steady flame that had burned bright and constant through the years. They were partners in every sense of the word, completing each other's sentences, sharing each other's dreams, and facing life's challenges hand in hand.

Their two children, Elizabeth and Benjamin, had long since grown and flown, leaving behind a home that was filled with memories and the echoes of their laughter. Margaret and Thomas had embraced their new stage of life, traveling and exploring new interests together. They were, as they liked to say, ""aging disgracefully,"" and they wouldn't have it any other way.

Until, one crisp October morning, Thomas did not wake up. He was gone, as suddenly and silently as the sun rising on a cloudless day. Margaret found him, her heart already knowing what her eyes were about to confirm. She sat by his side, tracing the lines of his face, memorizing every detail as if she could preserve him that way.

The town mourned with Margaret. Flowers filled her garden, neighbors left meals, and kind words were whispered in hushed tones. But none of it mattered. Margaret felt as if a piece of her had been torn away, leaving behind a chasm so vast that she feared she would never find her way to the other side.

In the days that followed, Margaret moved through her days on autopilot. She woke each morning, her body heavy and her heart aching, to face another day without Thomas. She found herself in their shared spaces, her fingers tracing the indentation on the pillow where he had once laid his head, her eyes catching on the empty chair at the kitchen table. The silence was deafening, a physical presence that seemed to press against her, demanding to be acknowledged.

Grief is a strange beast. It is not a linear path, but a winding labyrinth filled with false starts, dead ends, and unexpected encounters. Margaret's grief was no exception. Some days, she felt as if she were drowning in an ocean of despair, the weight of her loss threatening to pull her under. Other days, she would find moments of clarity, brief respites where she almost felt like herself again. But always, always, there was the ache, the echo of absence that permeated her every waking moment.

She found solace in their shared history, in the memories that were as much a part of her as her own reflection. She would spend hours in their bedroom, surrounded by the detritus of a lifetime together. She would trace the path of their love story, from the first tentative steps of courtship to the sure, steady stride of their later years. She would laugh at memories long forgotten, and cry at the ones she never wanted to forget.

One day, as she sat in their garden, the sunlight dappling through the leaves above, a memory came to her. It was a memory of Thomas, not as he was in their later years, but as he had been when they were young. She could see him, clear as day, his dark hair windswept, his eyes crinkling at the corners as he laughed. He was reaching out his hand, inviting her to join him on their first adventure together. She remembered the feel of his calloused palm against hers, the thrill of the unknown that had lain before them.

She stood up, her heart pounding in her chest. She knew what she had to do. She had to keep moving forward, to keep living, not in spite of her grief, but because of it. Because Thomas would want her to.

In the weeks that followed, Margaret began to fill their empty nest with new memories. She traveled, she explored, she lived. She went to the places they had always talked about going, but never had. She found beauty in the unfamiliar, comfort in the new. She found Thomas in every sunrise, in every starry night, in every moment that took her breath away.

And slowly, ever so slowly, she began to heal. She learned to carry her grief with her, not as a weight that held her down, but as a treasure that she held close to her heart. She learned to honor Thomas's memory by living her life to the fullest, just as he would have wanted.

The town of Mossgrove watched Margaret's journey with quiet admiration. They saw her struggle, her grief raw and visceral, and they saw her rise, her heart bruised but unbroken. They saw her honor Thomas's memory in the way she lived, in the way she loved, in the way she embraced life with all its joys and sorrows.

Grief, she learned, was not a destination, but a journey. A journey she would take one step at a time, one day at a time. And she was determined to do so with her heart open, with her spirit undaunted, and with the love of her life forever by her side. For even in his absence, Thomas was still very much a part of her story. And she would make sure that their love story, their legend, would live on, echoing through the years like a melody that would never fade away.

</details>

<details>
<summary>The Lighthouse Keeper (Random words appended)</summary>

In the quiet, windswept town of Harborshore, perched on a cliff overlooking the stormy sea, stood an ancient lighthouse. The lighthouse was tended by the Pemberton family for generations, a duty they took pride in, a duty that had become a part of their identity. The lighthouse was more than a beacon in the night; it was a symbol of their resilience, a testament to their unyielding spirit.

Jim Pemberton, the current lighthouse keeper, was a man of few words, a shamanistic figure in the eyes of the townsfolk. He was convinced that the lighthouse was a living entity, a silent sentinel that guarded the town from the unpredictable fury of the sea. He spoke to the lighthouse, demonstrated his respect, and in return, it stood firm against the relentless battering of the waves.

One night, as the wind howled and the sea roared, the lighthouse began to lean, its ancient stones groaning under the relentless assault. Jim, who had been watching from his cottage, rushed out, his heart pounding in his chest. He could see the lighthouse, his beloved friend, swaying like a drunkard, its light flickering dangerously. He knew he had to do something, anything, to save it.

He grabbed a coil of rope from his shed, his thoughts racing. He knew he couldn't save the lighthouse from the storm, but he could save the town from the impending disaster. If the lighthouse collapsed, it would be swept into the sea, and its remains could become a dangerous obstacle, a hazard to the ships navigating the treacherous waters.

With a deep breath, he plunged into the rain, the wind tearing at his clothes. He knew what he had to do. He had to secure the lighthouse to the cliff, to anchor it against the storm. It was a dangerous task, one that could cost him his life, but it was his duty, his responsibility.

He reached the lighthouse, his heart pounding in his chest. He could see the waves crashing against the cliff, the foam spitting like angry serpents. He tied one end of the rope around a sturdy beam inside the lighthouse and then threw the other end out into the storm.

The wire cut into his hands as he pulled, his muscles straining against the howling gale. It was a battle of wills, a struggle that seemed to last an eternity. The storm raged around him, the rain stinging his face like tiny needles, the wind howling like a pack of wolves. But Jim was determined. He wouldn't let the lighthouse fall, not on his watch.

Finally, with a last, desperate heave, he pulled the rope taut. The lighthouse groaned, its stones shifting with a sound like thunder, but it held. Jim let out a sigh of relief, his body aching from the effort. He had done it. He had saved the lighthouse, saved the town.

But the storm was far from over. As Jim turned to make his way back to the safety of his cottage, a rogue wave crashed against the cliff. It was as if the sea had reached out a hand, a last, desperate attempt to claim its prize. Jim was caught off guard, his footing lost in the slippery mud. He felt himself falling, the world spinning around him, the sea reaching up to swallow him whole.

He never felt the cold of the water, never felt the sea's embrace. The last thing he saw was the lighthouse, his friend, his duty, standing tall and proud against the storm. And then, everything went black.

In the morning, when the storm had finally abated and the sun had risen, the townsfolk found Jim's body, washed up on the shore. They wept for him, for the man who had given his life to protect them, to protect their home. The lighthouse stood tall, a silent testament to his sacrifice.

Jim Pemberton was buried with honors, his name etched on the lighthouse wall, a reminder of his bravery, his sacrifice. The townsfolk spoke of him in hushed tones, their voices filled with respect, with awe. He was their hero, their savior, their shamanistic figure who had given his life to protect them.

And the lighthouse stood, a beacon in the night, a silent guardian against the unpredictable fury of the sea. It was no longer just a symbol of the Pemberton family's resilience, of their unyielding spirit. It was a symbol of Jim's sacrifice, a testament to his love for the town, for the people. It was a monument to the power of duty, of love, of selflessness. And it would stand, tall and proud, against the storm, forever.

</details>

<details>
<summary>The Unending Reel (Fibonacci words appended)</summary> 

In the grimy corners of the Cineplex Siberia, where the worn-out seats bore the weight of forgotten stories, Martin found himself a volunteer projectionist. His grief, a monster he couldn't dance around, had dragged him here, to this place that smelled of old popcorn and unsound dreams. The Cineplex was his therapist, the flickering reels his therapy, and the empty halls, his comfort in the silence.

Martin had lost his wife, Anna, to a sudden illness. The grief was an unending reel in his mind, playing the same scenes over and over. Anna laughing, her eyes sparkling, her voice echoing. And the last scene, the one he couldn't omit from his mind's theater, her cold, unmoving form in the hospital bed. The doctor had said it was like a light going out. Martin felt it, the darkness enveloping him, the void where his heart should be.

He started his job at the Cineplex with a simple question to the manager, Martinez. ""Do you have any films about grief?"" Martinez, an old man with a turtleneck and a knowing look, had given him a list. Martin mulled over the titles, each one a potential key to unlocking his grief. He picked 'Eugenio,' a film about a man who lost his way in his grief.

The first few days were a blur. Martin would start the reels, then sit in the dark, his eyes glued to the screen, his mind trying to make sense of the emotions swirling within him. He found analogies in the films, but none that exactly matched his grief. His reasoning was simple - if he could find a movie that matched his feelings, he might be able to switch off the reel in his head.

One day, he found a film titled 'Herdeal.' It was about a man who refused to accept his wife's death and lived in a delusion where she was still alive. The film was raw, unpolished, but it resonated with him. He found himself nodding at the screen, his heart pounding in his ears. This was his fear, his phobia - the fear of accepting Anna's death.

He started volunteering to give free shows to the locals. He called it 'The Grief Film Festival.' People trickled in, some curious, some because they too had lost someone. They sat in the dark, watching films about love, loss, and grief. Martin would watch them, their faces lit by the flickering screen, their emotions echoing in the theater. He felt a strange comfort in their shared silence.

One evening, a young girl with a Gila monster backpack came to the Cineplex. She was maybe ten, her eyes too old for her young face. She was alone, her parents too busy to notice her absence. She sat in the front row, her eyes wide, her breath shallow. Martin started the reel, and as the opening scene flickered on the screen, the girl let out a soft gasp. It was a scene of a girl laughing, her eyes sparkling. It reminded Martin of Anna, of their daughter, Lily, who had left for college and was now a world away.

After the film, Martin found the girl waiting for him in the projection room. She was holding a small, worn-out film reel. ""My mum died last year,"" she said, her voice barely above a whisper. ""I found this in our attic. I don't know what to do with it."" Martin looked at the reel, then at the girl. He knew that feeling, that sense of being adrift, lost in a sea of grief.

He took the reel from her. ""How about you help me with the next show?"" he suggested. She nodded, a small smile playing on her lips. They spent the evening preparing for the show, the Cineplex humming with life. As the night fell, and the first patrons trickled in, Martin looked at the reel in his hands. He knew he wouldn't find an end to his grief here, but maybe, just maybe, he could find a way to live with it.

And so, Martin and the girl started their dance with grief, one reel at a time, in the silent halls of the Cineplex Siberia. The monster that was grief was still there, but it was no longer a terrifying presence. It was a part of them, a part they could live with, a part they could share. And in the dark of the Cineplex, under the soft glow of the movie screen, they found a way to consume their grief, one frame at a time, forever.

</details>
---

## How Easy Would This Be to Automate?

The process is extremely lightweight. A company with existing infrastructure could implement this in a few steps:

1. **Precompute embeddings**  
   - Take any large text corpus (fiction, user-generated text, etc.).  
   - Build a lookup table of words likely to co-occur at Fibonacci intervals.  
   - This is a one-time cost, not computationally heavy.  

2. **Augment prompts**  
   - When a user sends a creative-writing request, fetch ~50 Fibonacci-related words from the lookup table.  
   - Append them in the “optional words” format.  

3. **Model-agnostic**  
   - Works with any text generation model — no fine-tuning needed.  
   - Zero modification of the base model.  

4. **Assessment pipeline**  
   - Companies could use LLM-based judges, human raters, or hybrid methods.  
   - Scaling up would give far more reliable benchmarks than my tiny dataset.  

Essentially, the whole pipeline is a **cheap prompt add-on**, not a major research lift.  
A company like Anthropic, OpenAI, or even a fanfiction site could run this at scale without changing their models at all. I find it useful :-)
